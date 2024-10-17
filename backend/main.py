import time
from pathlib import Path
from typing import Dict

import uvicorn
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.responses import FileResponse

# OSS_ROOT = "/birme/data"
OSS_ROOT = "/home/shiby/PycharmProjects/birme-sd-variant/backend/data"
IMG_SUFFIX = [".png", ".jpeg", ".jpg", ".webp", ".bmp"]
root_folder = Path(OSS_ROOT)


class Response(BaseModel):
    code: int
    data: Dict
    message: str


app = FastAPI()

# Comment out or remove the CORSMiddleware configuration
origins = [
    "http://localhost",
    "http://10.0.5.72:10004",
    "http://10.0.6.64:5500",
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/folder/{folder_path:path}")
def get_folder(folder_path: str = "") -> Response:
    """
    获取文件夹结构接口
    :param folder_path: 目标文件夹
    :return:
    """
    target_folder = root_folder.joinpath(folder_path)
    if not target_folder.exists() or target_folder.is_file():
        return Response(code=1001, data={}, message="Directory is not exist.")
    dir_list = []
    file_list = []
    for f in target_folder.iterdir():
        if f.is_dir():
            dir_list.append(f.name)
        else:
            if f.suffix in IMG_SUFFIX:
                file_list.append(f.name)
    data = {"dir_list": dir_list, "file_list": file_list}
    response = Response(code=1000, data=data, message="success")
    return response


@app.put("/folder/{folder_path:path}")
def create_folder(folder_path: str) -> Response:
    """
    新建文件夹接口
    :return:
    """
    target_folder = root_folder.joinpath(folder_path)
    if not target_folder.parent.exists():
        return Response(code=10002, data={}, message="Parameter Error")
    target_folder.mkdir(exist_ok=True)
    return Response(code=1000, data={}, message="success")


@app.get("/img/{img_path:path}")
def get_img(img_path):
    """
    下载图片接口
    :param img_path: 图片地址
    :return:
    """
    target_path = root_folder.joinpath(img_path)
    if not target_path.is_file() or not target_path.exists():
        return Response(code=1002, data={}, message="file is not exist.")

    return FileResponse(target_path, headers={
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }, media_type="image/png")


@app.post("/img/")
async def upload_img(img_path: str = Form(...), file: UploadFile = File(...)) -> Response:
    """
    上传图片接口
    :param img_path:
    :param file:
    :return:
    """
    if img_path.startswith("/"):
        img_path = img_path[1:]
    target_path = root_folder.joinpath(img_path)
    if not target_path.parent.exists() or not target_path.parent.is_dir():
        return Response(code=1001, data={}, message="Directory is not exist.")
    target_path = target_path.with_name(f"{target_path.stem}-{int(time.time())}{target_path.suffix}")
    with target_path.open("wb") as buffer:
        buffer.write(await file.read())
    return Response(code=1000, data={}, message="success")


if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=18000, reload=True)
