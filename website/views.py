from django.shortcuts import render

# Create your views here.
def main(request):
    context = { 'page' : 'home' }
    return render(request, 'website/mainpage.html', context)

def about_us(request):
    context = { 'page' : 'about-us' }
    return render(request, 'website/about_us.html', context)

def contact(request):
    context = { 'page' : 'contact' }
    return render(request, 'website/contact.html', context)