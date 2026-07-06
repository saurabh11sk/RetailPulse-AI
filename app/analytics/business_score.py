def calculate_business_score(kpis):

    score = 100

    score -= kpis["low_stock"] * 2

    if kpis["profit"] < 0:
        score -= 20

    score = max(0, min(score, 100))

    return score