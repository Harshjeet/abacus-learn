from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserProfileV2(APIView):
    """
    v2 accepts name + age
    returns richer response
    """
    def post(self, request):
        name = request.data.get("name")
        age = request.data.get("age")

        return Response({
            "version": "v2",
            "user": {
                "name": name,
                "age": age
            },
            "message": f"Hello {name}, you are {age} years old"
        }, status=status.HTTP_201_CREATED)
