#Created by Clare Johnson 2015 clare.johnson@coleggwent.ac.uk
import math
import random
global prime, root


def secretnumber ():
    secret = int(random.randint(0,100))
    return secret

print ("Alice and Bob agree the prime")
prime = 17
print ("The prime is ",prime, "\n")


print ("Alice and Bob agree the primitive root to use")
root = 3
print ("The root is",root, "\n")


print ("At this stage, Alice, Bob & Eve all know the prime and the root", "\n")

#Alice chooses a secret number
alicesecret = secretnumber()
print ("Alice chooses a secret number",alicesecret)


#Bob chooses a secret number (bs)
bobsecret = secretnumber()
print ("Bob chooses a secret number", bobsecret, "\n")

#Alice sends her public key to Bob
print ("Alice calculates her public key as A = root ^ alicesecret mod prime")
alicepublic = (root ** alicesecret) % prime
print ("Alice's public key is",alicepublic, "\n")

#Bob sends his public key to Alice
print ("Bob calculates his public key as B = root ^ bobsecret mod prime")
bobpublic = (root ** bobsecret) % prime
print ("Bob's public key is", bobpublic, "\n")

print ("Alice and Bob exchange their public keys")
print ("Eve now knows Alice and Bob's public keys", "\n")

#Alice now calculates the shared key K:
print ("Alice calculates the shared key as K = B ^ alicesecret mod prime")
alicekey = (bobpublic ** alicesecret) % prime


#And Bob calculates the shared key K:
print ("Bob calculates the shared key as K = A ^ bobsecret mod prime")
bobkey = (alicepublic ** bobsecret) % prime
print ("Alice calculates the shared key and gets", alicekey)
print ("Bob calculates the shared key and gets", bobkey, "\n")

#Both Alice and Bob now share a key which Eve cannot calculate
print ("Eve does not know the shared private key that Alice & Bob can now use")
print ("Poor Eve :(", "\n")
print ("If you have found this Python snippet useful, please let me know!")


