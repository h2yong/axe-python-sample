"""使用spaCy作为工具的外文词性标注、命名实体识别服务.

reference: https://spacy.io/usage/linguistic-features
词性标注类型: https://spacy.io/api/annotation#pos-tagging
命名实体标注类型: https://spacy.io/api/annotation#named-entities
"""

import spacy  # type: ignore

from app.config import AVAILABLE_LANGUAGES


class SpacyService(object):
    """spacy服务."""

    def __init__(self, model_path_dict: dict[str, str]):
        """SpacyService包含外文(包括英文等)的词法分析方法.

        Args:
            model_path_dict (dict): 每个语种对应一个模型文件夹路径

        """
        self.model_path_dict = model_path_dict
        self.models = dict()
        for _language, model_name in self.model_path_dict.items():
            self.models[_language] = spacy.load(model_name)

    def postag(self, sentence: str, _language: str) -> list[str]:
        """对输入的外文句子中的单词进行词性标注.

        Args:
            sentence (str): 外文句子
            _language (str): 语种

        Returns:
            list: 每个单词的词性

        """
        doc = self.models[_language](sentence)
        return [token.pos_ for token in doc]

    def recognize_named_entity(self, sentence: str, _language: str) -> list[str]:
        """对输入的外文句子中的单词进行命名实体识别.

        Args:
            sentence (str): 外文句子
            _language (str): 语种

        Returns:
            list: 每个单词的命名实体识别标注。非命名实体由"O"标记, 命名实体由"B"/"I"-NER标记, B/I表示该词是命名实体的起始或中间

        """
        doc = self.models[_language](sentence)
        res = []
        for token in doc:
            if token.ent_iob_ == "O":
                res.append(token.ent_iob_)
            else:
                res.append("{}-{}".format(token.ent_iob_, token.ent_type_))
        return res

    def batch_analyze(self, sentences: list[str], _language: str) -> list[dict[str, list[str]]]:
        """对输入的外文句子进行批量分析.

        Args:
            sentences (list): 多个外文句子
            _language (str): 语种

        Returns:
            list: 每个句子的分析结果, 每个分析结果由text、tag、ner组成, 分别表示句中的单词、词性、命名实体标注

        """
        res = []
        docs = self.models[_language].pipe(sentences, batch_size=100, n_threads=3)
        for doc in docs:
            texts = [token.text for token in doc]
            postags = [token.pos_ for token in doc]
            ner_list = []
            for token in doc:
                if token.ent_iob_ == "O":
                    ner_list.append(token.ent_iob_)
                else:
                    ner_list.append("{}-{}".format(token.ent_iob_, token.ent_type_))
            res.append({"text": texts, "tag": postags, "ner": ner_list})
        return res


MODEL_PATH_DICT = {}  # 存储language对应的模型名称, 如: {"ENGLISH": "en_core_web_sm"}
for language_with_model_name in AVAILABLE_LANGUAGES:
    split_list: list[str] = language_with_model_name.split("|")
    MODEL_PATH_DICT[split_list[0]] = split_list[1]

spacy_service_object = SpacyService(MODEL_PATH_DICT)
