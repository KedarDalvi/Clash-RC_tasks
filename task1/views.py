from django.shortcuts import render
from django.http import HttpResponse



lst=[]
for i in range(0,21):
	lst.append(i)



def home(request):
	context={'list':lst}
	return render(request,'task1/home.html',context)

def about(request):
    return render(request,'task1/about.html')

def case(request):
    num1 = int(request.GET['number1'])
    num2 = int(request.GET['number2'])
    m=[]
    if num1<num2:
        for i in range(num1,(num2+1)):
            m.append(i)
        context = {
            'list1': m,
        }
        return render(request, 'task1/case.html', context)
    elif first==last:
        return HttpResponse("<p>Starting point and end point are same")
    else:
        return HttpResponse('<p>Starting point has to be less than ending point<p>')