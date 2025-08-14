from django.contrib import admin # type: ignore
from.models import departments,contacts
# Register your models here.
admin.site.register(departments)
admin.site.register(contacts)