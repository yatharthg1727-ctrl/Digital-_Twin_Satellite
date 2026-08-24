def check_health(data):

    alerts = []

    if data["battery"] < 40:
        alerts.append("Low Battery")

    if data["temperature"] > 60:
        alerts.append("High Temperature")

    if data["fuel"] < 30:
        alerts.append("Low Fuel")

    if data["signal"] < 40:
        alerts.append("Weak Signal")

    return alerts