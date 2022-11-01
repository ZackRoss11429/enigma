import numpy as np

# plugboard configuration where letters are assigned to other letters (a-l, h-s, z-o etc) -- 10 substitutions
# then of 5 rotors 3 will be placed into one of the 3 rotor slots
# and each of those rotors to display a particular letter of its alphabet
# number of configurations: 26! / (6! * 10! * 2^10) = ~ 159,000,000,000,000,000,000
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
# every rotor has the alphabet on each side which rotates every time there's a new letter.
# The first rotor turns 1.5 index, the next 1.25 and the next 1
plugboard = [["a", "f"], ["b", "b"], ["c", "z"], ["d", "d"], ["e", "e"], ["f", "a"], ["g", "m"], ["h", "i"], ["i", "h"],
             ["j,t"], ["k", "n"], ["l", "y"], ["m", "g"], ["n", "k"], ["o", "s"], ["p", "p"], ["q", "v"], ["r", "r"],
             ["s", "o"], ["t", "j"], ["u", "u"], ["v", "q"], ["w", "w"], ["x", "x"], ["y", "l"], ["z", "c"]]
# plugboard which is configured to substitute up to 10 letters with other letters
# maximum 10 substitutions (switch both related letter indexes)

alphabetpos = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
               "u", "v", "w", "x", "y", "z"]

rotororder = [cog5, cog3, cog2]  # This places the rotors into the 3 slots
rotor1preset = "g"  # This is what letter the first rotor shifts the first letter to
rotor2preset = "j"  # This is what letter the second rotor shifts the first letter to
rotor3preset = "v"  # This is what letter the third rotor shifts the first letter to
rotororder[0] = np.roll(rotororder[0],alphabetpos.index(rotor1preset))
rotororder[1] = np.roll(rotororder[1],alphabetpos.index(rotor2preset))
rotororder[2] = np.roll(rotororder[2],alphabetpos.index(rotor3preset))
# Each letter will be shifted 3 times then each rotor will rotate its given turns

plaintext = input("Enter message:\n")  # This is what the user inputs
separated = list(plaintext) # Splits up the text input into each character and places into a list
plugboardtext = [] # This will be the text after the input letters are substituted in the configured way
for i in range(0, len(separated)):
    if separated[i] in alphabetpos: # this will ignore non-alphabet characters such as spaces/punctuation/numbers
        plugboardtext.append(plugboard[alphabetpos.index(separated[i])][1])
# This iteratively appends each substituted letter of the user's input to the plugboardtext list
print(rotororder)
print(cog5)


print(plugboardtext)
