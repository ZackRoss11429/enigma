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
    def __init__(self, plaintext, backwardrotortext,
                 plugboardpass):  # this will initialise all the variables necessary for the plugboard to work

        pairs = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g", "h": "h", "i": "i",
                 "j": "j", "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "q", "r": "r",
                 "s": "s", "t": "t", "u": "u", "v": "v", "w": "w", "x": "x", "y": "y", "z": "z"}
        # this dictionary will be used to represent the alphabet before the plugboard is properly configured to
        # substituted.
        pairitems = list(pairs.keys())

        # plugboardconfig = "dcbawfqupyktzxoigrslhvenjm"
        plugboardconfig = "abcdefghijklmnopqrstuvwxyz"
        #  This plugboard configuration consisting of 10 pairs of letter substitutions

        plugboardtext = []
        #  This creates a list that is the length of the inputted 'plaintext' for each letter to be encrypted

        finaltext = []

        self.plaintext = plaintext
        self.plugboardpass = plugboardpass
        self.pairs = pairs
        self.plugboardtext = plugboardtext
        self.pairitems = pairitems
        self.finaltext = finaltext
        self.backwardrotortext = backwardrotortext
        #  this just makes it easier to refer to each of the variables

        for i in range(0, 26):
            pairs[pairitems[i]] = plugboardconfig[i]
        #  this converts the 'pairs' dictionary to properly substitute pairs of letters using 'plugboardconfig'

    def plugboard(self, plaintext, backwardrotortext, plugboardpass):
        # this is the function that will use the initialised variables and settings to encrypt the input
        for i in range(0, len(self.plaintext)):
            if not self.plugboardpass:
                self.plugboardtext.append(self.pairs.get(plaintext[i]))
            if self.plugboardpass:
                self.finaltext.append(self.pairs.get(self.backwardrotortext[i]))

        if not self.plugboardpass:
            return "Word after plugboard: " + ''.join(self.plugboardtext)

        if self.plugboardpass:
            return "Word after final plugboard: " + ''.join(self.finaltext)
        #  when the program is run and this function is called, it will return the now encrypted input, 'plugboardtext'


class Rotors:  # this is the rotors class that will be the second section of encryption of the inputted text
    ciphers = {"I": "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "II": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
               "III": "BDFHJLCPRTXVZNYEIWGAKMUSQO", "IV": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
               "V": "VZBRGITYUPSDNHLXAWMJQOFECK"}
    # this is a dictionary of the different possible rotors to use. Each contain a different substitution
    # cipher where every letter of the cipher refers to what position it's now holding in the alphabet (I-K's
    # p is a, e is b etc.)

    rotororder = ["III", "II", "I"]  # these are the three rotors that have been configured to be used for
    # the encryption

    ringsettings = [2, 1, 1]
    # this sets the initial position of each rotor's substitution cipher. a ring setting of 2 will have it start
    # 2 letters later (example: XFGHLQ will be GHLQXF)

    rotorpreset = [26, 1, 1]
    # this sets the initial position of each rotor (example: the first rotor shifts input of C
    # to G)

    rotors = {
        'I': (
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"),
        'II': (
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"),
        'III': (
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"),
        'IV': (
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"),
        'V': (
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z")}
    # dictionary of all the rotors' sides where everytime one is turned which represents how much an inputted
    # letter is shifted. After every inputted letter, the rotor rotates by one so if it starts 6 it will go
    # to 7 or at 26 will become 1 again

    rotortext = []
    backwardrotortext = []

    for i in range(3):
        ciphers[rotororder[i]] = list(ciphers[rotororder[i]])
        ciphers[rotororder[i]] = np.roll(ciphers[rotororder[i]], -(ringsettings[i] + 1))
        ciphers[rotororder[i]] = list(ciphers[rotororder[i]])
        # this will iteratively go through the 'rotororder' list to determine which rotor is being used, then it
        # will then search the ciphers list for that rotor name and then rotate the cipher by the setting number

        rotors[rotororder[i]] = np.roll(rotors[rotororder[i]], -rotorpreset[i] + 1)
        rotors[rotororder[i]] = list(rotors[rotororder[i]])
        # this will further shift the inputted letter by however much the ring is set to a rotor configured
        # to a 4 with a ring setting of 6, every letter inputted will be shifted by 10 letters

    turnover = {'I': "q", 'II': "e", 'III': "v", 'IV': "j", 'V': "z"}  # there's a physical notch on each

    # rotor that when rotated to will rotate the next rotor by one

    shifts = [[], [], []]
    ciphershifts = [[], [], []]

    def __init__(self, plugboardtext, backward, reflectortext):
        # this initialises the variables necessary for using the rotors to encrypt
        self.ciphers = Rotors.ciphers
        self.rotororder = Rotors.rotororder
        self.ringsettings = Rotors.ringsettings
        self.rotors = Rotors.rotors
        self.rotorpreset = Rotors.rotorpreset
        self.turnover = Rotors.turnover
        self.rotortext = Rotors.rotortext
        self.backwardrotortext = Rotors.backwardrotortext
        self.shifts = Rotors.shifts
        self.ciphershifts = Rotors.ciphershifts

    def rotor(self, plugboardtext, backward, reflectortext):
        alphabetpos = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                       "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        if not backward:
            for i in range(len(plugboardtext)):
                self.rotors[self.rotororder[0]] = np.roll(self.rotors[self.rotororder[0]], -1)
                self.rotors[self.rotororder[0]] = list(self.rotors[self.rotororder[0]])

                self.ciphers[self.rotororder[0]] = np.roll(self.ciphers[self.rotororder[0]], -1)
                self.ciphers[self.rotororder[0]] = list(self.ciphers[self.rotororder[0]])
                # this will rotate the first rotor before the inputted text passes through
                if self.rotors[self.rotororder[0]][0] == self.turnover[self.rotororder[0]]:
                    # this if statement will check if the first rotor has reached the turnover point and will rotate the
                    # second rotor by one while rotating the first rotor again by one (double stepping)
                    self.rotors[self.rotororder[0]] = np.roll(self.rotors[self.rotororder[0]], -1)
                    self.rotors[self.rotororder[0]] = list(self.rotors[self.rotororder[0]])

                    self.rotors[self.rotororder[1]] = np.roll(self.rotors[self.rotororder[1]], -1)
                    self.rotors[self.rotororder[1]] = list(self.rotors[self.rotororder[1]])

                    self.ciphers[self.rotororder[1]] = np.roll(self.ciphers[self.rotororder[1]], -1)
                    self.ciphers[self.rotororder[1]] = list(self.ciphers[self.rotororder[1]])
                    if self.rotors[self.rotororder[1]][0] == self.turnover[self.rotororder[1]]:
                        # this if statement will check if the second rotor has reached the turnover point and will rotate
                        # the third rotor by one while rotating the second rotor again by one (double stepping)
                        self.rotors[self.rotororder[1]] = np.roll(self.rotors[self.rotororder[1]], -1)
                        self.rotors[self.rotororder[1]] = list(self.rotors[self.rotororder[1]])

                        self.rotors[self.rotororder[2]] = np.roll(self.rotors[self.rotororder[2]], -1)
                        self.rotors[self.rotororder[2]] = list(self.rotors[self.rotororder[2]])

                        self.ciphers[self.rotororder[2]] = np.roll(self.ciphers[self.rotororder[2]], -1)
                        self.ciphers[self.rotororder[2]] = list(self.ciphers[self.rotororder[2]])

                self.shifts[0].append(self.rotors[self.rotororder[0]][0])
                self.ciphershifts[0].append(self.ciphers[self.rotororder[0]][0])
                self.shifts[1].append(self.rotors[self.rotororder[1]][0])
                self.ciphershifts[1].append(self.ciphers[self.rotororder[1]][0])
                self.shifts[2].append(self.rotors[self.rotororder[2]][0])
                self.ciphershifts[2].append(self.ciphers[self.rotororder[2]][0])

                for j in range(3):
                    self.rotortext.append(self.ciphers[self.rotororder[j]][alphabetpos.index(plugboardtext[i])].lower())
                    position = alphabetpos.index(self.rotortext[len(self.rotortext) - 1])
                    alphabetpos = np.roll(alphabetpos, -ord(self.rotors[self.rotororder[j]][0]) - 97)
                    alphabetpos = list(alphabetpos)
                    self.rotortext[len(self.rotortext) - 1] = alphabetpos[position]

            return "Word after rotor 1: " + ''.join(self.rotortext[:len(plugboardtext)]) + \
                   "\nWord after rotor 2: " + ''.join(self.rotortext[len(plugboardtext):len(plugboardtext) * 2]) + \
                   "\nWord after rotor 3: " + ''.join(self.rotortext[len(plugboardtext) * 2:len(plugboardtext) * 3])

        if backward:
            for i in range(len(reflectortext)):
                for j in range(2, 0, -1):
                    position = alphabetpos.index(reflectortext[i])
                    alphabetpos = np.roll(alphabetpos, -ord(self.shifts[j][i]) - 97)
                    alphabetpos = list(alphabetpos)
                    self.ciphers[self.rotororder[j]] = np.roll((self.ciphers[self.rotororder[j]]),
                                                               -ord(self.ciphershifts[j][i]) - 97)
                    self.ciphers[self.rotororder[j]] = list(self.ciphers[self.rotororder[j]])
                    self.backwardrotortext.append(alphabetpos[position])
                    self.backwardrotortext.append(self.ciphers[self.rotororder[j]][alphabetpos.index(
                        self.backwardrotortext[len(self.backwardrotortext) - 1])].lower())

            return "Word after returning through rotor 3: " + ''.join(self.backwardrotortext[:len(reflectortext)]) + \
                   "\nWord after returning through rotor 2: " + ''.join(
                self.backwardrotortext[len(reflectortext):len(reflectortext) * 2]) + \
                   "\nWord after returning through rotor 1: " + ''.join(
                self.backwardrotortext[len(reflectortext) * 2:len(reflectortext) * 3])


class Reflector:
    def __init__(self, rotortext):
        ukwb = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        etw = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        reflectortext = []

        self.reflectortext = reflectortext
        self.etw = etw
        self.ukwb = ukwb

    def reflector(self, rotortext):
        for i in range(len(rotortext)):
            self.reflectortext.append(self.ukwb[self.etw.index(rotortext[i].upper())].lower())
        return "Word after reflector: " + ''.join(self.reflectortext)


plaintext = input("Input message:\n")  # takes user input
plaintext = ''.join(filter(str.isalpha, plaintext))
# this will filter out any character that is not a letter of the alphabet, including spaces
plaintext = plaintext.lower()
# this makes any uppercase character lowercase
p = Plugboard(plaintext, [], False)
# this will run the Plugboard class with the user's input
print(p.plugboard(plaintext, [], False))
# this prints what encrypted string by the plugboard outputs
r = Rotors(p.plugboardtext, False, [])
# this runs the Rotors class using the output from the plugboard
print(r.rotor(p.plugboardtext, False, []))

r.rotortext = r.rotortext[len(p.plugboardtext) * 2:len(p.plugboardtext) * 3]
re = Reflector(r.rotortext)
print(re.reflector(r.rotortext))

r = Rotors(p.plugboardtext, True, re.reflectortext)
print(r.rotor(p.plugboardtext, True, re.reflectortext))

r.backwardrotortext = r.backwardrotortext[len(re.reflectortext) * 2:len(re.reflectortext) * 3]
p = Plugboard(plaintext, r.backwardrotortext, True)
print(p.plugboard(plaintext, r.backwardrotortext, True))
