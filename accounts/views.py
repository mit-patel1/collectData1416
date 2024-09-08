from rest_framework.views import APIView
from accounts.serializers import RegisterSerializer, LoginSerializer
from rest_framework import status
from rest_framework.response import Response


class RegistarAPI(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)

            if not serializer.is_valid():
                content = {
                    'data': serializer.errors,
                    'message': 'Somthing went wrong.'
                }
                return Response(content, status=status.HTTP_404_NOT_FOUND)
            
            serializer.save()

            content = {
                'data': {},
                'message': 'Your account is created.'
            }
            return Response(content, status=status.HTTP_201_CREATED)


        except Exception as e:
            content = {
                    'data': {},
                    'message': str(e)
                }
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    

class LoginAPI(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)

            if not serializer.is_valid():
                content = {
                    'data': serializer.errors,
                    'message': 'Somthing went wrong.'
                }
                return Response(content, status=status.HTTP_404_NOT_FOUND)
            
            refresh = serializer.get_jwt_token(serializer.data)

            content = {
                'data': {"Token":{'refresh': str(refresh),'access': str(refresh.access_token)}},
                'message': 'Log in successfull.'
            }
            return Response(content, status=status.HTTP_200_OK)


        except Exception as e:
            content = {
                    'data': {},
                    'message': str(e)
                }
            return Response(content, status=status.HTTP_404_NOT_FOUND)