from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SetDataRegisterSerializer

class SetDataRegister(APIView):
    serializer_class = SetDataRegisterSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            vd = serializer.validated_data
            request.session['user_info_data'] = {
                'email' : vd['email'],
                'phone_number': vd['phone_number'],
                'fullname' : vd['fullname']
            }
            return Response(serializer.data)
        return Response(serializer.errors)
