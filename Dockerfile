FROM python:3.11

WORKDIR /img_fucker

COPY pyproject.toml poetry.lock ./
COPY envs / 
RUN redis-server ;
RUN apt-get update \
    && apt-get install -y curl \
    && apt-get install -y build-essential \
    && apt-get install -y python3-dev

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN pip install tesseract-ocr && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY ./img_fucker /img_fucker


CMD ["poetry", "run", "python", "main.py"]
