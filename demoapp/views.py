from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import User,Student
from .serializer import UserSerializer
import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

@csrf_exempt
def hello_post_api(request):

    if request.method == 'POST':
        
        return HttpResponse("This is a POST API response. CSRF check skipped.")
    else:
        return HttpResponse("Send a POST request to this URL to see the API response.")

@csrf_exempt
def echo(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)
    data = json.loads(request.body or '{}')
    return JsonResponse({'received': data}, status=201)

# get method
def get_echo(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'GET only'}, status=405)
    data = json.loads(request.body or '{}')
    return JsonResponse({'received': data}, status=201)

@csrf_exempt
def update_echo(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body or '{}')
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        return JsonResponse({'action': 'updated', 'received': data}, status=200)
    return JsonResponse({'error': 'PUT only'}, status=405)

@csrf_exempt
def delete_echo(request):
    if request.method == 'DELETE':
        return JsonResponse({'action': 'deleted'}, status=204)
    return JsonResponse({'error': 'DELETE only'}, status=405)


@method_decorator(csrf_exempt, name='dispatch')
class SimplePostView(View):
    def post(self, request):
        data = json.loads(request.body or '{}')
        # Return the received data
        return JsonResponse({'received': data}) 

    def get(self, request):
        #data = json.loads(request.body or '{}')
        # Return the received data
        return JsonResponse({'received': "get"})

    def put(self, request):
        data = json.loads(request.body or '{}')
        return JsonResponse({'received': data})

    def delete(self, request):
        return JsonResponse({'action': 'deleted'}, status=204)

# using DRF 
class DRFView(APIView):
    def post(self, request):
        data = request.data
        return Response(
            {'received': data, 'framework': 'DRF'},
            status=status.HTTP_201_CREATED
        ) 
        
    def get(self, request):
            return Response(
            {'received': "get", 'framework': 'DRF'}
        )


# using serializer
class UserSerializerView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer   
    


def simple_page(request):
    # Data without model
    products = [
        {'name': 'Book', 'price': 299, 'description': 'A good book'},
        {'name': 'Pen', 'price': 19, 'description': 'Blue ink pen'},
    ]
    return render(request, 'product_no_db.html', {'products': products})

@csrf_exempt
def student_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        student = Student.objects.create(
            name=data['name'],
            age=data['age'],
            roll=data['roll']
        )
        return JsonResponse({'id': student.id, 'name': student.name, 'age': student.age, 'roll': student.roll}, status=201)
    
    elif request.method == 'GET':
        students = Student.objects.all()
        students_data = [{'id': s.id, 'name': s.name, 'age': s.age, 'roll': s.roll} for s in students]
        return JsonResponse({'students': students_data})


# checking admin data
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_page(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)   # creates session
            return redirect("/demoapp/home/")
    return render(request, "admin_user.html")

def home(request):
    if not request.user.is_authenticated:
        return HttpResponse("Not logged in")
    return HttpResponse(f"Hello {request.user.username}")



class ProfileAPI(APIView):
    def get(self, request):
        return Response({"user": request.user.username})