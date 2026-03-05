import plotly.express as px
import plotly.graph_objects as go


def generate_chart(df, chart_type, x=None, y=None, color=None):

    if chart_type == "Bar":
        fig = px.bar(df, x=x, y=y, color=color)

    elif chart_type == "Line":
        fig = px.line(df, x=x, y=y, color=color)

    elif chart_type == "Scatter":
        fig = px.scatter(df, x=x, y=y, color=color)

    elif chart_type == "Histogram":
        fig = px.histogram(df, x=x)

    elif chart_type == "Box":
        fig = px.box(df, x=x, y=y)

    elif chart_type == "Violin":
        fig = px.violin(df, x=x, y=y)

    elif chart_type == "Pie":
        fig = px.pie(df, names=x, values=y)

    elif chart_type == "Sunburst":
        fig = px.sunburst(df, path=[x], values=y)

    elif chart_type == "Treemap":
        fig = px.treemap(df, path=[x], values=y)

    elif chart_type == "Area":
        fig = px.area(df, x=x, y=y)

    elif chart_type == "Density Heatmap":
        fig = px.density_heatmap(df, x=x, y=y)

    elif chart_type == "3D Scatter":
        fig = px.scatter_3d(df, x=x, y=y, z=color)

    elif chart_type == "Bubble":
        fig = px.scatter(df, x=x, y=y, size=color)

    else:
        fig = None

    return fig
