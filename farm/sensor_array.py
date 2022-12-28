from .sensor import Sensor

# represents an array of sensors to sample
class SensorArray:
    def __init__(self):
        self.array = []
        self.samples = []

    def append(self, sensor:Sensor):
        self.array.append(sensor)

    def read(self):
        ret = []
        for s in self.array:
            ret.append(s.read())
        return ret

    def publish(self):
        for s in self.array:
            s.publish()