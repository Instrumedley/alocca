from django.contrib import admin
from .models import Portfolio
from .models import Instrument
from .models import Trade

admin.site.register(Portfolio)
admin.site.register(Instrument)
admin.site.register(Trade)
