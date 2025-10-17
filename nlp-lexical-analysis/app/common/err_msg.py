"""全局错误码定义."""

from typing import Any

from flask import Response, jsonify  # type: ignore


ERROR_MSG = {
    "OK": {"err_code": 0, "err_msg": "OK"},
    "PYTHON_ERR": {"err_code": 1, "err_msg": "replace with python error msg"},
    "LANGUAGE_NOT_SUPPORTED": {"err_code": 2, "err_msg": "language is not supported"},
    "PARAMS_MISSING": {"err_code": 3, "err_msg": "Parameters is missing"},
}


def get_err_msg_dict(err_code: str) -> dict[str, object] | None:
    """根据err_code获取ERROR_MSG.

    Args:
        err_code: 错误码
    Returns:
        ERROR_MSG

    """
    assert err_code in ERROR_MSG.keys()
    return ERROR_MSG.get(err_code)


def util_make_response(msg: Any, status_code: int = 200) -> Response:
    """返回Response.

    Args:
        msg: 错误码, 错误信息dict
        status_code: 状态码

    Return:
        错误码, 错误信息dict

    """
    assert isinstance(msg, dict)
    resp = jsonify(msg)
    resp.status_code = status_code
    return resp
