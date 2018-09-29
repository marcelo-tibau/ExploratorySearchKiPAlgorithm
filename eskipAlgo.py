#Exploratory Search KiP Algorithm
  
class NoChoicesLeft(Error): pass

def choose(*choices):
    for choice in choices:
        try:
            return choice()
        except NoChoicesLeft:
            continue

        
class KeyWord:
    
    def __init__(self, filenames):
        self.filenames = filenames
        self.index = buildindex.BuildIndex(self.filenames)
        self.invertedIndex = self.index.totalIndex
        self.regularIndex = self.index.regdex


    def oneWordKeyWord(self, word):
        pattern = re.compile('[\W_]+')
        word = pattern.sub(' ', word)
        if word in self.invertedIndex.keys():
            return self.rankResults([filename for filename in self.invertedIndex[word].keys()], word)
        else:
            return []

	
        
        
##########################################################
#choose X satisfying P(X) {
#	init var list Q = []
			
#		compare q1 to q1+1 { 
#			if q1 < q1+1 & q1+1 contains q1
#				q1 == K1 & q1+1 == K2
#			else if q1 !== q1+1
#				q1+1 == K3
#			else
#				q1 == K4
#			add to list Q
#			}
#		end compare