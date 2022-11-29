# Plugboard that connects 10 pairs of letters together so when a letter is inputted, if it's one of the substituted pairs 
# then it will be replaced as the other letter of its pair
# 5 rotors that each have a substitution cipher (reordering of the alphabet). 3 can be chosen and placed in any order.
# Each rotor have 26 letters to shift the inputted letter to depending on what the rotor index is set to
# Ring settings which decides what order the substitution cipher starts in
# Inputted letter is shifted first, substituted then placed into the next rotor.
# When a letter has passed through the rotors, it will go through the reflector's substitution cipher then ran backwards through the rotors
# Once that process is done, the first rotor will rotate by one. After it reaches the letter which allows the next rotor to move, the second
# rotor rotates by one. Same process for the third rotor.
# Afterwards, it will go through the plugboard once more before appearing as the final letter in the lamp board




import numpy as np

plugboard = [["a", "f"], ["b", "b"], ["c", "z"], ["d", "d"], ["e", "e"], ["f", "a"], ["g", "m"], ["h", "i"], ["i", "h"],
             ["j", "t"], ["k", "n"], ["l", "y"], ["m", "g"], ["n", "k"], ["o", "s"], ["p", "p"], ["q", "v"], ["r", "r"],
             ["s", "o"], ["t", "j"], ["u", "u"], ["v", "q"], ["w", "w"], ["x", "x"], ["y", "l"], ["z", "c"]]

plugboardcipher = "fbzdeamihtnygkspvrojuqwxlc"

for i in range(1, 26):
    plugboard[i-1][1] = plugboardcipher[i-1]
# plugboard which is configured to substitute up to 10 letters with other letters
# maximum 10 substitutions (switch both related letter indexes)
# plugobardcipher allows for easier configuring of the plugboard

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
# These are the rotors that have not been shifted in any way.

rotorselection = {"cog1": 0, "cog2": 1, "cog3": 2, "cog4": 3, "cog5": 4}
# This dictionary allows for the correct substitution cipher to be used for the right rotor

rotorsubs = [
    [["a", "e"], ["b", "k"], ["c", "m"], ["d", "f"], ["e", "l"], ["f", "g"], ["g", "d"], ["h", "q"], ["i", "v"],
     ["j", "z"], ["k", "n"], ["l", "t"], ["m", "o"], ["n", "w"], ["o", "y"], ["p", "h"], ["q", "x"], ["r", "u"],
     ["s", "s"], ["t", "p"], ["u", "a"], ["v", "i"], ["w", "b"], ["x", "r"], ["y", "c"], ["z", "j"]],
    # Rotor 1 substitution cipher: EKMFLGDQVZNTOWYHXUSPAIBRCJ. This holds the substitution cipher for the first rotor
    [["a", "a"], ["b", "j"], ["c", "d"], ["d", "k"], ["e", "s"], ["f", "i"], ["g", "r"], ["h", "u"], ["i", "x"],
     ["j", "b"], ["k", "l"], ["l", "h"], ["m", "w"], ["n", "t"], ["o", "m"], ["p", "c"], ["q", "q"], ["r", "g"],
     ["s", "z"], ["t", "n"], ["u", "p"], ["v", "y"], ["w", "f"], ["x", "v"], ["y", "o"], ["z", "e"]],
    # Rotor 2 substitution cipher: AJDKSIRUXBLHWTMCQGZNPYFVOE. This holds the substitution cipher for the second rotor
    [["a", "b"], ["b", "d"], ["c", "f"], ["d", "h"], ["e", "j"], ["f", "l"], ["g", "c"], ["h", "p"], ["i", "r"],
     ["j", "t"], ["k", "x"], ["l", "v"], ["m", "z"], ["n", "n"], ["o", "y"], ["p", "e"], ["q", "i"], ["r", "w"],
     ["s", "g"], ["t", "a"], ["u", "k"], ["v", "m"], ["w", "u"], ["x", "s"], ["y", "q"], ["z", "o"]],
    # Rotor 3 substitution cipher: BDFHJLCPRTXVZNYEIWGAKMUSQO. This holds the substitution cipher for the third rotor
    [["a", "e"], ["b", "s"], ["c", "o"], ["d", "v"], ["e", "p"], ["f", "z"], ["g", "j"], ["h", "a"], ["i", "y"],
     ["j", "q"], ["k", "u"], ["l", "i"], ["m", "r"], ["n", "h"], ["o", "x"], ["p", "l"], ["q", "n"], ["r", "f"],
     ["s", "t"], ["t", "g"], ["u", "k"], ["v", "d"], ["w", "c"], ["x", "m"], ["y", "w"], ["z", "d"]],
    # Rotor 4 substitution cipher: ESOVPZJAYQUIRHXLNFTGKDCMWB. This holds the substitution cipher for the fourth rotor
    [["a", "v"], ["b", "z"], ["c", "b"], ["d", "r"], ["e", "g"], ["f", "i"], ["g", "t"], ["h", "y"], ["i", "u"],
     ["j", "p"], ["k", "s"], ["l", "d"], ["m", "n"], ["n", "h"], ["o", "l"], ["p", "x"], ["q", "a"], ["r", "w"],
     ["s", "m"], ["t", "j"], ["u", "q"], ["v", "o"], ["w", "f"], ["x", "e"], ["y", "c"], ["z", "k"]]]
# Rotor 5 substitution cipher: VZBRGITYUPSDNHLXAWMJQOFECK. This holds the substitution cipher for the fifth rotor

# every rotor has the alphabet on each side. Each is preset at a particular letter. Every letter is wired to another
# randomly Every letter that's inputted will go through each rotor then into a reflector which pairs every letter.
# The new letter will then go backwards through the rotors and shifted , then finally gone through the plugboard
# again. Every letter cycle, the rotor will rotate once. When a full revolution of the first is done, the second one
# rotates by one. When the second rotor fully rotates, the third will rotate once.


rotor1cipher = "NKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2cipher = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3cipher = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
rotor4cipher = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
rotor5cipher = "VZBRGITYUPSDNHLXAWMJQOFECK"
rotorciphers = [rotor1cipher, rotor2cipher, rotor3cipher, rotor4cipher, rotor5cipher]

# The above shows each of the rotors' ciphers. They are placed here and can be modified if desired

for i in range(1, 26):
    rotorsubs[0][i - 1][1] = list(rotor1cipher.lower())[i]
    rotorsubs[1][i - 1][1] = list(rotor2cipher.lower())[i]
    rotorsubs[2][i - 1][1] = list(rotor3cipher.lower())[i]
    rotorsubs[3][i - 1][1] = list(rotor4cipher.lower())[i]
    rotorsubs[4][i - 1][1] = list(rotor5cipher.lower())[i]

# the rotorsubs list shows the default substitution cipher used for each rotor. Each cipher can be edited by changing
# the strings above

alphabetpos = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
               "u", "v", "w", "x", "y", "z"]
# this list helps compare the positioning of the before and after of going through the rotors

rotororder = [cog3, cog1, cog5]  # This places the rotors into the 3 slots
rotoridentifier = ["cog3", "cog1", "cog5"]  # This is to cross-check with the rotorselection dictionary to ensure the
# correct substitution cipher is used with the right rotor

firstrotorcipher = rotorciphers[rotorselection[rotoridentifier[0]]]
rotorciphers[rotorselection[rotoridentifier[0]]] = (rotorciphers[rotorselection[rotoridentifier[0]]])[:-1] + \
                                                       (rotorciphers[rotorselection[rotoridentifier[0]]])[-1]

secondrotorcipher = rotorciphers[rotorselection[rotoridentifier[1]]]
rotorciphers[rotorselection[rotoridentifier[1]]] = (rotorciphers[rotorselection[rotoridentifier[1]]])[:-1] + \
                                                           (rotorciphers[rotorselection[rotoridentifier[1]]])[-1]

thirdrotorcipher = rotorciphers[rotorselection[rotoridentifier[2]]]
rotorciphers[rotorselection[rotoridentifier[2]]] = (rotorciphers[rotorselection[rotoridentifier[2]]])[:-1] + \
                                                               (rotorciphers[rotorselection[rotoridentifier[2]]])[-1]
# The above variables creates a reference for what each rotor has been chosen so the correct cipher can be used for it
# This is because there can be any rotor in any of the 3 positions so the code will need to know what's in each slot
# As well, this is current rolling the cipher backwards by one as later in the encoding process, it will try to detect
# When a rotor has done a full revolution by checking if the current letter the rotor is set to is the same as its start
# This will then detect a full revolution when the rotors haven't rotated as they'll be the same as the rotor preset
# Which will cause the cipher to automatically rotate


rotor1preset = "k"  # This is what letter the first rotor shifts the first letter to
rotor2preset = "q"  # This is what letter the second rotor shifts the first letter to
rotor3preset = "o"  # This is what letter the third rotor shifts the first letter to
rotororder[0] = np.roll(rotororder[0], alphabetpos.index(rotor1preset) + 2)
rotororder[1] = np.roll(rotororder[1], alphabetpos.index(rotor2preset) + 2)
rotororder[2] = np.roll(rotororder[2], alphabetpos.index(rotor3preset) + 2)
# the module above converts it to its own type of array, so it needs to be converted back to a regular list to be used
# again. On an enigma machine, each rotor is turned
rotororder[0] = list(rotororder[0])
rotororder[1] = list(rotororder[1])
rotororder[2] = list(rotororder[2])
# Each letter will be shifted and substituted 3 times then each rotor will rotate in its given way

reflector = [["a", "e"], ["b", "j"], ["c", "m"], ["d", "z"], ["e", "a"], ["f", "l"], ["g", "y"], ["h", "x"], ["i", "v"],
             ["j", "b"], ["k", "w"], ["l", "f"], ["m", "c"], ["n", "r"], ["o", "q"], ["p", "u"], ["q", "o"], ["r", "n"],
             ["s", "t"], ["t", "s"], ["u", "p"], ["v", "i"], ["w", "k"], ["x", "h"], ["y", "g"], ["z", "d"]]
# Default reflector substitution cipher: EJMZALYXVBWFCRQUONTSPIKHGD

reflectorcipher = "EJMZALYXVBWFCRQUONTSPIKHGD"  # This can be edited to change the reflector's substitution cipher
for i in range(1, 26):
    reflector[i][1] = list(reflectorcipher.lower())[i]

# The letter that is outputs from the rotors will then be substituted following a cipher used by the reflector

plaintext = input("Enter message:\n")  # This is what the user inputs
separated = (list(plaintext))  # Splits up the text input into each character and places into a list
separated = [i.lower() for i in separated]  # makes any uppercase characters lowercase

plugboardtext = []  # This will be the text after the input letters are substituted in the configured way

firstrotor = []  # This list will be the text after going through the first rotor
secondrotor = []  # This list will be the text after going through the second rotor
thirdrotor = []  # This list will be the text after going through the third rotor

reflected = []  # This list will be the text after going through the reflector
backwardthird = []  # This list will be the text after coming back through the third rotor
backwardsecond = []  # This list will be the text after coming back through the second rotor
backwardfirst = []  # This list will be the text after coming back through the first rotor
finaltext = []  # This list will be the text after going through the plugboard again. This is the final list
#  Above is more to better show every time each letter is shifted


for i in range(0, len(separated)):
    if separated[i] in alphabetpos:  # this will ignore non-alphabet characters such as spaces/punctuation/numbers
        plugboardtext.append(plugboard[alphabetpos.index(separated[i])][1])
# This iteratively appends each substituted letter of the user's input to the plugboardtext list

for i in range(0, len(plugboardtext)):

    firstrotor.append(rotorsubs[rotorselection[rotoridentifier[0]]][alphabetpos.index(plugboardtext[i])][1])
    firstrotor[i] = (rotororder[0][alphabetpos.index(firstrotor[i])])

    secondrotor.append(rotorsubs[rotorselection[rotoridentifier[1]]][rotororder[0].index(firstrotor[i])][1])
    secondrotor[i] = (rotororder[1][rotororder[0].index(secondrotor[i])])

    thirdrotor.append(rotorsubs[rotorselection[rotoridentifier[2]]][rotororder[1].index(secondrotor[i])][1])
    thirdrotor[i] = (rotororder[2][rotororder[1].index(thirdrotor[i])])

    # This iteratively will place each letter going in as where it is in the alphabet (abcd...z) and then substitute it
    # for how each rotor's substitution cipher is ordered (rzgjsirt for example). It will then do the same with this new
    # letter and count how many shifts each rotor is from abcdefg...z and then shift this letter by that amount. It will
    # do the same for every rotor. So for example: a->k->l -> l->s->q -> q->z->j

    reflected.append(reflector[rotororder[2].index(thirdrotor[i])][1])
    # The letters going into the reflector are substituted using a cipher

    backwardthird.append(rotororder[2][alphabetpos.index(reflected[i])])
    backwardthird[i] = (rotorsubs[rotorselection[rotoridentifier[2]]][rotororder[2].index(backwardthird[i])][1])

    backwardsecond.append(rotororder[1][rotororder[2].index(backwardthird[i])])
    backwardsecond[i] = (rotorsubs[rotorselection[rotoridentifier[1]]][rotororder[1].index(backwardsecond[i])][1])

    backwardfirst.append(rotororder[0][rotororder[1].index(backwardsecond[i])])
    backwardfirst[i] = (rotorsubs[rotorselection[rotoridentifier[0]]][rotororder[0].index(backwardfirst[i])][1])

    # Above shows each letter going backwards through the rotors being shifted and substituted again

    finaltext.append(plugboard[rotororder[0].index(backwardfirst[i])][1])
    # Finally, the letters are fed through the plugboard one last time

    rotororder[0] = np.roll(rotororder[0], 1)  # This shows the first rotor being rotated after every letter
    rotororder[0] = list(rotororder[0])
    reflector = np.roll(reflector, 1, axis=1)  # This shifts the reflector's substitution cipher by one every letter
    reflector = list(reflector)

    rotorciphers[rotorselection[rotoridentifier[0]]] = (rotorciphers[rotorselection[rotoridentifier[0]]])[-1] + \
                                                       (rotorciphers[rotorselection[rotoridentifier[0]]])[:-1]
    firstrotorcipher = rotorciphers[rotorselection[rotoridentifier[0]]]

    for j in range(1, 26):
        rotorsubs[rotorselection[rotoridentifier[0]]][j-1][1] = firstrotorcipher[j-1].lower()

    # This will determine the correct cipher for the selected first rotor (out of the 5) and every letter, the cipher
    # will rotate by one and thus every new letter gets a shifted substitution cipher plus one more shift than the
    # previous.
    if rotororder[0][0] == rotor1preset:
        rotororder[1] = np.roll(rotororder[1], 1)
        rotororder[1] = list(rotororder[1])
        rotorciphers[rotorselection[rotoridentifier[1]]] = (rotorciphers[rotorselection[rotoridentifier[1]]])[-1] + \
                                                           (rotorciphers[rotorselection[rotoridentifier[1]]])[:-1]
        secondrotorcipher = rotorciphers[rotorselection[rotoridentifier[1]]]

        for j in range(1, 26):
            rotorsubs[rotorselection[rotoridentifier[1]]][j - 1][1] = secondrotorcipher[j - 1].lower()

        # This will determine the correct cipher for the selected second rotor and every letter,
        # the cipher will rotate by one and thus every new letter gets a shifted substitution cipher plus one more
        # shift than the previous. This only happens when the second rotor is rotated, which only happens when its
        # previous rotor does a full revolution

        if rotororder[1][0] == rotor2preset:
            rotororder[2] = np.roll(rotororder[2], 1)
            rotororder[2] = list(rotororder[2])

            rotorciphers[rotorselection[rotoridentifier[2]]] = (rotorciphers[rotorselection[rotoridentifier[2]]])[-1] + \
                                                               (rotorciphers[rotorselection[rotoridentifier[2]]])[:-1]
            thirdrotorcipher = rotorciphers[rotorselection[rotoridentifier[2]]]

            for j in range(1, 26):
                rotorsubs[rotorselection[rotoridentifier[2]]][j - 1][1] = thirdrotorcipher[j - 1].lower()

            # This will determine the correct cipher for the selected third rotor and every letter,
            # the cipher will rotate by one and thus every new letter gets a shifted substitution cipher plus one more
            # shift than the previous. This only happens when the second rotor is rotated, which only happens when its
            # previous rotor does a full revolution

    # Every letter that's passed through will rotate the first rotor once. After a full revolution, it will rotate
    # the second rotor and after that full revolution, the third rotor will turn This makes 26^3 possible rotor
    # combinations

print("Original Text: ", ''.join(i for i in separated))
print("Text after Plugboard: ", ''.join(i for i in plugboardtext))
print("Text after First Rotor: ", ''.join(i for i in firstrotor))
print("Text after Second Rotor: ", ''.join(i for i in secondrotor))
print("Text after Third Rotor: ", ''.join(i for i in thirdrotor))
print("Text after Reflector: ", ''.join(i for i in reflected))
print("Text after going backwards through Third Rotor: ", ''.join(i for i in backwardthird))
print("Text after going backwards through Second Rotor: ", ''.join(i for i in backwardsecond))
print("Text after going backwards through First Rotor: ", ''.join(i for i in backwardfirst))
print("Text after Plugboard: ", ''.join(i for i in finaltext))

# Drawbacks
# The next rotor will rotate by one when the previous makes a full revolution. This is done by a rod pushing the
# first rotor to make it rotate. The rods for the second and third can't be rotated by its rod as it's blocked by the
# edge of the first rotor but at a point on that edge, there's a gap that allows the second rotor to be pushed (same
# process happens with the third rotor). This means that at a certain rotation of each rotor will push the next rotor
# So it's never going to be exactly a full revolution for each one.
# One difference is the reflector which will shift all of its connections by one letter. This is instead of it always
# substituting the same
# Another difference is another setting that can be changed is what substitution cipher each of the rotors/reflector use
