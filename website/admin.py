from django.contrib import admin
from website.models import LowonganKerja, DataBarang, Area, Cabang
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header = 'Baraka Administration'
admin.site.index_title = 'Baraka Web Admin'
admin.site.site_title = 'Baraka Site Admin'

admin.site.register(Area)
admin.site.register(Cabang)
admin.site.register(DataBarang)
admin.site.unregister(Group)
admin.site.register(LowonganKerja)