
import smbus

class Device:
    def __init__(self, bus: smbus, address):
        self._bus = bus
        self._address = address

    def write(self, buffer, start, end):
        self._bus.write_i2c_block_data(self._address, )
        return 0

    def read(self, buffer):
        count = len(buffer)
        return self._bus.read_i2c_block_data(self._address, 0, count)

    def read(self, buffer, count):
        #should make sure buffer has enough space?
        #count = len(buffer)
        return self._bus.read_i2c_block_data(self._address, 0, count)
