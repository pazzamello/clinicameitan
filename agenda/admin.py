# -*- encoding: utf-8 -*-

from agenda.models import ItemAgenda, Person, Phone, Patient, HealthProfessional, Document
from django.contrib import admin

class ItemAgendaAdmin(admin.ModelAdmin):
	fields = ('data', 'hora', 'titulo', 'descricao', 'participantes')
	list_display = ('data', 'hora', 'titulo')
	list_display_links = ('data', 'hora', 'titulo')

	def queryset(self, request):
		qs = super(ItemAgendaAdmin, self).queryset(request)
		return qs.filter(usuario=request.user)
	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		obj.save()
class PersonAdmin(admin.ModelAdmin):
    pass
class PhoneAdmin(admin.ModelAdmin):
    pass
class PatientAdmin(admin.ModelAdmin):
    pass
class HealthProfessionalAdmin(admin.ModelAdmin):
    pass
class DocumentAdmin(admin.ModelAdmin):
    pass
admin.site.register(ItemAgenda, ItemAgendaAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(HealthProfessional, HealthProfessionalAdmin)
admin.site.register(Document, DocumentAdmin)

