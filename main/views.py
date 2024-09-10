from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'appname' : 'main',
        'name': 'Damar Aryaputra Rahman',
        'class': 'KKI'
    }

    return render(request, "main.html", context)