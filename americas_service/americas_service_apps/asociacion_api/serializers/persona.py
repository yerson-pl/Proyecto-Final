from rest_framework import serializers
from americas_service_apps.auths.models.person import Person
from americas_service_apps.auths.choices.enums import GENDER_CHOICES


class PersonSerializer(serializers.ModelSerializer):
	# gender = serializers.s

    class Meta:
        model = Person
        fields = '__all__'
