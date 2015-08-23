from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email


class Note(models.Model):
    user = models.ForeignKey(User)
    body = models.TextField()
    create_ts = models.DateTimeField(null=False, auto_now_add=True)
    update_ts = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        db_table = "note"

    def __str__(self):
        return str(self.user) + " user_id: " + str(self.id)

