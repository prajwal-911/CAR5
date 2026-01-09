import sys


if len(sys.argv) == 4:
    script_name = sys.argv[0]
    distance = float(sys.argv[1])
    speed = float(sys.argv[2])
    road_type = sys.argv[3].lower()
else:
    
    distance = 100.0
    speed = 50.0
    road_type = "city"


if road_type == "highway":
    mileage = 20  
elif road_type == "city":
    mileage = 15   
elif road_type == "offroad":
    mileage = 10   
else:
    print("Invalid road type! Use: highway, city, or offroad.")
    sys.exit()


trip_time_hours = distance / speed


fuel_used = distance / mileage

print("Distance (km):", distance)
print("Speed (km/h):", speed)
print("Road Type:", road_type)
print("Estimated Trip Time (hours):", trip_time_hours)
print("Estimated Fuel Used (liters):", fuel_used)
print("Car program running")
print("empty ")