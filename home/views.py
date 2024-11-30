from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student
from home.serializers import StudentSerializer


# Create your views here.

# Create a new student
@api_view(['POST'])
def create_student(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

import logging
logger = logging.getLogger(__name__)
# Get all students
@api_view(['GET'])
def list_students(request):
    logger.debug("Request method: %s", request.method)
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


# Update a student by ID
@api_view(['PUT'])
def update_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete a student by ID
@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    student.delete()
    return Response({'message': 'Student deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


def get_student_by_id(request, id):
    try:
        student = Student.objects.get(id=id)
        return JsonResponse({'id': student.id, 'name': student.name, 'age': student.age, 'course': student.course})
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)