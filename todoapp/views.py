from django.http.response import JsonResponse
from django.shortcuts import render, redirect

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from todoapp.models import Costlist
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    complete_amount = 0
    #cost_items = Costlist.objects.all().order_by("-added_date")
    # for cost_item in cost_items:
    #    complete_amount += cost_item.amount
    return render(request, 'todoapp/index.html', {"complete_amount": complete_amount})


@api_view(['POST'])
def add_cost(request):
    if not request.user.is_authenticated:
        if request.is_ajax():
            return JsonResponse({}, status=404)
        return redirect('/login')

    content = request.POST['content']
    amount = request.POST['amount']
    person_used = request.POST['person']
    print(content)
    Costlist.objects.create(
        user=request.user,
        text=content,
        amount=amount,
        person_used=person_used)
    return HttpResponseRedirect("/add_item/")


def list_view_of_costs(request):
    try:
        qs = Costlist.objects.filter(user=request.user or None)
        costs_list = [x.serialize() for x in qs]
        data = {
        "costs_list": costs_list
        }
        return JsonResponse(data, status=200)
    except:
        print("error")
        return JsonResponse(data={}, status=404)
    


@csrf_exempt
def delete_todo(request, todo_id):
    Costlist.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/add_item/")


def cost_of_year(request):
    return render(request, 'todoapp/completeSelavu.html')


def login(request, *args, **keywargs):
    return render(request, 'login.html')


def is_auth_or_no(request):
    is_authenticated = False
    if request.user.is_authenticated:
        is_authenticated = True
    return JsonResponse({"is_authenticated": is_authenticated}, status=200)
