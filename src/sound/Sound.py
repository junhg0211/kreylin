import wave
from threading import Thread

from pyaudio import PyAudio


def play_wav(path):
    def target():
        chunk = 1024
        f = wave.open(path)
        p = PyAudio()
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()), channels=f.getnchannels(),
                        rate=f.getframerate(), output=True)

        data = f.readframes(chunk)
        while data:
            stream.write(data)
            data = f.readframes(chunk)

        stream.start_stream()
        stream.close()

        p.terminate()

    thread = Thread(target=target)
    thread.start()
