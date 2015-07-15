from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render,get_object_or_404
from .forms import DoctorForm
from .forms import FamilyForm
from .forms import PatientForm
from .forms import LoginForm
from .models import Doctor
from .models import Patient
from .models import FamilyMember
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect


def selecttype(request):
	return render_to_response('type.html')


def register(request):
	if 'type' in request.GET and request.GET['type']:
		type = request.GET['type']

		if type == "patient":
			form = PatientForm()
			return render(request, 'patient.html', {'form' : form})
		elif type == "doctor":
			form = DoctorForm()
			return render(request, 'doctor.html', {'form' : form})
		else:
			form = FamilyForm()
			return render(request, 'family.html', {'form' : form})



def patientregister(request):
	if request.method == "POST":
		form = PatientForm(request.POST)
		if form.is_valid():
			patient = form.save()
			#patient.save()
			return render(request, 'patient.html', {'form': form, 'success': 'Register Success !'})
	else:
		form = PatientForm()
	return render(request, 'patient.html', {'form': form})


def doctorregister(request):
	if request.method == "POST":
		form = DoctorForm(request.POST)
		if form.is_valid():
			doctor = form.save()
			#doctor.save()
			return render(request, 'doctor.html', {'form': form, 'success': 'Register Success !'})
	else:
		form = DoctorForm()

	return render(request, 'doctor.html', {'form': form})


def familyregister(request):
	if request.method == "POST":
		form = FamilyForm(request.POST)
		if form.is_valid():
			family = form.save()
			#family.save()
			return render(request, 'family.html', {'form': form, 'success': 'Register Success !'})
	else:
		form = FamilyForm()


	return render(request, 'family.html', {'form': form})


def login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid() :
			username = request.POST.get('username', '')
			password = request.POST.get('password', '')
			type = form.cleaned_data['accounttype']
			
			if username and password :
				if type == 'Patient' :
					try:
						patient = Patient.objects.get(uname = username)		
					except Patient.DoesNotExist :
						return render(request, 'login.html', {'form':form, 'error': True})
					else:
						if password == patient.password :
							patientform = PatientForm(instance = patient)
							return render(request, 'profile.html', {'form' : patientform})
						else:
							return render(request, 'login.html', {'form':form, 'error': True})

				elif type == 'Doctor' :
					try:
						doctor = Doctor.objects.get(uname = username)
					except Doctor.DoesNotExist :
						return render(request, 'login.html', {'form':form, 'error': True})
					else:
						if password == doctor.password :
							doctorform = DoctorForm(instance = doctor)
							return render(request, 'profile.html', {'form' : doctorform})
						else:
							return render(request, 'login.html', {'form':form, 'error': True})

				elif type == 'FamilyMember' :
					try:
						fm = FamilyMember.objects.get(uname =username)
					except FamilyMember.DoesNotExist :
						return render(request, 'login.html', {'form':form, 'error': True})
					else:
						if password == fm.password :
							familyform = FamilyForm(instance = fm)
							return render(request, 'profile.html', {'form' : familyform})
						else:
							return render(request, 'login.html', {'form':form, 'error': True})

	else:
		form = LoginForm()

	return render(request, 'login.html', {'form' : form}) 

	@csrf_exempt
	def test(request):
		if request.method == "POST":
			username = request.POST.get('username', '')
			password = request.POST.get('password', '')
			type = request.POST.get('type','')

			if username and password:
				


			if username == "seven" and password == "123456" :
				response = JsonResponse({'success': 1})
			else:
				response = JsonResponse({'success': 0})
			return HttpResponse(response)

		else:
			response = JsonResponse({'success': 0})
			return HttpResponse(response)

