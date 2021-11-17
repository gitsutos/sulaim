from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from todoapp.models import Todo
from django.http import HttpResponseRedirect


# Create your views here.
def empty(request):
    return HttpResponseRedirect("add_item/")


def index(request):
    complete_amount = 0
    todo_items = Todo.objects.all().order_by("-added_date")
    for todo_item in todo_items:
        complete_amount += todo_item.amount
    return render(request, 'todoapp/index.html', {"todo_items": todo_items,
                                                    "complete_amount":complete_amount})


@csrf_exempt
def AddDo(request):
    now_date = timezone.now()
    content = request.POST['content']
    amount = request.POST['amount']
    person_used = request.POST['person']
    print(now_date, '\n', content)
    Todo.objects.create(added_date=now_date, 
		text=content, 
		amount=amount, 
		person_used=person_used)
    return HttpResponseRedirect("/add_item/")
    
    

@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/add_item/")
    
    

@csrf_exempt
def cost_of_year(request):
    return render(request, 'todoapp/completeSelavu.html')
