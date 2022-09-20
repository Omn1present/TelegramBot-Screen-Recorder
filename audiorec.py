import pyaudio
import wave
from pydub import AudioSegment

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 15
WAVE_OUTPUT_FILENAME = "result.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=2,
                frames_per_buffer=chunk)
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(p.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
while True:
    data = stream.read(chunk, exception_on_overflow=False)
    waveFile.writeframes(data)


