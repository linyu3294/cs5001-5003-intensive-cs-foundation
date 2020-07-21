''' CS5001 
    Spring 2019
    Lab 3 -- encryption/decryption
    Sample Solution 
'''

FIRST_VALID = 97
LAST_VALID = 122
MAX_SHIFT = 25

def encrypt(msg, shift):
    ''' Function encrypt:
        Input: string to encrypt, shift amount
        Returns: encrypted string
        Does: Converts each letter to lowercase, shifts right
            by the shift amount. If the letter plus shift amount
            is > 122 ('z'), wrap around to begin again at 97 ('a').
    '''
    msg = msg.lower()
    encrypted = ''
    if shift < 0 or shift > MAX_SHIFT:
        shift = 1
    
    for letter in msg:
        position = ord(letter)

        if position < FIRST_VALID or position > LAST_VALID:
            new_letter = letter
        else:
            new_position = position + shift
            if new_position > LAST_VALID:
                new_position = new_position % LAST_VALID + (FIRST_VALID - 1)
            new_letter = chr(new_position)
           
        encrypted += new_letter

    return encrypted

def decrypt(enc_msg, shift):
    ''' Function decrypt:
        Input: encoded string to decrypt, shift amount
        Returns: original message
        Does: Converts each letter to lowercase, shifts left
            in the alphabet by the shift amount. If letter minus
            shift amount is < 97 ('a'), wrap around to begin
            again at 122 ('z')
    '''
    enc_msg = enc_msg.lower()
    original_msg = ''
    if shift < 0 or shift > MAX_SHIFT:
        shift = 1

    for letter in enc_msg:
        position = ord(letter)

        if position < FIRST_VALID or position > LAST_VALID:
            new_letter = letter

        else:
            new_position = position - shift
            if new_position < FIRST_VALID:
                new_position = LAST_VALID - (FIRST_VALID - new_position) + 1
            new_letter = chr(new_position)
            
        original_msg += new_letter
        
    return original_msg

def slide(msg, slide_amount):
    ''' Function slide
        Input: string, slide amount
        Returns: modified string
        Does: shifts each letter in the string forward by the
              given number of positions, rotating around to
              position 0 when we reach the end.
    '''
    slide_amount = slide_amount % len(msg)

    list_version = list(msg)
    for i in range(len(msg)):
        pos = (i + slide_amount) % len(msg)
        list_version[pos] = msg[i]
    return ''.join(list_version)

def unslide(msg, slide_amount):
    slide_amount = slide_amount % len(msg)

    orig_string = ""
    for i in range(len(msg)):
        pos = (i + slide_amount) % len(msg)
        orig_string += msg[pos]
    return orig_string
