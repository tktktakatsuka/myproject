from django.shortcuts import render

# Create your views here.
# memo_app/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # 先ほど作成したhtmlを第2引数に指定する