from django.db import models

# Create your models here.
class MovieData(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    typ = models.CharField(max_length=200, default='action')
    
''' обычный HTTP-запрос используется для отображения данных 
о погоде непосредственно на веб-странице для пользователя, 
в то время как API-запрос используется для получения данных 
о погоде для обработки в приложении или скрипте 
с последующим использованием этих данных для выполнения каких-либо действий.'''