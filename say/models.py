from django.db import models

class testInfo(models.Model):
    title = models.CharField(max_length=20)
    ttpub_date = models.DateField()
    tread = models.IntegerField(default=0)
    tcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table='testinfo'