import pyaudio
import wave
import sys
import time
import src.constants as constants
import yaml

from src.config import loadConfig

def delay(l):
    for i in range(l,0,-1):
      sys.stdout.write(str(i)+' ')
      sys.stdout.flush()
      time.sleep(1)
    sys.stdout.write('\n')

class CustomRecorder:
  def __init__(self, seconds):
    config = loadConfig()['recorder']
    
    self.FORMAT = pyaudio.paInt16
    self.CHANNELS = config['channels']
    self.RATE = config['rate']
    self.CHUNK = config['chunk_size']
    self.RECORD_SECONDS = config['record_length'] 
    self.WAVE_OUTPUT_FILENAME = config['output_filename']
    self.TIMEOUT_BEFORE_RECORDING = config['timeout_before_recording']
    self.audio = pyaudio.PyAudio()

  def setFileName(self, filename):
    assert(isinstance(filename, str))
    self.WAVE_OUTPUT_FILENAME = filename
  
  def setRecordingLength(self, seconds):
    assert(isinstance(seconds, int))
    self.RECORD_SECONDS = seconds

  def getRecordingLength(self):
    return self.RECORD_SECONDS

  def getFileName(self):
    return self.WAVE_OUTPUT_FILENAME

  def setTimeoutBeforeRecording(self, seconds):
    assert(isinstance(seconds, int))
    self.TIMEOUT_BEFORE_RECORDING = seconds

  def getTimeoutBeforeRecording(self):
    return self.TIMEOUT_BEFORE_RECORDING

  def printConfig(self):
    print("rate: {}".format(self.RATE))
    print("chunk size: {}".format(self.CHUNK))
    print("output file: {} ".format(self.WAVE_OUTPUT_FILENAME))
    print(constants.BOLD + constants.CYAN + "recording length: {} seconds".format(self.RECORD_SECONDS) + constants.END)

  def recordAndWriteToFile(self):
    self.printConfig()
    stream = self.audio.open(
      format=self.FORMAT, channels=self.CHANNELS,
      rate=self.RATE, input=True,
      frames_per_buffer=self.CHUNK
    )

    print("CustomRecorder will be recording in...")
    delay(self.TIMEOUT_BEFORE_RECORDING)
    print("Recording...")

    frames = []
    
    for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
        data = stream.read(self.CHUNK, exception_on_overflow=False)
        frames.append(data)
    print("recording finished.")

    stream.stop_stream()
    stream.close()
    self.audio.terminate()

    waveFile = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(self.CHANNELS)
    waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
    waveFile.setframerate(self.RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    print("finished writing to {}.".format(self.WAVE_OUTPUT_FILENAME))

 
