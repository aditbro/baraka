from django.shortcuts import render
from website.models import LowonganKerja

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

def loker_jabar(request):
    data_loker = LowonganKerja.objects.filter(daerah="JABAR")
    context = { 'page' : 'career', 'loker' : data_loker, 'img': 'banner_jawa_barat.png' }
    return render(request, 'website/loker.html', context)

def loker_jateng(request):
    data_loker = LowonganKerja.objects.filter(daerah="JATENG")
    context = { 'page' : 'career', 'loker' : data_loker, 'img': 'banner_jawa_tengah.png' }
    return render(request, 'website/loker.html', context)

def loker_jatim(request):
    data_loker = LowonganKerja.objects.filter(daerah="JATIM")
    context = { 'page' : 'career', 'loker' : data_loker, 'img': 'banner_jawa_timur.png' }
    return render(request, 'website/loker.html', context)

def loker_jakarta(request):
    data_loker = LowonganKerja.objects.filter(daerah="JKT")
    context = { 'page' : 'career', 'loker' : data_loker, 'img': 'banner_dki_jakarta.png' }
    return render(request, 'website/loker.html', context)

def loker_detail(request, id):
    try:
        data_loker = LowonganKerja.objects.get(id=id)
        context = { 'page' : 'career', 'loker' : data_loker }
        return render(request, 'website/loker_detail.html', context)
    except LowonganKerja.DoesNotExist as e:
        return main(request)