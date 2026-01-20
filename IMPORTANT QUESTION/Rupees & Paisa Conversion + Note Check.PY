paisa = int(input("Enter total paisa: "))

rupees = paisa // 100
remaining_paisa = paisa % 100

print(f"{rupees} Rupees and {remaining_paisa} Paisa")

# Check if rupees can be formed using only 5 and 10 notes
possible = False
for i in range(rupees // 5 + 1):
    if (rupees - 5 * i) % 10 == 0:
        possible = True
        break

print("Only 5 & 10 Rupee Notes Possible:", "Yes" if possible else "No")
