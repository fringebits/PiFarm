import smbus

class Bus:
    def __init__(self, bus_index):
        self._index = bus_index
        self._bus = smbus.SMBus(self._index)

    def read_i2c_block_data(self, address, cmd, len):
        return self._bus.read_i2c_block_data(address, cmd, len)