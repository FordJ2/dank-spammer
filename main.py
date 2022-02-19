import time
import multiprocessing
import pyautogui
import random

def rand(time):
	return random.random()*2+time

def countdown():
	print('commence countdown')
	for x in range(5, 0, -1):
		print(x)
		time.sleep(rand(2))
	print('bravo 6 going dark')	 

def beg():
	time.sleep(rand(10))
	while True:
		pyautogui.typewrite('pls beg')
		pyautogui.press('enter')
		print('begged')
		time.sleep(rand(45))

def dep():
	time.sleep(rand(20))
	while True:
		pyautogui.typewrite('pls dep all')
		pyautogui.press('enter')
		print('deposited all')
		time.sleep(rand(2))
		pyautogui.typewrite('pls use padlock')
		pyautogui.press('enter')
		print('padlocked')
		time.sleep(rand(60*5))

def hunt():
	time.sleep(rand(30))
	while True:
		pyautogui.typewrite('pls hunt')
		pyautogui.press('enter')
		print('hunted')
		time.sleep(rand(40))

def fish():
	time.sleep(rand(40))
	while True:
		pyautogui.typewrite('pls fish')
		pyautogui.press('enter')
		print('fished')
		time.sleep(rand(40))

def meme():
	time.sleep(rand(50))
	while True:
		pyautogui.typewrite('pls pm')
		pyautogui.press('enter')
		time.sleep(rand(2))
		pyautogui.typewrite(random.choice(['f', 'r', 'i', 'c', 'k']))
		pyautogui.press('enter')
		print('memed')
		time.sleep(rand(40))

def main():
	counter = multiprocessing.Process(target=countdown)
	proc1 = multiprocessing.Process(target=beg)
	proc2 = multiprocessing.Process(target=dep)
	proc3 = multiprocessing.Process(target=hunt)
	proc4 = multiprocessing.Process(target=fish)
	proc5 = multiprocessing.Process(target=meme)

	counter.start()
	proc1.start()
	proc2.start()
	proc3.start()
	proc4.start()
	proc5.start()

if __name__ == "__main__":
	main()
