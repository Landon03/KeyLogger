import os
import time as t
# starts music to green sally
os.system("color 0a")
os.system("start /min sally.mp3")
# 5 minute workout to green sally
sallyup = 'green sally up'
os.system('cls')
sallydown = 'green sally down'

for i in range(1000000000000000):
	print(sallyup)
	t.sleep(5)
	print(sallydown)

