from django.conf.urls import url
from . import login
	
urlpatterns = [
    url(r'^selecttype/', login.selecttype),
    url(r'^register/',login.register),
    url(r'^patientregister/',login.patientregister),
    url(r'^doctorregister/',login.doctorregister),
    url(r'^familyregister/',login.familyregister),
    url(r'^login/',login.test),	
    
]
