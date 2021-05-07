
import time
import esc.bus
import esc.sensor_tmp102

def main():
    bus = esc.Bus(1)
    sen = esc.SensorTMP102(bus)

    #while True:
    val = sen.readTemp()
    print(val)
    #time.sleep(1)

if __name__ == "__main__":
    main()