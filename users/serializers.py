from rest_framework import serializers

from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password',)


class UserSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'avatar', 'phone', 'city', 'payment')


class UserPublicSerializer(serializers.ModelSerializer):
    model = User
    fields = ('first_name', 'last_name', 'avatar', 'city')
