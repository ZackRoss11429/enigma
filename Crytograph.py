# Plugboard that connects 10 pairs of letters together so when a letter is inputted, if it's one of the substituted
# pairs then it will be replaced as the other letter of its pair 5 rotors that each have a substitution cipher (
# reordering of the alphabet). 3 can be chosen and placed in any order. Each rotor have 26 letters to shift the
# inputted letter to depending on what the rotor index is set to Ring settings which decides what order the
# substitution cipher starts in Inputted letter is shifted first, substituted then placed into the next rotor. When a
# letter has passed through the rotors, it will go through the reflector's substitution cipher then ran backwards
# through the rotors Once that process is done, the first rotor will rotate by one. After it reaches the letter which
# allows the next rotor to move, the second rotor rotates by one. Same process for the third rotor. Afterwards,
# it will go through the plugboard once more before appearing as the final letter in the lamp board

class Plugboard:
    def __init__(self, pairs, indexes, input):
        self.pairs = {"a": "f", "b": "b", "c": "z", "d": "d", "e": "e", "f": "a", "g": "m", "h": "i", "i": "h",
                      "j": "t", "k": "n", "l": "y", "m": "g", "n": "k", "o": "s", "p": "p", "q": "v", "r": "r",
                      "s": "o", "t": "j", "u": "u", "v": "q", "w": "w", "x": "x", "y": "l", "z": "c"}

        self.index = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
                      "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
                      "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

        self.index = ""

    def __str__(self):
        return "Word after plugboard:" f"{self.}"

    plugboardtext = Plugboard("b")



