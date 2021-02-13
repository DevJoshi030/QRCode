from rest_framework import serializers

from .models import QRCode


class ListTableSerializer(serializers.ModelSerializer):

    class Meta:

        model = QRCode
        fields = ('link', 'table_id', 'restaurant')
