from django.db import models
from django.contrib.auth.models import User
from time import time
from django.utils import timezone

# Create your models here.
class TicketType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)

    #     TICKET_TYPES = {
    #     ('software', 'Software app'),
    #     ('hardware', 'Hardware Malfunction'),
    #     ('new_user', 'New User'),
    #     ('prophet', 'Prophet'),
    #     ('project', 'Project'),
    # }

class Ticket(models.Model):

    STATUS_CHOICES = {
        ('open', 'Open'),
        ('in_progress','In Progress'),
        ('complete','Completed'),
        ('cancel','Cancelled'),
    }

    title = models.CharField(max_length=200)
    requester = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='requester')
    request_time = models.DateTimeField(default=timezone.now, null=True)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.SET_NULL, null=True, related_name='ticket_type')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="open")
    ticket_description = models.CharField(max_length=10000)
    start_time = models.DateTimeField(default=timezone.now, null=True)
    end_time = models.DateTimeField(default=timezone.now, null=True)
    it_staff_comment = models.CharField(max_length=10000)
    assigned_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_by')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_to')

    def __str__(self):
        return str(self.title)


class TicketCheckList(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, related_name='ticket_check_list')
    completed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='completed_by')
    description = models.CharField(max_length=10000)
    completed_date = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return str(self.description)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class TicketTags(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, related_name='ticket_tag')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, related_name='tag')

    def __str__(self):
        return str(self.tag)


class TicketImage(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, related_name='ticket_image')
    boxend_image = models.ImageField(null=True)

