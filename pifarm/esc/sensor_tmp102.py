
_DEFAULT_ADDRESS = 0x48

_REG_CONFIG = 0x01
_REG_TLOW = 0x02
_REG_THIGH = 0x03

class SensorTMP102:
    def __init__(self, esc_bus):
        self._device = Device(esc_bus, _DEFAULT_ADDRESS)

    def readTemperature(self):
        data = self._device.block_read(_REG_TEMPERATURE, 2)
        tempC = self.bytesToTemp(data)
        print tempC
        return tempC
