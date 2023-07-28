#####################################################################################################
# Name: John Gilbert
# Class: CS4770
# Date: 09/29/2022
# File: RSA_Decrypt.py
# Description: Takes an E and N value from a file and a cypher text and decrypts the message with RSA
#####################################################################################################
from math import sqrt
import sys

def gcd(num_one, num_two):
    if(num_one < num_two):
        lower_num = num_one
    else:
        lower_num = num_two
    for i in reversed(range(lower_num)):
        if (num_one % i == 0 and num_two % i == 0):
            return i
    return 1

def main():
    e,n = sys.stdin.buffer.readline().split()
    e = int(e)
    n = int(n)
    cypher_text = sys.stdin.buffer.read()
    p = 0 
    q = 0
    for i in range(2, int(sqrt(n))):
        if (n%i == 0):
            p = i
            q = int(n/i)
            break
    if (p == 0 and q == 0):
        print("Error could not find p and q")
        exit(1)
    lambda_p = p - 1
    lambda_q = q - 1
    lambda_n = int(abs(lambda_p * lambda_q))
    d = pow(e, -1, lambda_n)
    if (e > lambda_n and gcd(e, lambda_n) != 1):
        print("An error occured: e = " + str(e) + " lambda_n = " + str(lambda_n) + " gcd = " + str(gcd(e, lambda_n)))
        exit(1)
    barr = bytearray()
    for c in cypher_text:
        barr.append(c)
        if(len(barr) % 16 == 0):
            sys.stdout.write(chr(pow(int.from_bytes(barr, byteorder='big'), d, n)))
            barr = bytearray()
    sys.stdout.write('\n' + str(e) + " " + str(n))
    

if __name__ == "__main__":
    main()