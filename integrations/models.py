from django.db import models


class FaireAPI(models.Model):
    class Meta:
        verbose_name = 'Faire API'
        verbose_name_plural = 'Faire API'

    integration_name = models.CharField(max_length=50)
    api_key = models.CharField(max_length=100)


class FaireAPIEndpoints(models.Model):
    class Meta:
        verbose_name = 'Faire API Endpoints'
        verbose_name_plural = 'Faire API Endpointss'
    
    endpoint_name = models.CharField(max_length=100)
    endpoint_url = models.CharField(max_length=250)
