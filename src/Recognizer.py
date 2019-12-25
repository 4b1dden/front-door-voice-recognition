import os
import speech_recognition as sr
from src.CustomRecorder import CustomRecorder 

class Recognizer:
  def __init__(self, lang="en-US",seconds=3):
    self.language = lang

    self.recognizer = sr.Recognizer()
    self.recorder = CustomRecorder(seconds)
    self.TIMEOUT_BEFORE_RECORDING = 3

    self.recorder.setTimeoutBeforeRecording(self.TIMEOUT_BEFORE_RECORDING)
  
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
  
