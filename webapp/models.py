from django.db import models
from django.contrib.auth.models import User


from django_countries.fields import CountryField




SERVICE_CHOICES = (
    ('Plumbing', 'Plumbing'),
    ('Cleaning', 'Cleaning'),
    ('Electrical', 'Electrical'),
    ('AC', 'AC'),
    ('Landscaping', 'Landscaping'),
    ('Pest Control', 'Pest Control'),
    ('Roofing', 'Roofing'),
    ('Painting', 'Painting'),
    ('Carpeting', 'Carpeting'),
    )



RIO_GRANDE_VALLEY_CITIES = (
    ('Brownsville', 'Brownsville'),
    ('McAllen', 'McAllen'),
    ('Edinburg', 'Edinburg'),
    ('Harlingen', 'Harlingen'),
    ('Mission', 'Mission'),
    ('Pharr', 'Pharr'),
    ('Weslaco', 'Weslaco'),
    ('San Benito', 'San Benito'),
    ('Mercedes', 'Mercedes'),
    ('Alamo', 'Alamo'),
)








class Record(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='records')

    creation_date = models.DateTimeField(auto_now_add= True)

    first_name = models.CharField(max_length = 100)

    last_name = models.CharField(max_length=100)

    email = models.CharField(max_length= 255)

    phone = models.CharField(max_length= 20)

    address = models.CharField(max_length= 300)

    city = models.CharField(max_length= 300, choices = RIO_GRANDE_VALLEY_CITIES)

    postal = models.IntegerField()

    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)

    service_date = models.DateTimeField()

    Commentary = models.TextField(max_length= 300,)

    def __str__(self):

        return self.first_name + " " + self.last_name





