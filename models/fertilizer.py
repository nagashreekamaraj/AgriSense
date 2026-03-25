def recommend_fertilizer(N, P, K):
    if N < 50:
        return "Add Nitrogen"
    elif P < 40:
        return "Add Phosphorus"
    elif K < 40:
        return "Add Potassium"
    return "Soil is optimal"