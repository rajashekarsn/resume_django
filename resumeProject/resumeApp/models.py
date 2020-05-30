from django.db import models


class NavMenuItems(models.Model):
    item_name = models.CharField(max_length=30)
    item_link_href = models.CharField(max_length=30)


class AboutInfo(models.Model):
    about_first_name = models.CharField(max_length=30)
    about_second_name = models.CharField(max_length=30)
    about_address = models.TextField(max_length=300)
    about_mobile_number = models.CharField(max_length=10)
    about_email = models.EmailField()
    about_description = models.TextField(max_length=1000)


class Experience(models.Model):
    company = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    role_description = models.TextField(max_length=1000)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return self.company


class RoleBullets(models.Model):
    role_bullets = models.TextField(max_length=1000)
    company = models.ForeignKey(Experience, on_delete=models.CASCADE)

    def __str__(self):
        return self.role_bullets


class Education(models.Model):
    degree = models.CharField(max_length=30)
    university = models.CharField(max_length=30, blank=True)
    specialization = models.CharField(max_length=30, blank=True)
    percentage = models.CharField(max_length=5, blank=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)


class LanguagesTools(models.Model):
    description = models.TextField(max_length=1000)


class Interests(models.Model):
    description = models.TextField(max_length=1000)


class Awards(models.Model):
    award = models.TextField(max_length=1000)


