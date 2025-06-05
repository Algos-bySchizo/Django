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
     #getting the text and displaying it in the terminal an URL as well!
    ujtext= request.GET.get('text', 'default')
    removepunc= request.GET.get('removepunc', 'off')
    capitalize= request.GET.get('capitalize','off')
    newlineremover=request.GET.get('newlineremover','off')
    spaceremover=request.GET.get('spaceremover','off')
    charcounter=request.GET.get('charcounter','off')
    # the print statements lets me know in the console if I've checked the check boxes or not and if the  
    # check boxes are checked and function is still not performing as it should that means there's a logical issue in the code
    print(removepunc)
    print(capitalize)
    print(newlineremover)
    print(spaceremover)
    print(charcounter)
    remove_punc=None
    capitalized_text=None
    new_line_remover=None
    space_remover=None
    char_counter=None
    # the print statement below tells me what I've given in as input
    print(ujtext)
    #Analyzing the text!
    analyzed_text=ujtext
    
    if removepunc=='on':
        punctuations="""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""   
        # analyzed_text=''.join(char for char in analyzed_text if char not in punctuations)
        analyzed_text=''
        for char in ujtext:
            if char not in punctuations:
                analyzed_text+=char
            elif char=="\n":
                analyzed_text+=char
        remove_punc=analyzed_text
        # for char in ujtext:
        #     if char not in punctuations:
        #         analyzed_text= analyzed_text+char
    if capitalize=='on':
        analyzed_text=ujtext.upper()
        capitalized_text=analyzed_text
    
    if charcounter=='on':
        analyzed_text=len(ujtext)
        char_counter=analyzed_text
    
    if newlineremover=='on':
        analyzed_text=''
        for char in ujtext:
            if char!='\n':
                analyzed_text+=char
                new_line_remover=analyzed_text
    
    if spaceremover=='on':
        analyzed_text=''
        for index, char in enumerate(ujtext):
            if not(ujtext[index]==' ' and ujtext[index+1]==' '):
                analyzed_text+=char
                space_remover=analyzed_text

    elif capitalize!='on' and removepunc!='on' and newlineremover!='on' and charcounter=='on' and spaceremover=='on':
        return HttpResponse("""<h2>Check atleast one of the check boxes</h2>
         <a href='/'><-- Back to Home!</a>""")    
    
    jdict = {
        'purpose': 'Processed',
        'remove_punctuations': remove_punc,
        'CAPITALIZED': capitalized_text,
        'NewLineRemover': new_line_remover,
        'charcounter': char_counter,
        'spaceremover': space_remover   }
    return render(request, 'analyze.html', jdict)
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
