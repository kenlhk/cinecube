from django.shortcuts import render

# Create your views here.


def index(request):
    
   
    
    context_dict = {}
    context_dict['title'] = "CineCube"
   
    
    return render(request, 'payments/index.html', context=context_dict)