from rest_framework import serializers

from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField()

    class Meta:
        model = Listing
        fields = (
            "id",
            "user_email",
            "event",
            "description",
            "price",
            "status",
            "date",
            "slug",
            "get_absolute_url"
        )