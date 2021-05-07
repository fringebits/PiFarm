
import time
import smbus
from esc import sensor_tmp102

def main():
    bus = smbus.SMBus(1)
    sen = sensor_tmp102.SensorTMP102(bus)

    while True:
        val = sen.readTemperature()
        print(val)
        time.sleep(1)

if __name__ == "__main__":
    main()