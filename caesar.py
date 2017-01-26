def alphabet_position(letter):
    """
    Recieves a letter and returns the 0-based numberical position of
    that letter within the alphabet.
    """
    if letter.isupper():
        alphaidx=ord(letter)-65
    else:
        alphaidx=ord(letter)-97
    return alphaidx

def rotate_character(char, rot):
    """
    shifts character "char" by rotation amount "rot" to the right, wrapping if amount is past alphabet.
    """
    if char.isalpha():
        new_char = ((alphabet_position(char)+rot)%26)+(ord(char)-alphabet_position(char))
        new_char = chr(new_char)
    else:
        return char
    return new_char

def encrypt(text, rot):
    encrypt_txt =""
    for i in text:
        encrypt_txt=encrypt_txt+(rotate_character(i, rot))
    return encrypt_txt

