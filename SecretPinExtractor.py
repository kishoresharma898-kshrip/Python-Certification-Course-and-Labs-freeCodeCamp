# In this workshop you will create a pin extractor, the pin digits are hidden in each line of a poem.
# The function pin_extractor() takes a list(Python array) of poems and extracts the secret_codes for each of the poem which will be passed as the input into the list.
# The pin_extractor() function iterates over the list, for each poem in poems, a string named secret_code, and a list named lines which splits the poem into lines based on a new line search(i.e, divide the poem into lines based on "\n" character).
# And then a second loop iterates over the lines and extractes the line along with its index using enumerate() function.
# Then again, each line that was extracted in the outer loop is again divided into words using the same split method.
# And then for each line if the length of each word is greater than the respected line's index secret_code is concatenated with the string form of the word at the line_index(respected line's index) position.
# Else, secret_code is concatenated with string "0".
# Then, the secret_code for each peom is appended to the secret_codes list.
# Finally, the list of secret codes(the list secret_codes) for each input poem is returned as output.

# Code:
def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes    

# Input:    

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

poem4 = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""


print(pin_extractor([poem, poem2, poem3, poem4]))

# Output: ['5202', '3346', '50000', '5262']