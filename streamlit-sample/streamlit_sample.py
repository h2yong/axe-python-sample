"""streamlit sample."""

import numpy as np
import pandas as pd
import streamlit as st


# markdown
st.markdown("Streamlit Demo")

# 设置网页标题
st.title("一个傻瓜式构建可视化 web的 Python 神器 -- streamlit")

# 展示一级标题
st.header("1. 安装")

st.text("和安装其他包一样，安装 streamlit 非常简单，一条命令即可")
code1 = """pip3 install streamlit"""
st.code(code1, language="bash")


# 展示一级标题
st.header("2. 使用")

# 展示二级标题
st.subheader("2.1 生成 Markdown 文档")

# 纯文本
st.text("导入 streamlit 后，就可以直接使用 st.markdown() 初始化")

# 展示代码, 有高亮效果
code2 = """import streamlit as st
st.markdown('Streamlit Demo')"""
st.code(code2, language="python")

st.header("3. 数据图表支持")
st.subheader("3.1 图表组件")

df = pd.DataFrame(np.random.randn(10, 5), columns=("第%d列" % (i + 1) for i in range(5)))

st.table(df)

df = pd.DataFrame(np.random.randn(10, 5), columns=("第%d列" % (i + 1) for i in range(5)))

st.dataframe(df.style.highlight_max(axis=0))

st.subheader("3.2 监控组件")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.subheader("3.3 折线图")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

st.subheader("3.4 柱状图")
chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data)

st.subheader("3.4 面积图")
df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"])
st.map(df)
