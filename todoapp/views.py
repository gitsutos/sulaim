from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
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
    return render(request, 'pages/index.html', {"complete_amount": complete_amount})


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
    return HttpResponseRedirect("/cost-manager-by-tos/add_item/")


def list_view_of_costs(request):
    try:
        qs = Costlist.objects.filter(user=request.user or None)
        costs_list = [x.serialize() for x in qs]
        # print(costs_list)
        data = {
            "costs_list": costs_list
        }
        return JsonResponse(data, status=200)
    except:
        print("error")
        return JsonResponse(data={}, status=400)


@csrf_exempt
def delete_todo(request, todo_id):
    Costlist.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/add_item/")


def cost_of_year(request):
    return render(request, 'pages/complete.html')


def login_view(request, *args, **keywargs):
    if request.user.is_authenticated:
        return redirect('/cost-manager-by-tos/add_item/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('/cost-manager-by-tos/add_item/')
            else:
                HttpResponse('USER IS NOT ACTIVE')
        else:
            JsonResponse({}, status=401)
            return render(request, 'login.html', {"error_msg": "User name and password does not match"})

    return render(request, 'login.html')


def is_auth_or_no(request):
    is_authenticated = False
    if request.user.is_authenticated:
        is_authenticated = True
    return JsonResponse({"is_authenticated": is_authenticated}, status=200)


def sign_up_view(request):
    registered = False
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/login/')
        else:
            print(form.errors)
            print("error")
            JsonResponse({"error": 'password not match'}, status=404)
    else:
        form = UserForm()
        registered = False

    return render(request, "sign_up.html", context={"form": form})


def logout_view(request):
    logout(request)
    return redirect('/cost-manager-by-tos/add_item/')
