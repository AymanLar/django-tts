from django.shortcuts import render
from gTTS.templatetags.gTTS import say

# Create your views here.

def index(request):
    obj = say(language='en-us', text="Text input")
    return render(request, 'index.html', {'obj':obj})
