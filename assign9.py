
seconds = int(input("Enter total seconds: "))

hours = seconds // 3600
remaining_seconds = seconds % 3600

minutes = remaining_seconds // 60
final_seconds = remaining_seconds % 60

print(seconds, "second =", hours, "Hour,", minutes, "Minute and", final_seconds, "Second.")
