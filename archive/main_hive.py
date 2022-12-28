
import driver_ic2

def main():
    bus = EscBus(1)
    sen = EscSensorTMP102(bus)

    while True:
        val = sen.readTemp()
        time.sleep(1)

if __name__ == "__main__":
    main()