from django.db import models


class URL(models.Model):
    product_ID = models.IntegerField()
    product_URL = models.CharField(max_length=300)
    product_shop = models.CharField(max_length=10)


class Info(models.Model):
    product_ID = models.ForeignKey(URL, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=30)
    product_name = models.CharField(max_length=200)
    product_manufacturer = models.CharField(max_length=30)


class Cost(models.Model):
    product_ID = models.ForeignKey(URL, on_delete=models.CASCADE)
    product_cost = models.IntegerField()
    last_update = models.TimeField()


class Picture(models.Model):
    product_ID = models.ForeignKey(URL, on_delete=models.CASCADE)
    picture_URl = models.CharField(max_length=300)

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
