#from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Todo


def todo_list(request):
    """
    Returns all todos
    """
    # get all todos
    todos = Todo.objects.all()

    # prepare data to return
    data = {'todos': list(todos.values())}

    # return JSON
    return JsonResponse(data)


def todo_detail(request, pk):
    """
    returns a single todo
    """
    try:
        # find todo by id
        todo = Todo.objects.get(id=pk)
    except ObjectDoesNotExist:
        return JsonResponse({
            'status_code': 404,
            'error': f'Todo with id {pk} does not exist.'
        })
    else:
        # prepare data to return
        data = {
            'id': todo.id,
            'title': todo.title,
            'completed': todo.completed,
            'user': todo.user.username,
        
        }
        # return JSON
        return JsonResponse(data)
