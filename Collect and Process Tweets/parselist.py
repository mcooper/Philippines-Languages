# -*- coding: utf-8 -*-

wdir=r'Users/matthewcooper/pyworkingdirectory'
import os

os.chdir('/Users/matthewcooper/pyworkingdirectory')


TagLit = 'Tagalog_Literary_Text.txt'
TagRel = 'Tagalog_Religious_Text.txt'
TagWik1 = 'tlFromWikiCorp.txt'
TagWik2 = 'tlrandwikicorp.txt'
BikLit = 'Bikol_Literary_Text.txt'
BikRel = 'Bikol_Religious_Text.txt'
BikWik1 = 'bclFromWikiCorp.txt'
BikWik2 = 'bclrandwikicorp.txt'
CebLit = 'Cebuano_Literary_Text.txt'
CebRel = 'Cebuano_Religious_Text.txt'
CebWik1 = 'cebFromWikiCorp.txt'
CebWik2 = 'cebrandwikicorp.txt'
HilLit = 'Hiligaynon_Literary_Text.txt'
HilRel = 'Hiligaynon_Religious_Text.txt'
HilWik1 = 'hilwiki.txt'
HilWik2 = 'hilwiki2.txt'
IloLit = 'Ilocano_Literary_Text.txt'
IloRel = 'Ilocano_Religious_Text.txt'
IloWik1 = 'iloFromWikiCorp.txt'
IloWik2 = 'ilorandwikicorp.txt'
KapLit = 'Kapampangan_Literary_Text.txt'
KapRel = 'Kapampangan_Religious_Text.txt'
KapWik1 = 'pamFromWikiCorp.txt'
KapWik2 = 'pamrandwikicorp.txt'
PanLit = 'Pangasinense_Literary_Text.txt'
PanRel = 'Pangasinense_Religious_Text.txt'
PanWik1 = 'pagFromWikiCorp.txt'
PanWik2 = 'pagrandwikicorp.txt'
WarLit = 'Waray_Literary_Text.txt'
WarRel = 'Waray_Religious_Text.txt'
WarWik1 = 'warFromWikiCorp.txt'
WarWik2 = 'warrandwikicorp.txt'
ZamLit = 'ZamLit.txt'
ZamRel = 'ZamRel.txt'
ZamWik1 = 'cbk-zamFromWikiCorp.txt'
ZamWik2 = 'cbk-zamrandwikicorp.txt'

def parselist(w,x,y,z):
    f = open(w, 'r')
    w1 = f.read()
    f = open(x, 'r')
    x1 = f.read()
    f = open(y, 'r')
    y1 = f.read()
    f = open(z, 'r')
    z1 = f.read()
    corpora = [w1,x1,y1,z1]
    parsedtweets = []
    chunked = []
    for line in corpora:
        badchars = ('\n', '.', ',', '<i>', '</i>', '<b>', '</b>', '<u>', '</u>', '\r', '?', '!', '\t', '(',')')
        for item in badchars:        
            line = line.replace(item,' ')
        newwords = line.split(' ')
        chunked.append(newwords)
    for thiny in chunked:
        for word in thiny:
            parsedtweets.append(word)
    
    #cleanwords        
    cleanparsed = []    
    for word in parsedtweets:
        newword = ''
        for letter in word:
            if 96<ord(letter)<123:
                newword += letter
            if 64<ord(letter)<91:
                newword += chr(ord(letter)+32)
        if newword[:4] != 'http' and len(newword)>2:
            cleanparsed.append(newword) 
            
        #Remove English & Spanish Words
    English = []
    f = open('EnglishWordList.txt')
    English = f.read().splitlines()
    f.close()

    Spanish = []
    f = open('SpanishWordList.txt')
    Spanish = f.read().splitlines()
    f.close()
    
    for item in English:
        if item in cleanparsed:
            cleanparsed.remove(item)
            
    for item in Spanish:
        if item in cleanparsed:
            cleanparsed.remove(item)
            
    parsedtweets = list(set(cleanparsed))
    return parsedtweets

Tagalog = parselist(TagLit,TagRel,TagWik1,TagWik2)
Bikol = parselist(BikLit, BikRel, BikWik1,BikWik2)
Cebuano = parselist(CebLit, CebRel, CebWik1, CebWik2)
Hiligaynon = parselist(HilLit, HilRel, HilWik1, HilWik2)
Ilocano = parselist(IloLit, IloRel, IloWik1, IloWik2)
Kapampangan = parselist(KapLit, KapRel, KapWik1, KapWik2)
Pangasinense = parselist(PanLit,PanRel, PanWik1, PanWik2)
Waray = parselist(WarLit,WarRel, WarWik1, WarWik2)
Zam = parselist(ZamLit,ZamRel,ZamWik1,ZamWik2)


langlist = [Tagalog, Bikol, Cebuano, Hiligaynon, Ilocano, Kapampangan, Pangasinense, Waray, Zam]    

def unique(language):
    languages = [Tagalog, Bikol, Cebuano, Hiligaynon, Ilocano, Kapampangan, Pangasinense, Waray, Zam]
    uniqueset = []
    languages.remove(language)
    otherswordlist = []
    for lang in languages:
        for word in lang:
            otherswordlist.append(word)
    allothers = list(set(otherswordlist))
    for item in language:
        if item not in allothers:
            uniqueset.append(item)
    return uniqueset

TagalogU = unique(Tagalog)
BikolU = unique(Bikol)
CebuanoU = unique(Cebuano)
HiligaynonU = unique(Hiligaynon)
IlocanoU = unique(Ilocano)
KapampanganU = unique(Kapampangan)
PangasinenseU = unique(Pangasinense)
WarayU = unique(Waray)
ZamU = unique(Zam)

Langstrs = ['TagalogU','BikolU','CebuanoU','HiligaynonU','IlocanoU','KapampanganU','PangasinenseU','WarayU']

def common():
    langlist = [Tagalog, Bikol, Cebuano, Hiligaynon, Ilocano, Kapampangan, Pangasinense, Waray, Zam]
    langlistU = [TagalogU, BikolU, CebuanoU, HiligaynonU, IlocanoU, KapampanganU, PangasinenseU, WarayU]
    allwords = []
    for lang in langlist:
        for word in lang:
            allwords.append(word)
    allothers = list(set(allwords))
    for lang in langlistU:
        for word in lang:
            allothers.remove(word)
    return allothers

commonwords = common()

allLanguages = [TagalogU, BikolU, CebuanoU, HiligaynonU, IlocanoU, KapampanganU, PangasinenseU, WarayU, ZamU, commonwords]



f = open('TagalogNonU.txt', 'w')
for item in Tagalog:
    f.write('%s\n' %item)
f.close()

f = open()