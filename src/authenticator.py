from src.totp_generator import get_topt

def authenticate(transcription):
  assert(isinstance(transcription, str))
  
  topt = get_topt()
  attempted_pass = int("".join(transcription.split(" ")))
  print(attempted_pass, topt)

  return attempted_pass == topt
