from read_file import *
from random import randint

def getRandomListIndex(list, maxEl):
	lstLength = len(list)
	if (lstLength == maxEl):
		return 0
	return randint(0, lstLength - maxEl)
