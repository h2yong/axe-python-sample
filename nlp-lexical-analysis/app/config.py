"""配置项."""

import configparser
import os

from loguru import logger  # type: ignore


APP_CONFIG = configparser.ConfigParser()
APP_CONFIG["DEFAULT"] = {"REST_PORT": 5005, "LOG_LEVEL": "INFO", "AVAILABLE_LANGUAGES": "ENGLISH|en_core_web_sm"}

# 从环境变量中获取配置
for _key in APP_CONFIG.defaults().keys():
    val = os.environ.get(_key.upper(), None)
    if val is not None:
        logger.info(f"exist env {_key.upper()}, it's value is {val}")
        APP_CONFIG["DEFAULT"][_key] = val

logger.info("the app config is: [{}]".format(dict(APP_CONFIG["DEFAULT"])))

AVAILABLE_LANGUAGES: list[str] = APP_CONFIG["DEFAULT"]["AVAILABLE_LANGUAGES"].split(",")
SUPPORT_LANGUAGES: list[str] = [language_with_model_name.split("|")[0].upper() for language_with_model_name in AVAILABLE_LANGUAGES]
