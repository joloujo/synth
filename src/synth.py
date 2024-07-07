import pyaudio
import numpy as np
import typing
from enum import Enum

waveform = np.ndarray[typing.Any, np.dtype[np.float32]]

class Ratios(float, Enum):
    second: float = 16/15
    Second: float = 9/8
    third: float = 6/5
    Third: float = 5/4
    Fourth: float = 4/3
    tritone: float = 45/32
    Fifth: float = 3/2
    sixth: float = 8/5
    Sixth: float = 5/3
    seventh: float = 9/5
    Seventh: float = 15/8
    Octave: float = 2/1

class Note():
    def __init__(self, frequency: float, duration: float, glissDuration: float = 0):
        self.freq: float = frequency
        self.hold: float = duration - glissDuration
        self.gliss: float = glissDuration

class Synth():
    def __init__(self, rate: int):
        self.rate: int = rate
    
    def line(self, notes: list[Note]) -> waveform:
        freq: waveform = np.zeros((0), float)
        time: float = 0

        for i, note in enumerate(notes):
            hold: waveform = np.ones((round(note.hold * self.rate))) * note.freq * 2 * np.pi / self.rate
            freq = np.append(freq, hold)

            if (note.gliss > 0):
                gliss: waveform = np.linspace(note.freq * 2 * np.pi / self.rate, notes[i + 1].freq * 2 * np.pi / self.rate, int(note.gliss * self.rate))
                freq = np.append(freq, gliss)

            time += note.hold + note.gliss

        return np.sin(np.cumsum(freq))

    def relevel(self, sound: waveform, level: float|None = None) -> waveform:
        loudest = np.max(sound)
        if level:
            return sound/loudest * level
        else:
            if loudest > 1:
                return sound/loudest
            else:
                return sound

    @staticmethod
    def freq12TET(note: str) -> float:
        letter = note[0].upper()
        accidental = '' if len(note) <= 2 else note[1]
        octave = int(note[-1])

        noteNumbers = {
            'C': 12,
            'D': 14,
            'E': 16,
            'F': 17,
            'G': 19,
            'A': 21,
            'B': 23,
        }

        accidentalNumbers = {
            '': 0,
            'b': -1,
            '#': 1,
        }

        noteNumber = noteNumbers[letter] + accidentalNumbers[accidental] + 12 * octave
        freq = 440 * 2 ** ((noteNumber-69)/12)
        return freq

    def play(self, wave: waveform):

        leveledWave = self.relevel(wave, 0.50)

        p = pyaudio.PyAudio()

        stream = p.open(
            format=pyaudio.paFloat32,
            rate = self.rate,
            channels = 1,
            output=True
            )

        data = leveledWave.astype(np.float32).tobytes()

        stream.write(data)