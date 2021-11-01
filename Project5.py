#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Amna Khalid
October 31, 2018.
Project5.py
This program displays cryptography.
"""
def readfile (filename):
    '''
    This function opens a file, reads it and then converts it into
    a single string variable.
    PARAMETERS:
        filename - name of the file the function is going to open
    RETURN VALUE:
        data - the string that it returns from the file
    '''
    file = open(filename,'r')
    data = file.read()
    file.close()
    
    return data
        
    
def decode(cipher, key):
    '''
    This function deciphers a file.
    PARAMETERS:
        cipher - the file that needs to be deciphered
        key - number of spaces the letters have to move
    RETURN VALUE:
        s - the decoded text
        
    key = 17
    source = Frankenstein by Mary Shelly - Letter 1
    '''
    s = ''
    for x in range(0,len(cipher)):
        c = cipher[x]
        if c.isalpha():
            t = ord(cipher[x]) - 65
            l = ((t - key) % 26) + 65
            c = chr(l)
        s = s + c
        
    return s
            
def encode (plain, key):
    '''
    This function turns a file into a cipher.
    PARAMETERS:
        plain - the file that needs to be ciphered
        key - number of spaces the letters have to move
    RETURN VALUE:
        s - encoded version of the text
        
    Source = Dr. Jekyll and Mr. Hyde by Robert Louis Stevenson
    '''
    s = ''
    for x in range(0,len(plain)):
        c = plain[x]
        if c.isalpha():
            t = ord(plain[x]) - 65
            l = ((t + key) % 26) + 65
            c = chr(l)
            
        s = s + c
    return s

def main():
    '''
    Calls other functions and tries different keys for the decode 
    function.
    '''
    f1 = readfile('cipher.txt')
    for key in range(0,26):
        d = decode(f1,key)
        print(key,':','\n', d, '\n')
    f2 = readfile('plain.txt')
    e = encode(f2, 11)
    print(e)
    
main()
    
        
        
        