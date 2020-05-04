"""
Service is going to transcribe audio files audio
links for dependency issues:
https://github.com/bambocher/pocketsphinx-python/issues/28
brew install portaudio
pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio
"""
import speech_recognition as sr
import os
from pathlib import Path

from services.exceptions import FileNotSupported


class TranscriberService(object):

    def __init__(self, debug=False):
        self.recognizer = sr.Recognizer()
        self.debug = debug

        # supported audio files according to sphinx
        self._supportedFiles = [
            "wav",
            "mp3",
            "raw"
        ]
        pass

    def is_file_supported(self, file_abs_path):
        basename = os.path.basename(file_abs_path)
        info = os.path.splitext(basename)
        extension = ((info[1])[1:]).lower()
        return self._supportedFiles.__contains__(extension)

    def convert_to_string(self, file_abs_path):
        if not self.is_file_supported(file_abs_path):
            raise FileNotSupported(f"The {self.__class__.__name__} can not handle this type of file : {file_abs_path}")
        with sr.AudioFile(file_abs_path) as source:
            audio = self.recognizer.record(source)
        try:
            text = self.recognizer.recognize_sphinx(audio)
            if self.debug:
                print("[DEBUG]", text)
            return text
        except sr.UnknownValueError:
            print("[ERROR] Sphinx could not understand audio")
        except sr.RequestError as e:
            print("[ERROR] Sphinx error; {0}".format(e))


# transcriber = TranscriberService(debug=True)
# p = Path("example/english.wav").resolve()
# print(str(p))
# transcriber.convert_to_string(str(p))
