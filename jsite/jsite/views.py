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

def analyze(request):
     #getting the text and displaying it in the terminal an URL as well!
    ujtext= request.GET.get('text', 'default')
    removepunc= request.GET.get('removepunc', 'off')
    print(removepunc)
    print(ujtext)
    #Analyzing the text!
    if removepunc=='on':
        punctuations="""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""   
        analyzed=''
        for char in ujtext:
            if char not in punctuations:
                analyzed= analyzed+char
        jdict={'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request,'analyze.html',jdict)
    else:
        return HttpResponse("""<h2>Check the remove Punctuations check box</h2>
         <a href='/'><-- Back to Home!</a>""")    

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
