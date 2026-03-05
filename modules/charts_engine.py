import plotly.express as px

def bar_chart(df, x, y):

    fig = px.bar(df, x=x, y=y)
    return fig


def line_chart(df, x, y):

    fig = px.line(df, x=x, y=y)
    return fig


def scatter_chart(df, x, y):

    fig = px.scatter(df, x=x, y=y)
    return fig
