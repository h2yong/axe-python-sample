import streamlit as st
import pandas as pd
from collections import Counter

st.set_page_config(layout="centered")  # 设置页面布局

st.title("文本词频分析器")

# 用户输入文本
text_input = st.text_area("请在这里输入您的文本：", height=200)

if text_input:
    words = text_input.lower().split()
    word_counts = Counter(words)

    st.subheader("词频统计结果：")
    # 将结果展示为表格
    df = pd.DataFrame(word_counts.items(), columns=["词语", "出现次数"]).sort_values(by="出现次数", ascending=False)
    st.dataframe(df)

    st.subheader("最常见的词语：")
    num_words = st.slider("显示多少个最常见的词语？", 1, 20, 5)

    top_words = word_counts.most_common(num_words)
    for word, count in top_words:
        st.write(f"- **{word}**: {count} 次")
