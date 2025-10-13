"""layout sample."""

import dash
import pandas as pd
import plotly.express as px

from dash import dcc, html
from dash.dependencies import Input, Output


# 准备一些示例数据
df = pd.DataFrame(
    {
        "城市": ["北京", "上海", "广州", "深圳", "北京", "上海", "广州", "深圳"],
        "产品": ["A", "B", "A", "C", "B", "C", "B", "A"],
        "销售额": [100, 150, 120, 200, 110, 160, 130, 180],
    }
)

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("销售数据分析仪表盘"),
        html.Div(
            [
                html.Label("选择城市:"),
                dcc.Dropdown(id="city-dropdown", options=[{"label": i, "value": i} for i in df["城市"].unique()], value="北京", multi=False),
            ]
        ),
        dcc.Graph(id="sales-bar-chart"),
    ]
)


# 定义回调函数, 根据选择的城市更新图表
@app.callback(Output("sales-bar-chart", "figure"), Input("city-dropdown", "value"))
def update_graph(selected_city):
    """根据选择的城市更新图表."""
    filtered_df = df[df["城市"] == selected_city]
    return px.bar(filtered_df, x="产品", y="销售额", title=f"{selected_city} 各产品销售额")


if __name__ == "__main__":
    app.run(debug=True)
