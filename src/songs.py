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
