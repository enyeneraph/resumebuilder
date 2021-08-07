from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import *

# Create your views here.

def home(request):
    if request.method == 'POST':
        pdform = PersonalDetailsForm(request.POST, request.FILES)
        edform = EducationFormSet(request.POST)
        sform = SkillFormSet(request.POST)
        empform = Employment_HistoryFormSet(request.POST)
        pform = ProjectFormSet(request.POST)
        cform = CertificationsFormSet(request.POST)
        form = [pdform, edform, sform, empform, pform, cform]
        form_valid = [i.is_valid() for i in form]
        if all(form_valid):
            a = pdform.save(commit=False)
            a.session_id = request.session.session_key
            a.save()

            instances = edform.save(commit=False)
            for i in instances:
                i.user_id = a.user_id
                i.save()

            s_instances = sform.save(commit=False)
            for i in s_instances:
                i.save()
                i.user.add(a)
                
            for i in form[2:]:
                instances = i.save(commit=False)
                for instance in instances:
                    instance.user_id = a.user_id
                    instance.save()
                
            
            return HttpResponseRedirect('/resume/results/')
        else:
            return HttpResponse([i.errors for i in form])
            # return render(request, 'result.html', context={'name':name, 'email':email})
    else:
        pdform = PersonalDetailsForm()
        #I was battling with prepopulated and forms I did not ask for, turns out, default behaviour is to populate form with all instances existing in the database.
        edform = EducationFormSet(queryset=Education.objects.none())
        sform = SkillFormSet(queryset=Skill.objects.none())
        empform = Employment_HistoryFormSet(queryset=Employment_History.objects.none())
        pform = ProjectFormSet(queryset=Project.objects.none())
        cform = CertificationsFormSet(queryset=Certifications.objects.none())
        return render(request, 'form.html', {'pdform': pdform, 'edform': edform, 'sform': sform, 'empform': empform, 'pform': pform, 'cform': cform})

def results(request):
    pk = request.user.pk
    first_name = Personal_Details.objects.get(pk = pk)
    # request.user.pk
    context = {'first_name':first_name}
    return render(request, 'cv_template.html')
    