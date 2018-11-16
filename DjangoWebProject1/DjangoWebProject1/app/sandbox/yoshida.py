from django.db import models

def add(x, y):
    return x + y

class Stock(models.Model):
    # code : INTEGER型で、主キー
    code = models.IntegerField(primary_key=True)
    # 企業名 : 文字列30桁
    name = models.CharField(max_length=30)
    # 時価総額 : 文字列30桁
    capit = models.FloatField()
