from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'homepage.html')


def about_us(request):
    return render(request, 'aboutUs.html')


def documents(request):
    return render(request, 'documents.html')


def events(request):
    return render(request, 'eventCalendar.html')


def outreach(request):
    return render(request, 'outreach.html')


def image_archive(request):
    return render(request, 'imageArchive.html')

def prog_comp(request):
	return render(request, 'progComp.html')
