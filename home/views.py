from rest_framework.views import APIView
from home.models import UserData
from rest_framework import status
from rest_framework.response import Response
from home.serializers import UserDataSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q
from django.core.paginator import Paginator



class PublicUserDataAPI(APIView):

    def get(self, request):
        try:
            query = Q()
            if request.GET.get('search'):
                query.add(Q(name__icontains=request.GET.get('search')) | Q(email__icontains=request.GET.get('search')), query.connector)

            objs = UserData.objects.filter(query)
            # objs = UserData.objects.filter(query).order_by("?") # rendom data get

            page = request.GET.get('page', 1)
            paginator = Paginator(objs, 5)
            serializer = UserDataSerializer(paginator.page(page), many=True)
            
            content = {
                'data': serializer.data,
                'message': 'Success.'
            }
            return Response(content, status=status.HTTP_200_OK)

        except Exception as e:
            content = {
                    'data': {},
                    'message': str(e)
                }
            return Response(content, status=status.HTTP_404_NOT_FOUND)


class UserDataAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            query = Q()
            if request.user:
                query.add(Q(user=request.user), query.connector)
            
            if request.GET.get('search'):
                query.add(Q(name__icontains=request.GET.get('search')), query.connector)

            objs = UserData.objects.filter(query)
            serializer = UserDataSerializer(objs, many=True)
            
            content = {
                'data': serializer.data,
                'message': 'Success.'
            }
            return Response(content, status=status.HTTP_200_OK)

        except Exception as e:
            content = {
                    'data': {},
                    'message': str(e)
                }
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            data = request.data
            data['user'] = request.user.id
            serializer = UserDataSerializer(data=data)

            if not serializer.is_valid():
                content = {
                    'data': serializer.errors,
                    'message': 'Somthing went wrong.'
                }
                return Response(content, status=status.HTTP_404_NOT_FOUND)

            serializer.save()
            content = {
                'data': serializer.data,
                'message': 'Record save successfull.'
            }
            return Response(content, status=status.HTTP_200_OK)

        except Exception as e:
            content = {
                    'data': {},
                    'message': str(e)
                }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
    

    def put(self, request):
        try:
            data = request.data
            user_data = UserData.objects.get(uid= data['uid'])

            if not user_data:
                content = {
                    'data': {},
                    'message': 'Record not found.'
                }
                return Response(content, status=status.HTTP_404_NOT_FOUND)
            
            print('request.user', request.user != user_data.user , request.user.is_superuser)
            
            if (request.user != user_data.user and not request.user.is_superuser):
                content = {
                    'data': {},
                    'message': 'You don`t have permission to do this.'
                }
                return Response(content, status=status.HTTP_404_NOT_FOUND)

            serializer = UserDataSerializer(user_data, data=data, partial=True)

            if not serializer.is_valid():
                content = {
                    'data': serializer.errors,
                    'message': 'Somthing went wrong.'
                }
                return Response(content, status=status.HTTP_404_NOT_FOUND)

            serializer.save()
            content = {
                'data': serializer.data,
                'message': 'Record save successfull.'
            }
            return Response(content, status=status.HTTP_200_OK)

        except Exception as e:
            content = {
                    'data': {},
                    'message': str(e)
                }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request):
        try:
            data = request.data
            user_data = UserData.objects.get(uid= data['uid'])

            if not user_data:
                content = {
                    'data': {},
                    'message': 'Record not found.'
                }
                return Response(content, status=status.HTTP_404_NOT_FOUND)
            
            if request.user != user_data.user or not request.user.is_superuser:
                content = {
                    'data': {},
                    'message': 'You don`t have permission to do this.'
                }
                return Response(content, status=status.HTTP_404_NOT_FOUND)

            user_data.delete()
            content = {
                'data': {},
                'message': 'Record deleted successfull.'
            }
            return Response(content, status=status.HTTP_200_OK)

        except Exception as e:
            content = {
                    'data': {},
                    'message': str(e)
                }
            return Response(content, status=status.HTTP_404_NOT_FOUND)