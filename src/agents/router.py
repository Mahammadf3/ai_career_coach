def route_by_risk(state):

    risk = state["risk_level"]

    if risk == "HIGH":
        return "improvement"

    return "final_report"