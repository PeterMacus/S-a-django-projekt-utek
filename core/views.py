from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Student, Team, Competition, TeamMembership, CompetitionRegistration
from .forms import StudentForm, TeamForm, CompetitionForm, CompetitionRegistrationForm

def home(request):
    return render(request, 'core/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nesprávne meno alebo heslo.')
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

# ── ŠTUDENTI ──────────────────────────────────────────────
def student_list(request):
    students = Student.objects.all()
    trieda = request.GET.get('trieda')
    if trieda:
        students = students.filter(trieda__icontains=trieda)
    return render(request, 'core/student_list.html', {'object_list': students})

@login_required
def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'core/form.html', {'form': form, 'title': 'Pridať študenta'})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'core/form.html', {'form': form, 'title': 'Upraviť študenta'})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'core/confirm_delete.html', {'object': student})

# ── TÍMY ──────────────────────────────────────────────────
def team_list(request):
    teams = Team.objects.all()
    nazov = request.GET.get('nazov')
    if nazov:
        teams = teams.filter(nazov_timu__icontains=nazov)
    return render(request, 'core/team_list.html', {'teams': teams})

def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    all_students = Student.objects.all()
    return render(request, 'core/team_detail.html', {'team': team, 'all_students': all_students})

@login_required
def team_create(request):
    form = TeamForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('team_list')
    return render(request, 'core/form.html', {'form': form, 'title': 'Pridať tím'})

@login_required
def add_student_to_team(request, team_pk, student_pk):
    team = get_object_or_404(Team, pk=team_pk)
    student = get_object_or_404(Student, pk=student_pk)
    TeamMembership.objects.get_or_create(team=team, student=student)
    return redirect('team_detail', pk=team_pk)

@login_required
def remove_student_from_team(request, team_pk, student_pk):
    TeamMembership.objects.filter(team_id=team_pk, student_id=student_pk).delete()
    return redirect('team_detail', pk=team_pk)

# ── SÚŤAŽE ────────────────────────────────────────────────
def competition_list(request):
    competitions = Competition.objects.all()
    typ = request.GET.get('typ')
    datum = request.GET.get('datum')
    if typ:
        competitions = competitions.filter(typ__icontains=typ)
    if datum:
        competitions = competitions.filter(datum=datum)
    return render(request, 'core/competition_list.html', {'competitions': competitions})

@login_required
def competition_create(request):
    form = CompetitionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('competition_list')
    return render(request, 'core/form.html', {'form': form, 'title': 'Pridať súťaž'})

# ── REGISTRÁCIA TÍMU DO SÚŤAŽE ────────────────────────────
@login_required
def zmena_stavu_registracie(request, pk, stav):
    ALLOWED_STAVY = ['Schválené', 'Neschválené', 'Čaká na schválenie']
    reg = get_object_or_404(CompetitionRegistration, pk=pk)
    if stav in ALLOWED_STAVY:
        reg.stav_registracie = stav
        reg.save()
    return redirect('competition_list')

@login_required
def register_team_to_competition(request, team_pk):
    team = get_object_or_404(Team, pk=team_pk)
    form = CompetitionRegistrationForm(request.POST or None)
    if form.is_valid():
        reg = form.save(commit=False)
        reg.team = team
        reg.save()
        return redirect('team_detail', pk=team_pk)
    return render(request, 'core/form.html', {'form': form, 'title': f'Registrovať tím {team.nazov_timu} do súťaže'})