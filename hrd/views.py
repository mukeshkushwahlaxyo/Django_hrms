from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout

from employee.models import User
from hrd.models import Employee,TypesMast,StatusMast,GradesMast,DesigMast,ComapnyMast,AcademicsMast,BankDetails,Document
from employee.forms import SignUpForm,EmployeeEditForm
from hrd.forms import PersonalInfo,OfficeInfo,AcademicsInfo,BankInfo,Documents

from rolepermissions.roles import assign_role
from rolepermissions.checkers import has_role
from rolepermissions.roles import get_user_roles
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
import datetime
import os
from django.conf import settings

class Employees:

	@login_required
	def index(request):		
		# if has_role(request.user,'is_employee'):
		# 	return HttpResponse('role')
		user = User.objects.all()
		return render(request, "employees/index.html",{'user':user})

	@login_required	
	def EmployeeCreate(request):	
		form = SignUpForm()
		return render(request, "registration.html",{'form':form})


	def saveEmployee(request):	
		form = SignUpForm(request.POST)
		if request.POST:
			if form.is_valid():

				user1 = form.save()
				assign_role(user1, 'is_employee')
				emp = Employee(user_id=user1.id)
				emp.save()
				# form.refresh_from_db()
				# raw_password = form.cleaned_data.get('password1')
				# user = authenticate(username=user1.username, password=raw_password)
				 # user = User.objects.get(id=1)
			
				# login(request, user)
				return redirect('/hrd/employees')
				# if request.user.is_authenticated:
					
					# role = get_user_roles(user)
					# return HttpResponse(role)
					# return HttpResponse(request.user.username)
					
			else:
			 	 return render(request, "registration.html",{'form':form})
		else:
			return render(request, "registration.html",{'form':form}) 

	@login_required		
	def deleteEmployee(request,id):
		user = User.objects.get(pk=id)
		group = Group.objects.get(name='is_employee') 
		user.groups.remove(group)
		user.delete();
		return redirect('/hrd/employees')

	@login_required
	def editEmployee(request,id=''):
		if request.method=='POST':
			data = User.objects.get(id=id)
			form = EmployeeEditForm(request.POST,instance = data)		
			if form.is_valid():
				form.save();
				return redirect('/hrd/employees')
		else:
			data = User.objects.get(id=id)
			form = EmployeeEditForm(instance = data)
			return render(request, "employees/edit.html",{'form':form,'id':id})

	@login_required
	def showTabs(request,page,id):
		employee = Employee.objects.get(user_id=id)		
		if page == 'main':
			main = render(request, "employees/empinfo.html",{'id':id})

		if page == 'personal':
			if request.method == 'POST':
				form = PersonalInfo(request.POST,instance=employee)
				if form.is_valid():
					form.save()
					return HttpResponse(status=200)
				else:
					main = render(request, "employees/forms/personal.html",{'form':form},status=201)	
			else:
				form = PersonalInfo(instance=employee)
				main = render(request, "employees/forms/personal.html",{'form':form})	

		if page == 'office':
			if request.method =='POST':
				form = OfficeInfo(request.POST,instance=employee)
				if form.is_valid():
					form.save()
					return HttpResponse(status=200)
				else:
					main = render(request, "employees/forms/office.html",{'form':form},status=201)
			else:
				form = OfficeInfo(instance=employee)
				main = render(request, "employees/forms/office.html",{'form':form})	

		if page == 'academics':
			file = request.FILES.get('document')
			obj = AcademicsMast()	
			if request.method=='POST':			
				form =AcademicsInfo(request.POST)
				if form.is_valid():

					AcademicsMast.objects.create(
						doman_of_study= request.POST.get('doman_of_study'),
						name_of_board= request.POST.get('name_of_board'),
						complete_in= request.POST.get('complete_in'),
						gared= request.POST.get('gared'),
						document= file.name,
						note= request.POST.get('gared'),
						emp_id= request.POST.get('emp_id'),
						)

					today_folder = datetime.datetime.now().strftime("%B%d_%Y")+'/document/'
					path_to_img = os.path.join(settings.MEDIA_ROOT, today_folder)
					if not os.path.exists(path_to_img):
						os.mkdir(path_to_img)
					img_path = os.path.join(path_to_img, file.name)

					with open(img_path, 'wb+') as destination:
						if file.multiple_chunks:  # size is over than 2.5 Mb
							for chunk in file.chunks():
								destination.write(chunk)
						else:
							destination.write(file.read())
					data = AcademicsMast.objects.filter(emp_id=id)
					return render(request, "employees/tableRefresh/academicTable.html",{'data':data,'id':id})
				else:
					data = AcademicsMast.objects.filter(emp_id=id)
					main = render(request, "employees/forms/academics.html",{'form':form,'id':id,'data':data},status=201)
			else:	
				form  = AcademicsInfo()
				data  = AcademicsMast.objects.filter(emp_id=id)
				main  = render(request, "employees/forms/academics.html",{'form':form,'id':id,'data':data})
		if page == 'bankinfo':
			if request.method=='POST':
				form = BankInfo(request.POST,request.FILES)
				file = request.FILES.get('document')
				if form.is_valid():
					BankDetails.objects.create(
						accou_hol_name=request.POST.get('accou_hol_name'),
						accou_num =request.POST.get('accou_num'),
						bank_name =request.POST.get('bank_name'),
						ifsc_code =request.POST.get('ifsc_code'),
						branch =request.POST.get('branch'),
						document =file.name,
						note =request.POST.get('note'),
						emp_id = request.POST.get('emp_id')
						)

					today_folder = datetime.datetime.now().strftime("%B%d_%Y")+'/bankinfo/'
					path_to_img = os.path.join(settings.MEDIA_ROOT, today_folder)
					if not os.path.exists(path_to_img):
						os.mkdir(path_to_img)
					img_path = os.path.join(path_to_img, file.name)

					with open(img_path, 'wb+') as destination:
						if file.multiple_chunks:  # size is over than 2.5 Mb
							for chunk in file.chunks():
								destination.write(chunk)
						else:
							destination.write(file.read())
					data = BankDetails.objects.filter(emp_id=id)
					return render(request, "employees/tableRefresh/bankinfoRefresh.html",{'data':data,'id':id},status=200)

				else:
					form = BankInfo(request.POST)
					data = BankDetails.objects.filter(emp_id=id)
					main = render(request, "employees/forms/bankinfo.html",{'form':form,'id':id,'data':data},status=201)	
			else:
				form = BankInfo()
				data = BankDetails.objects.filter(emp_id=id)
				main = render(request, "employees/forms/bankinfo.html",{'form':form,'id':id,'data':data})

		if page == 'document':
			if request.method == 'POST':
				form = Documents(request.POST,request.FILES)
				file = request.FILES.get('files')
				if form.is_valid():
					Document.objects.create(
						document_title=request.POST.get('document_title'),
						document_status =request.POST.get('document_status'),
						note =request.POST.get('note'),
						file =file.name,
						emp_id = request.POST.get('emp_id')
						)

					today_folder = datetime.datetime.now().strftime("%B%d_%Y")+'/document/'
					path_to_img = os.path.join(settings.MEDIA_ROOT, today_folder)
					if not os.path.exists(path_to_img):
						os.mkdir(path_to_img)
					img_path = os.path.join(path_to_img, file.name)

					with open(img_path, 'wb+') as destination:
						if file.multiple_chunks:  # size is over than 2.5 Mb
							for chunk in file.chunks():
								destination.write(chunk)
						else:
							destination.write(file.read())
					data = Document.objects.filter(emp_id=id)
					return render(request, "employees/tableRefresh/documentRefresh.html.html",{'data':data,'id':id},status=200)
				else:
					data = Document.objects.filter(emp_id=id)					
					main = render(request, "employees/forms/document.html",{'form':form,'data':data,'id':id},status=201)
			else:
				form = Documents()
				data = Document.objects.filter(emp_id=id)
				main = render(request, "employees/forms/document.html",{'form':form,'data':data,'id':id})		
									
		return main

