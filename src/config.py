import yaml

def loadConfig():
  with open("settings.yaml", 'r') as stream:
      try:
          return yaml.safe_load(stream)
      except yaml.YAMLError as exc:
          print("Could not load yaml config. Ensure settings.yaml file is present. {}".format(exc))
          return {}

def dumpConfig(config):
  with open("settings.yaml", "w") as f:
    yaml.dump(config, f)