meter = int(input("Enter distance in meters: "))

km = meter // 1000               
remaining_meter = meter % 1000  

print(meter, "meter =", km, "Km and", remaining_meter, "meter.")
