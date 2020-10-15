"""
This is the first homework of the scientific programming subject.
Author: Francesc Roura Adserias
Date: 20201013

Given a string and a shift, an encrypted message is issued.
"""
#message="Pbatenghyngvbaf, lbh unir fhpprrqrq va qrpelcgvat gur fgevat."

print("Enter a message to be dencrypted:")
message = input()
print("Enter the shift that has been used to encrypt the message:")
shift = int(input())

# define function
def decrypt( str, shift):
   shift=-shift
   abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
   # Python3 program to Split string into characters 
   def split(word): 
        return [char for char in word]

   sabc = split(abc)
   #smessage = split(message)
   m=[]
   #sABC=split(ABC)

   values=list(range(1, len(sabc)+1))
   d = dict(zip(sabc, values))
   rev_d = dict(zip(values, sabc))
   for a in str:
       if a.islower():
           #print("lower")
           #print(a)
           if (d[a] + shift) > 26:
               shi = shift - 26
           if (d[a] + shift) < 1:
               shi = shift + 26
           else:
               shi = shift
           m.append(rev_d[d[a]+shi])
       elif (a.islower()!=True)&(a in d):
           if (d[a] + shift) > 52:
               shi = shift - 26
           if (d[a] + shift) < 26:
               shi = shift + 26
           else:
               shi = shift
           m.append(rev_d[d[a]+shi])       
       else:
           #print("anything else")
           #print(a)
           m.append(a)
   print('The initial message was:')
   print(''.join(m))
   return

decrypt(message, shift) 
