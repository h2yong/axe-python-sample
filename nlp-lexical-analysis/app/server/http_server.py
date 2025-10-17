"""HTTP/REST server with flask framework."""

import traceback

from flasgger import Swagger  # type: ignore
from flask import Flask, Response, request  # type: ignore
from loguru import logger  # type: ignore

from app.common.err_msg import get_err_msg_dict, util_make_response
from app.config import SUPPORT_LANGUAGES
from app.core.spacy_service import spacy_service_object


app = Flask(__name__)
# setup swagger
app.config["SWAGGER"] = {"title": "使用spacy作为工具的外文词性标注、命名实体识别服务"}
swagger = Swagger(app)


@app.route("/v1/nlp/<language>/batch", methods=["POST"])  # type: ignore
def handle_batch_analyze(language: str) -> Response:
    """批量分析, 词性、命名实体识别结果.

    ---
    tags:
      - sentences: 外文句子的列表。必填
      - text: 对应句子的单词列表。
      - tag: 对应句子的词性列表。
      - ner: 对应句子的命名实体标注。
    parameters:
      - name: language
        in: path
        type: string
        enum: ['ENGLISH']
        required: true
        default: ENGLISH
      - name: body
        in: body
        required: true
        schema:
          properties:
            sentences:
              type: array
              items:
                type: string
    responses:
      200:
        description: 返回分析结果, 包括词性、命名实体识别结果。
        schema:
          properties:
            result:
              type: array
              items:
                type: object
                properties:
                  text:
                    type: array
                    items:
                      type: string
                  tag:
                    type: array
                    items:
                      type: string
                  ner:
                    type: array
                    items:
                      type: string
        examples:
          application/json:
            {
              "result": [
                {
                  "text": ["Autonomous", "cars", "shift", "insurance", "liability", "toward", "manufacturers"],
                  "tag": ["ADJ", "NOUN", "VERB", "NOUN", "NOUN", "ADP", "NOUN"],
                  "ner": ["O", "O", "O", "O", "O", "O", "o"]
                }
              ]
            }
    """
    logger.info("NLP batch analyze api be called: {}".format(request))
    payload = request.json
    sentences = payload.get("sentences", None)

    if sentences is None:
        return util_make_response(get_err_msg_dict("PARAMS_MISSING"))
    if language.upper() not in SUPPORT_LANGUAGES:
        return util_make_response(get_err_msg_dict("LANGUAGE_NOT_SUPPORTED"))

    try:
        result = spacy_service_object.batch_analyze(sentences, language)
    except Exception:
        logger.error(traceback.format_exc())
        return util_make_response(get_err_msg_dict("PYTHON_ERR"))

    return util_make_response({"result": result})


@app.route("/v1/nlp/<language>/postag", methods=["POST"])  # type: ignore
def handle_postag(language: str) -> Response:
    """词性标注.

    ---
    tags:
      - sentence: 外文句子。必填
    parameters:
      - name: language
        in: path
        type: string
        enum: ['ENGLISH']
        required: true
        default: ENGLISH
      - name: body
        in: body
        required: true
        schema:
          properties:
            sentence:
              type: string
    responses:
      200:
        description: 返回词性标注结果
        schema:
          properties:
            postags:
              type: array
              items:
                type: string
        examples:
          application/json:
            {
              "postags": ["ADJ", "NOUN", "VERB", "NOUN", "NOUN", "ADP", "NOUN"]
            }
    """
    logger.info("NLP posttag api be called: {}".format(request))
    payload = request.json
    sentence = payload.get("sentence", None)

    if sentence is None:
        return util_make_response(get_err_msg_dict("PARAMS_MISSING"))
    if language not in SUPPORT_LANGUAGES:
        return util_make_response(get_err_msg_dict("LANGUAGE_NOT_SUPPORTED"))

    try:
        postags = spacy_service_object.postag(sentence, language)
    except Exception:
        logger.error(traceback.format_exc())
        return util_make_response(get_err_msg_dict("PYTHON_ERR"))

    return util_make_response({"postags": postags})


@app.route("/v1/nlp/<language>/ner", methods=["POST"])  # type: ignore
def handle_ner(language: str) -> Response:
    """命名实体识别.

    ---
    tags:
      - sentence: 外文句子。必填
    parameters:
      - name: language
        in: path
        type: string
        enum: ['ENGLISH']
        required: true
        default: ENGLISH
      - name: body
        in: body
        required: true
        schema:
          properties:
            sentence:
              type: string
    responses:
      200:
        description: 返回命名实体标注结果
        schema:
          properties:
            named_entities:
              type: array
              items:
                type: string
        examples:
          application/json:
            {
              "named_entities": ["B-GPE", "I-GPE", "O", "O", "O", "O", "O"]
            }
    """
    logger.info("NLP ner api be called: {}".format(request))
    payload = request.json
    sentence = payload.get("sentence", None)

    if sentence is None:
        return util_make_response(get_err_msg_dict("PARAMS_MISSING"))
    if language not in SUPPORT_LANGUAGES:
        return util_make_response(get_err_msg_dict("LANGUAGE_NOT_SUPPORTED"))

    try:
        named_entities = spacy_service_object.recognize_named_entity(sentence, language)
    except Exception:
        logger.error(traceback.format_exc())
        return util_make_response(get_err_msg_dict("PYTHON_ERR"))

    return util_make_response({"named_entities": named_entities})
