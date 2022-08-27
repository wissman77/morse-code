import winsound
import time

alphabet = {'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----',
            ', ': '--..--',
            '.': '.-.-.-',
            '?': '..--..',
            '/': '-..-.',
            '-': '-....-',
            '(': '-.--.',
            ')': '-.--.-'
            }

unit = 100  # ms
frequency = 3000  # Hz


def play_dot():
    winsound.Beep(frequency, 1 * unit)


def play_dash():
    winsound.Beep(frequency, 3 * unit)


def play_char(ch):
    if ch == ' ':
        time.sleep(7 * unit / 1000)
        return '<space>'

    morse_value = alphabet[ch]
    for d in morse_value:
        if d == '.':
            play_dot()
        else:
            play_dash()
        time.sleep(1 * unit / 1000)

    return morse_value


def convert_text_to_morse(text):
    for ch in text.upper():
        print(play_char(ch), end='')


def main():
    print("Please enter text to convert to morse code:")
    text = input('> ')
    convert_text_to_morse(text)
    print()


if __name__ == '__main__':
    main()
