from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from planetarium.models import (
    AstronomyShow,
    ShowTheme,
    ShowSession,
    PlanetariumDome,
    Reservation,
    Ticket,
)


class AstronomyShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = "__all__"


class AstronomyShowListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = ("id", "title", "image")


class AstronomyShowImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = ("id", "image")


class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields = "__all__"


class ShowSessionSerializer(serializers.ModelSerializer):
    astronomy_show_title = serializers.CharField(source="astronomy_show.title", read_only=True)
    dome_name = serializers.CharField(source="planetarium_dome.name", read_only=True)
    dome_capacity = serializers.IntegerField(source="planetarium_dome.capacity", read_only=True)
    tickets_sold = serializers.IntegerField(read_only=True)
    tickets_available = serializers.IntegerField(read_only=True)

    class Meta:
        model = ShowSession
        fields = [
            "id", "show_time", "astronomy_show", "planetarium_dome",
            "astronomy_show_title", "dome_name", "dome_capacity",
            "tickets_sold", "tickets_available"
        ]


class ShowSessionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowSession
        fields = "__all__"


class PlanetariumDomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetariumDome
        fields = "__all__"


class PlanetariumDomeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetariumDome
        fields = ("id", "image")


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Ticket.objects.all(),
                fields=["show_session", "row", "seat"]
            )
        ]
        model = Ticket
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=False, allow_empty=False)

    class Meta:
        model = Reservation
        fields = ["id", "tickets", "created_at", "user"]

    def create(self, validated_data):
        with transaction.atomic():
            tickets_data = validated_data.pop("tickets")
            reservation = Reservation.objects.create(**validated_data)

            for ticket_data in tickets_data:
                Ticket.objects.create(reservation=reservation, **ticket_data)

            return reservation


class ReservationListSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=False, allow_empty=False)
    class Meta:
        model = Reservation
        fields = ["id", "tickets", "created_at", "user"]