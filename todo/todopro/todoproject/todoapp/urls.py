from . import views
from django.urls import path
app_name = "todoapp"
urlpatterns = [

    path('',views.todo,name="todo"),
    path('delete/<int:tkid>/',views.delete,name='delete'),
    path('update /<int:fmid>/',views.update,name='update'),
    path('cbv/',views.todoListview.as_view(),name='cbv'),
    path('cv/<int:pk>/',views.tododetail.as_view(),name='cv'),
    path('up/<int:pk>/',views.todoup.as_view(),name='up'),
    path('delete/<int:pk>/', views.tododelete.as_view(), name='delete')

]