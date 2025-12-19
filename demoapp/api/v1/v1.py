from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserProfileV1(APIView):
    def post(self, request):
        name = request.data.get("name")

        return Response({
            "version": "v1",
            "name": name,
            "message": f"Hello {name}"
        }, status=status.HTTP_201_CREATED)
