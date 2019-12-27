from src.totp_generator import get_topt
from src.config import loadConfig

def authenticate(transcription):
  assert(isinstance(transcription, str))
  config = loadConfig()['totp']
  
  topt = str(get_topt())
  while len(topt) != config['length']:
    p = "0" + topt
    topt = p

  attempted_pass = "".join(transcription.split(" "))

  return attempted_pass == topt
