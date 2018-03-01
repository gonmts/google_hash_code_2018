from read_file import *
from random import randint

def getRandomListIndex(list, maxEl):
	lstLength = len(list)
	index = randint(0, lstLength - maxEl)
	return index
