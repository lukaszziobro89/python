# print all values provided in args
def print_everything(*args):
    """Prints all values provided as argument."""
    for element in args:
        print(str(element))

# ------------------------------------------------------------------------


# print whole text until provided sign
def print_till_character(input_text, find_sign):
    """Prints all characters till provided sign."""
    first_occurance = input_text.find(find_sign)
    print(input_text[:first_occurance])

# ------------------------------------------------------------------------


# print whole text until Nth occurrence of provided character
def print_till_nth(input_text, find_character, occurrence=1):
    """Prints all characters until n'th ocurrence of provided character"""
    indexes_list = []
    input_text_length = len(input_text)
    try:
        for character in range(input_text_length):
            if occurrence <= 0:
                print("Occurrance number must be greater then '0'.")
                break
            if len(find_character) != 1:
                print("You can provide only 1 sign.")
                break
            elif input_text[character] == find_character:
                indexes_list.append(character)
                print("Element '{}' occurs {} time(s) in sentence '{}'."
                      .format(find_character, len(indexes_list), input_text))
            else:
                pass
        print("Provided text until {} occurrence of '{}': {}"
              .format(occurrence, find_character, input_text[:indexes_list[occurrence - 1]]))
    except IndexError as IndErr:
        print("Error occurred: {}.".format(IndErr))
    except SyntaxError as SynErr:
        print("Syntax error occurred: {}.".format(SynErr))
    except TypeError as TypErr:
        print("Type error: {}.".format(TypErr))

# ------------------------------------------------------------------------

print_till_nth("ABC","C",1)
print_till_nth()