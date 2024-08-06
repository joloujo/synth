from synth import *
import numpy as np

rate: int = 44100
s = Synth(rate)

# ---------- END OF LIKE LEAVES WE'LL FALL IN LOVE ----------
likeLeaves: waveform = np.zeros(9 * rate, float)
likeLeaves += s.line([
    Note(s.freq12TET('Db3') * Ratios.Octave * Ratios.Second, 3), 
    Note(s.freq12TET('Db4') * Ratios.Sixth, 3, 2), 
    Note(s.freq12TET('Ab4') * Ratios.Third, 3),
    ])
likeLeaves += s.line([
    Note(s.freq12TET('Db3') * Ratios.Fifth, 4), 
    Note(s.freq12TET('Db3') * Ratios.Fifth, 2),
    Note(s.freq12TET('Ab3'), 3),
    ])
# print(s.freq12TET('Db3') * Ratios.Fifth)
# print(s.freq12TET('Ab3'))
likeLeaves += s.line([
    Note(s.freq12TET('Db3') * Ratios.Third, 3), 
    Note(s.freq12TET('Db3') * Ratios.third, 3, 2), 
    Note(s.freq12TET('Ab2') * Ratios.Fifth, 3),
    ])
likeLeaves += s.line([
    Note(s.freq12TET('Db3'), 3), 
    Note(s.freq12TET('Db3'), 3, 2),
    Note(s.freq12TET('Ab2'), 3),
    ])

# ---------- CRY JUST INTONATION ----------
beat = 60 / 100
intermediateGliss = 0.25 * beat
longGliss = 2  * beat

cryJI: waveform = np.zeros(round(21 * beat * rate), float)
cryJI += s.line([
    Note(s.freq12TET('F#4'), 4 * beat, intermediateGliss), 
    Note(s.freq12TET('F#4') * Ratios.Third, 4 * beat), 
    Note(0, 1 * beat), 
    Note(s.freq12TET('B3') * Ratios.Sixth, 1 * beat, intermediateGliss),
    Note(s.freq12TET('D4') * Ratios.Fifth, 1 * beat, intermediateGliss),
    Note(s.freq12TET('G#4') * Ratios.third, 4 * beat, longGliss),
    Note(s.freq12TET('F#4') * Ratios.Third, 6 * beat),
    ])
cryJI += s.line([
    Note(s.freq12TET('F#4'), 9 * beat, intermediateGliss),
    Note(s.freq12TET('B3') * Ratios.Fifth, 1 * beat, intermediateGliss),
    Note(s.freq12TET('D4') * Ratios.Third, 1 * beat, intermediateGliss),
    Note(s.freq12TET('G#3') * Ratios.seventh, 4 * beat, longGliss),
    Note(s.freq12TET('F#4'), 6 * beat),
])
# print(s.freq12TET('F#4'), s.freq12TET('B3') * Ratios.Fifth, s.freq12TET('D4') * Ratios.Third, s.freq12TET('G#3') * Ratios.seventh, s.freq12TET('F#4'))
cryJI += s.line([
    Note(s.freq12TET('F#4'), 4 * beat, intermediateGliss), 
    Note(s.freq12TET('F#3') * Ratios.seventh, 4 * beat), 
    Note(0, 1 * beat), 
    Note(s.freq12TET('B3') * Ratios.third, 1 * beat, intermediateGliss),
    Note(s.freq12TET('D4'), 1 * beat, intermediateGliss),
    Note(s.freq12TET('G#3') * Ratios.tritone, 4 * beat, longGliss),
    Note(s.freq12TET('F#3') * Ratios.Fifth, 6 * beat),
    ])
# print(s.freq12TET('B3') * Ratios.third, s.freq12TET('D4'), s.freq12TET('G#3') * Ratios.tritone)
cryJI += s.line([
    Note(s.freq12TET('F#4'), 4 * beat, intermediateGliss), 
    Note(s.freq12TET('F#3') * Ratios.seventh, 1 * beat, intermediateGliss),
    Note(s.freq12TET('F#3') * Ratios.Fifth, 3 * beat), 
    Note(0, 1 * beat), 
    Note(s.freq12TET('B3'), 1 * beat, intermediateGliss),
    Note(s.freq12TET('D3') * Ratios.Fifth, 1 * beat, intermediateGliss),
    Note(s.freq12TET('G#3'), 4 * beat, longGliss),
    Note(s.freq12TET('F#3'), 6 * beat),
    ])

# ---------- CRY 12-TET ----------
intermediateGliss = 0.25 * beat
longGliss = 2  * beat
cry12TET: waveform = np.zeros(round(21 * beat * rate), float)
cry12TET += s.line([
    Note(s.freq12TET('F#4'), 4 * beat, intermediateGliss), 
    Note(s.freq12TET('A#4'), 4 * beat), 
    Note(0, 1 * beat), 
    Note(s.freq12TET('G#4'), 1 * beat, intermediateGliss),
    Note(s.freq12TET('A4'), 1 * beat, intermediateGliss),
    Note(s.freq12TET('B4'), 4 * beat, longGliss),
    Note(s.freq12TET('A#4'), 6 * beat),
    ])
cry12TET += s.line([
    Note(s.freq12TET('F#4'), 21 * beat),
])
cry12TET += s.line([
    Note(s.freq12TET('F#4'), 4 * beat, intermediateGliss), 
    Note(s.freq12TET('E4'), 4 * beat), 
    Note(0, 1 * beat), 
    Note(s.freq12TET('D4'), 1 * beat, intermediateGliss),
    Note(s.freq12TET('D4'), 1 * beat, intermediateGliss),
    Note(s.freq12TET('D4'), 4 * beat, longGliss),
    Note(s.freq12TET('C#4'), 6 * beat),
    ])
cry12TET += s.line([
    Note(s.freq12TET('F#4'), 4 * beat, intermediateGliss), 
    Note(s.freq12TET('E4'), 1 * beat, intermediateGliss),
    Note(s.freq12TET('C#4'), 3 * beat), 
    Note(0, 1 * beat), 
    Note(s.freq12TET('B3'), 1 * beat, intermediateGliss),
    Note(s.freq12TET('A3'), 1 * beat, intermediateGliss),
    Note(s.freq12TET('G#3'), 4 * beat, longGliss),
    Note(s.freq12TET('F#3'), 6 * beat),
    ])

# ---------- After You're Gone ----------
chord: list[float] = [
    s.freq12TET('C4'),
    s.freq12TET('C4') * Ratios.Third,
    s.freq12TET('C4') * Ratios.Fifth,
]
interval: float = Ratios.Fifth
chordSlide: waveform = np.zeros(round(6 * rate), float)
for note in chord:
    chordSlide += s.line([
    Note(note, 4, 2), 
    Note(note * interval, 2), 
    ])

# ---------- After You're Gone 12-TET ----------
beat = 60 / 100
intermediateGliss: float = 0.25 * beat
afterYoureGone: waveform = np.zeros(round(6 * beat * rate), float)
afterYoureGone += s.line([
    Note(s.freq12TET('Eb5'), 2/3 * beat),
    Note(s.freq12TET('Eb5'), 1/3 * beat),
    Note(s.freq12TET('Eb5'), 2/3 * beat),
    Note(s.freq12TET('G5'), (1/3 + 4) * beat), 
    ]) / 4
afterYoureGone += s.line([
    Note(s.freq12TET('G4'), 2/3 * beat),
    Note(s.freq12TET('Bb4'), 1/3 * beat),
    Note(s.freq12TET('C5'), 2/3 * beat),
    Note(s.freq12TET('D5'), (1/3 + 4) * beat), 
    ])
afterYoureGone += s.line([
    Note(s.freq12TET('Bb3'), 2/3 * beat),
    Note(s.freq12TET('G3'), 1/3 * beat),
    Note(s.freq12TET('G3'), 2/3 * beat),
    Note(s.freq12TET('Bb3'), (1/3 + 4) * beat), 
    ]) / 3
afterYoureGone += s.line([
    Note(s.freq12TET('Eb3'), 2/3 * beat),
    Note(s.freq12TET('Eb3'), 1/3 * beat),
    Note(s.freq12TET('Eb3'), 2/3 * beat),
    Note(s.freq12TET('Eb3'), (1/3 + 4) * beat), 
    ]) / 2

# ---------- Heart Of My Heart ----------
beat = 60 / 120
intermediateGliss: float = 0.25 * beat
longGliss = 1  * beat
heart: waveform = np.zeros(round(12 * beat * rate), float)
heart += s.line([
    Note(s.freq12TET('Db3') * Ratios.Seventh, 6 * beat, longGliss),
    Note(s.freq12TET('Ab3') * Ratios.Third, 6 * beat), 
    ]) / 4
heart += s.line([
    Note(s.freq12TET('Db3') * Ratios.Fifth, 6 * beat, longGliss),
    Note(s.freq12TET('Ab3'), 6 * beat), 
    ])
heart += s.line([
    Note(s.freq12TET('Db3') * Ratios.Third, 6 * beat, longGliss),
    Note(s.freq12TET('Ab2') * Ratios.Fifth, 6 * beat), 
    ]) / 3
heart += s.line([
    Note(s.freq12TET('Db3'), 3 * beat, intermediateGliss),
    Note(s.freq12TET('Db3') * Ratios.Second, 1 * beat, intermediateGliss),
    Note(s.freq12TET('Db3'), 2 * beat, longGliss),
    Note(s.freq12TET('Ab2'), 6 * beat), 
    ]) / 2

# ---------- One Moment in Time ----------
beat = 60 / 60
shortGliss: float = 0.25 * beat
oneMoment: waveform = np.zeros(round(8 * beat * rate), float)
oneMoment += s.line([
    Note(s.freq12TET('Db4') * Ratios.Sixth, 2 * beat),
    Note(s.freq12TET('Bb3') * Ratios.seventh, 2/3 * beat),
    Note(s.freq12TET('Db4') * Ratios.Sixth, 2/3 * beat),
    Note(s.freq12TET('Db5'), 2/3 * beat),
    Note(s.freq12TET('Eb4') * Ratios.third, 2 * beat, shortGliss),
    Note(s.freq12TET('Gb4'), 2 * beat), 
    ]) / 4
oneMoment += s.line([
    Note(s.freq12TET('Db4') * Ratios.Fifth, 1 * beat, shortGliss),
    Note(s.freq12TET('Db4') * Ratios.Fourth, 1 * beat),
    Note(s.freq12TET('Bb3') * Ratios.Fifth, 2/3 * beat),
    Note(s.freq12TET('Db4') * Ratios.Third, 2/3 * beat),
    Note(s.freq12TET('Db4') * Ratios.Fifth, 2/3 * beat),
    Note(s.freq12TET('Eb4') * Ratios.Second, 1 * beat, shortGliss),
    Note(s.freq12TET('Eb4'), 1 * beat, shortGliss),
    Note(s.freq12TET('Gb3') * Ratios.seventh, 2 * beat),
    ])
oneMoment += s.line([
    Note(s.freq12TET('Db4'), 2 * beat),
    Note(s.freq12TET('Bb3') * Ratios.third, 2/3 * beat),
    Note(s.freq12TET('Db4'), 2/3 * beat),
    Note(s.freq12TET('Db3') * Ratios.Sixth, 2/3 * beat),
    Note(s.freq12TET('Eb3') * Ratios.Fifth, 2 * beat, shortGliss),
    Note(s.freq12TET('Gb3') * Ratios.Third, 2 * beat), 
    ]) / 3
oneMoment += s.line([
    Note(s.freq12TET('Db3') * Ratios.Third, 2 * beat),
    Note(s.freq12TET('Bb3'), 2/3 * beat),
    Note(s.freq12TET('Db3') * Ratios.Fifth, 2/3 * beat),
    Note(s.freq12TET('Db3') * Ratios.Third, 2/3 * beat),
    Note(s.freq12TET('Eb3'), 2 * beat, shortGliss),
    Note(s.freq12TET('Gb2') * Ratios.Fifth, 2 * beat), 
    ]) / 2
