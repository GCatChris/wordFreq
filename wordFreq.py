

class wordList(object):
	def __init__(self, word, count):
		self.word = word
		self.count = count		
	def displayWord(self):
		print '%s: %d' % (self.word, self.count)
	def updateCount(self):
		self.count += 1
	def getWord(self):
		return self.word
	def getCount(self):
		return self.count

def wordFreq():
	filename = open(r'C:\Users\Chris\Desktop\jill.txt', 'r')
	text = []
	word_list = []
	
	for line in filename:
		#if(line.startswith("JILL")):
		line = line.split(' ')
		text.append(line)
			
	for i in range(len(text)):
		for j in range(len(text[i])):
			if j > 0:
				text[i][j] = text[i][j].strip(',;[]().?!\n')
				word_list.append(text[i][j])
				
	word_list.sort()
	word_Frequency = []
	dict = wordList(word_list.pop(), 1)
	while(len(word_list) > 0):
		if(dict.getWord() == word_list[len(word_list) - 1]):
			dict.updateCount()
			word_list.pop()
		else:
			word_Frequency.append(dict)
			dict = wordList(word_list.pop(), 1)
		
	print len(word_Frequency)
	bubbleSort(word_Frequency)
	for word in word_Frequency:
		word.displayWord()
		

def bubbleSort(freq_list):
	length = len(freq_list) - 1
	sorted = False
	comparisons = 0
	while not sorted:
		sorted = True
		for i in range(length):
			if freq_list[i].getCount() < freq_list[i + 1].getCount():
				comparisons += 1
				sorted = False
				freq_list[i], freq_list[i+1] = freq_list[i+1], freq_list[i]
		
	print comparisons
			
		
		
		
		
wordFreq()