from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import user_credentials
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
@api_view(['POST'])
def api_request(request):
    data = request.data
    signup_required_fields = ['name', 'email', 'phone_num', 'password', 'cpass']
    login_required_fields = ['user_email', 'user_password']

    if all(data.get(key) for key in signup_required_fields):
        check_email = user_credentials.objects.filter(email = data['email'])
        if data['password'] != data['cpass']:
            return Response({'msg': "Passwords don't match"}, status=400)
        elif check_email.exists():
            return Response({'msg': 'Email already exist'})
        else:
            user_credentials.objects.create(
            name = data['name'],
            email = data['email'],
            phone_num = data['phone_num'],
            password = make_password(data['password'])
            )
            return Response({'msg': 'Signup Successful! You can now login to your account'})
        
    elif all(data.get(value) for value in login_required_fields):
         user = user_credentials.objects.filter(email = data['user_email'])
         user_data = user.first()
         if user.exists() and check_password(data['user_password'],user_data.password):
            session_data = {
            'name' : user_data.name,
            'email' : user_data.email,
            'phone_num' : user_data.phone_num
            }
            return Response(session_data)
         else:
            return Response({'msg': 'Invalid email or password'}, status=400)
        
    else:
        return Response({'msg': 'Please fill out all fields!'}, status=400)