from django.shortcuts import render,HttpResponse
import json
from django.http import JsonResponse

# Create your views here.
# 数据库
DB = ['nihao','shj']

def home(request):
    return render(request,'home.html')


def send_msg(request):
    text = request.GET.get('text')
    DB.append(text)

    return HttpResponse("OK")


def get_msg(request):
    index = int(request.GET.get('index'))
    context = {
        "data": DB[index:],
        "max_index": len(DB)
    }
    return JsonResponse(context)

