import sys

from caesar_cypher_characters import letters, numbers, symbols

print(
    """                                                           
                                                           
 $$$$$$$\ $$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$\   $$$$$$\  
$$  _____|\____$$\ $$  __$$\ $$  _____| \____$$\ $$  __$$\ 
$$ /      $$$$$$$ |$$$$$$$$ |\$$$$$$\   $$$$$$$ |$$ |  \__|
$$ |     $$  __$$ |$$   ____| \____$$\ $$  __$$ |$$ |      
\$$$$$$$\\$$$$$$$ |\$$$$$$$\ $$$$$$$  |\$$$$$$$ |$$ |      
 \_______|\_______| \_______|\_______/  \_______|\__|      
                                                           
                                                           
                                                           """
)
print(
    """                              $$\                           
                              $$ |                          
 $$$$$$$\ $$\   $$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$  _____|$$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ /      $$ |  $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$$\ \$$$$$$$ |$$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |      
 \_______| \____$$ |$$  ____/ \__|  \__| \_______|\__|      
          $$\   $$ |$$ |                                    
          \$$$$$$  |$$ |                                    
           \______/ \__|                                    \n\n"""
)


def caesar(text, shift_amount):
    new_text = ""
    if direction == "decode":
        shift_amount = -shift_amount
    for char in text.lower():
        if char in symbols:
            index = symbols.index(char)
            new_text += symbols[index + shift_amount % len(symbols)]
        elif char in letters:
            index = letters.index(char)
            new_text += letters[index + shift_amount % len(letters)]
        elif char in numbers:
            index = numbers.index(char)
            new_text += numbers[index + shift_amount % len(numbers)]
    print(new_text)


should_continue = True


while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    if not direction == "encode" and not direction == "decode":
        print("Unrecognised input.")
        sys.exit()

    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    caesar(text, shift)
    should_continue = input("Do you want to go again? (y/n): ") == "y"
