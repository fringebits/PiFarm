import json

class Config:
    DefaultFilename = 'config.json'
    PrivateFilename = 'private.json'
    Instance = None
    def Init(config = DefaultFilename, private = PrivateFilename):
        Config.Instance = Config(config, private)

    def __init__(self, config, private) -> None:
        with open(config) as f:
            self.config = json.load(f)
        with open(private) as f:
            self.private = json.load(f)

    def get(self, key):
        return self.config[key]

    def getChannelKey(self, value, mode):
        key = f'{value}-channel-{mode}'
        if key in self.private:
            return self.private[key]
        return None