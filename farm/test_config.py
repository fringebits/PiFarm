import farm
import pytest

@pytest.fixture(scope="session", autouse=True)
def logging_setup():
    farm.init_logs(True)
 
def test_config():
    farm.Config.Init()
    assert farm.Config.Instance is not None

    cfg = farm.Config.Instance
    assert cfg.get('version') is not None
    assert cfg.getChannelKey('test', 'write') is not None