from string import ascii_uppercase
import random

def Diana(Text, Key):
    return ascii_uppercase[(25 - ord(Key) - ord(Text)) % 26]

def CodeGroup(Text, Size):
        return " ".join("".join(Text[i:i+Size]) for i in range(0, len(Text), Size))

def MakeKeystream(Seed,Text):
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
    
def GetSeed(Mask,Password,Length,Seed):
    if Seed == []:
        for x in range(Length):
            Seed.append(Diana(Mask[x],Password[x]))
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

def Encipher(Alphabet1,Alphabet2,Location,Length,Text,Seed=""):
    Location = Location - 1
    Init1 = Alphabet1[Location:Location+Length]
    Init2 = Alphabet2[Location:Location+Length]
    
    Text=OnlyAZ(Text)
    Password = MakePassword(Init1,Init2)
    Seed = MakeSeed(Seed,Length)
    Mask = MakeMask(Password,Seed)
    Keystream = MakeKeystream(Seed,Text)
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
    print("w/ Mask:    "+CodeGroup("".join(Mask)+"".join(Ciphertext),5))

def Decipher(Alphabet1,Alphabet2,Location,Length,Text):
    Location = Location - 1
    Init1 = Alphabet1[Location:Location+Length]
    Init2 = Alphabet2[Location:Location+Length]
    
    Text=OnlyAZ(Text)
    Password = MakePassword(Init1,Init2)
    Mask = Text[0:Length]
    Seed = GetSeed(Mask, Password, Length,[])
    Text = Text[Length:]
    Keystream = MakeKeystream(Seed,Text)
    Plaintext = Encrypt(Mask,Text,Keystream)
    print("Init1:      "+"".join(Init1))
    print("Init2:      "+"".join(Init2))
    print("")
    print("Password:   "+Password)
    print("Mask:       "+Mask)
    print("Seed:       "+Seed)
    print("")
    print("Input:      "+CodeGroup((Text),5))
    print("Keystream:  "+CodeGroup(Keystream,5))
    print("Output:     "+CodeGroup("".join(Plaintext),5))
