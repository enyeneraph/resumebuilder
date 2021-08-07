# from typing_extensions import Required
from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT, SET_NULL
# from django.db.models.base import Model

# Create your models here.
class Personal_Details(models.Model):
    user_id = models.AutoField(primary_key=True)
    session_id = models.CharField(max_length=32, default='missed')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    professional_title = models.CharField(max_length = 50)
    city_of_residence = models.CharField(max_length= 50)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    summary = models.TextField(max_length= 400)
    image = models.ImageField(upload_to ='images/', null=True, blank= True)

    def __str__(self) -> str:
        return  "%s %s" %(self.first_name, self.last_name)


class Education(models.Model):
    degree_choices = (
        ("OND/HND", "OND/HND"),
        ("Bachelor's degree", "Bachelor's degree"),
        ("Master's degree", "Master's degree"),
        ("Doctorate degree", "Doctorate degree"),
        ("Phd", "Phd")
    )
    user = models.ForeignKey(to=Personal_Details, on_delete=CASCADE)
    degree = models.CharField(max_length=20, choices= degree_choices)
    major = models.CharField(max_length= 50)
    institution = models.CharField(max_length= 100, help_text= "Enter your institution here, e.g University of Uyo, Uyo")
    start_date = models.DateField(help_text="Enter the date you started school here", auto_now_add=False, auto_now= False)
    end_date = models.DateField(help_text="Enter the date you finished / the date you're expected to finish")

    def __str__(self) -> str:
        return  "%s  in %s" %(self.degree, self.major)


class Skill(models.Model):
    skill = models.CharField(max_length = 100)
    user = models.ManyToManyField(Personal_Details)

    def __str__(self) -> str:
        return  "%s" %(self.skill)




class Employment_History(models.Model):
    user = models.ForeignKey(to=Personal_Details, on_delete=CASCADE)
    job_title = models.CharField(max_length= 50)
    company_name = models.CharField(max_length= 50)
    company_location_city = models.CharField(max_length = 50)
    company_location_country = models.CharField(max_length = 50)
    job_start_date = models.DateField()
    job_end_date = models.DateField()
    responsibilities = models.TextField(max_length= 400)

    def __str__(self) -> str:
        return  "%s, %s" %(self.job_title, self.company_name)



class Project(models.Model):
    user = models.ForeignKey(to=Personal_Details, on_delete=CASCADE)
    project_name = models.CharField(max_length = 50)
    project_description = models.CharField(max_length = 200)
    link = models.URLField()

    def __str__(self) -> str:
        return  "%s" %(self.project_name)



class Certifications(models.Model):
    user = models.ForeignKey(to=Personal_Details, on_delete=RESTRICT)
    certificate_name = models.CharField(max_length = 50)
    institute = models.CharField(max_length= 100)
    year_obtained = models.DateField(auto_now_add=False, auto_now=False)

    def __str__(self) -> str:
        return  "%s" %(self.certificate_name)






