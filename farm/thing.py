import farm
import time
import thingspeak
import sys
import json
import logging
logger = logging.getLogger()

things = farm.Config('things.json')

class Thing:
    TestDelay = 10

    def Create(name, field_map=None):
        config = things.get(f'thing-{name}')
        if config is None:
            return None
        result = Thing(name, field_map)
        result.config = config
        return result

    def __init__(self, name, field_map=None):
        logger.debug(f'Creating thing {name}...')
        self.name = name
        self.field_map = field_map
        self.last_sample = None
        self.config = things.get(f'thing-{self.name}')

    def publish(self, sample):
        ch = self._channel('write')
        if ch is None:
            return False

        assert sample is not None

        data = {}

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
        logger.info(f'Thing.publish {self.name}, data={data}')

        ch.update(data)

        if "pytest" in sys.modules:       
            time.sleep(Thing.TestDelay)

        return True

    def read(self):
        ch = self._channel('read')

        if ch is None:
            return None

        data = {'results':1}
        
        ret = ch.get(data)
        logger.info(f'Thing.get {self.name}, data={ret}')
        result = json.loads(ret)
        logger.info(f'{type(result)}')

        if "pytest" in sys.modules:       
            time.sleep(Thing.TestDelay)

        return result

    def _channel(self, mode):
        if mode == 'write':
            return thingspeak.Channel(self.config['channel_id'], self.config['write_key'])
        if mode == 'read':
            return thingspeak.Channel(self.config['channel_id'], self.config['read_key'])
        assert False, f'Invalid mode={mode}'
