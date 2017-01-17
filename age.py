import sentlex
import sentlex.sentanalysis
import csv
import math

f=open('Output.txt',"r")
lines=f.readlines()
age=[]
gen=[]
edu=[]
name=[]
for x in lines:
    name.append(x.split(' ')[0])
    age.append(x.split(' ')[1])
    gen.append(x.split(' ')[2])
    edu.append(x.split(' ')[3])
    
age1 = map(int, age)
print ("Hi %s Welcome to Music Recommendation System" % name)
print "your:"
#print ("age = %s" % age1)
#print ("Gender = %s" % gen)
#print ("Education = %s" % edu)

for i in age1:
    if i > 13 and i < 19:
        a1 = 0.35
        
    elif i > 18 and i < 31:
        a1 = 0.325
        
    elif i > 30:
        a1 = 0.3

for i in gen:
    if i == 'MALE':
        M = 0.52
        
    else:
        M = 0.54
        
for i in edu:
    if i == 'GRADUATE':
        G = 0.04
        
    else:
        G = 0.03
        
S = a1 + M + G
#print S
P = math.exp(S)
#print P
f.close()

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

tup1 = sum1/row_count
tup2 = sum2/row_count
SM1 = (tup1 + tup2)/2
#print SM1

print ("Sentiment Intensity Metric = %s" % SM1)
#data = classifier.resultdata
#print data
print ("Correction Factor = %s" % P)

eSM = SM1 * P
print ("enhanced Sentiment Intensity value = %s" % eSM)

