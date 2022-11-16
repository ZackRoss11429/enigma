import numpy as np

# plugboard configuration where letters are assigned to other letters (a-l, h-s, z-o etc) -- 10 substitutions
# then of 5 rotors 3 will be placed into one of the 3 rotor slots
# and each of those rotors to display a particular letter of its alphabet
# number of configurations: 26! / (6! * 10! * 2^10) = ~ 159,000,000,000,000,000,000

plugboard = [["a", "f"], ["b", "b"], ["c", "z"], ["d", "d"], ["e", "e"], ["f", "a"], ["g", "m"], ["h", "i"], ["i", "h"],
             ["j,t"], ["k", "n"], ["l", "y"], ["m", "g"], ["n", "k"], ["o", "s"], ["p", "p"], ["q", "v"], ["r", "r"],
             ["s", "o"], ["t", "j"], ["u", "u"], ["v", "q"], ["w", "w"], ["x", "x"], ["y", "l"], ["z", "c"]]
# plugboard which is configured to substitute up to 10 letters with other letters
# maximum 10 substitutions (switch both related letter indexes)

cog1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z"]
cog2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z"]
cog3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z"]
cog4 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z"]
cog5 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z"]
# every rotor has the alphabet on each side. Each is preset at a particular letter. Every letter is wired to another randomly
# Every letter that's inputted will go through each rotor then into a reflector which pairs every letter.
# The new letter will then go backwards through the rotors and shifted , then finally gone through the plugboard again.
# Every letter cycle, the rotor will rotate once. When a full revolution of the first is done, the second one rotates by one.
# When the second rotor fully rotates, the third will rotate once.

alphabetpos = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
               "u", "v", "w", "x", "y", "z"]
# this list helps compare the positioning of the before and after of going through the rotors

rotororder = [cog5, cog3, cog2]  # This places the rotors into the 3 slots
rotor1preset = "h"  # This is what letter the first rotor shifts the first letter to
rotor2preset = "s"  # This is what letter the second rotor shifts the first letter to
rotor3preset = "k"  # This is what letter the third rotor shifts the first letter to
rotororder[0] = np.roll(rotororder[0], alphabetpos.index(rotor1preset) + 2)
rotororder[1] = np.roll(rotororder[1], alphabetpos.index(rotor2preset) + 2)
rotororder[2] = np.roll(rotororder[2], alphabetpos.index(rotor3preset) + 2)
#  the module above converts it to its own type of array so it needs to be converted back to a regular list to be used again
rotororder[0] = list(rotororder[0])
rotororder[1] = list(rotororder[1])
rotororder[2] = list(rotororder[2])
# Each letter will be shifted and substituted 3 times then each rotor will rotate in its given way

reflector = [["a", "e"], ["b", "j"], ["c", "m"], ["d", "z"], ["e", "a"], ["f", "l"], ["g", "y"], ["h", "x"], ["i", "v"],
             ["j", "b"], ["k", "w"], ["l", "f"], ["m", "c"], ["n", "r"], ["o", "q"], ["p", "u"], ["q", "o"], ["r", "n"],
             ["s", "t"], ["t", "s"], ["u", "p"], ["v", "i"], ["w", "k"], ["x", "h"], ["y", "g"], ["z", "d"]]
# Reflector substitution cipher: EJMZALYXVBWFCRQUONTSPIKHGD

# Every letter is paired with another so after going through the rotors, they're substituted for their letter pair

plaintext = input("Enter message:\n")  # This is what the user inputs
separated = list(plaintext)  # Splits up the text input into each character and places into a list
plugboardtext = []  # This will be the text after the input letters are substituted in the configured way
firstrotorsub = [["a", "e"], ["b", "k"], ["c", "m"], ["d", "f"], ["e", "l"], ["f", "g"], ["g", "d"], ["h", "q"], ["i", "v"],
                 ["j", "z"], ["k", "n"], ["l", "t"], ["m", "o"], ["n", "w"], ["o", "y"], ["p", "h"], ["q", "x"], ["r", "u"],
                 ["s", "s"], ["t", "p"], ["u", "a"], ["v", "i"], ["w", "b"], ["x", "r"], ["y", "c"], ["z", "j"]]
# Rotor 1 substitution cipher: EKMFLGDQVZNTOWYHXUSPAIBRCJ. This holds the substitution cipher for the first rotor
firstrotor = []  # This list will be the text after going through the first rotor
secondrotorsub = [["a", "a"], ["b", "j"], ["c", "d"], ["d", "k"], ["e", "s"], ["f", "i"], ["g", "r"], ["h", "u"], ["i", "x"],
                 ["j", "b"], ["k", "l"], ["l", "h"], ["m", "w"], ["n", "t"], ["o", "m"], ["p","c"], ["q", "q"], ["r", "g"],
                 ["s", "z"], ["t", "n"], ["u", "p"], ["v", "y"], ["w", "f"], ["x", "v"], ["y", "o"], ["z", "e"]]
# Rotor 2 substitution cipher: AJDKSIRUXBLHWTMCQGZNPYFVOE. This holds the substitution cipher for the second rotor
secondrotor = []  # This list will be the text after going through the second rotor
thirdrotorsub = [["a", "b"], ["b", "d"], ["c", "f"], ["d", "h"], ["e", "j"], ["f", "l"], ["g", "c"], ["h", "p"], ["i", "r"],
                 ["j", "t"], ["k", "x"], ["l", "v"], ["m", "z"], ["n", "n"], ["o", "y"], ["p","e"], ["q", "i"], ["r", "w"],
                 ["s", "g"], ["t", "a"], ["u", "k"], ["v", "m"], ["w", "u"], ["x", "s"], ["y", "q"], ["z", "o"]]
# Rotor 3 substitution cipher: BDFHJLCPRTXVZNYEIWGAKMUSQO. This holds the substitution cipher for the third rotor
thirdrotor = []  # This list will be the text after going through the third rotor
reflected = []  # This list will be the text after going through the reflector
backwardthird = []  # This list will be the text after coming back through the third rotor
backwardsecond = []  # This list will be the text after coming back through the second rotor
backwardfirst = []  # This list will be the text after coming back through the first rotor
finalplugboardtext = []  # This list will be the text after going through the plugboard again
#  Above is more to better show every time each letter is shifted

finalseparated = []  # This will be where the final text will be spliced into

for i in range(0, len(separated)):
    if separated[i] in alphabetpos:  # this will ignore non-alphabet characters such as spaces/punctuation/numbers
        plugboardtext.append(plugboard[alphabetpos.index(separated[i])][1])
# This iteratively appends each substituted letter of the user's input to the plugboardtext list

for i in range(0, len(plugboardtext)):

    firstrotor.append(firstrotorsub[alphabetpos.index(plugboardtext[i])][1])
    firstrotor[i] = (rotororder[0][alphabetpos.index(plugboardtext[i])]) # Seems that the rotor doesn't rotate every letter input
    secondrotor.append(secondrotorsub[rotororder[0].index(firstrotor[i])][1])
    secondrotor[i] = (rotororder[1][rotororder[0].index(firstrotor[i])])
    thirdrotor.append(thirdrotorsub[rotororder[1].index(secondrotor[i])][1])
    thirdrotor = (rotororder[2][rotororder[1].index(secondrotor[i])])
    # This iteratively checks the positioning of each letter in the previous alphabet set and places it in the same index
    # in the new index of the list. So the first rotor is set to G so if P passes through, it sees what position P is in
    # then shifts it to the same position in the rotor (initial G -> L -> B -> Z for example)

    reflected.append(reflector[rotororder[2].index(thirdrotor[i])][1])
    # Can't seem to figure out how to search the letter pair in the reflector and use that

    rotororder[0] = np.roll(rotororder[0], 1)
    rotororder[0] = list(rotororder[0])
    if rotororder[0] == rotor1preset:
        rotororder[1] = np.roll(rotororder[1], 1)
        rotororder[1] = list(rotororder[1])
        if rotororder[1] == rotor2preset:
            rotororder[2] = np.roll(rotororder[2], 1)
            rotororder[2] = list(rotororder[2])
    # Every letter that's passed through will rotate the first rotor once.
    # After a full revolution, it will rotate the second rotor and after thats full revolution, the third rotor will turn
    # This makes 26^3 possible rotor combinations
print(thirdrotor)
print(reflected)
# finaltext = ''.join(i for i in finalseparated)
# print(finaltext)
