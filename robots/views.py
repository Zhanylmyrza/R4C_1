import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
from .models import Robot

@csrf_exempt
def robot_create(request):
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            model = data.get('model')
            version = data.get('version')
            created = data.get('created')

            if not all([model, version, created]):
                return JsonResponse({"error": "All fields (model, version, created) are required."}, status=400)

            if len(model) != 2:
                return JsonResponse({"error": "Model must have exactly 2 characters."}, status=400)
            if len(version) != 2:
                return JsonResponse({"error": "Version must have exactly 2 characters."}, status=400)


            created_date = parse_datetime(created)
            if not created_date:
                return JsonResponse({"error": "Invalid date format."}, status=400)


            robot = Robot.objects.create(
                model=model,
                version=version,
                created=created_date
            )
            return JsonResponse({"message": "Robot created successfully.", "id": robot.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)

    return JsonResponse({"error": "Only POST method is allowed."}, status=405)
