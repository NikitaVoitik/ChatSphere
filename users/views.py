from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from rest_framework.views import APIView


# Create your views here.
class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'User registered successfully'}, status=201)