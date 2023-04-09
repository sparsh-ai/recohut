import yaml


class Config:
    def __init__(self, file):
        self.file = file
        with open(file, 'r') as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)

    def getConfigObject(self):
        return self.config

