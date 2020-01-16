from django.urls import path
from . import views

urlpatterns = [
	path('', views.Habit_show, name = 'Habit_show'),
	path('addhabit/', views.Add_Habit, name = 'Add_Habit'),
	path('edithabit/', views.Edit_Habit, name = 'Edit_Habit'),
	path('deletehabit/', views.Delete_Habit, name = 'Delete_Habit'),
	path('modifyhabit/', views.Modify_Habit, name = 'Modify_Habit'),
	path('chartshow/', views.Chart_show, name= 'Chart_show'),
	]