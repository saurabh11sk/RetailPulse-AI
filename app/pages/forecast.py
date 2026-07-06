import streamlit as st

from analytics.forecast_chart import forecast_plot


def show_forecast(data):

    st.title("📈 Demand Forecast")

    if data is None:
        st.info("📁 Upload a dataset to continue.")
        return

    forecast = data["forecast"]

    st.plotly_chart(
        forecast_plot(forecast),
        use_container_width=True
    )

    st.divider()

    st.subheader("Forecast Data")

    st.dataframe(
        forecast.tail(30),
        use_container_width=True
    )