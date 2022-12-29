
import smbus

class Device:
    def __init__(self, bus: smbus, address):
        self._bus = bus
        self._address = address

    # def write(self, buffer, start, end):
    #     if (end is None):
    #         end = len(buffer)

    #     # I can't tell if 'start' is the destination or the first byte in the buffer.
    #     # if it's the first byte in the buffer, what is the destination??

    #     return self._bus.write_i2c_block_data(self._address, start, list(buffer[:end]))

    def read(self, buffer):
        count = len(buffer)
        return self._bus.read_i2c_block_data(self._address, 0, count)

    def read(self, buffer, count):
        #should make sure buffer has enough space?
        #count = len(buffer)
        return self._bus.read_i2c_block_data(self._address, 0, count)

    def readinto(self, buffer):
        count = len(buffer)
        data = self._bus.read_i2c_block_data(self._address, 0, count)
        buffer[0:len(data)] = data
