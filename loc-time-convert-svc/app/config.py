"""配置项."""

import configparser
import os

from loguru import logger  # type: ignore


APP_CONFIG = configparser.ConfigParser()
APP_CONFIG["DEFAULT"] = {
    "REST_PORT": 8010,
    "ES_URL": "http://elasticsearch:9200",
}

# 从环境变量中获取配置
for _key in APP_CONFIG.defaults().keys():
    val = os.environ.get(_key.upper(), None)
    if val is not None:
        logger.info(f"exist env {_key.upper()}, it's value is {val}")
        APP_CONFIG["DEFAULT"][_key] = val

logger.info("the app config is: [{}]".format(dict(APP_CONFIG["DEFAULT"])))
