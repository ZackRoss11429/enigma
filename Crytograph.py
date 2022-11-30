# Plugboard that connects 10 pairs of letters together so when a letter is inputted, if it's one of the substituted
# pairs then it will be replaced as the other letter of its pair 5 rotors that each have a substitution cipher (
# reordering of the alphabet). 3 can be chosen and placed in any order. Each rotor have 26 letters to shift the
# inputted letter to depending on what the rotor index is set to Ring settings which decides what order the
# substitution cipher starts in Inputted letter is shifted first, substituted then placed into the next rotor. When a
# letter has passed through the rotors, it will go through the reflector's substitution cipher then ran backwards
# through the rotors Once that process is done, the first rotor will rotate by one. After it reaches the letter which
# allows the next rotor to move, the second rotor rotates by one. Same process for the third rotor. Afterwards,
# it will go through the plugboard once more before appearing as the final letter in the lamp board

import numpy as np


class Plugboard:
    def __init__(self, plaintext):

        pairs = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g", "h": "h", "i": "i",
                 "j": "j", "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "q", "r": "r",
                 "s": "s", "t": "t", "u": "u", "v": "v", "w": "w", "x": "x", "y": "y", "z": "z"}
        pairitems = list(pairs.keys())

        indexes = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
                   "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
                   "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

        plugboardconfig = "dcbawfqupyktzxoigrslhvenjm"

        plugboardtext = [None] * len(plaintext)

        self.plaintext = plaintext
        self.pairs = pairs
        self.indexes = indexes
        self.plugboardtext = plugboardtext
        self.pairitems = pairitems

        for i in range(0, 26):
            pairs[pairitems[i]] = plugboardconfig[i]

    def plugboard(self):
        for i in range(0, len(self.plaintext)):
            self.plugboardtext[i] = self.pairs.get(plaintext[i])
        return "Word after plugboard: " + ''.join(self.plugboardtext)


class Rotors:
    def __init__(self, plugboardtext):
        ciphers = {"I-K": "PEZUOHXSCVFMTBGLRINQJWAYDK", "II-K": "ZOUESYDKFWPCIQXHMVBLGNJRAT",
                   "III-K": "EHRVXGAOBQUSIMZFLYNWKTPDJC", "UKW-K": "IMETCGFRAYSQBZXWLHKDVUPOJN",
                   "ETW-K": "QWERTZUIOASDFGHJKPYXCVBNML"}

        rotororder = ["III-K", "I-K", "ETW-K"]
        ringsettings = [4, 2, 7]

        for i in range(0, 3):
            ciphers[rotororder[i - 1]] = ciphers[rotororder[i - 1]][-(ringsettings[i - 1]):] + \
                                         ciphers[rotororder[i - 1]][:-(ringsettings[i - 1])]

            print(ciphers[rotororder[i - 1]])

        rotors = [("I-K", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)),
                  ("II-K", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)),
                  ("III-K", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)),
                  ("UKW-K", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)),
                  ("ETW-K", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26))]

        rotorpreset = [4, 6, 23]
        rotateletter = 12

        for j in range(0, 3):
            print(rotors[j][0], rotororder[j])
            #np.roll(rotors[rotors.index(rotororder[j-1])][1], rotorpreset[j-1])
            #np.array(rotors)


        self.ciphers = ciphers
        self.rotororder = rotororder
        self.ringsettings = ringsettings
        self.rotors = rotors
        self.rotorpreset = rotorpreset
        self.rotateletter = rotateletter


# class Reflector:
plaintext = input("Input message:\n")
p = Plugboard(plaintext)
print(p.plugboard())
r = Rotors(p.plugboardtext)
