from string import ascii_uppercase
import random

def Diana(Text, Key):
    return ascii_uppercase[(25 - ord(Key) - ord(Text)) % 26]

def CodeGroup(Text, Size):
        return " ".join("".join(Text[i:i+Size]) for i in range(0, len(Text), Size))

def MakeKeystream(Seed):
    RNG = list("".join(Seed)) + [''] * len(Text)
    for x in range(len(Text)):
        RNG[x+len(Seed)]=(Diana(RNG[x],RNG[x+1]))
    RNG = RNG[len(Seed):]
    return "".join(RNG)
   
def OnlyAZ(Text):
    Text=Text.upper()
    NText=""
    for Char in Text:
        if Char in ascii_uppercase:
            NText += Char
    return(NText)

def MakeSeed(Seed,Length):
    #Making Seed. If you want a custom seed, assign it as a string to Seed at the same length as Init and Password.
    Seed = list(Seed)
    if Seed == []:
        for x in range(Length):
            Seed.append(random.choice(ascii_uppercase))
        return "".join(Seed)
    else:
        return "".join(Seed)

def MakePassword(Init1,Init2):
    #Making Password (finding trigraphs of Init1 and Init2
    Password = []
    if len(Init1) == len(Init2):
        for x in range(len(Init1)):
            Password.append(Diana(Init1[x],Init2[x]))
    else:
        raise ValueError("Inits are not of the same length")
    return "".join(Password)

def MakeMask(Password,Seed):
    Mask = []
    for x in range(len(Seed)):
        Mask.append(Diana(Password[x], Seed[x]))
    return "".join(Mask)

def Encrypt(Mask,Text,Keystream):
    Ciphertext = []
    for x in range(len(Text)):
        Ciphertext.append(Diana(Text[x],Keystream[x]))
    return Ciphertext


Alphabet1 = list("GPLUCZKOWXBDEQNVSHTAMRJIFY")
Alphabet2 = list("WZIFNROTAXSLPGVYDJUMEHBQKC")

Length = 8
Location = 6



Text = OnlyAZ("GKGAOVGTKOTFLXVXHABPWVOWZEOUIWJ")

#Making Inits under chosen starting location and length
Init1 = Alphabet1[Location:Location+Length]
Init2 = Alphabet2[Location:Location+Length]

Password = MakePassword(Init1,Init2)
Seed = MakeSeed("YUKJZIVZ",Length)
Mask = MakeMask(Password,Seed)
Keystream = MakeKeystream(Seed)
Ciphertext = Encrypt(Mask,Text,Keystream)


print("Init1:      "+"".join(Init1))
print("Init2:      "+"".join(Init2))
print("")
print("Password:   "+Password)
print("Seed:       "+Seed)
print("Mask:       "+Mask)
print("")
print("Input:      "+CodeGroup((Text),5))
print("Keystream:  "+CodeGroup(Keystream,5))
print("Output:     "+CodeGroup("".join(Ciphertext),5))
