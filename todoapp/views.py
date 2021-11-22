from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,redirect

from .forms import UserSignUpForm
from mysite.settings import LOGIN_URL
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate,login,logout
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from todoapp.models import Costlist
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    # print(request.user)
    complete_amount = 0
    #cost_items = Costlist.objects.all().order_by("-added_date")
    #for cost_item in cost_items:
    #    complete_amount += cost_item.amount
    return render(request, 'todoapp/index.html', {"complete_amount":complete_amount})

@api_view(['POST'])
def add_cost(request):
    if not request.user.is_authenticated:
        return redirect(LOGIN_URL)
   
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
    qs = Costlist.objects.filter(user=request.user or None)
    costs_list = [x.serialize() for x in qs]   
    data = {
        "response":costs_list
    }
    return JsonResponse(data, status=200)

@csrf_exempt
def delete_todo(request, todo_id):
    Costlist.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/cost-manager-by-tos/add_item/")
    
    

def cost_of_year(request):
    return render(request, 'todoapp/completeSelavu.html')

def user_login(request, *args , **keywargs):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect("/cost-manager-by-tos/add_item/")

            else:
                return HttpResponse("ACCONT IS NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            return HttpResponse("invalid login detailes ")
    else:
        return render(request,'login.html',{})
    
def user_logout(request):
    if not request.user.is_authenticated:
        return HttpResponse("<h1>PAGE NOT FOUND !</h1>")
    logout(response)
    return HttpResponseRedirect('/cost-manager-by-tos/add_item/')


def use_sign_up(request):
    registered = False

    if request.method == 'POST':
        form = UserSignUpForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            registered = False
    
        else:
            print(form.errors)
    
    else:
        form=UserSignUpForm

    return render(request, 'signup.html' ,{"form":form})