from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from blogs.models import Entry, Blog, UserComment

User = get_user_model() 


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['blog', 'headline', 'body_text', 'bg_image', 'authors']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComment
        fields = ['user', 'comment', 'entry']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, data):
        user = User(**data)
        errors = dict() 
        try:
            validate_password(data['password'], user=user)
        except Exception as e:
            errors['password'] = list(e.messages)
        if errors:
             raise serializers.ValidationError(errors)

        return super(UserSerializer, self).validate(data)
