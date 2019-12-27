import yaml
from os import path

basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "settings.yaml"))

def loadConfig():
  with open(filepath, 'r') as stream:
      try:
          return yaml.safe_load(stream)
      except yaml.YAMLError as exc:
          print("Could not load yaml config. Ensure settings.yaml file is present. {}".format(exc))
          return {}

def dumpConfig(config):
  with open("settings.yaml", "w") as f:
    yaml.dump(config, f)