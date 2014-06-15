from django.db import models

class CallPerson(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Connection(models.Model):
    init_person = models.ForeignKey(CallPerson, null=False, related_name='init_person')
    answer_person = models.ForeignKey(CallPerson, null=False, related_name='answer_person')
    duration = models.IntegerField(default=0)
    date = models.DateTimeField('Date')

    def __str__(self):
        return "{} {} {} {}".format(self.init_person, self.answer_person, self.duration, self.date)

    def was_answered(self):
        return self.duration > 0
