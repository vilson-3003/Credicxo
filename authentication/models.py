from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.dispatch import receiver
from credixco_task.settings import EMAIL_HOST_USER
from smtplib import SMTPException

# Create your models here.
class User(AbstractUser):
    # Boolean fields to select the type of account.
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)



class Admin(models.Model):
    admin = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.admin.username


class Teacher(models.Model):
    teacher = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    mobile_no = models.BigIntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.teacher.username


class Student(models.Model):
    student = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    mobile_no = models.BigIntegerField(default=0)

    def __str__(self):
        return self.student.username


@receiver(reset_password_token_created)
def password_reset_token_created(reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={} {}".format("Hello "+reset_password_token.user.username+",\n\nPlease follow this link: http://127.0.0.1:8000/api/passwordreset?token=", reset_password_token.key, " to reset your password.\n\n\nWith Best Regards;\nTeam Romeo")
    pass_reset = "Password Reset : Credixo {title}".format(
        title="Forgot Password")
    # email_plaintext_message = MIMEText(email_plaintext_message ,'html')
    try:
        mail = send_mail(pass_reset, email_plaintext_message, EMAIL_HOST_USER, [reset_password_token.user.email], fail_silently=True)
        print(email_plaintext_message, mail)
    except SMTPException as e:
        print(e)