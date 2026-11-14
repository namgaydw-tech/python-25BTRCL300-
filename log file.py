
try:
    error_count = 0

    with open("log.txt", "r") as file:
        for line in file:
            print(line, end="")

            if "ERROR" in line:
                error_count += 1

    print("\nTotal number of errors:", error_count)

except FileNotFoundError:
    print("Error: log.txt file does not exist.")


