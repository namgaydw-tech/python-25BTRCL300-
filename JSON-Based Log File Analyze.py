
import json

try:
    with open("logs.json", "r", encoding="utf-8-sig") as file:
        logs = json.load(file)

    info_count = 0
    warning_count = 0
    error_count = 0

    print("\nApplication Log Records:")
    print("-" * 40)

    for log in logs:
        print("Timestamp:", log["timestamp"])
        print("Level:", log["level"])
        print("Message:", log["message"])
        print("-" * 40)

        if log["level"] == "INFO":
            info_count += 1
        elif log["level"] == "WARNING":
            warning_count += 1
        elif log["level"] == "ERROR":
            error_count += 1

    print("\nLog Analysis Summary:")
    print("Total Logs:", len(logs))
    print("INFO Messages:", info_count)
    print("WARNING Messages:", warning_count)
    print("ERROR Messages:", error_count)

except FileNotFoundError:
    print("Error: logs.json file does not exist.")

except json.JSONDecodeError:
    print("Error: Invalid JSON data.")

except (KeyError, TypeError, ValueError):
    print("Error: Invalid log record structure.")

