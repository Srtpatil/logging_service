import log_ingestor.models as models
from django.contrib import admin

admin.site.register(models.Log)
admin.site.register(models.LogLevel)
admin.site.register(models.LogResource)
