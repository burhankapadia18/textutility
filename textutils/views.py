# custom made file - BK

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text
    txt = request.POST.get('text', 'default')

    # check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullCaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    purpose = ''
    # check which checkbox is on
    if removepunc == 'on':
        analyzed = ""
        for char in txt:
            if char not in punctuations:
                analyzed = analyzed + char
        txt = analyzed
        purpose += 'Removed Punctuations, '
    if fullcaps == "on":
        analyzed = ""
        for char in txt:
            analyzed = analyzed + char.upper()
        txt = analyzed
        purpose += 'Changed to Uppercase, '
    if newlineremover == "on":
        analyzed = ""
        for char in txt:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        txt = analyzed
        purpose += 'newline removed, '
    if extraspaceremover == "on":
        analyzed = ""
        for idx, char in enumerate(txt):
            if not(txt[idx] == " " and txt[idx+1] == " "):
                analyzed = analyzed + char
        txt = analyzed
        purpose += 'Removed extra spaces'

    if removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on':
        params = {'purpose': 'Error!!!', 'analyzed_text': 'None of the options selected'}
        return render(request, 'analyze.html', params)

    params = {'purpose': purpose, 'analyzed_text': txt}
    return render(request, 'analyze.html', params)