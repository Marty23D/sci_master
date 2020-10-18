#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 18:08:40 2020

@author: francesc
"""
print("Enter a message to be encrypted or decryprted:")
message = input()
print("Enter the shift that has been used to encrypt the message:")
shift = int(input())
print("Enter the seed:")
seed = int(input())
print("Enter the mode (Encrypt 'E' or decrypt 'D'):")
mode = input()

# define function
def crypt( str, shift, seed, mode):
   if mode == 'D':
       shift=-shift
       shif = -3
   elif mode == 'E':
       shift=shift
       shif = +3
   else:
       import sys
       sys.exit('enter a valid mode ("E" or "D")')
   alphabet = 'abcdefghijklmnopqrstuvwxyz'
   punct = '.,:;_?¿!-'
   #seed = 42  # the secret key known by both parties 
   import random
   random.seed(seed)

   new_alphabet = list(alphabet)
   random.shuffle(new_alphabet)
   print(new_alphabet)
   dummy_punct = list(punct)
   random.shuffle(dummy_punct)
   print(dummy_punct)
   # Python3 program to Split string into characters 
   def split(word): 
        return [char for char in word]

   sabc = split(new_alphabet)
   spunct = split(dummy_punct)
   #smessage = split(message)
   m=[]
   #sABC=split(ABC)

   values=list(range(1, len(sabc)+1))
   d = dict(zip(sabc, values))
   rev_d = dict(zip(values, sabc))
   p_values=list(range(1, len(spunct)+1))
   p_d = dict(zip(spunct, p_values))
   p_rev_d = dict(zip(p_values, spunct))

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
       elif (a.islower()!=True)&(a.lower() in d):
           #print("lower")
           #print(a)
           if (d[a.lower()] + shift) > 26:
               shi = shift - 26
           if (d[a.lower()] + shift) < 1:
               shi = shift + 26
           else:
               shi = shift
           dum = rev_d[d[a.lower()]+shi]
           m.append(dum.upper())      
       else:
           if (p_d[a] + shif) > 9:
               shi = shif - 9
           if (p_d[a] + shif) < 1:
               shi = shif + 9
           else:
               shi = shift
           dum = p_rev_d[p_d[a]+shi]
           m.append(p_rev_d[p_d[a]+shi])
   print('The initial message was:')
   print(''.join(m))
   return

#for i in list(range(1, shift+1)):
#    print('--If the test shift was', i)
#    crypt(message,i,seed,mode)
#    print('--------------')
crypt(message,shift,seed,mode)
