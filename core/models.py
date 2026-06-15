from django.db import models

class Teacher(models.Model):
    meno = models.CharField(max_length=100)
    priezvisko = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.meno} {self.priezvisko}"

class Student(models.Model):
    meno = models.CharField(max_length=100)
    priezvisko = models.CharField(max_length=100)
    trieda = models.CharField(max_length=10)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.meno} {self.priezvisko}"

class Team(models.Model):
    nazov_timu = models.CharField(max_length=100)
    popis = models.TextField(blank=True)
    veduci_timu = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    datum_vytvorenia = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nazov_timu

class Competition(models.Model):
    nazov_sutaze = models.CharField(max_length=200)
    miesto = models.CharField(max_length=200)
    datum = models.DateField()
    typ = models.CharField(max_length=100)

    def __str__(self):
        return self.nazov_sutaze

class TeamMembership(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    rola_v_time = models.CharField(max_length=100, blank=True)

    class Meta:
        unique_together = ('student', 'team')

    def __str__(self):
        return f"{self.student} → {self.team}"

class CompetitionRegistration(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    stav_registracie = models.CharField(max_length=50, default='Čaká na schválenie')

    class Meta:
        unique_together = ('team', 'competition')

    def __str__(self):
        return f"{self.team} → {self.competition}"