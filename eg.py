import csv
import sys
import sentlex
import sentlex.sentanalysis

#reload(sys)
#sys.setdefaultencoding('utf8')
sum1 = 0
sum2 = 0
SWN = sentlex.SWN3Lexicon()
classifier = sentlex.sentanalysis.BasicDocSentiScore()
with open('keyword.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        makeitastring = ''.join(map(str, row))
        r = classifier.classify_document(makeitastring, tagged=False, L=SWN, a=True, v=True, n=False, r=False, negation=False, verbose=False)
        #print r[0]
        sum1 += r[0]
        #print sum
        sum2 += r[1]
        


with open('keyword.csv', 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)
    row_count = len(data)
    #print row_count


print sum1
print sum2
print row_count
tup1 = sum1/row_count
tup2 = sum2/row_count
print tup1
print tup2
SM = (tup1 + tup2)/2
print SM
