
from .device import Device

#
# Reference reading tmp102 device; https://github.com/n8many/TMP102py/blob/master/tmp102.py
#

_DEFAULT_ADDRESS = 0x48

_REG_TEMPERATURE = 0x00
_REG_CONFIG = 0x01
_REG_TLOW = 0x02
_REG_THIGH = 0x03

tempConvert = {
    'C': lambda x: x,
    'K': lambda x: x+273.15,
    'F': lambda x: x*9/5+32,
    'R': lambda x: (x+273.15)*9/5
}

tempConvertInv = {
    'C': lambda x: x,
    'K': lambda x: x-273.15,
    'F': lambda x: (x-32)*5/9,
    'R': lambda x: (x*5/9)-273.15
}

class SensorTMP102:
    def __init__(self, esc_bus):
        self._device = Device(esc_bus, _DEFAULT_ADDRESS)
        self._units = 'F'

    def readTemperature(self):
        data = self._device.read(_REG_TEMPERATURE, 2)
        tempC = self.bytesToTemp(data)
        result = tempConvert[self._units](tempC)
        return result

    def readConfig(self, num, location=0, length=0):
        data = self._device.read(_REG_CONFIG, 2)
        if (num == 3):
            #Full register dump
            return data
        else:
            mask = 2**length - 1
            return (data[num] >> location) & mask        

    def bytesToTemp(self, data):
            # Adjustment for extended mode
            ext = self.readConfig(1, 4, 1)
            #ext = data[1] & 0x01
            res = int((data[0] << (4+ext)) + (data[1] >> (4-ext)))

            if (data[0] | 0x7F is 0xFF):
                # Perform 2's complement operation (x = x-2^bits)
                res = res - 4096*(2**ext)
                
            # Outputs temperature in degC
            return res*0.0625