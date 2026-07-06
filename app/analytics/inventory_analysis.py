def inventory_summary(df):
    low_stock = df[df["Current_Stock"] <= df["Reorder_Level"]]

    over_stock = df[df["Current_Stock"] > (df["Reorder_Level"] * 3)]

    healthy_stock = df[
        (df["Current_Stock"] > df["Reorder_Level"]) &
        (df["Current_Stock"] <= df["Reorder_Level"] * 3)
    ]

    return {
        "low_stock": low_stock,
        "over_stock": over_stock,
        "healthy_stock": healthy_stock
    }