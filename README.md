# Birme项目修改版，目的是为了支持在线批量裁剪网盘中的图片
New Feature
* 后端可设置文件夹地址(_目前是本地OS地址，如果需要引入云盘SDK可支持云盘访问_)
* 前端可获取服务器后端设置的地址中的文件等信息
* 支持批量上传图片直接保存到云盘
* 在线新建文件夹等

## front

## backend
后端启动命令：
terminal
```shell
fastapi run main.py --port 8080
```
docker
```shell
docker run -it -v ./data:/birme/data -p 18000:18000 --name birme-backend  birme-backend:v1
```
