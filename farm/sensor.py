import thingspeak
import logging
logger = logging.getLogger()

import farm
import random

class Sensor:
    def __init__(self, name, field_map=None):
        logger.debug(f'Creating sensor {name}...')
        self.name = name
        self.channel = None
        self.field_map = field_map
        self.last_sample = None
        self.write_key = farm.Config.Instance.getChannelKey(self.name, 'write')
        self.read_key = farm.Config.Instance.getChannelKey(self.name, 'read')

    def read(self):
        self.last_sample = 0
        return self.last_sample

    def get_last(self):
        ch = self._channel()
        if ch is None:
            return False

        options = {'api-key':self.read_key, 'results':1}
        ch.get(options)

    def publish(self, sample = None):
        ch = self._channel()
        if ch is None:
            return False

        if sample is None:
            sample = self.last_sample

        assert sample is not None

        data = {'api-key':self.write_key}

        fields = self.field_map
        if fields is None:
            fields = [*range(1,len(sample)+1)]

        ii = 0
        for value in sample:
            if ii >= len(fields):
                # logger.debug(f'Field map only has {len(fields)}')
                break
            index = fields[ii]
            assert index <= 8, f'Field index out of range [1..8]: {index}'
            data[f'field{index}'] = value
            ii += 1
        logger.info(f'data={data}')

        ch.update(data)
        return True

    def _channel(self):
        if self.write_key == None:
            return None
        if self.channel == None:
            self.channel = thingspeak.Channel(self.name, self.write_key)
        return self.channel

class RandomSensor(Sensor):
    def __init__(self, name, field_map=None, num_fields=3, sample_range=100):
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