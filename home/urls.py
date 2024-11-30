from django.urls import path

from .views import *
urlpatterns = [

    path('students', create_student, name='students-add'),
    path('students/list', list_students, name='list_stu'),
    path('students/<int:pk>/update', update_student, name='update_student'),
    path('students/<int:pk>/delete', delete_student, name='delete_student'),
    path('students/<int:id>/data',get_student_by_id, name='get_student_by_id'),
]
