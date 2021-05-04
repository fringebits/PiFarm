
import time
import esc_sensor_tmp102

def main():
    bus = EscBus(1)
    sen = EscSensorTMP102(bus)

    #while True:
    val = sen.readTemp()
    print(val)
    #time.sleep(1)

if __name__ == "__main__":
    main()