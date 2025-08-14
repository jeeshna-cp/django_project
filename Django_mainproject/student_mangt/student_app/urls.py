from django.urls import path # type: ignore
from. import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('add_student',views.add_student,name='add_student'),
    path('contact/',views.contact,name='contact'),
    path('student_view',views.student_view,name='student_view'),
    path('update/<int:pk>/',views.update_student,name='update'),
    path('delete/<int:pk>/',views.delete_student,name='delete'),
  
]
