# 城市时区查询服务

根据城市名查询time_zone_location和time_zone。

## 目录说明
```bash
├── app
│   ├── config.py                      # 配置文件读取代码
│   ├── constant.py                    # 常量定义类
│   ├── search_data                    # 查询elasticsearch城市数据
│   └── server                         # route和服务核心代码
├── datasets
│   ├── creat_index_bulk_data.py       # 将城市(英文)数据导入到elasticsearch的脚本
│   └── update_all_the_cities.json     # 城市(英文)数据
├── docker-compose
│   └── docker-compose-local.yml       # 本地测试依赖数据库
├── docs                               # 文档目录
│   └── 城市时区查询服务接口文档.adoc  # 接口文档
├── pyproject.toml                     # uv包依赖/代码扫描/代码格式规范配置文件
├── README.md
├── run_app.py                         # 程序启动入口
└── tests                              # 集成和单元测试代码
```

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
- [ ] 使用高性能json工具orjson来替换elasticsearch，减低部署复杂度。