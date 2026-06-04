from django.contrib.auth import get_user_model
from incidents.models import Incident
from incidents.views import _send_incident_status_change_email

User = get_user_model()

incident = Incident.objects.first()
if not incident:
    print('No incidents found in the database. Creating a test reporter and incident may fail if required fields are missing.')
    try:
        reporter, created = User.objects.get_or_create(username='test_reporter', defaults={'email': 'reporter@example.com', 'password': 'pass'})
        dispatcher, created = User.objects.get_or_create(username='test_dispatcher', defaults={'email': 'dispatcher@example.com', 'password': 'pass', 'role': 'dispatcher'})
        incident = Incident.objects.create(
            title='Test Incident',
            description='Automated test incident for email notifications',
            incident_type='flood',
            latitude=10.0,
            longitude=10.0,
            location_description='Test location',
            reported_by=reporter,
            assigned_to=dispatcher,
        )
        print('Created test incident with id', incident.pk)
    except Exception as e:
        print('Failed to create test incident:', e)
        raise SystemExit(1)

old_status = incident.status
print('Calling _send_incident_status_change_email for incident id', incident.pk, 'old_status=', old_status)
_send_incident_status_change_email(incident, old_status, None)
print('Email helper called — check console output above for the rendered email (console backend).')
