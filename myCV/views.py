from django.shortcuts import render
def index(request):
    return render(request, '../../myProject/templates/index.html')
