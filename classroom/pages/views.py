from django.shortcuts import render

# Create your views here.
tr = ['A','B','C','D']
st={'a':22,'b':23,'c':24,'d':25}
def info(request):
    context={'teacher': tr,
    'student' : st.keys()}
    return render(request, 'info.html', context)

def student(request, name):
    context = {
        'name' : name
        ,'age' : st[name]}
    return render(request, 'student.html',context)

def first(request):
    return render(request, 'first.html')