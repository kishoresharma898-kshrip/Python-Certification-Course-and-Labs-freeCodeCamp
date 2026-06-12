'''
This is a workshop, where you need to create a program called caesar cipher 
which is an encryption method that shifts letters in the alphabet to encode 
messages.'''

# Code:

def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

input_text = 'Courage is found in unlikely places.'

encrypted_text = encrypt(input_text, 13)
decrypted_text = decrypt(encrypted_text, 13)
#print(input_text)
print(encrypted_text) # Output: Pbhentr vf sbhaq va hayvxryl cynprf.
print(decrypted_text) # Output: Courage is found in unlikely places.