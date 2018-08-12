#Author: JC
#Date: 8/9/2018
#Version: 1.0

# The mapping from digit to corresponding characters
MAPPING = ('0','1','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ')

def phone_mnemonic(phone_number):
    def phone_mnemonic_helper(digit):
        if digit == len(phone_number):
        # if all digits are processed, so add partical_mnemonic t omnemonics.
        # add a copy since subsequent cals modify partial_mnemonic
            mnemonics.append(''.join(partial_mnemonics))
        else:
            # try all possible characters for this digits
            for c in MAPPING[int(phone_number[digit])]:
                partial_mnemonics[digit]= c
                phone_mnemonic_helper(digit + 1)
    mnemonics, partial_mnemonics = [], [0] * len(phone_number)
    phone_mnemonic_helper(0)
    return len(mnemonics),mnemonics

phone_number = '123'
print(phone_mnemonic(phone_number))