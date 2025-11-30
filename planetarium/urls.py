from django.urls import include, path
from rest_framework import routers

from planetarium.views import (
    AstronomyShowViewSet,
    ShowThemeViewSet,
    PlanetariumDomeViewSet,
    ShowSessionViewSet,
    ReservationViewSet,
    TicketViewSet,
)

app_name = "planetarium"

router = routers.DefaultRouter()

router.register("astronomy_show", AstronomyShowViewSet)
router.register("show_theme", ShowThemeViewSet)
router.register("planetarium_dome", PlanetariumDomeViewSet)
router.register("show_session", ShowSessionViewSet)
router.register("reservation", ReservationViewSet)
router.register("ticket", TicketViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
