from django.db import models


class Instrument(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    holding_value = models.FloatField(null=True)
    total_profit_loss = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Trade(models.Model):
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument,on_delete=models.CASCADE)
    volume = models.FloatField(null=True)
    buy_value = models.FloatField(null=True)
    sell_value = models.FloatField(null=True)
    profit_loss = models.FloatField(null=True)