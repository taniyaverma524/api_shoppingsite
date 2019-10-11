from apps.users.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password


class UserCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    confirm_password = serializers.CharField(min_length=5)
    password = serializers.CharField(min_length=5)
    first_name = serializers.CharField(max_length=60, required=True)
    last_name = serializers.CharField(max_length=60, required=True)
    mobile = serializers.CharField(max_length=20, required=True)
    is_email_verified = serializers.BooleanField(default=False)
    gender = serializers.CharField( max_length=20)
    class Meta():
        fields='__all__'
        extra_kwargs = {'confirm_password'}
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("password and confirm password does not match")
        if 'device_type' not in data:
            data['device_type'] = 'website'
        data.pop('confirm_password')
        return data

    def create(self, validated_data):
    #     user = User.objects.create_user(validated_data['username'], validated_data['email'],
    #                                     make_password(validated_data['password']))
    #     return user
    #     return User.objects.create(**validated_data)
        user=User.objects.create(
                                 email=validated_data['email'],username=validated_data['username'],password=make_password(validated_data['password'])
                                 ,first_name=validated_data['first_name'],last_name=validated_data['last_name'],
                                 mobile=validated_data['mobile'],gender=validated_data['gender'],is_email_verified=validated_data['is_email_verified']
                                 )
        return user






class UserProfileChangeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField( required=False,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(min_length=5 ,required=False)
    confirm_password = serializers.CharField(min_length=5,required=False)
    first_name = serializers.CharField(max_length=60, required=False)
    last_name = serializers.CharField(max_length=60, required=False)
    mobile = serializers.CharField(max_length=20, required=False)
    is_email_verified = serializers.BooleanField(default=False,required=False)
    gender = serializers.CharField(max_length=20,required=False)
    class Meta():
        model = User
        fields = "__all__"

    def update(self, instance, validated_data):


        instance.email = validated_data.get('email', instance.email)

        instance.username = validated_data.get('username', instance.username)
        # instance.password = validated_data.get('password', instance.password)
        # instance.confirm_password = validated_data.get('confirm_password', instance.confirm_password)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.mobile = validated_data.get('mobile', instance.mobile)

        instance.gender = validated_data.get('gender', instance.gender)
        instance.is_email_verified = validated_data.get('is_email_verified', instance.is_email_verified)
        instance.save()
        # print(instance.gender)
        return instance

