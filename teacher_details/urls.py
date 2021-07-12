from django.urls import path,include
# from teacher_details.views import *
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
            path('first_view/',login_required(Firstclassbased_View.as_view())),
            path('teacherslist/',login_required(Read_Teachers.as_view()),name='teachers_index'),
            path('teachersdetails/<int:pk>/',login_required(Detail_Teachers.as_view())),
            path('teacherscreate/',login_required(Create_Teachers.as_view())),
            path('teachersupdate/<int:pk>/',login_required(Update_Teachers.as_view())),
            path('teachersdelete/<int:pk>/',login_required(Delete_Teachers.as_view())),
]