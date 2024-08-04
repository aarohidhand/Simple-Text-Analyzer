givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

class TextAnalyzer(object):
    
    def __init__ (self, text):

        formattedtext = text.replace(',','').replace('.','').replace('?','').replace('!','')
        formattedtext = formattedtext.lower()
        self.fmttext = formattedtext

    def freqAll(self):
         
        wordlist= self.fmttext.split()

        freqmap= {}

        for word in set(wordlist):
            freqmap[word] = wordlist.count(word)
        return freqmap 

    def freqOf(self, word):

        freqdict= self.freqAll()

        if word in freqdict:
            return freqdict[word]
        else:
            return 0
        
analysed = TextAnalyzer(givenstring)
print ('Formatted text:',analysed.fmttext)
print ('\nFrequency of words:', analysed.freqAll())
word='lorem'
print (word, 'comes', analysed.freqOf(word), 'times')