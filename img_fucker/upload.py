import requests

api_url = "http://0.0.0.0:1453/analyze_img/"
image_filename = "3.png"

with open(image_filename, "rb") as image_file:
    files = {"file": (image_filename, image_file, "image/png")}
    response = requests.post(api_url, files=files)

    if response.status_code == 200:
        result = response.json()

        result['content'] = result['content'].replace("\n", " ")
        
        print("Result:", result)
    else:
        print("Error:", response.text)
