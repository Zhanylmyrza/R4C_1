from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
from robots.models import Robot
from customers.models import Customer

def create_order(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        robot_serial = request.POST.get('robot_serial')

        try:
            customer = Customer.objects.get(id=customer_id)
            robot = Robot.objects.get(serial=robot_serial)

            order = Order.objects.create(customer=customer, robot=robot, robot_serial=robot_serial)
            return JsonResponse({"message": "Order created successfully.", "order_id": order.id}, status=201)
        
        except Customer.DoesNotExist:
            return JsonResponse({"error": "Customer not found."}, status=400)
        except Robot.DoesNotExist:
            return JsonResponse({"error": "Robot not available."}, status=400)
    return JsonResponse({"error": "Only POST method is allowed."}, status=405)
