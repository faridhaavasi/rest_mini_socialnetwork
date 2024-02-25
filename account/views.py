from rest_framework.views import APIView
from rest_framework.response import Response
from random import randint
from .serializers import SetDataRegisterSerializer, SetcodeRegister

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
                'code': code
            }
            print(code)
            return Response(serializer.data)
        return Response(serializer.errors)





