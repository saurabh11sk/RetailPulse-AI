def calculate_business_score(kpis):

    score = 100

    score -= kpis["low_stock"] * 2

    if kpis["profit"] < 0:
        score -= 20

    if score < 0:
        score = 0

    if score > 100:
        score = 100

    return score