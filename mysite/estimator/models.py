from django.db import models

# Create your models here.
class Poll(models.Model):
    text = models.CharField(max_length =255)
    pub_date = models.DateField()


    def __str__(self):
        return self.text

class Choice(models.Model):
    """docstring fo Choice."""

    question = models.ForeignKey(Poll, on_delete = models.CASCADE,null=True, blank=True)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
#It allows to print the pices of the characters in the ORM this is in 24 25 tutorial

    def __str__(self):
        return "{} - {}" .format(self.question.text[:25], self.choice_text[:25])
