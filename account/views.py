from rest_framework.views import APIView
from rest_framework.response import Response
from random import randint
from .serializers import SetDataRegisterSerializer, SetcodeRegisterSerializer
from . models import User
from rest_framework_simplejwt.views import TokenObtainPairView

class SetDataRegister(APIView):
    serializer_class = SetDataRegisterSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            code = randint(0, 99999)
            vd = serializer.validated_data
            request.session['user_info_data'] = {
                'email' : vd['email'],
                'phone_number': vd['phone_number'],
                'fullname' : vd['fullname'],
                'password' : vd['password'],
                'code': code
            }
            # TODO sms verifycation code
            print(code)
            return Response(serializer.data)
        return Response(serializer.errors)

class SetcodeRegister(APIView):
    serializer_class = SetcodeRegisterSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            vd = serializer.validated_data
            user_info_data = request.session['user_info_data']
            print(user_info_data)
            if vd['code'] == str(user_info_data['code']):
                User.objects.create_user(fullname=user_info_data['fullname'],
                    phone_number=user_info_data['phone_number'],
                    email =user_info_data['email'],
                    password=user_info_data['password'])

                del (request.session['user_info_data'])
                return Response(request.data)
            return Response(serializer.errors)



