import pyaudio
import numpy as np
import typing
import json
from enum import Enum

rate = 44100
samples = rate * 9

class NoteTypes(Enum):
    NOTE = 1 
    GLISS = 2
    
class Note():
    def __init__(self, frequency: float, duration: float, noteType: NoteTypes = NoteTypes.NOTE):
        self.frequency: float = frequency
        self.duration: float = duration
        self.type: NoteTypes = noteType

def line(notes: list[Note]) -> np.ndarray[typing.Any, np.dtype[np.float32]]:
    freq: np.ndarray[typing.Any, np.dtype[np.float32]] = np.zeros((0), float)
    time: float = 0

    for i, note in enumerate(notes):
        new: np.ndarray[typing.Any, np.dtype[np.float32]] = np.empty((0), np.float32)
        match note.type:
            case NoteTypes.NOTE:
                new = np.ones((int(note.duration * rate))) * note.frequency * 2 * np.pi / rate
            case NoteTypes.GLISS:
                nextNote = notes[i + 1]
                new = np.linspace(note.frequency * 2 * np.pi / rate, nextNote.frequency * 2 * np.pi / rate, int(note.duration * rate))

        freq = np.append(freq, new)
        time += note.duration        

    print(freq)

    return np.sin(np.cumsum(freq))

def relevel(sound: np.ndarray[typing.Any, np.dtype[np.float32]], level: float|None = None) -> np.ndarray[typing.Any, np.dtype[np.float32]]:
    loudest = np.max(sound)
    if level:
        return sound/loudest * level
    else:
        if loudest > 1:
            return sound/loudest
        else:
            return sound

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

def play(wave: np.ndarray[typing.Any, np.dtype[np.float32]]):
    p = pyaudio.PyAudio()

    stream = p.open(
        format=pyaudio.paFloat32,
        rate = rate,
        channels = 1,
        output=True
        )

    data = wave.astype(np.float32).tobytes()

    stream.write(data)

wave: np.ndarray[typing.Any, np.dtype[np.float32]] = np.zeros(samples, float)

second = 16/15
Second = 9/8
third = 6/5
Third = 5/4
Fourth = 4/3
tritone = 45/32
Fifth = 3/2
sixth = 8/5
Sixth = 5/3
seventh = 9/5
Seventh = 15/8
Octave = 2

wave += line([
    Note(freq12TET('Db3') * Octave * Second, 2), 
    Note(0, 1), 
    Note(freq12TET('Db4') * Sixth, 1), 
    Note(freq12TET('Db4') * Sixth, 2, NoteTypes.GLISS),
    Note(freq12TET('Ab4') * Third, 3),
    ])

wave += line([
    Note(freq12TET('Db3') * Fifth, 4), 
    Note(freq12TET('Db3') * Fifth, 2, NoteTypes.GLISS),
    Note(freq12TET('Ab3'), 3),
    ])

print(freq12TET('Db3') * Fifth)
print(freq12TET('Ab3'))

wave += line([
    Note(freq12TET('Db3') * Third, 2), 
    Note(0, 1), 
    Note(freq12TET('Db3') * third, 1), 
    Note(freq12TET('Db3') * third, 2, NoteTypes.GLISS),
    Note(freq12TET('Ab2') * Fifth, 3),
    ])

wave += line([
    Note(freq12TET('Db3'), 2), 
    Note(0, 1), 
    Note(freq12TET('Db3'), 1), 
    Note(freq12TET('Db3'), 2, NoteTypes.GLISS),
    Note(freq12TET('Ab2'), 3),
    ])

wave = relevel(wave, 0.90) * 0.25

play(wave)
