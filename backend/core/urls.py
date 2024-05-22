from django.urls import path, include
from rest_framework import routers, documentation
from core import views

router = routers.DefaultRouter()
router.register(r'patients', views.PatientsView, 'patients')

urlpatterns = [
    path("v1/", include(router.urls)),
    path("docs/", documentation.include_docs_urls(title="Patients API"))
]
