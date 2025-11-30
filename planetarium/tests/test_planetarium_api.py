from datetime import datetime
from django.utils.timezone import make_aware

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from planetarium.models import (
    AstronomyShow,
    ShowSession,
    PlanetariumDome
)

ASTRONOMY_SHOW_URL = reverse("planetarium:astronomyshow-list")
SHOW_SESSION_URL = reverse("planetarium:showsession-list")


def sample_astronomy_show(**params):
    defaults = {
        "title": "Sample astronomy show",
        "description": "Sample description",
    }
    defaults.update(params)
    return AstronomyShow.objects.create(**defaults)


def sample_planetarium_dome(**params):
    defaults = {
        "name": "Main Dome",
        "rows": 15,
        "seats_in_row": 20,
    }
    defaults.update(params)
    return PlanetariumDome.objects.create(**defaults)


def sample_show_session(**params):
    planetarium_dome = sample_planetarium_dome()
    astronomy_show = sample_astronomy_show()

    defaults = {
        "show_time": make_aware(datetime(2023, 6, 2, 14, 0, 0)),
        "astronomy_show": astronomy_show,
        "planetarium_dome": planetarium_dome,
    }
    defaults.update(params)
    return ShowSession.objects.create(**defaults)


class UnauthenticatedPlanetariumApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(ASTRONOMY_SHOW_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedPlanetariumApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@test.com",
            "testpass",
        )
        self.client.force_authenticate(self.user)

    def test_list_astronomy_shows(self):
        sample_astronomy_show()
        sample_astronomy_show()

        res = self.client.get(ASTRONOMY_SHOW_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data["results"]), 2)

    def test_retrieve_astronomy_show_detail(self):
        show = sample_astronomy_show()

        url = reverse("planetarium:astronomyshow-detail", args=[show.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["title"], show.title)

    def test_list_show_sessions(self):
        sample_show_session()
        sample_show_session()

        res = self.client.get(SHOW_SESSION_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data["results"]), 2)

    def test_retrieve_show_session_detail(self):
        session = sample_show_session()

        url = reverse("planetarium:showsession-detail", args=[session.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["astronomy_show"], session.astronomy_show.id)

    def test_create_astronomy_show_forbidden(self):
        payload = {
            "title": "New Show",
            "description": "New Description",
        }
        res = self.client.post(ASTRONOMY_SHOW_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_show_session_forbidden(self):
        dome = sample_planetarium_dome()
        show = sample_astronomy_show()

        payload = {
            "show_time": "2023-06-03T14:00:00Z",
            "astronomy_show": show.id,
            "planetarium_dome": dome.id,
        }
        res = self.client.post(SHOW_SESSION_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class AdminPlanetariumApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "admin@admin.com", "testpass", is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_create_astronomy_show(self):
        payload = {
            "title": "New Astronomy Show",
            "description": "New Description",
        }
        res = self.client.post(ASTRONOMY_SHOW_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        show = AstronomyShow.objects.get(id=res.data["id"])
        self.assertEqual(show.title, payload["title"])
        self.assertEqual(show.description, payload["description"])

    def test_create_show_session(self):
        dome = sample_planetarium_dome()
        show = sample_astronomy_show()

        payload = {
            "show_time": "2023-06-03T14:00:00Z",
            "astronomy_show": show.id,
            "planetarium_dome": dome.id,
        }
        res = self.client.post(SHOW_SESSION_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        session = ShowSession.objects.get(id=res.data["id"])
        self.assertEqual(session.astronomy_show, show)
        self.assertEqual(session.planetarium_dome, dome)