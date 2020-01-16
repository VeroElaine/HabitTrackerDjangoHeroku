from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import Habit.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", Habit.views.Habit_show, name = "Habit_show"),
	path("addhabit/", Habit.views.Add_Habit, name = "Add_Habit"),
	path("edithabit/", Habit.views.Edit_Habit, name = "Edit_Habit"),
	path("deletehabit/", Habit.views.Delete_Habit, name = "Delete_Habit"),
	path("modifyhabit/", Habit.views.Modify_Habit, name = "Modify_Habit"),
	path("chartshow/", Habit.views.Chart_show, name= "Chart_show"),
    path("admin/", admin.site.urls),
]
