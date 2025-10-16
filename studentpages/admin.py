from django.contrib import admin

from studentpages.models import Student, Teacher, User, Taskanswer, Task, Daylist, Lesson, Portfolio, Studgroup, Department

# Register your models here.
studentpages_models = [
    admin.site.register(Student),
    admin.site.register(Teacher),
    admin.site.register(User),
    admin.site.register(Taskanswer),
    admin.site.register(Task),
    admin.site.register(Daylist),
    admin.site.register(Lesson),
    admin.site.register(Portfolio),
    admin.site.register(Studgroup),
    admin.site.register(Department),
]