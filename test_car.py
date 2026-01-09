import subprocess
import sys


def run_script(args):
    """Helper function to run car.py with arguments"""
    result = subprocess.run(
        [sys.executable, "car.py"] + args,
        capture_output=True,
        text=True
    )
    return result.stdout, result.stderr


def test_default_values():
    output, _ = run_script([])
    assert "Distance (km): 100.0" in output
    assert "Speed (km/h): 50.0" in output
    assert "Road Type: city" in output
    assert "Estimated Trip Time (hours): 2.0" in output
    assert "Estimated Fuel Used (liters):" in output


def test_highway_road_type():
    output, _ = run_script(["200", "100", "highway"])
    assert "Road Type: highway" in output
    assert "Estimated Trip Time (hours): 2.0" in output
    assert "Estimated Fuel Used (liters): 10.0" in output


def test_city_road_type():
    output, _ = run_script(["150", "50", "city"])
    assert "Road Type: city" in output
    assert "Estimated Trip Time (hours): 3.0" in output
    assert "Estimated Fuel Used (liters): 10.0" in output


def test_offroad_road_type():
    output, _ = run_script(["100", "25", "offroad"])
    assert "Road Type: offroad" in output
    assert "Estimated Trip Time (hours): 4.0" in output
    assert "Estimated Fuel Used (liters): 10.0" in output


def test_invalid_road_type():
    output, _ = run_script(["100", "50", "water"])
    assert "Invalid road type!" in output
