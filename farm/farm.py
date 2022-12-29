import farm
import logging
import time
logger = logging.getLogger()

def run():
    ## init the farm    
    sensors = farm.SensorArray()
    sensors.append(farm.Sensor_tmp102('test'))

    while True:
        sensors.read()
        sensors.publish()
        time.sleep(60)
