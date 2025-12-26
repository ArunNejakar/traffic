def analyze_traffic(junction_name, vehicle_count, avg_speed):
    """
    Analyze traffic congestion level based on vehicle count and average speed
    """

    if avg_speed >= 40 and vehicle_count <= 50:
        congestion = "LOW"
        action = "NORMAL FLOW"

    elif avg_speed >= 20 and vehicle_count <= 100:
        congestion = "MODERATE"
        action = "SIGNAL TIMING ADJUSTMENT"

    else:
        congestion = "HIGH"
        action = "TRAFFIC DIVERSION REQUIRED"

    return {
        "junction": junction_name,
        "vehicle_count": vehicle_count,
        "average_speed": avg_speed,
        "congestion": congestion,
        "suggested_action": action
    }
