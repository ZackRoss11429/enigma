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


# this module will be essential for rotating lists of variables/objects


class Plugboard:  # this creates the class of 'Plugboard', the first encryptor of the input text
    def __init__(self, plaintext):  # this will initialise all the variables necessary for the plugboard to work

        pairs = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g", "h": "h", "i": "i",
                 "j": "j", "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "q", "r": "r",
                 "s": "s", "t": "t", "u": "u", "v": "v", "w": "w", "x": "x", "y": "y", "z": "z"}
        # this dictionary will be used to represent the alphabet before the plugboard is properly configured to
        # substituted.
        pairitems = list(pairs.keys())

        indexes = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
                   "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
                   "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
        #  This dictionary will equate each letter of the alphabet to its number position in the alphabet.

        plugboardconfig = "dcbawfqupyktzxoigrslhvenjm"
        #  This plugboard configuration consisting of 10 pairs of letter substitutions

        plugboardtext = [None] * len(plaintext)
        #  This creates a list that is the length of the inputted 'plaintext' for each letter to be encrypted

        self.plaintext = plaintext
        self.pairs = pairs
        self.indexes = indexes
        self.plugboardtext = plugboardtext
        self.pairitems = pairitems
        #  this just makes it easier to refer to each of the variables

        for i in range(0, 26):
            pairs[pairitems[i]] = plugboardconfig[i]
        #  this converts the 'pairs' dictionary to properly substitute pairs of letters using 'plugboardconfig'

    def plugboard(self):
        # this is the function that will use the initialised variables and settings to encrypt the input
        for i in range(0, len(self.plaintext)):
            self.plugboardtext[i] = self.pairs.get(plaintext[i])
        return "Word after plugboard: " + ''.join(self.plugboardtext)
        #  when the program is run and this function is called, it will return the now encrypted input, 'plugboardtext'


class Rotors:  # this is the rotors class that will be the second section of encryption of the inputted text
    def __init__(self, plugboardtext):  # this initialises the variables necessary for using the rotors to encrypt
        ciphers = {"I-K": "PEZUOHXSCVFMTBGLRINQJWAYDK", "II-K": "ZOUESYDKFWPCIQXHMVBLGNJRAT",
                   "III-K": "EHRVXGAOBQUSIMZFLYNWKTPDJC", "UKW-K": "IMETCGFRAYSQBZXWLHKDVUPOJN",
                   "ETW-K": "QWERTZUIOASDFGHJKPYXCVBNML"}
        #  this is a dictionary of the different possible rotors to use. Each contain a different substitution cipher
        #  where every letter of the cipher refers to what position it's now holding in the alphabet
        #  (I-K's p is a, e is b etc.)

        rotororder = ["III-K", "I-K", "ETW-K"]  # these are the three rotors that have been configured to be used for
        # the encryption

        ringsettings = [4, 2, 7]
        # this contains how many shifts the rotors will initially do as well as what they're configured to
        # so if the first rotor is set to start at 5 while its ringsetting is 4, it'll start at 9.

        rotorpreset = [4, 6, 23]
        # this is what each of the rotors are configured to start at (example: the first rotor shifts input of C to G)

        rotors = {
            'I-K': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26),
            'II-K': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26),
            'III-K': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26),
            'UKW-K': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26),
            'ETW-K': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)}
        # dictionary of all the rotors' sides where everytime one is turned which represents how much an inputted letter
        # is shifted. After every inputted letter, the rotor rotates by one so if it starts 6 it will go to 7 or at 26
        # will become 1 again


        for i in range(0, 3):
            rotors[rotororder[i - 1]] = rotors[rotororder[i - 1]][-(ringsettings[i - 1]):] + \
                                        rotors[rotororder[i - 1]][:-(ringsettings[i - 1])]
            # this will iteratively go through the 'rotororder' list to determine which rotor is being used, then it
            # will then search the rotors list for that rotor name and then rotate its number list by one

            np.roll(rotors[rotororder[i]], -ringsettings[i])
            rotors = dict(rotors)
            # this will further shift the inputted letter by however much the ring is set to
            # a rotor configured to a 4 with a ring setting of 6, every letter inputted will be shifted by 10 letters


        rotateletter = 12  # when the rotor is set the 12, the next rotor will rotated by 1

        self.ciphers = ciphers
        self.rotororder = rotororder
        self.ringsettings = ringsettings
        self.rotors = rotors
        self.rotorpreset = rotorpreset
        self.rotateletter = rotateletter


# class Reflector:

plaintext = input("Input message:\n")  # takes user input
plaintext = ''.join(filter(str.isalpha, plaintext))
# this will filter out any character that is not a letter of the alphabet, including spaces
plaintext = plaintext.lower()
# this makes any uppercase character lowercase
p = Plugboard(plaintext)
p.plugboard()
# this will run the Plugboard class with the user's input
print(p.plugboard())
# this prints what encrypted string by the plugboard outputs
r = Rotors(p)
# this runs the Rotors class using the output from the plugboard
