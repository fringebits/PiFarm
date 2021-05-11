
import time
from smbus2 import SMBus, i2c_msg

tempConvert = {
    'C': lambda x: x,
    'K': lambda x: x+273.15,
    'F': lambda x: x*9/5+32,
    'R': lambda x: (x+273.15)*9/5
}

_SHTC3_ADDRESS = 0x70 # Address of the SHTC3
_WRITE_COMMAND_DELAY = 0.01

def make_writemsg(command):
    return i2c_msg.write(_SHTC3_ADDRESS, [command >> 8, command & 0xff])

def write_command(bus, command, delay = _WRITE_COMMAND_DELAY):
    #msg = i2c_msg.write(_SHTC3_ADDRESS, [command >> 8, command & 0xff])
    msg = make_writemsg(command)
    bus.i2c_rdwr(msg)

    if (delay > 0):
        time.sleep(delay)

def checkCrc(data, ref):
    #upper = packet >> 8
    #lower = packet & 0x00ff
    #data = [upper, lower]

    # print("data: " + data)
    print(data)
    print(ref)

    crc = 0xff
    poly = 0x31

    for byte in data:
        crc = crc ^ byte
        ii = 0
        while ii < 8:
            if (crc & 0x80) != 0:
                crc = ((crc << 1) ^ poly) & 0xff
            else:
                crc <<= 1
            ii += 1

    print(crc)
    print(ref ^ crc)

    if (ref ^ crc) != 0:
        return False

    return True

def update(bus):
    write_command(bus, 0x3517) # wakeup

    write_command(bus, 0x7ca2, 0.1) # measurement: temperature first, normal power mode

    #pkt_write = i2c_msg.write(_SHTC3_ADDRESS, [0xE1])
    pkt_read = i2c_msg.read(_SHTC3_ADDRESS, 6)
    #bus.i2c_rdwr(pkt_write, pkt_read)
    bus.i2c_rdwr(pkt_read)
    data = list(pkt_read)
    print(data)
    print(checkCrc(data[:2], data[2]))
    print(checkCrc(data[3:5], data[5]))

    rawTemp = data[0] << 8 | data[1]
    tempC = -45.0 + 175.0 * (float(rawTemp) / 65535.0)
    print(tempC)
    print(tempConvert['F'](tempC))

    rawHumidity = data[3] << 8 | data[4]
    pctHumidity = 100.0 * (float(rawHumidity) / 65535.0)
    print(pctHumidity)

def main():
    bus = SMBus(1)

    write_command(bus, 0x3517) # wakeup

    write_command(bus, 0x805d, 0.05)

    write_command(bus, 0x3517) # wakeup

    if True:
        write_command(bus, 0xefc8, 0.001) # readout of id register

        ret = i2c_msg.read(_SHTC3_ADDRESS, 3)
        bus.i2c_rdwr(ret)
        data = list(ret)
        print(data)

        id = ((data[0] & 0xff) << 8) | (data[1] & 0xff)
        print(id)

        validCrc = checkCrc(data[:2], data[2])
        print(validCrc)

    if True:
        update(bus)

    #ret = bus.read_i2c_block_data(_SHTC3_ADDRESS, 0, 3)

    #ret = bus.read_byte_data(0x70, 3) # THIS FAILS
    #print(ret)

if __name__ == "__main__":
    main()