import pyaudio
import numpy as np
import typing

rate = 44100
samples = rate * 9

waveform = np.ndarray[typing.Any, np.dtype[np.float32]]
    
class Note():
    def __init__(self, frequency: float, duration: float, glissDuration: float = 0):
        self.freq: float = frequency
        self.hold: float = duration - glissDuration
        self.gliss: float = glissDuration

def line(notes: list[Note]) -> waveform:
    freq: waveform = np.zeros((0), float)
    time: float = 0

    for i, note in enumerate(notes):
        hold: waveform = np.ones((int(note.hold * rate))) * note.freq * 2 * np.pi / rate
        freq = np.append(freq, hold)

        if (note.gliss > 0):
            gliss: waveform = np.linspace(note.freq * 2 * np.pi / rate, notes[i + 1].freq * 2 * np.pi / rate, int(note.gliss * rate))
            freq = np.append(freq, gliss)

        time += note.hold + note.gliss

    print(freq)

    return np.sin(np.cumsum(freq))

def relevel(sound: waveform, level: float|None = None) -> waveform:
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

def play(wave: waveform):
    p = pyaudio.PyAudio()

    stream = p.open(
        format=pyaudio.paFloat32,
        rate = rate,
        channels = 1,
        output=True
        )

    data = wave.astype(np.float32).tobytes()

    stream.write(data)

wave: waveform = np.zeros(samples, float)

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
    Note(freq12TET('Db3') * Octave * Second, 3), 
    Note(freq12TET('Db4') * Sixth, 3, 2), 
    Note(freq12TET('Ab4') * Third, 3),
    ])

wave += line([
    Note(freq12TET('Db3') * Fifth, 4), 
    Note(freq12TET('Db3') * Fifth, 2),
    Note(freq12TET('Ab3'), 3),
    ])

print(freq12TET('Db3') * Fifth)
print(freq12TET('Ab3'))

wave += line([
    Note(freq12TET('Db3') * Third, 3), 
    Note(freq12TET('Db3') * third, 3, 2), 
    Note(freq12TET('Ab2') * Fifth, 3),
    ])

wave += line([
    Note(freq12TET('Db3'), 3), 
    Note(freq12TET('Db3'), 3, 2),
    Note(freq12TET('Ab2'), 3),
    ])

wave = relevel(wave, 0.50)

play(wave)
