from django.shortcuts import render

# Create your views here.
def main(request):
    context = { 'page' : 'home' }
    return render(request, 'website/mainpage.html', context)