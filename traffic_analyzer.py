import os

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


# 🔹 Read Jenkins parameters from environment variables
junction = os.getenv("JUNCTION_NAME")
vehicle_count = int(os.getenv("VEHICLE_COUNT"))
avg_speed = int(os.getenv("AVG_SPEED"))

# 🔹 Call function
result = analyze_traffic(junction, vehicle_count, avg_speed)

# 🔹 Print output (THIS appears in Jenkins console)
print("------ Traffic Analysis Report ------")
print(f"Junction        : {result['junction']}")
print(f"Vehicle Count   : {result['vehicle_count']}")
print(f"Average Speed   : {result['average_speed']} km/h")
print(f"Congestion Level: {result['congestion']}")
print(f"Suggested Action: {result['suggested_action']}")
print("-------------------------------------")
