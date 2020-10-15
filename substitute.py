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
   elif mode == 'E':
       shift=shift
   else:
       import sys
       sys.exit('enter a valid mode ("E" or "D")')
   alphabet = 'abcdefghijklmnopqrstuvwxyz'
   #seed = 42  # the secret key known by both parties 
   import random
   random.seed(seed)

   new_alphabet = list(alphabet)
   random.shuffle(new_alphabet)
   print(new_alphabet)
   # Python3 program to Split string into characters 
   def split(word): 
        return [char for char in word]

   sabc = split(new_alphabet)
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
           #print("anything else")
           #print(a)
           m.append(a)
   print('The initial message was:')
   print(''.join(m))
   return

for i in list(range(1, shift+1)):
    print('--If the test shift was', i)
    crypt(message,i,seed,mode)
    print('--------------')
crypt(message,shift,seed,mode)
