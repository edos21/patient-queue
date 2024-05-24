from django.urls import path, include
from rest_framework import routers, documentation
from core.views import PatientsView, StationsView, PatientStatusView, NextPatientView, EndTurnView

router = routers.DefaultRouter()
router.register(r'patients', PatientsView, 'patients')
router.register(r'stations', StationsView, 'stations')
router.register(r'status', PatientStatusView, 'status')

urlpatterns = [
    path("v1/", include(router.urls)),
    path("docs/", documentation.include_docs_urls(title="Patients API")),
    path('v1/stations/<int:station_id>/next_patient/', NextPatientView.as_view(), name='next_patient'),
    path('v1/stations/<int:station_id>/end_turn/', EndTurnView.as_view(), name='end_turn'),
]
