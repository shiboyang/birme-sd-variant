FROM python:3.10-slim

WORKDIR /birme

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir -i https://mirrors.cloud.tencent.com/pypi/simple -r requirements.txt

RUN mkdir data

COPY ./main.py ./main.py

EXPOSE 8000

CMD ["fastapi", "run", "main.py", "--port", "18000"]





