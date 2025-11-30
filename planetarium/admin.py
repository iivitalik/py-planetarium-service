from django.contrib import admin

from planetarium.models import (
    AstronomyShow,
    ShowTheme,
    Reservation,
    PlanetariumDome,
    Ticket,
    ShowSession
)


admin.site.register(AstronomyShow)
admin.site.register(ShowTheme)
admin.site.register(Reservation)
admin.site.register(PlanetariumDome)
admin.site.register(Ticket)
admin.site.register(ShowSession)
