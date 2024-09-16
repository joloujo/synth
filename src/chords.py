import re

def note2Num(note: str) -> int | None:

    regex_match = re.match('([abcdefg][#b]?)(\d+)', note.lower())

    if regex_match == None:
        return None

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

    return noteNumbers[letter] + accidentalNumbers[accidental] + 12 * octave


def chord2Note(chord: str) -> list[int] | None:

    regex_match = re.match('([abcdefg][#b]?)(m)?', chord.lower())

    if regex_match == None:
        return None
    
    groups = regex_match.groups()
    root_note = groups[0]
    chord_type = groups[1]

    match chord_type:
        case t if t in []:
            return [1]
        case _:
            root = note2Num(root_note)
            return [1]
