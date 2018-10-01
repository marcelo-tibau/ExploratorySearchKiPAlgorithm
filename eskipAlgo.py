#Exploratory Search KiP Algorithm
  
class NoChoicesLeft(Error): pass

def choose(*choices):
    for choice in choices:
        try:
            return choice()
        except NoChoicesLeft:
            continue

import re
        
class KeyWord:
    
    def __init__(self, filenames):
        self.filenames = filenames
        self.index = buildindex.BuildIndex(self.filenames)
        self.invertedIndex = self.index.totalIndex
        self.regularIndex = self.index.regdex


    def oneWordKeyWordQuery(self, word):
        pattern = re.compile('[\W_]+')
        word = pattern.sub(' ', word)
        if word in self.invertedIndex.keys():
            return self.rankResults([filename for filename in self.invertedIndex[word].keys()], word)
        else:
            return []

    def freeTextTermQuery(self, string):
        pattern = re.complile('[\W_]+')
        string = pattern.sub(' ', string)
        result = []
        for word in string.split():
            result += self.oneWordKeyWordQuery(word)
        return self.rankResults(list(set(result)), string)

    def PhraseTermQuery(self, string):
        pattern = re.compile('[\W_]+')
        string = pattern.sub(' ', string)
        listOfLists, result = [],[]
        for word in string.split():
            listOfLists.append(self.oneWordKeyWordQuery(word))
        setted = set(listOfLists[0]).intersection(*listOfLists)
        for filename in setted:
            temp = []
            for word in string.split():
                temp.append(self.invertedIndex[word][filename][:])
            for i in range(len(temp)):
                for ind in range(len(temp[i])):
                    temp[i][ind] -= i
                if set(temp[0]).intersection(*temp):
                    result.append(filename)
            return self.rankResults(result, string)
            
    def makeVectors(self, documents):
        vecs = {}
        for doc in documents:
            docVec = [0]*len(self.index.getUniques())
            for ind, term in enumerate(self.index.getUniques()):
                docVec[ind] = self.index.generateScore(term, doc)
            vecs[doc] = docVec
        return vecs
        
    def queryVector(self, query):
        pattern = re.compile('[\W_]+')
        query = pattern.sub(' ', query)
        queryls = query.split()
        queryVec = [0]*len(queryls)
        index = 0
        for ind, word in enumerate(queryls):
            queryVec[index] = self.queryFreq(word, query)
            index += 1
        queryidf = [self.index.idf[word] for word in self.index.getUniques()]
        magnitude = pow(sum(map(lambda x: x**2, queryVec)),.5)
        freq = self.termfreq(self.index.getUniques(), query)
        tf = [x/magnitude for x in freq]
        final = [tf[i]*queryidf[i] for i in range(len(self.index.getUniques()))]
        return final
        
    def queryFreq(self, term, query):
        count = 0
        for word in query.split():
            if word == term:
                count += 1
        return counts
        
    def termFreq(self, terms, query):
        temp = [0]*len(terms)
        for i, term in enumerate(terms):
            temp[i] = self.queryFreq(term, query)
        return temp
        
    def dotProduct(self, doc1, doc2):
        if len(doc1) != len(doc2):
            return 0
        return sum([x*y for x,y in zip(doc1, doc2)])

    def rankResults(self, resultsDocs, query):
        vectors = self.makeVectors(resultDocs)
        queryVec = self.queryVector(query)
        results = [[self.dotProduct(vectors[result], queryVec), result] for result in resultDocs]
        results.sort(key=lambda x: x[0])
        results = [x[1] for x in results]
        return results
	       
##########################################################


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