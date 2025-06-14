#I have created this file ~ Junaidy!!
from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

# def ex1(request):
#     return render(request,'ex1.html')

def analyze(request):
    ujtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcounter = request.POST.get('charcounter','off')
    countedanalyzed=None
    # print(removepunc, capitalize, newlineremover, spaceremover, charcounter)
    # print(ujtext)
    purposes=[]
    if (removepunc != 'on' and capitalize != 'on' and newlineremover != 'on' and spaceremover != 'on' and charcounter != 'on'):
        return render(request,'error_when_no_util.html')

    analyzed = ujtext

    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''.join(char for char in analyzed if char not in punctuations)
        purposes.append("Removed Punctuations")

    if capitalize == 'on':
        analyzed = analyzed.upper()
        purposes.append("Capitalized Text")

    if newlineremover == 'on':
        analyzed = ''.join(char for char in analyzed if char != '\n' and char != '\r')
        purposes.append("Extra New Lines Removed")

    if spaceremover == 'on':
        analyzed = ' '.join(analyzed.split())
        purposes.append("Extra Spaces Removed")

    if charcounter == 'on': 
        countedanalyzed=len(analyzed) 
        purposes.append("Characeters Counted")

    return render(request, 'analyze.html', {
        'purpose': ', '.join(purposes),
        'analyzed': analyzed,
        'countedanalyzed': countedanalyzed,
    })
# 