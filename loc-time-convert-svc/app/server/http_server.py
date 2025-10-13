"""根据城市名称查询时区相关信息."""

import datetime

import pytz  # type: ignore

from flasgger import Swagger  # type: ignore
from flask import Flask, request  # type: ignore
from loguru import logger  # type: ignore
from timezonefinder import TimezoneFinder  # type: ignore

from app.search_data.search_api import elastic_client


app = Flask(__name__)
# setup swagger
app.config["SWAGGER"] = {"title": "根据城市名称查询时区相关信息"}
swagger = Swagger(app)

@app.route("/name", methods=["GET"])  # type: ignore
def get_time_zone_location() -> dict[str, str]:
    """根据城市名称查询时区相关信息.

    ---
    tags:
      - 根据城市名称查询时区相关信息
    parameters:
      - name: city_name
        in: query
        type: string
        required: true
        description: 城市名(英文)
    responses:
      200:
        description: 城市名对应的时区信息
        examples:
          application/json: {"date": "2025-10-13",
                             "day_of_week": "1",
                             "es_city_name": "Mberengwa District",
                             "input_name": "Mberengwa District",
                             "time": "12:41:32",
                             "time_zone": "Etc/GMT-2",
                             "time_zone_location": "Africa/Johannesburg"}
    """
    city_name = request.args.get("city_name", default="")
    logger.info("The existence of the city is being determined...")
    loc_latitude, loc_longitude, es_name = elastic_client.search_data(city_name)
    if (loc_latitude, loc_longitude) == (float(-999), float(-999)):
        logger.info({"msg": "The city name was not found!"})
        loc_timezones = "Asia/Shanghai"
        now_time = datetime.datetime.now(pytz.timezone(loc_timezones))
        return {
            "input_name": city_name,
            "es_city_name": es_name,
            "date": now_time.strftime("%Y-%m-%d"),
            "time": now_time.strftime("%H:%M:%S"),
            "time_zone": "Etc/GMT-8",
            "day_of_week": now_time.strftime("%w"),
            "time_zone_location": loc_timezones,
        }

    tf = TimezoneFinder(in_memory=True)
    # 由经纬度得到该地区时区
    loc_timezones = tf.timezone_at(lng=loc_longitude, lat=loc_latitude)
    # 由时区得到相应的local_time
    now_time = datetime.datetime.now(pytz.timezone(loc_timezones))
    temp = now_time.strftime("%z")  # 偏移的时区
    opt = temp[0]
    if temp[2] == "0":
        if temp[1] == "1":
            offset = 10
        else:
            offset = int(temp[1])
    else:
        offset = int(temp[1:3])
    new_opt = "-" if opt == "+" else "-"
    new_time_zone = "Etc/GMT%s%d" % (new_opt, offset)
    return {
        "input_name": city_name,
        "es_city_name": es_name,
        "date": now_time.strftime("%Y-%m-%d"),
        "time": now_time.strftime("%H:%M:%S"),
        "time_zone": new_time_zone,
        "day_of_week": now_time.strftime("%w"),
        "time_zone_location": loc_timezones,
    }
