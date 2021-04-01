import operator
from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return  render(req, 'home.html')

def about(req):
    return  render(req, 'about.html')

def count(req):
    fulltext = req.GET['FullText']

    wordlist = fulltext.split()

    worddict = {}

    for word in wordlist:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1

    sortedwords = sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)

    
    return  render(req, 'count.html', {'FullText': fulltext,'count': len(wordlist), 'sortedwords': sortedwords })