from django.shortcuts import render

def index(request):
   return render (request, 'index.html')

def dev(request):
   return render(request,'devloper.html')



def result(request):
   raw_text = request.GET.get('text1')
   removepanc = request.GET.get('puncb')
   exspaceremover = request.GET.get('removeexspace')
   analytics = request.GET.get('analytics')
   analysed=''
   panc = """,./?;:}{[]"!@#=$'%^&*()~`<>"""

   if removepanc == 'on':
         for char in raw_text:
            if char not in panc:
               analysed += char
   elif exspaceremover == 'on':
         for char in raw_text:
            if char == char or char == ' ':
               analysed += char
   elif analytics == 'on':
      pass

   else:
      analysed = raw_text                   

   dictf={'raw_text' : analysed}
 
   return render (request,'result.html', dictf)
