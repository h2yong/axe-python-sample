"""测试城市获取的time_zone_location和time_zone是否正确."""

from app.server.http_server import app


test_client = app.test_client()


def test_loc_time_server() -> None:
    response = test_client.get("/name", headers={"Content-Type": "application/json"}, query_string={"city_name": "Mberengwa District"})

    print(response.json)
    assert response.status_code == 200
    assert response.json["time_zone_location"] == "Africa/Johannesburg"
    assert response.json["es_city_name"] == "Mberengwa District"
    assert response.json["time_zone"] == "Etc/GMT-2"
