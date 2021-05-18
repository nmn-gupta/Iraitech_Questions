# Create your views here.
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


def calculate(x, n):
    s = 0
    for i in range(1, n + 1):
        s += (1 / (x ** i))
    return s


class CalculateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

    authentication_classes = []

    def post(self, request, *args, **kwargs):
        x = request.POST.get("x", 1)
        y = request.POST.get("n", 1)
        result = calculate(x, n)
        data = {}
        data["result"] = result

        return JsonResponse(status=200, data=data)
