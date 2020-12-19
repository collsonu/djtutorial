from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removeunc = request.POST.get('analyse', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    counttt = request.POST.get('counttt' , 'off')
    if removeunc == 'on':

        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for i in djtext:
            if i not in punctuation:
                analyzed = analyzed + i

        params = {'purpose': 'remove punctuations', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)

    if(fullcaps == "on"):
        analyzed = ""
        for i in djtext:
            analyzed = analyzed + i.upper()
        params = {'purpose': 'change to upper case', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)

    if(counttt == "on"):
        analyzed = 0
        for i in djtext:
            analyzed += 1
        params = {'purpose': 'count char', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')


def about(request):
    return HttpResponse('hello mr. sonu hooware you?')
