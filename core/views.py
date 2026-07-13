from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ChangePasswordSerializer

class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_serializer(self, *args, **kwargs):
        return ChangePasswordSerializer(*args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update_password(request)
        
    def post(self, request, *args, **kwargs):
        return self.update_password(request)

    def update_password(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            old_password = serializer.data.get("old_password")
            new_password = serializer.data.get("new_password")
            
            if not user.check_password(old_password):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            
            user.set_password(new_password)
            user.save()
            return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
