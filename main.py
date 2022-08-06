from data import morse_dict       
#Morse code dictionary


LOGO_PATH = "logo.txt"


#Some invitation
def greeting():
    with open(LOGO_PATH) as logo:
        print(logo.read())
        
    print("Hi!\n Welcome to our Morse Encoder!")


#This finction handles logic of the app
def processer():
    print("Would You like to encode ('e') or decode ('d') a message?")
    #Let's ensure case-insensetive input
    user_input = input().lower()

    if user_input == 'e':
        message = input("Type in Your message: ").lower()
        result = encode(message)
    elif user_input == 'd':
        message = input("Type in Your message: ").lower()
        result = decode(message)
    else:
        print("Unknown option...")
        processer()

    print(f"\nHere is the result: {result}")

    print("\nDo You want to continue?")
    user_input = input().lower()
    
    if user_input == 'yes':
        processer()
    else:
        print("\n\nWe'll miss You.\nHave a great day ;)")


#Encode a normal string using Morse Code
def encode(message):
    encoded_message = []
    
    for symbol in message:
        if symbol in morse_dict:
            encoded_message.append(morse_dict[symbol] + ' ')
        else:
            return f"Morse Code doesn't familiar with this dude {symbol}..."
                      
    result = "".join(encoded_message)
    result = result.strip()
    
    return result


#Decode message back to human-readable text
def decode(message):
    message = message.split()
    decoded_message = []
    list_of_keys = list(morse_dict.keys())
    list_of_values = list(morse_dict.values())
    
    for symbol in message:
        if symbol in list_of_values:
            position = list_of_values.index(symbol)
            decoded_message.append(list_of_keys[position])
        else:
            print(f"The {symbol} symbol isn't in a Morse Code dictionary.")
            return "Invalid input"

    result = "".join(decoded_message)
    
    return result


greeting()
processer()