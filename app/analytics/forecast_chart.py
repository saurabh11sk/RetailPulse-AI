import plotly.express as px


def forecast_plot(forecast):
    fig = px.line(
        forecast,
        x="ds",
        y="yhat",
        title="30-Day Revenue Forecast"
    )

    return fig