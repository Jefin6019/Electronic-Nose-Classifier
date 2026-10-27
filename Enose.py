import serial
import csv
import time
from datetime import datetime

# ==========================
# CONFIGURATION
# ==========================
PORT = "COM3"      # Change to your ESP32 COM port
BAUD = 115200

# ==========================
# INPUT LABEL
# ==========================
label = input(
    "Enter label (Clean_Air/LPG/Smoke/Alcohol/Perfume/CO2):"
).strip()

# Create unique filename for every session
filename = f"{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

print(f"\nConnecting to {PORT}...")

ser = serial.Serial(PORT, BAUD, timeout=1)

# ESP32 resets when serial opens
time.sleep(5)
ser.reset_input_buffer()

sample_count = 0

with open(filename, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "timestamp",
        "mq2",
        "mq5",
        "mq9",
        "mq135",
        "temp",
        "humidity",
        "label"
    ])

    print(f"\nLogging to {filename}")
    print("Press CTRL+C to stop.\n")

    try:
        while True:

            line = ser.readline().decode(
                "utf-8",
                errors="ignore"
            ).strip()

            if not line:
                continue

            values = line.split(",")

            # Skip ESP32 header
            if values[0] == "mq2":
                continue

            if len(values) != 6:
                continue

            try:
                mq2 = int(values[0])
                mq5 = int(values[1])
                mq9 = int(values[2])
                mq135 = int(values[3])
                temp = float(values[4])
                humidity = float(values[5])

                row = [
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
                    mq2,
                    mq5,
                    mq9,
                    mq135,
                    temp,
                    humidity,
                    label
                ]

                writer.writerow(row)
                file.flush()

                sample_count += 1

                print(
                    f"{sample_count:05d} | "
                    f"MQ2:{mq2} MQ5:{mq5} MQ9:{mq9} MQ135:{mq135} "
                    f"T:{temp:.1f}°C H:{humidity:.1f}%"
                )

            except ValueError:
                continue

    except KeyboardInterrupt:
        print("\n=================================")
        print("Collection Finished")
        print(f"Samples : {sample_count}")
        print(f"Saved   : {filename}")
        print("=================================")

    finally:
        ser.close()