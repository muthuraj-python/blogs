from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.core import serializers

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from blogs.models import Entry, Blog, UserComment
from .serializers import EntrySerializer, BlogSerializer, \
								UserSerializer, UserCommentSerializer

User = get_user_model()


class EntryView(generics.ListCreateAPIView):
	queryset = Entry.objects.filter(published=True)
	serializer_class = EntrySerializer


class BlogsView(generics.ListCreateAPIView):

	queryset = Blog.objects.all()
	serializer_class  = BlogSerializer

class UserCommentView(generics.ListCreateAPIView):
	queryset = UserComment.objects.all()
	serializer_class = UserCommentSerializer

class UsersView(generics.CreateAPIView):

	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (AllowAny,)

	def create(self, request, *arg, **karg):
		# import ipdb;ipdb.set_trace()
		user_serializer = self.serializer_class(data=request.data)
		if user_serializer.is_valid():
			user, created = User.objects.get_or_create(username = request.data['username'])
			user.set_password(request.data['password'])
			user.save()
			token = Token.objects.create(user=user)
			return Response(data={"token":token.key, "user_id": user.id})
		else:
			return Response(data=user_serializer.errors)
