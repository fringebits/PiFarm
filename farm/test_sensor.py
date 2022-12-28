import thingspeak
import farm

def test_sensor():
    s = farm.RandomSensor('test')
    ret = s.read()
    assert len(ret) == 3

def test_sensor_array():
    array = farm.SensorArray()
    array.append(farm.RandomSensor('test'))
    array.append(farm.RandomSensor('foo'))
    ret = array.read()
    assert len(ret) == 2
    assert len(ret[0]) == 3
    assert len(ret[1]) == 3
    array.publish()

def test_sensor_publish():
    s = farm.RandomSensor('test')
    ret = s.read()
    assert len(ret) == 3
    assert s.publish(ret)

    s = farm.RandomSensor('test', [1, 2, 4])
    ret = s.read()
    assert len(ret) == 3
    assert s.publish(ret)
