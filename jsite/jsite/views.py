#I have created this file ~ Junaidy!!
from django.shortcuts import render
from django.http import HttpResponse

""" Code for Video-6 (Perosnal Navigator) """

def index(request):    
    return HttpResponse('''<h1>homepage</h1>
                        <ul> 
                            <li><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django CodeWithHarry </a></li>
                            <li><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django CodeWithHarry </a></li>
                            <li><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django CodeWithHarry </a></li>
                            <li><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django CodeWithHarry </a></li>
                            <li><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django CodeWithHarry </a></li>
                        </ul>
                        ''')

# def about(request):
#     return HttpResponse('About this page')

""" Code for Video-7 (Laying the Pipeline) """

# def index(request):
#     return HttpResponse(""" 
#     <h1>Text Utility Functions</h1>
#     <ul>
#         <li><a href="/removepunc">Remove Punctuations</a></li>
#         <li><a href="/capitalizefirst">Capitalize First</a></li>
#         <li><a href="/newlineremove">New Line Remover</a></li>
#         <li><a href="/spaceremove">Space Remover</a></li>
#         <li><a href="/charcount">Char Counter</a></li>
#     </ul>                    
#                     """)

# def removepunc(request):
#     return HttpResponse(""" 
#         <h2>Remove Punctuations</h2>
#         <a href='/'><-- Back to Home!</a>
#                         """)

# def capfirst(request):
#     return HttpResponse(""" 
#         <h2>Captialize First</h2>
#         <a href='/'><-- Back to Home!</a>
#                         """)

# def newlineremove(request):
#     return HttpResponse(""" 
#         <h2>New Line Remover</h2>
#         <a href='/'><-- Back to Home!</a>
#                         """)

# def spaceremove(request):
#     return HttpResponse(""" 
#         <h2>Space Remover</h2>
#         <a href='/'><-- Back to Home!</a>
#                         """)

# def charcount(request):
#     return HttpResponse(""" 
#         <h2>Character Counter</h2>
#         <a href='/'><-- Back to Home!</a>
#                         """)

""" Code for Video-8 (Django Templates) """

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

    print(removepunc, capitalize, newlineremover, spaceremover, charcounter)
    print(ujtext)

    if (removepunc != 'on' and capitalize != 'on' and newlineremover != 'on' and spaceremover != 'on' and charcounter != 'on'):
        return render(request,'error_when_no_util.html')

    analyzed = ujtext

    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''.join(char for char in analyzed if char not in punctuations)

    if capitalize == 'on':
        analyzed = analyzed.upper()

    if newlineremover == 'on':
        analyzed = ''.join(char for char in analyzed if char != '\n' and char != '\r')

    if spaceremover == 'on':
        analyzed = ' '.join(analyzed.split())

    countedanalyzed = len(analyzed) if charcounter == 'on' else 'char counter off' 

    return render(request, 'analyze.html', {
        'purpose': 'Processed',
        'analyzed': analyzed,
        'countedanalyzed': countedanalyzed,
    })
# def removepunc(request):
#      #getting the text and displaying it in the terminal an URL as well!
#     ujtext= request.GET.get('text', 'default')
#     print(ujtext)
#     #Analyzing the text!
    
#     return HttpResponse(""" 
#         <h2>Remove Punctuations</h2>
#         <a href='/'><-- Back to Home!</a>
#                         """)

# def capfirst(request):
#     return HttpResponse(""" 
#         <h2>Captialize First</h2>
#         <a href='/'><-- Back to Home!</a>
#                         """)

# def newlineremove(request):
#     return HttpResponse(""" 
#         <h2>New Line Remover</h2>
#         <a href='/'><-- Back to Home!</a>
#                         """)

# def spaceremove(request):
#     return HttpResponse(""" 
#         <h2>Space Remover</h2>
#         <a href='/'><-- Back to Home!</a>
#                         """)

# def charcount(request):
#     return HttpResponse(""" 
#         <h2>Character Counter</h2>
#         <a href='/'><-- Back to Home!</a>
#                         """)
