from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'MAHI','age':13,'hobbies':['cricket','football']}
    return render(request,'data_render.html',context=d)

def conditions(request):
    d={'a':10000,'b':1500,'c':200}
    return render(request,'conditions.html',context=d)

