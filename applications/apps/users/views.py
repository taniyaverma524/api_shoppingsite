from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.serializers import UserCreateSerializer, UserProfileChangeSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.contrib.auth import login as auth_login
from rest_framework.permissions import IsAuthenticated
from rest_framework import  permissions
from django.contrib.auth import logout




class RegistrationApiView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        user_object=User.objects.all()
        user_serializer = UserProfileChangeSerializer(user_object,many=True)
        return Response(user_serializer.data,)

    def post(self, request, format=None):
        user_serializer = UserCreateSerializer(data=request.data)
        if user_serializer.is_valid():
            user=user_serializer.save()
            if user:
                return Response({
                'status': status.HTTP_201_CREATED,
                'message': 'you are successfully registered',
                'data': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'name': user.first_name

                }},
                status=status.HTTP_201_CREATED
                )
        else:
            print(user_serializer.errors)
        return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class UserEditApiView(APIView):
    def get_object(self,pk):
        try:

            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Http404
    def get(self, request, pk, format=None ):
        user_object= self.get_object(pk)
        user_serializer= UserProfileChangeSerializer(user_object)
        return Response(user_serializer.data)

    def put(self  , request, pk, format=None):
        user_object= self.get_object(pk)
        print(user_object,request.data)
        user_serializer=UserProfileChangeSerializer(user_object, data=request.data)
        if user_serializer.is_valid():
            user= user_serializer.save()
            if user:
                return Response({
                    'status':status.HTTP_201_CREATED,
                    'message' : 'you are successfully changed your profile',
                    'data' : {
                        'id' : user.id,
                        'username': user.username,
                        'email': user.email,
                        'name': user.first_name

                    } },
                    status=status.HTTP_201_CREATED
                                  )

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request, pk,format=None):
        user_object = self.get_object(pk)
        print(user_object)

        user_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class LoginApiView(APIView):

    def post(self,request):
        username=request.data.get('username',None)
        password=request.data.get('password',None)
        print(username,password)
        if username and password :
            user= authenticate(username=username,password=password)
            print(user,'user')
            if user :
                auth_login(request, user)
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': 'You have been successfully logged in',
                        'data': {
                            'username': user.username,
                            'email': user.email,
                            'name': user.first_name
                        },
                    },
                    status=status.HTTP_200_OK)
            else:
                return Response(
                    {
                        'message': 'Invalid credentials.',
                        'data': {}
                    },
                    status=status.HTTP_401_UNAUTHORIZED)


class UserLogout(APIView):
    """
    Get:`
    API for user logout.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        print(request.user,'first')
        user = request.user
        logout(request)
        # token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        # print('************LOGOUT************')
        # print(token)
        # login_log = LoginLog.objects.get(user=user, login_token=token)
        # login_log.logout_time = timezone.now()
        # login_log.is_logged_out = True
        # login_log.save()
        print(request.user)
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': 'Logged out successfully'
            }, status=status.HTTP_200_OK)