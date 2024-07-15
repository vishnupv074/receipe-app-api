"""
Serializers for user API view
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
)

from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for users object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for user auth token"""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(
                request=self.context.get('request'),
                username=email,
                password=password
            )
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError(_('User is inactive'))
            else:
                raise serializers.ValidationError(_('Unable to log in with provided credentials.'), code='authorization')
        else:
            raise serializers.ValidationError(_('Must provide email and password.'))

        return data
