from django.shortcuts import render

# Create your views here.
def index(request):
    c = ''
    if request.method == 'POST':
        a = eval(request.POST.get('outer'))
        c = eval('a')
    return render(request, 'calcapp1/index.html', {'ans':c})