def rotate_character(s_char, a_rot):
    if s_char.isalpha():  # test if char is not alpha
        num_alp = alphabet_position(s_char)  # change char to int value
        if s_char.isupper():  # encypher uppercase
            num_alp += a_rot  # encypher: rotate eac by rotation number
            if num_alp > 25:
                num_alp %= 26
            r_alp = chr(num_alp + 65)  # converting bac to char using ASCII
        else:  # encypher lowercase
            num_alp += a_rot  # encypher: rotate eac by rotation number
            if num_alp > 25:
                num_alp %= 26
            r_alp = chr(num_alp + 97)  # converting bac to char using ASCII
    else:
        r_alp = s_char
    return r_alp


def alphabet_position(alp_let):
    AlphaUpToNum = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
                    "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22,
                    "X": 23, "Y": 24, "Z": 25}
    AlphaLoToNum = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
                    "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22,
                    "x": 23, "y": 24, "z": 25}
    if alp_let.isupper():
        return AlphaUpToNum.get(alp_let)
    else:
        return AlphaLoToNum.get(alp_let)


def encrypt(start_phrase, rot_num):
    enc_phrase = ""
    for a_char in start_phrase:                         # go though each char
        enc_phrase += rotate_character(a_char, rot_num)  # add each encrypted char to the new string
    return enc_phrase
