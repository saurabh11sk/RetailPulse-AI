

# from components.sidebar import sidebar_navigation
# from ai.recommendation_engine import generate_recommendations
# from services.file_upload import load_csv
# from components.upload_widget import upload_csv
# from services.data_cleaning import clean_data
# from analytics.kpi_engine import calculate_kpis
# from utils.validators import validate_columns
# from analytics.charts import (
#     revenue_by_category,
#     daily_sales,
#     top_products
# )
# from dotenv import load_dotenv

# load_dotenv()
# import streamlit as st

# from analytics.inventory_analysis import inventory_summary
# from forecasting.demand_forecast import forecast_sales
# from analytics.forecast_chart import forecast_plot
# from ai.context_builder import build_business_context
# from ai.prompt_builder import build_prompt
# from ai.gemini_service import ask_gemini
# from utils.data_summary import generate_summary

# from components.ai_actions import ai_actions

# st.set_page_config(
#     page_title="RetailPulse AI",
#     page_icon="📊",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )
# # debug = st.sidebar.checkbox("🛠 Developer Mode")
# # # -------------------------
# # Sidebar
# # -------------------------

# # with st.sidebar:
# #     st.title("📊 RetailPulse AI")
# #     st.markdown("---")

# #     st.write("### Navigation")

# #     st.success("🏠 Dashboard")
# #     st.info("📦 Inventory")
# #     st.info("📈 Forecast")
# #     st.info("🤖 AI Assistant")
# #     st.info("📄 Reports")

# #     st.markdown("---")
# #     st.caption("Google Gen AI Hackathon 2026")

# page, debug = sidebar_navigation()

# # -------------------------
# # Main Title
# # -------------------------

# st.title("📊 RetailPulse AI")

# st.subheader("AI-Powered Retail Decision Intelligence Platform")

# st.write(
#     "Upload your retail sales data to receive intelligent insights, "
#     "inventory recommendations, demand forecasts, and AI-powered business decisions."
# )

# st.divider()

# # -------------------------
# # Upload CSV
# # -------------------------

# uploaded_file = upload_csv()

# if uploaded_file is not None:

#     df = load_csv(uploaded_file)

#     if df is not None:

#         if validate_columns(df):

#             clean_df = clean_data(df)
#             recommendations = generate_recommendations(clean_df)

#             kpis = calculate_kpis(clean_df)
#             inventory = inventory_summary(clean_df)
#             forecast = forecast_sales(clean_df)

#             st.success("✅ Dataset validated successfully!")

#             st.divider()

#             # -------------------------
#             # KPI Cards
#             # -------------------------

#             col1, col2, col3, col4 = st.columns(4)

#             with col1:
#                 st.metric("💰 Revenue", f"₹{kpis['revenue']:,.2f}")

#             with col2:
#                 st.metric("📦 Products Sold", f"{kpis['products_sold']:,}")

#             with col3:
#                 st.metric("⚠ Low Stock", kpis["low_stock"])

#             with col4:
#                 st.metric("💵 Profit", f"₹{kpis['profit']:,.2f}")

#             st.divider()

#             st.subheader("📄 Clean Dataset Preview")
#             st.dataframe(clean_df.head())

#             st.write(f"**Total Records:** {len(clean_df)}")
#             st.divider()

#             col1, col2 = st.columns(2)

#             with col1:
#                 st.plotly_chart(
#                     revenue_by_category(clean_df),
#                     use_container_width=True
#                 )

#             with col2:
#                 st.plotly_chart(
#                     daily_sales(clean_df),
#                     use_container_width=True
#                 )

#             st.plotly_chart(
#                 top_products(clean_df),
#                 use_container_width=True
#             )
#             st.divider()

#             st.subheader("📦 Inventory Intelligence")

#             tab1, tab2, tab3 = st.tabs([
#                 "🔴 Low Stock",
#                 "🟡 Overstock",
#                 "🟢 Healthy Stock"
#             ])

#             with tab1:
#                 st.dataframe(inventory["low_stock"])

#             with tab2:
#                 st.dataframe(inventory["over_stock"])

#             with tab3:
#                 st.dataframe(inventory["healthy_stock"])
#                 st.divider()

#             st.subheader("📈 Demand Forecast")

#             st.plotly_chart(
#                 forecast_plot(forecast),
#                 use_container_width=True
#             )
#             st.divider()
#             if debug:
#                 st.divider()
#                 st.subheader("🛠 Developer Mode")

#                 st.write("### Low Stock Products")
#                 st.dataframe(recommendations["low_stock"])

#                 st.write("### Top Selling Products")
#                 st.dataframe(recommendations["top_products"])

#                 st.write("### Slow Selling Products")
#                 st.dataframe(recommendations["slow_products"])

#                 st.write("### Top Revenue Categories")
#                 st.dataframe(recommendations["top_categories"])

#             st.subheader("🤖 AI Business Assistant")
#             actions = ai_actions()

#             question = st.text_input(
#                 "Or ask your own question"
#             )

#             if actions["inventory"]:
#                 question = "Which products should I reorder immediately?"

#             elif actions["sales"]:
#                 question = "Summarize today's sales performance."

#             elif actions["profit"]:
#                 question = "Analyze my business profit."

#             elif actions["risk"]:
#                 question = "Identify the biggest inventory risks."

#             elif actions["executive"]:
#                 question = "Give me an executive summary of my retail business."

#             if st.button("Ask Gemini"):

#                 with st.spinner("Analyzing your business..."):

#                     context = build_business_context(clean_df)

#                     prompt = build_prompt(
#                         question,
#                         context
#                     )
#                     st.subheader("Business Context")

#                     st.code(context)
#                     st.subheader("Generated Prompt")

#                     st.code(prompt)

#                     answer = ask_gemini(prompt)

#                 st.markdown(answer)

#from services.cloud_upload import upload_to_bigquery
from components.footer import app_footer
import streamlit as st
from dotenv import load_dotenv

from components.header import app_header
from components.sidebar import sidebar_navigation
from components.upload_widget import upload_csv

from services.file_upload import load_csv
from services.data_cleaning import clean_data

from utils.validators import validate_columns

from analytics.kpi_engine import calculate_kpis
from analytics.inventory_analysis import inventory_summary

from forecasting.demand_forecast import forecast_sales

from ai.recommendation_engine import generate_recommendations
from components.theme import load_theme

from utils.session_manager import (
    initialize_session,
    save_data,
    get_data
)

from router import route_page

load_dotenv()
initialize_session()

st.set_page_config(
    page_title="RetailPulse AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
load_theme()

page, debug = sidebar_navigation()

app_header()

uploaded_file = upload_csv()

data = get_data()

if uploaded_file is not None:

    df = load_csv(uploaded_file)

    if df is not None and validate_columns(df):

        clean_df = clean_data(df)

        # if st.sidebar.button("☁ Upload to BigQuery"):

        #     success = upload_to_bigquery(clean_df)

        #     if success:
        #         st.sidebar.success("Uploaded to BigQuery")
        #     else:
        #         st.sidebar.error("BigQuery not connected")

        data = {
            "clean_df": clean_df,
            "kpis": calculate_kpis(clean_df),
            "inventory": inventory_summary(clean_df),
            "forecast": forecast_sales(clean_df),
            "recommendations": generate_recommendations(clean_df)
        }
        save_data(data)

route_page(page, data, debug)
app_footer()