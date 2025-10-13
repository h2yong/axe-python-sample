"""textblob简单例子."""

import pytest

from textblob import TextBlob


@pytest.mark.parametrize("text", ["这部电影真的很棒", "I love this movie. It's amazing!"])
def test_textblob(text: str):
    """情感分析测试.

    :param text: 文本内容
    """
    blob = TextBlob(text)
    if blob.sentiment.polarity > 0:
        result = "正面"
    elif blob.sentiment.polarity == 0:
        result = "中性"
    else:
        result = "负面"

    print(result)
    print(f"情感极性: {blob.sentiment.polarity}")
    print(f"主观性分数: {blob.sentiment.subjectivity}")


@pytest.mark.parametrize("text", ["this is a gaod ideo", "I havv goood speling!"])
def test_textblob_correct(text: str):
    """拼写检查和更正."""
    blob = TextBlob(text)

    corrected_blob = blob.correct()
    print(f"原文: {text}")
    print(f"更正: {corrected_blob}")
