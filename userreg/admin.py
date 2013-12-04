from django.contrib import admin
from userreg.models import RegisteredUser

from django.http import HttpResponse
import csv

# Register your models here.

class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'ip', 'date')
    list_filter = ['date']
    search_fields = ['email']

    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        if not request.user.is_staff:
            raise PermissionDenied
        opts = self.model._meta
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')
        writer = csv.writer(response)
        field_names = [field.name for field in opts.fields]
        # write first row with header information
        writer.writerow(field_names)
        # write data rows
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.description = 'Export selected objects as a csv file'

admin.site.register(RegisteredUser, RegisteredUserAdmin)
