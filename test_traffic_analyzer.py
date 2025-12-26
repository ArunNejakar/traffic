from traffic_analyzer import analyze_traffic


def test_low_congestion():
    result = analyze_traffic("MG Road", 40, 45)
    assert result["congestion"] == "LOW"
    assert result["suggested_action"] == "NORMAL FLOW"


def test_moderate_congestion():
    result = analyze_traffic("Ring Road", 80, 30)
    assert result["congestion"] == "MODERATE"
    assert result["suggested_action"] == "SIGNAL TIMING ADJUSTMENT"


def test_high_congestion():
    result = analyze_traffic("Silk Board", 150, 15)
    assert result["congestion"] == "HIGH"
    assert result["suggested_action"] == "TRAFFIC DIVERSION REQUIRED"
