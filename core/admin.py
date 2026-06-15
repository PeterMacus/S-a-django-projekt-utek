from django.contrib import admin
from .models import Student, Team, Competition, Teacher, TeamMembership, CompetitionRegistration

admin.site.register(Student)
admin.site.register(Team)
admin.site.register(Competition)
admin.site.register(Teacher)
admin.site.register(TeamMembership)
admin.site.register(CompetitionRegistration)
