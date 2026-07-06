def generate_insights(kpis):

    insights = []

    if kpis["low_stock"] > 10:
        insights.append(
            "⚠ High number of products require immediate restocking."
        )

    if kpis["profit"] < 0:
        insights.append(
            "🔴 Business is currently running at a loss."
        )
    else:
        insights.append(
            "🟢 Business is generating positive profit."
        )

    if kpis["revenue"] > 1000000:
        insights.append(
            "📈 Revenue crossed ₹10 Lakhs."
        )

    return insights