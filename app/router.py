from pages.dashboard import show_dashboard
from pages.inventory import show_inventory
from pages.forecast import show_forecast
from pages.ai_assistant import show_ai_assistant
from pages.reports import show_reports
from pages.executive_summary import show_executive_summary


def route_page(page, data, debug):

    if page == "🏠 Dashboard":
        show_dashboard(data, debug)

    elif page == "📦 Inventory":
        show_inventory(data)

    elif page == "📈 Forecast":
        show_forecast(data)

    elif page == "🤖 AI Assistant":
        show_ai_assistant(data, debug)

    elif page == "📄 Reports":
        show_reports(data)

    elif page == "📑 Executive Summary":
        show_executive_summary(data)