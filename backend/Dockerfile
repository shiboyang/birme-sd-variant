FROM python:3.10-slim

WORKDIR /birme

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir -i https://mirrors.cloud.tencent.com/pypi/simple -r requirements.txt

RUN mkdir data

COPY ./main.py ./main.py

EXPOSE 18000

ENTRYPOINT ["uvicorn", "main:app", "--root-path", "/api", "--port", "18000","--host", "0.0.0.0"]





