def generate_alerts(df):

    alerts = []

    low_stock = df[df["Current_Stock"] <= df["Reorder_Level"]]

    if len(low_stock) > 0:
        alerts.append(
            (
                "warning",
                f"{len(low_stock)} products are below the reorder level."
            )
        )

    negative_profit = df[df["Profit"] < 0]

    if len(negative_profit) > 0:
        alerts.append(
            (
                "error",
                f"{len(negative_profit)} transactions generated a loss."
            )
        )

    high_revenue = df["Revenue"].sum()

    if high_revenue > 1000000:
        alerts.append(
            (
                "success",
                "Revenue has crossed ₹10,00,000."
            )
        )

    return alerts