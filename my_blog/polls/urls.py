from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.get_question_list, name='question_list'),
    path("<int:pk>/", view=views.get_question_detail, name='queston_detail')
]