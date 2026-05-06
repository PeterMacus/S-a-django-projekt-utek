from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Team, Competition, TeamMembership

def home(request):
    return render(request, 'core/home.html')

def student_list(request):
    students = Student.objects.all()
    trieda = request.GET.get('trieda')
    if trieda:
        students = students.filter(trieda__icontains=trieda)
    return render(request, 'core/student_list.html', {'object_list': students})

def student_create(request):
    from .forms import StudentForm
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'core/form.html', {'form': form, 'title': 'Pridať študenta'})

def student_update(request, pk):
    from .forms import StudentForm
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'core/form.html', {'form': form, 'title': 'Upraviť študenta'})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'core/confirm_delete.html', {'object': student})

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'core/team_list.html', {'teams': teams})

def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    return render(request, 'core/team_detail.html', {'team': team})

def team_create(request):
    from .forms import TeamForm
    form = TeamForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('team_list')
    return render(request, 'core/form.html', {'form': form, 'title': 'Pridať tím'})

def competition_list(request):
    competitions = Competition.objects.all()
    return render(request, 'core/competition_list.html', {'competitions': competitions})

def competition_create(request):
    from .forms import CompetitionForm
    form = CompetitionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('competition_list')
    return render(request, 'core/form.html', {'form': form, 'title': 'Pridať súťaž'})

def add_student_to_team(request, team_pk, student_pk):
    team = get_object_or_404(Team, pk=team_pk)
    student = get_object_or_404(Student, pk=student_pk)
    TeamMembership.objects.get_or_create(team=team, student=student)
    return redirect('team_detail', pk=team_pk)

def remove_student_from_team(request, team_pk, student_pk):
    TeamMembership.objects.filter(team_id=team_pk, student_id=student_pk).delete()
    return redirect('team_detail', pk=team_pk)