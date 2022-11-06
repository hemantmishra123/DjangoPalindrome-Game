from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .Calander_Api import test_calendar
from.cal_Api import build_services
from rest_framework.authentication import TokenAuthentication
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .serializers import StudentSerializer
from .serializers import RecordSerializer
from.serializers  import UserSerializer
from .models import Student,Record 
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import random
String=''
users=User.objects.all()
print(StudentSerializer,"student serilize data")
print(RecordSerializer)
#for user in users:
 #   token=Token.objects.get_or_create(user=user)
  #  print(token)

#This is the Functions for the UserCount in the Tables nd showing the active users.
class UserCountView(APIView):
    #renderer_classes = [JSONRenderer]
    def get(self, request, format=None):
        user_count = User.objects.all()
        for user in user_count:
            if user.is_active:
                print(user)
                userSerializer=UserSerializer(user_count,many=True) 
        return Response(userSerializer.data)

#Api for Getting the Students Data from the Models and Regsiter the Student into the Database
class StudentApi(APIView):
    student_model = StudentSerializer
    def get_data(self):
        query=Student.objects.all()
        return query 
    
    def get(self,request,*args,**kwargs):
        students=self.get_data()
        serializeData= StudentSerializer(students,many=True)
        return Response(serializeData.data)
    
    #This  is the Post Request data enter 
    def post(self,request,*args,**kwargs):
        stu_data =  request.data 
        new_student = Student.objects.create(Name=stu_data['Name'],Roll_No=stu_data['Roll_No'],Father=stu_data['Father'],Mother=stu_data['Mother'],Math=stu_data['Math'],English=stu_data['English'],Physics=stu_data['Physics'])

        new_student.save()
        serializers=StudentSerializer(new_student)
        return Response(serializers.data)



def home(request):
    return render(request, 'App_auth/demo.html')

def demo(request):
    test=build_services()
    print(test)
    return HttpResponse('ok')

def login_or_signup(request):
    #return HttpResponse('ok')
    return render(request, 'App_auth/login_or_signup.html')


#This is Function for Erp
class ErpView(APIView):
    Record_model = RecordSerializer

    def get_data(self):
        query=Record.objects.all()
        return query 
    
    def get(self,request,*args,**kwargs):
        records=self.get_data()
        Records= RecordSerializer(records,many=True)
        return Response(Records.data)
       
def Erp(request):
    Records= Record.objects.all()
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            print(request.user)
            return HttpResponse('ok')
        else:
            return HttpResponse("data is not found ")
    

    return HttpResponse("Data is called")

#Method for the Signup Request and call .
def signup(request):
    context={}
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        rpassword = request.POST.get('confirmpassword')
        username = User.objects.filter(username=email)
        print(username,"username")
        
        if password==rpassword and len(username)==0:
            createUser = User.objects.create_user(username=email,password=password)
            createUser.save()
            print("user created")
            return render(request, 'App_auth/login_or_signup.html')
        
        
        else:
            context={'error':"Password does match please check the field carefuy"}
            return render(request, 'App_auth/signup.html',context)

    

    
    return render(request, 'App_auth/signup.html')

def login_signup(request):
    context={}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        users= User.objects.filter(username=email)
        if len(users)!=0:
            user = authenticate(username=email, password=password)
            print(user)
            if user:
                login(request, user)
                print("this is the Logined user hello i am here ")
                context={'error':"user Login sucessfully"}
                return render(request,'App_auth/demo.html',context)
            else:
                context = {'error': "Password is incorrect"}
                return render(request,'App_auth/login_or_signup.html',context)

        else:
            context = {"error":"This users does not exist please signup"}
            return  render(request,'App_auth/login_or_signup.html',context)


    return render(request,'App_auth/login_or_signup.html')

def Delete(request):
    UserName=request.user.username
    user=User.objects.filter(username=UserName)
    user.delete()
    return render(request,'App_auth/login_or_signup.html')

def Start(request):
    global String
    context={"data":String}
    if(len(String)==0):
        String=''
        return render(request,'App_auth/demo.html',context)
    
    elif(len(String)>=6):
        String=''
        return render(request,'App_auth/demo.html',context)
    else:
        return render(request,'App_auth/demo.html',context)

    


def updateboard(request):
    global String 
    context={}
    if request.method=="POST":
        pk= request.POST.get('Character')
        String+=pk 
        item=random.randint(0,9)
        String+=str(item)
        if(len(String)<6):
            context={'data':len(String),'flag':1}
            return render(request,'App_auth/demo1.html',context)

        if(len(String)==6):
            j=len(String)-1
            for i in range(len(String)):
                if(String[i]==String[j] and i<j):
                    j-=1
                elif(i>=j):
                    bit=True
                    string="String is Pallindrome"
                    context={'data':string,'bit':bit}    
                else:
                    bit=True
                    string ="String is not a pallindrome"
                    context={'data':string,'bit':bit}
                    break
        
    else:
        return render(request,'App_auth/demo1.html',context)

    return render(request,'App_auth/demo1.html',context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_auth:login-or-signup'))

