

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello Render! Django is working 🎉</h1>")
