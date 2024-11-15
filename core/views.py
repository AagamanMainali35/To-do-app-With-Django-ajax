from django.shortcuts import render, redirect, get_object_or_404
from core.models import tasks
from .serializer import TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.middleware.csrf import get_token


# Regular view to render home page
def home(request):
    csrf=get_token(request)
    datas = tasks.objects.all()
    context = {'data': datas,"csrf_token":csrf}
    return render(request, 'Todolist.html', context)

# API view to get all tasks
@api_view(['GET'])
def getData(request):
    datas = tasks.objects.all()
    serializer = TodoSerializer(datas, many=True)
    return Response(serializer.data)

# API view to get a single task by ID
@api_view(['GET'])
def getSingleData(request, id):
    datas = get_object_or_404(tasks, id=id)
    serializer = TodoSerializer(datas, many=False)
    return Response(serializer.data)

# API view to delete a task by ID
@api_view(['DELETE'])
def delete(request, id):
    datas = get_object_or_404(tasks, id=id)
    datas.delete()
    return Response({'success': 'Data deleted successfully'})

# API view to create a new task
@api_view(['POST'])
def createdata(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': 'Task created successfully'}, status=201)
    return Response(serializer.errors, status=400)

# API view to update a task by ID
@api_view(['PATCH'])
def update(request, id):
    task = get_object_or_404(tasks, id=id)
    serializer = TodoSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': 'Updated successfully'})
    return Response({'error': 'Update failed'}, status=400)

# API view to delete all tasks
@api_view(['DELETE'])
def deleteall(request):
    tasks.objects.all().delete()
    return Response({'success': 'All tasks deleted successfully'})

