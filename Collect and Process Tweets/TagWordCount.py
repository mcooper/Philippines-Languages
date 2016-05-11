import os
os.chdir('Z:\matthewcooper\pyworkingdirectory')

def Tagalog():
    tweets = parsetweets('alltweetstext2.txt')
    tweets.remove('"x"\n"')
    parsedtweets = createwords(tweets)
    cleanwords = cleanwords1(parsedtweets)

    Tagalog = []
    f = open('TagalogNonU.txt', 'r')
    Tagalog = f.read().splitlines()
    f.close()

    Tagalogwords = []
    for tweet in cleanwords:
        Tag = 0
        for word in tweet:
            if word in Tagalog:
                Tag += 1
        Tagalogwords.append(Tag)

    f = open('TagalogCountFromWindows.txt', 'w')
    for item in Tagalogwords:
        f.write('%s\n' %item)
    f.close()

    return Tagalogwords

def parsetweets(tweets):
    f = open(tweets)
    alltweets = []
    alltweets = f.read().split('$hr0oby ')
    f.close()
    return alltweets

def createwords(tweets):
    parsedtweets = []
    for line in tweets:
        newline = line.strip('"\n"')
        newwords = newline.split(' ')
        parsedtweets.append(newwords)
    return parsedtweets

def cleanwords1(parsedtweets):
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
