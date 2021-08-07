from django.db.models import fields
from django.forms import ModelForm, modelformset_factory
from resume.models import *

class PersonalDetailsForm(ModelForm):
    class Meta:
        model = Personal_Details
        fields = ['first_name', 'last_name', 'professional_title', 'city_of_residence', 'phone', 'email', 'summary', 'image']

# class EducationForm(ModelForm):
#     class Meta:
#         model = Education
#         exclude = ('user',)
        # fields = ['degree', 'major', 'institution', 'start_date', 'end_date']

# class SkillForm(ModelForm):
#     class Meta:
#         model = Skill
#         fields = ['skill',]

EducationFormSet = modelformset_factory(Education, fields = ['degree','major', 'institution', 'start_date', 'end_date'], extra= 2)

Employment_HistoryFormSet = modelformset_factory(Employment_History, fields= ['job_title', 'company_name', 'company_location_city', 'company_location_country', 'job_start_date', 'job_end_date', 'responsibilities'], extra=2)

SkillFormSet = modelformset_factory(Skill, fields = ['skill',], extra= 5)


ProjectFormSet = modelformset_factory(Project, fields = ['project_name', 'project_description', 'link'], extra= 3)

CertificationsFormSet = modelformset_factory(Certifications, fields= ['certificate_name', 'institute', 'year_obtained'], extra=2)


# class Employment_HistoryForm(ModelForm):
#     class Meta:
#         model = Employment_History
#         exclude = ('user',)



# class ProjectForm(ModelForm):
#     class Meta:
#         model = Project
#         exclude = ('user',)



# class CertificationsForm(ModelForm):
#     class Meta:
#         model = Certifications
#         exclude = ('user',)


# EducationFormSet = modelformset_factory(Education, fields = ['degree','major', 'institution', 'start_date', 'end_date'], extra= 2)
