# engine/risk_logic.py

def calculate_risk_level(score):
    if score >= 20: return "CRITICAL"
    if score >= 15: return "HIGH"
    if score >= 7:  return "MEDIUM"
    return "LOW"

def get_residual_score(likelihood, impact):
    # Proportionality logic: Mitigations usually reduce likelihood more than impact
    res_l = max(1, likelihood - 2)
    res_i = max(1, impact - 1)
    score = res_l * res_i
    return score, calculate_risk_level(score)