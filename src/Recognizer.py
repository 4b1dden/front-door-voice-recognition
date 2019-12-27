import os
import speech_recognition as sr
from src.CustomRecorder import CustomRecorder 
import src.constants as constants

class Recognizer:
  def __init__(self, seconds=None, lang=constants.LANG_SK):
    self.language = lang

    self.recognizer = sr.Recognizer()
    self.recorder = CustomRecorder(seconds if seconds else None)
  
  def setLanguage(self, lang):
    self.language = lang

  def printConfig(self):
    print("Lang: {}".format(self.language))

  def setFileName(self, filename):
    self.recorder.setFileName(filename)
  
  def getFileName(self):
    return self.recorder.getFileName()

  def setRecordingLength(self, seconds):
    self.recorder.setRecordingLength(seconds)

  def getRecordingLength(self):
    return self.recorder.getRecordingLength()

  def removeRecordingFile(self):
    filename = self.recorder.getFileName()
    if os.path.exists(filename):
      os.remove(filename)
      print("{} removed.".format(filename))

  def listenAndTranscribe(self):
    print("Initiating listening & transcription session.")
    self.printConfig()

    self.recorder.recordAndWriteToFile()

    with sr.WavFile(self.recorder.getFileName()) as source:
      audio = self.recognizer.record(source)    
      transcript = self.recognizer.recognize_google(audio, language=self.language)

      self.removeRecordingFile()

      return transcript
  
