from prophet import Prophet
import pandas as pd


def forecast_sales(df, days=30):
    sales = (
        df.groupby("Date")["Revenue"]
        .sum()
        .reset_index()
    )

    sales.columns = ["ds", "y"]

    model = Prophet(
        daily_seasonality=True
    )

    model.fit(sales)

    future = model.make_future_dataframe(periods=days)

    forecast = model.predict(future)

    return forecast[
        ["ds", "yhat", "yhat_lower", "yhat_upper"]
    ]