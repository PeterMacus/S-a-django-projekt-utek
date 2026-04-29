from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def student_list(request):
    # Fiktívne dáta pre testovanie frontendu
    students = [
        {'meno': 'Samuel', 'priezvisko': 'Škuta', 'trieda': '4.A', 'email': 'samuel@skola.sk'},
        {'meno': 'Peter', 'priezvisko': 'Macúš', 'trieda': '4.B', 'email': 'peter@skola.sk'},
    ]
    return render(request, 'core/student_list.html', {'students': students})

def team_list(request):
    teams = [
        {'nazov': 'Koderi z Kysúc', 'veduci': 'Samuel Škuta', 'pocet_clenov': 2},
        {'nazov': 'Django Majstri', 'veduci': 'Peter Macúš', 'pocet_clenov': 5},
    ]
    return render(request, 'core/team_list.html', {'teams': teams})

def competition_list(request):
    competitions = [
        {'nazov': 'Zenit v programovaní', 'miesto': 'Online', 'datum': '15.05.2026', 'typ': 'Odborná'},
        {'nazov': 'Futbalový turnaj', 'miesto': 'Telocvičňa', 'datum': '20.06.2026', 'typ': 'Športová'},
    ]
    return render(request, 'core/competition_list.html', {'competitions': competitions})