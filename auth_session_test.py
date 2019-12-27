from src.authenticator import authenticate
from src.Recognizer import Recognizer
from src.totp_generator import get_topt

print("curr topt is {}".format(get_topt()))
r = Recognizer()
transcription = r.listenAndTranscribe()

if (authenticate(transcription)):
  print("AUTH SUCCESSFUL")
else:
  print("you done fucked up")