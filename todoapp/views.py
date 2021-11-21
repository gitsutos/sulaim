from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from rest_framework.decorators import api_view
from todoapp.models import Costlist
from django.http import HttpResponseRedirect


# Create your views here.
def empty(request):
    return HttpResponseRedirect("add_item/")


def index(request):
    print(request.user)
    complete_amount = 0
    cost_items = Costlist.objects.all().order_by("-added_date")
    for cost_item in cost_items:
        complete_amount += cost_item.amount
    return render(request, 'todoapp/index.html', {"todo_items": cost_items,
                                                    "complete_amount":complete_amount})

@api_view(['POST'])
def add_cost(request):
    if not request.user.is_authenticated:
        if request.is_ajax():
            return JsonResponse({}, status=404)
        return redirect('/login')
    now_date = timezone.now()
    content = request.POST['content']
    amount = request.POST['amount']
    person_used = request.POST['person']
    print(now_date, '\n', content)
    Costlist.objects.create(
        user=request.user,
		text=content, 
		amount=amount, 
		person_used=person_used)
    return HttpResponseRedirect("/add_item/")
    
    

def delete_todo(request, todo_id):
    Costlist.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/add_item/")
    
    

def cost_of_year(request):
    return render(request, 'todoapp/completeSelavu.html')

def login(request, *args , **keywargs):
    return render(request,'login.html')