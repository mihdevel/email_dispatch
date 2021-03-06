from django.db import models


class Email(models.Model):
  email = models.EmailField()
  group_id = models.ForeignKey('Group', on_delete=models.CASCADE)
  
  def __str__(self):
    return self.email


class Group(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name


class Dispatch(models.Model):
  template_id = models.ForeignKey('Template', on_delete=models.CASCADE)
  date = models.DateTimeField()
  
  def __str__(self):
    return str(self.template_id)


class Report(models.Model):
  dispatch_id = models.ForeignKey(Dispatch, on_delete=models.CASCADE)
  status = models.BooleanField()


class Template(models.Model):
  name = models.CharField(max_length=100)
  group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
  text = models.TextField()
  
  def __str__(self):
    return self.name