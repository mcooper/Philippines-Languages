# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 12:36:24 2014

@author: matthewcooper
"""
import wikipedia
import random

languages =     ['tl', #tagalog
                'bcl', #bikol
                'ceb', #cebuano
                        #hiligaynon
                'ilo', #Ilokano
                'pam', #Kapampangan
                'pag', #Pangasinense
                'war', #Waray
                'cbk-zam' #Chavacano
                ]

def collectRandom(lang, hangang):
    corpus = ''
    while len(corpus) < hangang: #should be 200,000
        wikipedia.set_lang(lang)
        try:        
            test = wikipedia.random(10)
            for item in test:
                corpus += str(wikipedia.page(item).content)
        except wikipedia.exceptions.PageError:
            pass
        except wikipedia.exceptions.DisambiguationError:
            pass
        except KeyError:
            pass
        print(len(corpus))
    
    f = open(lang + 'randwikicorp.txt', 'w')
    f.write(corpus)
    f.close()


        
def collectFrom(lang,start,hangang):
    wikipedia.set_lang(lang)
    lookpa = wikipedia.page(start).links
    lookna = [wikipedia.page(start)]
    corpus = str(wikipedia.page(start).content)
    while len(corpus) < hangang:
        random.shuffle(lookpa)
        item = lookpa[0]
        try:
            corpus += str(wikipedia.page(item).content)
        except wikipedia.exceptions.PageError:
            pass
        except wikipedia.exceptions.DisambiguationError:
            pass
        except KeyError:
            pass
        lookna.append(item)
        lookpa.remove(item)
        try: 
            for page in wikipedia.page(item).links:
                if page not in lookpa:
                    if page not in lookna:
                        lookpa.append(page)
        except wikipedia.exceptions.PageError:
            pass
        except wikipedia.exceptions.DisambiguationError:
            pass
        except KeyError:
            pass
        print('Corpus = ' + str(len(corpus)) + '   Searched = ' + str(len(lookna)) + '  Still = ' + str(len(lookpa)))
    
    f = open(lang + 'FromWikiCorp.txt', 'w')
    f.write(corpus)
    f.close()
    
for lang in languages[-2:]:
    collectRandom(lang, 1000000)
    collectFrom(lang,'Pilipinas',1000000)