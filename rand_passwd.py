#!/usr/bin/python

import sys
import random
import string

def print_err(err_str):
    raise ValueError('[Hata] >>>', err_str)

def main():
    # print ('Number of arguments:', len(sys.argv), 'arguments.')
    # print ('Argument List:', str(sys.argv))
    # file_name = sys.argv[0]
    if len(sys.argv[1:]) != 5: print_err('Parametreleri eksik girdiniz.')
    
    min_uppers = int(sys.argv[1])
    min_digits = int(sys.argv[2])
    min_puncts = int(sys.argv[3])
    passwd_len = int(sys.argv[4])
    nbr_of_passwds = int(sys.argv[5])

    min_lowers = passwd_len - (min_uppers + min_digits + min_puncts)

    if min_lowers < 1:
        print_err('Parola uzunlugunu en az ' + str(abs(1-min_lowers)) + ' arttirin.')
    if nbr_of_passwds < 1:
        print_err('Toplam parola sayisini en az ' + str(abs(1 - nbr_of_passwds)) + ' arttirin.')

    for i in range(nbr_of_passwds):
        passwd_arr = []
        passwd_arr += random.choices(string.ascii_uppercase, k=min_uppers)
        passwd_arr += random.choices(string.digits, k=min_digits)
        passwd_arr += random.choices(string.punctuation, k=min_puncts)
        passwd_arr += random.choices(string.ascii_lowercase, k=min_lowers)
        passwd_str = "".join(random.sample(passwd_arr, len(passwd_arr)))
        print(passwd_str)
    

if __name__ == '__main__':
    main()
