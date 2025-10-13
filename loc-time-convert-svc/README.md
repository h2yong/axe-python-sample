# 城市时区查询服务

根据城市名查询time_zone_location和time_zone。

## 目录说明

## 环境变量说明

| 变量        | 说明                      |
| :---------- | ------------------------- |
| `REST_PORT` | 服务端口号                |
| `ES_URL`    | elasticsearch地址(含端口) |

## docker镜像构建

`sudo docker build -t loc-time-convert-svc:0.1.0 .`

## docker实例启动

`sudo docker run -itd --name loc-time-convert-svc -p 8010:8010 --restart=always --network local --network-alias loc-time-convert-svc.server loc-time-convert-svc:0.1.0`

## 待完善功能TODO
- [ ] 城市名目前只有英文且数据不够完成，需完善多语言支持如中文。
- [ ] 增加简单web页面用于演示。
- [ ] 使用快速json查询工具来替换elasticsearch，减低部署复杂度。