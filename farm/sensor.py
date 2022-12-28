import farm
import random
import logging
logger = logging.getLogger()

class Sensor():
    def __init__(self, name, field_map=None):
        logger.debug(f'Creating sensor {name}...')
        self.name = name
        self.last_sample = None
        self.thing = farm.Thing.Create(name, field_map)

    def read(self):
        self.last_sample = 0
        return self.last_sample

    def publish(self):
        if self.thing is not None:
            return self.thing.publish(self.last_sample)            
        return False

    def fetch(self):
        if self.thing is not None:
            return self.thing.read()
        return None

class RandomSensor(Sensor):
    def __init__(self, name, num_fields=3, field_map=None, sample_range=100):
        super().__init__(name, field_map)
        self.num_fields = num_fields
        self.sample_range = sample_range

    def read(self):
        ret = []
        for ii in range(self.num_fields):
            val = random.randrange(self.sample_range)
            ret.append(val)
        self.last_sample = ret
        return ret