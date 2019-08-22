from django.db import models

# Create your models here.
class Risks(models.Model):
    customer_id= models.ForeignKey("Customer")
    location = models.CharField(max_length = 65, blank=True)
    condition = models.TextField()
    policy_id = models.ForeignKey("Policies", on_delete=models.CASCADE)
    background = models.CharField(max_length = 65, blank=True)
class Customer(models.Model):
    name = models.CharField(max_length = 65, blank=True)
    email= models.CharField(max_length = 65, blank=True)
    premium = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
class Policies(models.Model):
    policy_type = models.CharField(max_length = 65, blank=True)
    customer_id= models.ForeignKey("Customer")
    limit_of_liability = models.PositiveIntegerField()
    start_date = models.DateField()
    expiry_date = models.DateField()
    policy_id =models.ForeignKey("Policies", on_delete=models.CASCADE)
class Claims(models.Model):
    customer_id= models.ForeignKey("Customer")
    date_of_claim = models.DateField()
    claim_number = models.PositiveIntegerField()
    claim_description = models.TextField()
    claim_amount = models.PositiveIntegerField()


