from django.db import models
from customers.models import Customer
from robots.models import Robot  

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    robot_serial = models.CharField(max_length=5, blank=False, null=False)
    robot = models.ForeignKey(Robot, null=True, blank=True, on_delete=models.SET_NULL)  
