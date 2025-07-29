from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Appointment

@csrf_exempt  # Only for development; handle CSRF properly in production
def create_appointment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            name = data.get('name')
            email = data.get('email')  # get email
            phone = data.get('phone')
            city = data.get('city')
            date = data.get('date')
            time = data.get('time')
            services = ", ".join(data.get('services', []))  # comma-separated string

            if not all([name, email, phone, city, date, time, services]):
                return JsonResponse({'message': 'Missing fields'}, status=400)

            Appointment.objects.create(
                name=name,
                email=email,  # save email
                phone=phone,
                city=city,
                date=date,
                time=time,
                services=services
            )

            return JsonResponse({'message': 'Appointment created successfully'}, status=201)

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

    return JsonResponse({'message': 'Invalid method'}, status=405)
