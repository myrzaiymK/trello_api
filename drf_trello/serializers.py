from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from trello_app.models import *
from users.models import CustomUser
from rest_framework import serializers
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator



class BoardSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.CharField()
    title = serializers.CharField(required=False, allow_blank=True, max_length=150)
    image = serializers.ImageField()
    archive = serializers.BooleanField(default=False)

    extra_kwargs = {
        "image": {"required": False}
    }

    def create(self, validated_data):
        return Board.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.archive = validated_data.get('archive', instance.archive)
        instance.save()
        return instance



class ColumnSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    board_id = serializers.IntegerField()

    def create(self, validated_data):
        return Column.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.board_id = validated_data.get('board', instance.board_id)
        instance.save()
        return instance



class CommentSerializer(serializers.Serializer):
    user = serializers.CharField()
    author = serializers.CharField()
    body = serializers.CharField()
    created_on = serializers.DateField()
    card_id = serializers.IntegerField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.author = validated_data.get('author', instance.author)
        instance.body = validated_data.get('body', instance.body)
        instance.created_on = validated_data.get('created_on', instance.created_on)
        instance.card_id = validated_data.get('card_id', instance.card_id)
        instance.save()
        return instance



class MemberSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    board_id = serializers.IntegerField()
    member = serializers.CharField()

    def create(self, validated_data):
        return Member.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.board_id = validated_data.get('board_id', instance.board_id)
        instance.member = validated_data.get('member', instance.member)
        instance.save()
        return instance



class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())])

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['username'], validated_data['email'], validated_data[
            'password'])

        return user


class FavouriteSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    board_id = serializers.IntegerField()


    def create(self, validated_data):
        return Favourites.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.board_id = validated_data.get('board_id', instance.board_id)
        instance.save()
        return instance



class RecentViewsSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    board_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    views_time = serializers.DateTimeField()


    def create(self, validated_data):
        return RecentViews.objects.create(**validated_data)


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    #
    # def validate(self, request):
    #     email = request['data'].get['email']
    #     if CustomUser.objects.filter(email=email).exists():
    #         user = CustomUser.objects.get(email=email)
    #         token = PasswordResetTokenGenerator().make_token(user)
    #         current_site = get_current_site(request).domain
    #         relative_link = reverse('reset_password_confirm')
    #         absurl = 'http://' + current_site + relative_link + "?token=" + str(token)
    #         email_body = 'HI \n Use link below to reset your password \n' + absurl
    #         data = {'email_body': email_body, 'to_email': user.email,
    #                 'email_subject': 'Reset your password '}
    #         send_mail(data)
