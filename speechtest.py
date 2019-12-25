from src.Recognizer import Recognizer
from src import constants

r = Recognizer()
r.setLanguage(constants.LANG_SK)
r.setRecordingLength(5)

text = r.listenAndTranscribe()
print("Transcription: {}".format(text))