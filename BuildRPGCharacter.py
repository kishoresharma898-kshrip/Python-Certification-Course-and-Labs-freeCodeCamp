'''
In this lab you will practice the basics of Python by building a small app that creates a character for an RPG adventure.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

1. You should have a function named create_character.
2. The function should accept, in order, a character name followed by three stats: strength, intelligence, and charisma.
The character name should be validated:
3. If the character name is not a string, the function should return The character name should be a string.
4. If the character name is an empty string, the function should return The character should have a name.
5. If the character name is longer than 10 characters, the function should return The character name is too long.
6. If the character name contains spaces, the function should return The character name should not contain spaces.
The stats should also be validated:
7. If one or more stats are not integers, the function should return All stats should be integers.
8. If one or more stats are less than 1, the function should return All stats should be no less than 1.
9. If one or more stats are more than 4, the function should return All stats should be no more than 4.
10. If the sum of all stats is different than 7, the function should return The character should start with 7 points.
11. If all values pass the verification, the function should return a string with four lines:
the first line should contain the character name
lines 2-4 should start with the stat abbreviation, STR, INT or CHA (in this order), then a space, and then a number of full dots (●) equal to the value of the stat, and a number of empty dots (○) to reach 10. Example: if the value of strength is 3 there must be 3 full dots followed by 7 empty dots. The dots are given in the editor.
Here's the string that should be returned by create_character('ren', 4, 2, 1):

Example Code
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
NOTE: while str and int are common abbreviations for the stats, remember that those are reserved keywords in Python and should not be used as variable names.'''

# Code:
full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):

    output = ""
    
    # name validations:
    if not isinstance(name, str):
        return "The character name should be a string"
    elif name == "":
        return "The character should have a name"
    elif len(name) > 10:
        return "The character name is too long"
    elif name.count(" ") > 0:
        return "The character name should not contain spaces"
    
    # stats validations:
    elif (not isinstance(strength, int)) or (not isinstance(intelligence, int)) or (not isinstance(charisma, int)):
        return "All stats should be integers"
    elif (strength < 1) or (intelligence < 1) or (charisma < 1):
        return "All stats should be no less than 1"
    elif (strength > 4) or (intelligence > 4) or (charisma > 4):
        return "All stats should be no more than 4"
    elif (strength + intelligence + charisma) != 7:
        return "The character should start with 7 points"
    
    # if all validations are passed:
    else:
        output = name + "\n" + "STR " + (strength * full_dot) + ((10 - strength) * empty_dot) + "\n" + "INT " + (intelligence * full_dot) + ((10 - intelligence) * empty_dot) + "\n" + "CHA " + (charisma * full_dot) + ((10 - charisma) * empty_dot)
    
    return output

# Tests:

print(create_character('ren', 4, 2, 1))
# Ouput:
'''
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
'''
print()
print(create_character(3, 4, 2, 1)) # The character name should be a string
print()
print(create_character('', 4, 5, 1)) # The character should have a name
print()
print(create_character('AlexandrioD', 4, 2, 1)) # The character name is too long
print()
print(create_character('Alex Ria', 4, 4, 1)) # The character name should not contain spaces
print()
print(create_character('Bascher', "4", "2", 1)) # All stats should be integers
print()
print(create_character('Rhett', -4, 2, 1)) # All stats should be no less than 1
print()
print(create_character('Sandra', 4, 5, 1)) # All stats should be no more than 4
print()
print(create_character('John', 4, 1, 1)) # The character should start with  points


'''
Passed:1. You should have a function named create_character.
Passed:2. When create_character is called with a first argument that is not a string it should return The character name should be a string.
Passed:3. When create_character is called with a first argument that is a string it should not return The character name should be a string.
Passed:4. When create_character is called with a first argument that is an empty string, it should return The character should have a name.
Passed:5. When create_character is called with a first argument that is not an empty string, it should not return The character should have a name.
Passed:6. When create_character is called with a first argument that is longer than 10 characters it should return The character name is too long.
Passed:7. The create_character function should not say that the character is too long when it's not longer than 10 characters.
Passed:8. When create_character is called with a first argument that contains a space it should return The character name should not contain spaces.
Passed:9. When create_character is called with a first argument that does not contain a space it should not return The character name should not contain spaces.
Passed:10. When create_character is called with a second, third or fourth argument that is not an integer it should return All stats should be integers.
Passed:11. When create_character is called with a second, third and fourth argument that are all integers it should not return All stats should be integers.
Passed:12. When create_character is called with a second, third or fourth argument that is lower than 1 it should return All stats should be no less than 1.
Passed:13. When create_character is called with a second, third and fourth argument that are all no less than 1 it should not return All stats should be no less than 1.
Passed:14. When create_character is called with a second, third or fourth argument that is higher than 4 it should return All stats should be no more than 4.
Passed:15. When create_character is called with a second, third and fourth argument that are all no more than 4 it should not return All stats should be no more than 4.
Passed:16. When create_character is called with a second, third or fourth argument that do not sum to 7 it should return The character should start with 7 points.
Passed:17. When create_character is called with a second, third and fourth argument that sum to 7 it should not return The character should start with 7 points.
Passed:18. create_character('ren', 4, 2, 1) should return ren\nSTR ●●●●○○○○○○\nINT ●●○○○○○○○○\nCHA ●○○○○○○○○○.
Passed:19. When create_character is called with valid values it should output the character stats as required.'''