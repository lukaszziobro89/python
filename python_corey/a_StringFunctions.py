# print all values provided in args
def print_everything(*args):
    for element in args:
        print(element)


# ------------------------------------------------------------------------

# print whole text until provided sign
def print_till_character(input_text, find_sign):
    first_occurance = input_text.find(find_sign)
    print(input_text[:first_occurance])


# ------------------------------------------------------------------------

# print whole text until Nth occurrence of provided character
def print_till_nth(input_text, find_character, occurrence=1):
    indexes_list = []
    input_text_length = len(input_text)
    try:
        for character in range(input_text_length):
            if input_text[character] == find_character:
                indexes_list.append(character)
            else:
                pass
        print("Provided text until {} occurrence of '{}': {}"
              .format(occurrence, find_character, input_text[:indexes_list[occurrence - 1]]))
    except IndexError as IndErr:
        print("Error occurred: {}.".format(IndErr))
        print("Element '{}' occurs only {} time(s) in sentence '{}'."
              .format(find_character, len(indexes_list), input_text))
    except SyntaxError as SynErr:
        print("Syntax error occurred: {}.".format(SynErr))
    except TypeError as TypErr:
        print("Type error: {}.".format(TypErr))


# ------------------------------------------------------------------------


print_till_nth('jakis tam tekst dotyczacy tekstu', 't', 'a')
print_till_nth('jakis tam tekst dotyczacy tekstu', 't', 9)
print_till_nth('jakis tam tekst dotyczacy tekstu', 't')
print_till_nth('jakis tam tekst dotyczacy tekstu', 't', 2)

print_everything("Lukasz " "Ziobro")
print_till_character("Hello World! Do not print this.", "!")
print_till_character("Lukasz Ziobro", "z")
print_till_character("Lukasz Ziobro", "Z")
