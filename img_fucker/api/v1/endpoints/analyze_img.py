from fastapi import APIRouter, UploadFile, HTTPException, File
from fastapi.responses import JSONResponse
from utils import data_extraction
from core import ocr
from core.redis_config import redis_client
from utils.cache_hasher import get_md5_hash, get_cached_result
import json
from utils.http_errors import HTTP_ERRORS

router = APIRouter()

@router.post("/analyze_img/")
async def analyze_image(file: UploadFile = File(...)):
    allowed_image_extensions = {'jpg', 'jpeg', 'png'}
    
    file_extension = file.filename.split('.')[-1].lower()

    if file_extension not in allowed_image_extensions:
        raise HTTPException(status_code=400, detail=HTTP_ERRORS[400] + ": Only image files are allowed")
    
    content = await file.read()

    cached_result = get_cached_result(content)
    if cached_result:
        return JSONResponse(content=cached_result, status_code=200)

    try:
        extracted_text = ocr.extract_data(content)  
        if not extracted_text:
            raise HTTPException(detail=HTTP_ERRORS[204], status_code=204)

        findings = data_extraction.extract_sensitive_data(extracted_text)

        if not findings:
            raise HTTPException(status_code=204, detail=HTTP_ERRORS[204])

        result = {
            "content": extracted_text,
            "status": "successful",
            "findings": findings,
            "source": "live"  
        }

        content_hash = get_md5_hash(content)
        redis_client.set(content_hash, json.dumps(result), ex=300)  

        return JSONResponse(content=result, status_code=200)

    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=404, detail=HTTP_ERRORS[404] + ": " + str(e))
