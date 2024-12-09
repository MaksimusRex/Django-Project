from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Crime, CriminalMainInfo
from theProject2.crimes.forms import CrimeForm


def add_crime(request, criminal_id):
    criminal = get_object_or_404(CriminalMainInfo, pk=criminal_id)

    if request.method == 'POST':
        form = CrimeForm(request.POST)
        if form.is_valid():
            crime = form.save(commit=False)
            crime.criminal = criminal
            crime.save()
            return JsonResponse({'success': True})

    else:
        form = CrimeForm()

    return render(request, 'criminals/crime_form.html', {'form': form, 'criminal': criminal})