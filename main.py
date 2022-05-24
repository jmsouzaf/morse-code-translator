from morse_translator import MorseTranslator

translator = MorseTranslator()
option = input("Type 'c' if you'd like to convert text to morse code or type 'd' if you'd like to convert morse code to text: ").lower()

if option == "c":
    text = input("Please type what text you'd like to convert: ")
    print(f"Text: {text}\nMorse Code: {translator.str_to_morse(text)}")
elif option == "d":
    code = input("Please type what code you'd like to convert: ")
    print(f"Morse code: {code}\nText: {translator.morse_to_str(code)}")
else:
    print("Please type a valid option.")