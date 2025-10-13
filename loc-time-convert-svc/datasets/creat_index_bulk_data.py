"""导入城市经纬度等数据到es中."""

import json

from app.config import APP_CONFIG
from app.constant import AppConstant
from elasticsearch import Elasticsearch  # type: ignore
from elasticsearch.helpers import bulk  # type: ignore
from loguru import logger  # type: ignore


if __name__ == "__main__":
    es = Elasticsearch(APP_CONFIG["DEFAULT"]["ES_URL"])
    _index_mappings = {
        "mappings": {
            "properties": {
                "id": {"type": "integer", "index": "false"},
                "name": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
                "latitude": {"type": "keyword", "index": "false"},
                "longitude": {"type": "keyword", "index": "false"},
            }
        }
    }

    es.indices.delete(index=AppConstant.INDEX_NAME)

    if es.indices.exists(index="all_cities"):  # 判断es中是否存在该索引
        logger.info(f"index=[{AppConstant.INDEX_NAME}] already exists!")
        es.indices.delete(index=AppConstant.INDEX_NAME)

    res = es.indices.create(index=AppConstant.INDEX_NAME, body=_index_mappings)
    logger.info(res)
    ACTIONS = []
    file_name = "update_all_the_cities.json"
    with open(file_name, "r", encoding="utf8") as fp:
        json_data = json.load(fp)
        for i in json_data:
            action = {
                "_index": AppConstant.INDEX_NAME,
                "_source": {
                    "id": int(i["id"]),
                    "name": str(i["name"]),
                    "latitude": str(i["latitude"]),
                    "longitude": str(i["longitude"]),
                },
            }
            ACTIONS.append(action)
        res, _ = bulk(
            es,
            ACTIONS,
            index=AppConstant.INDEX_NAME,
            raise_on_error=True,
            request_timeout=100,
        )
        logger.info(f"the cities count is {res}.")

    logger.info("exit")
