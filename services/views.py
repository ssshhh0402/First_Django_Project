from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'services/index.html')

def artii(request):
    return render(request, 'services/artii.html')

def artii_result(request):
    import requests
    naeyong = request.GET.get('t_input')
    f_input = request.GET.get('f_input')
    url = 'http://artii.herokuapp.com/make?text={0}&font={1}'.format(naeyong,f_input)
    response = requests.get(url)

    context=  {
       'g_rim': response.text
    }
    return render(request, 'services/artii_result.html', context)


def push(request):
   return render(request, 'services/push.html')


def pull(request):
   num = request.POST.get('number')
   context={
      'num': num
   }
   return render(request, 'services/pull.html',context)