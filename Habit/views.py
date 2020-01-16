from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from .models import Habit
from .forms import AddForm

# Create your views here.
def Habit_show(request):
	habit = Habit.objects.order_by('id')
	return render(request, 'table_show.html', {'habit': habit})

def Add_Habit(request):
	if request.method == 'POST':
		habitform = AddForm(request.POST)
		habitform.save()
		habit = Habit.objects.order_by('id')
		return HttpResponse("Success")

def Edit_Habit(request):
	habit_list = Habit.objects.filter(habit=request.POST.get('EditID'))
	return render(request, 'edit_show.html', {'filter':habit_list})

def Delete_Habit(request):
	delete_id = request.POST.get('ehabit')
	Habit.objects.filter(habit=request.POST.get('ehabit')).delete()
	return HttpResponse("success")

def Modify_Habit(request):
	fhabit = request.POST.get('fhabit')
	mhabit = request.POST.get('habit')
	mtime = request.POST.get('Time')
	mMon = request.POST.get('Mon')
	mTue = request.POST.get('Tue')
	mWed = request.POST.get('Wed')
	mThu = request.POST.get('Thu')
	mFri = request.POST.get('Fri')
	mSat = request.POST.get('Sat')
	mSun = request.POST.get('Sun')
	Habit.objects.filter(habit=request.POST.get('fhabit')).update(habit=mhabit, Time=mtime, Mon=mMon, Tue=mTue, Wed=mWed, Thu=mThu, Fri=mFri, Sat=mSat, Sun=mSun)
	return HttpResponse("success")

def Chart_show(request):
	habit = Habit.objects.order_by('id')
	nDays = []
	nCount = 0
	for habi in habit:
		if habi.Mon == 'true':
			nCount += 1
		if habi.Tue == 'true':
			nCount += 1
		if habi.Wed == 'true':
			nCount += 1
		if habi.Thu == 'true':
			nCount += 1
		if habi.Fri == 'true':
			nCount += 1
		if habi.Sat == 'true':
			nCount += 1
		if habi.Sun == 'true':
			nCount += 1
		nDays.append(nCount)
		nCount = 0
	return render(request, 'chart_show.html', {'habit': habit, 'nDays':nDays})
