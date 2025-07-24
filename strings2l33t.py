def to_leet(text):

    text = text.lower()

    ask = input("Do you wantt to change space to _ ? (y/n): ")

    if ask == "Y" or ask == "y":
        text = text.replace(' ', '_')
    elif ask == "N" or ask == "n":
        o=0
    else:
        print("\033[31mError! Only 'y' and 'n' are allowed \033[0m")
        return 0

    leet_map = {
        'a': '4',
        'b': '8',
        'e': '3',
        'g': '9',
        'i': '1',
        'l': '1',
        'o': '0',
        's': '5',
        't': '7',
        'z': '2'
    }

    leet_text = ''.join(leet_map.get(c, c) for c in text)
    return leet_text

input_str = input("Enter: ")
leet_str = to_leet(input_str)
if leet_str != 0:
    print("Leet:", leet_str)
