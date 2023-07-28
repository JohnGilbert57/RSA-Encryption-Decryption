####################################################################################################
# Name: John Gilbert
# Class: CS4770
# Date: 09/29/2022
# File: RSA_Encrypt.py
# Description: Takes an E and N value from a file and a plain text and encrypts the message with RSA
####################################################################################################
import sys

def main():
    plaintext = input()
    e,n = input().split()
    e = int(e)
    n = int(n)
    sys.stdout.write(str(e) + " " + str(n) + '\n')
    sys.stdout.flush()
    for c in plaintext:
        sys.stdout.buffer.write(pow(ord(c), e, n).to_bytes(16, byteorder='big'))
if __name__ == "__main__":
    main()