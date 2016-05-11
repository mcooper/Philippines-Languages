# -*- coding: utf-8 -*-
"""
Created on Mon May 26 23:08:35 2014

@author: matthewcooper
"""

def parsetweets(tweets):
    f = open(tweets)
    alltweets = []
    alltweets = f.read().split('$hr0oby ')
    f.close()
    return alltweets
    
tweets = parsetweets('alltweetstext2.txt')
tweets.remove('"x"\n"')

def createwords(tweets):
    parsedtweets = []
    for line in tweets:
        newline = line.strip('"\n"')
        newwords = newline.split(' ')
        parsedtweets.append(newwords)
    return parsedtweets
    
parsedtweets = createwords(tweets)

'''
skip this for now
def cleanwords(tweets):
    for line in tweets:
        for word in line:
            if 'http' in word:
                line.remove(word)
            if "\\x" in word:
                line.remove(word)
            if '#' in word:
                line.remove(word)
            if '.com' in word:
                line.remove(word)
    return tweets
    
skip this for now
'''

def cleanwords(parsedtweets):
    cleantweets = []
    for tweet in parsedtweets:
        cleantweet = []
        for word in tweet:
            newword = ''
            for letter in word:
                if 96<ord(letter)<123:
                    newword += letter
                if 64<ord(letter)<91:
                    newword += chr(ord(letter)+32)
            if newword[:4] != 'http' and len(newword)>2:
                cleantweet.append(newword)
        cleantweets.append(cleantweet)
    return cleantweets
    
    
    
cleanwords = cleanwords(parsedtweets)    
    
Engwords = []
f = open('EnglishWordList.txt')
Engwords = f.read().splitlines()
f.close()

TagalogU = []
f = open('TagalogU.txt')
TagalogU = f.read().splitlines()
f.close()

BikolU = []
f = open('BikolU.txt')
BikolU = f.read().splitlines()
f.close()

CebuanoU = []
f = open('CebuanoU.txt')
CebuanoU = f.read().splitlines()
f.close()

HiligaynonU = []
f = open('HiligaynonU.txt')
HiligaynonU = f.read().splitlines()
f.close()

IlocanoU = []
f = open('IlocanoU.txt')
IlocanoU = f.read().splitlines()
f.close()

KapampanganU = []
f = open('KapampanganU.txt')
KapampanganU = f.read().splitlines()
f.close()

PangasinenseU = []
f = open('PangasinenseU.txt')
PangasinenseU = f.read().splitlines()
f.close()

WarayU = []
f = open('WarayU.txt')
WarayU = f.read().splitlines()
f.close()

Tagalog = []
f = open('Tagalog.txt')
Tagalog = f.read().splitlines()
f.close()

Bikol = []
f = open('Bikol.txt')
Bikol = f.read().splitlines()
f.close()

Cebuano = []
f = open('Cebuano.txt')
Cebuano = f.read().splitlines()
f.close()

Hiligaynon = []
f = open('Hiligaynon.txt')
Hiligaynon = f.read().splitlines()
f.close()

Ilocano = []
f = open('Ilocano.txt')
Ilocano = f.read().splitlines()
f.close()

Kapampangan = []
f = open('Kapampangan.txt')
Kapampangan = f.read().splitlines()
f.close()

Pangasinense = []
f = open('Pangasinense.txt')
Pangasinense = f.read().splitlines()
f.close()

Waray = []
f = open('Waray.txt')
Waray = f.read().splitlines()
f.close()

def classify(tweets):
    tweetlength = []
    Englishwords = []
    Commonwords = []
    Tagalogwords = []
    Bikolwords = []
    Cebuanowords = []
    Hiligaynonwords = []
    Ilocanowords = []
    Kapampanganwords = []
    Pangasinensewords = []
    Waraywords = []
    Zamwords = []
    Spanishwords = []
    for tweet in tweets:
        Length = len(tweet)
        English = 0
        Common = 0
        Tagalog = 0
        Bikol = 0
        Cebuano = 0
        Hiligaynon = 0
        Ilocano = 0
        Kapampangan = 0
        Pangasinense = 0
        Waray = 0
        Zam = 0
        Spanish = 0
        for word in tweet:
            if word in Engwords:
                English += 1
            elif word in commonwords:
                Common += 1
            elif word in TagalogU:
                Tagalog += 1
            elif word in BikolU:
                Bikol += 1
            elif word in CebuanoU:
                Cebuano += 1
            elif word in HiligaynonU:
                Hiligaynon += 1
            elif word in IlocanoU:
                Ilocano += 1
            elif word in KapampanganU:
                Kapampangan += 1
            elif word in PangasinenseU:
                Pangasinense += 1
            elif word in WarayU:
                Waray += 1
            elif word in ZamU:
                Zam += 1
            elif word in Spanwords:
                Spanish += 1
        tweetlength.append(Length)
        Englishwords.append(English)
        Commonwords.append(Common)
        Tagalogwords.append(Tagalog)
        Bikolwords.append(Bikol)
        Cebuanowords.append(Cebuano)
        Hiligaynonwords.append(Hiligaynon)
        Ilocanowords.append(Ilocano)
        Kapampanganwords.append(Kapampangan)
        Pangasinensewords.append(Pangasinense)
        Waraywords.append(Waray)
        Zamwords.append(Zam)
        Spanishwords.append(Spanish)
    Categories = [tweetlength, Englishwords, Commonwords, Tagalogwords, Bikolwords, Cebuanowords, Hiligaynonwords, Ilocanowords, Kapampanganwords, Pangasinensewords, Waraywords, Zamwords, Spanishwords]
    return Categories
    
def classifyTagalog(tweets):
    Tagalogwords = []
    for tweet in tweets:
        Tag = 0
        for word in tweet:
            if word in Tagalog:
                Tag += 1
        Tagalogwords.append(Tag)
        if tweets.index(tweet)%500==0:
            print(str(tweets.index(tweet)/len(tweets)*100)+' Percent Complete')
    return Tagalogwords
    


TagalogWordCount = classifyTagalog(cleanwords)

f = open('TagalogWordCount3.txt', 'w')
for item in TagalogWordCount:
    f.write('%s\n' %item)
f.close
    
f = open('tweetslength.txt', 'w')
for item in categories[0]:
    f.write('%s\n' %item)
f.close()

f = open('Engwords.txt', 'w')
for item in categories[1]:
    f.write('%s\n' %item)
f.close()

f = open('comwords.txt', 'w')
for item in categories[2]:
    f.write('%s\n' %item)
f.close()

f = open('tagwords.txt', 'w')
for item in categories[3]:
    f.write('%s\n' %item)
f.close()

f = open('bikwords.txt', 'w')
for item in categories[4]:
    f.write('%s\n' %item)
f.close()

f = open('cebwords.txt', 'w')
for item in categories[5]:
    f.write('%s\n' %item)
f.close()

f = open('hilwords.txt', 'w')
for item in categories[6]:
    f.write('%s\n' %item)
f.close()

f = open('ilowords.txt', 'w')
for item in categories[7]:
    f.write('%s\n' %item)
f.close()

f = open('kapwords.txt', 'w')
for item in categories[8]:
    f.write('%s\n' %item)
f.close()

f = open('panwords.txt', 'w')
for item in categories[9]:
    f.write('%s\n' %item)
f.close()

f = open('warwords.txt', 'w')
for item in categories[10]:
    f.write('%s\n' %item)
f.close()

f = open('zamwords.txt', 'w')
for item in categories[11]:
    f.write('%s\n' %item)
f.close()

f = open('Spanishwords.txt', 'w')
for item in categories[12]:
    f.write('%s\n' %item)
f.close()

def letstry(x):
    for item in select:
        if x in item:
            return 'SHIT'
    return 'works'
    
newselect = []
for item in select:
    newselect.append(item.replace('\n',''))