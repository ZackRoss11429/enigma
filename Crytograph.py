import random

# plugboard configuration where letters are assigned to other letters (a-l, h-s, z-o etc) -- 10 substitutions
# then of 5 rotors 3 will be placed into one of the 3 rotor slots and each of those rotors to display a particular letter of its alphabet
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
# every rotor has the alphabet on each side which rotates by 1 every time there's a new letter
plugboard = [["a", "f"], ["b", "b"], ["c", "z"], ["d", "d"], ["e", "e"], ["f", "a"], ["g", "m"], ["h", "i"], ["i", "h"],
             ["j,t"], ["k", "n"], ["l", "y"], ["m", "g"], ["n", "k"], ["o", "s"], ["p", "p"], ["q", "v"], ["r", "r"],
             ["s", "o"], ["t", "j"], ["u", "u"], ["v", "q"], ["w", "w"], ["x", "x"], ["y", "l"], ["z", "c"]]
# maximum 10 substitutions (switch both related letter indexes)

alphabetpos = ["0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
               "u", "v", "w", "x", "y", "z"]

rotororder = [cog5, cog3, cog2]
plaintext = input("Enter message:\n")
separated = list(plaintext)
plugboardtext = []
print(separated)
print(rotororder)
print(plugboard)
for i in range(0, len(separated)):
    #plugboardtext.append(plugboard[plugboard.index(alphabetpos.index[plugboard[i]]), 1])
    plugboardtext.append(plugboard[alphabetpos.index(separated[i])])
print(plugboardtext)
