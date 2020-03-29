from pynput.keyboard import Key, Controller
import time
o = Controller()

sentence = "sdguljbjvhxbjxhb"
time.sleep(5)
for chars in sentence:	
	o.type(chars)
	print(f"Keys-Typed: {chars}")
	time.sleep(0.5)

	
	
	