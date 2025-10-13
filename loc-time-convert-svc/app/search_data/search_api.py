"""elasticsearch客户端."""

from elasticsearch import Elasticsearch  # type: ignore
from loguru import logger  # type: ignore

from app.config import APP_CONFIG
from app.constant import AppConstant


class ElasticClientWithIndexName:
    """elasticsearch客户端."""

    def __init__(self) -> None:
        """elasticsearch客户端初始化."""
        self.es = Elasticsearch(APP_CONFIG["DEFAULT"]["ES_URL"])

    def search_data(self, city_name: str) -> tuple[float, float, str]:
        """根据城市名查询es_name信息.

        :param city_name: 城市名
        :returns:
            float(loc_latitude): 纬度
            float(loc_longitude): 经度
            es_name: es存储的城市名
        """
        doc = {"size": 1, "query": {"match": {"name": city_name}}}
        res = self.es.search(index=AppConstant.INDEX_NAME, body=doc)
        if not res["hits"]["hits"]:
            return float(-999), float(-999), ""

        loc_latitude = res["hits"]["hits"][0]["_source"]["latitude"]  # 纬度
        loc_longitude = res["hits"]["hits"][0]["_source"]["longitude"]  # 经度
        es_id = res["hits"]["hits"][0]["_source"]["id"]
        es_name = res["hits"]["hits"][0]["_source"]["name"]  # es存储的城市名
        logger.info({"msg": [{"id": es_id}, {"name": es_name}]})
        return float(loc_latitude), float(loc_longitude), es_name


elastic_client = ElasticClientWithIndexName()
