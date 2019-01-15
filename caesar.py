def alphabet_position(letter):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                'o', 'p','q', 'r', 's', 't', 'u', 
                'v', 'w', 'x', 'y', 'z']
    letter = letter.lower()
    result = alphabet.index(letter)
    return result

def rotate_character(char, rot):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                'o', 'p','q', 'r', 's', 't', 'u', 
                'v', 'w', 'x', 'y', 'z']

    if char.isalpha():
        index = alphabet_position(char)
        index += rot 
        index = index % 26
        letter = alphabet[index]

        if char.isupper():
            letter = letter.upper()
        return letter
    else:
        return char


def rotate_string(text, rot):
    letter_list = []
    crypto_string = ""
    for letter in range(len(text)):
        char = text[letter]
        char = rotate_character(char, rot)
        letter_list.append(char)
    for i in letter_list:
        crypto_string += i
    return crypto_string


def main():
    from sys import argv, exit
    if not(argv[1].isdigit()):
        print("usage: python caesar.py n")
        exit()
    #do stuff
    message = input("Type a message:")
    #print(message)
    #rotation = int(input("Rotate by:"))
    rotation = int(argv[1])
    print(rotate_string(message, rotation))


if __name__ == "__main__":
    main()
