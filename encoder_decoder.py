def encode(password): # Aiden Oswalts encoder
    encoded_string = ''
    for item in password:
        if 0 <= int(item) <= 6:
            encoded_string += str(int(item) + 3)
        elif item == '7':
            encoded_string += '0'
        elif item == '8':
            encoded_string += '1'
        elif item == '9':
            encoded_string += '2'
    return encoded_string

if __name__ == '__main__':
    end = False
    while end == False: # Controls when function ends
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        option = int(input('Please enter an option: '))

        if option == 1:
            encodeable = str(input('Please enter your password to encode: '))
            encoded_val = encode(encodeable)
            print('Your password has been encoded and stored!')

        elif option == 2:
            pass

        elif option == 3:
            end = True
