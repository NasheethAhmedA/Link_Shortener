import random

mapping = {
    "A": "x",
    "B": "g",
    "C": "k",
    "D": "Z",
    "E": "v",
    "F": "R",
    "G": "s",
    "H": "p",
    "I": "W",
    "J": "q",
    "K": "a",
    "L": "y",
    "M": "B",
    "N": "m",
    "O": "j",
    "P": "C",
    "Q": "e",
    "R": "T",
    "S": "D",
    "T": "U",
    "U": "L",
    "V": "i",
    "W": "h",
    "X": "o",
    "Y": "F",
    "Z": "n",
    "a": "G",
    "b": "z",
    "c": "K",
    "d": "H",
    "e": "r",
    "f": "J",
    "g": "t",
    "h": "I",
    "i": "w",
    "j": "f",
    "k": "b",
    "l": "c",
    "m": "E",
    "n": "u",
    "o": "M",
    "p": "V",
    "q": "S",
    "r": "d",
    "s": "P",
    "t": "A",
    "u": "Q",
    "v": "O",
    "w": "Y",
    "x": "l",
    "y": "N",
    "z": "X",
}


def LinkHash(string: str) -> str:
    random.seed(len(string))
    hashed = ""
    for ch in string:
        if ch not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            continue
        hashed += mapping[ch]
    return "".join(
        [
            random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
            for s in range(5)
        ]
    )
