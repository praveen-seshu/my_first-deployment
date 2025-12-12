from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def sample_response(request):
    return HttpResponse('hello')

def response2(request):
    return HttpResponse('Welcome to Django')

#jon response
def response_json(request):
    return JsonResponse({'data':[1,2,3]})

#if want to send list(array) as response we should set safe=F

def response_list(request):
    return JsonResponse([1,2,3,4],safe=False)

def response3(request):
    info= {'data':[{'name':'praveen','age':12,'city':'hyd'},{'name':'hemanth','age':22,'city':'hyd'},{'name':'pinky','age':22,'city':'hyd'}]}
    return JsonResponse(info)
#querry parameters
def querry_per(request):
    qp1=request.GET.get('name')
    qp2=request.GET.get('city')
    return JsonResponse(f'hello{qp1} from {qp2}',safe=False)

#querry peramsfor dynamic response
def info (request):
    products=(request.GET.get('product','mobile'))
    quantity=int(request.GET.get('quantity', 1))
    price=int(request.GET.get('price',20000))
    data={'product':products,'quantity':quantity,'total_price':quantity * price}
    return JsonResponse(data)
#filtering using querry perams
data=[1,2,3,4,5,6,7,8,9]
def filtering(request):
    filtered_date=[]
    ip= int(request.GET.get('num',1))
    
    for i in data:
        if i % ip == 0:
            filtered_date.append(i)
    return JsonResponse({'data':filtered_date})

#
student_details=[{'name':'praveen','age':22,'city':'hyd'},{'name':'seshu','age':22,'city':'bang'},{'name':'ambati','age':22,'city':'hyd'},{'name':'pramodh','age':22,'city':'bang'}]
def filterinfo(request):
    filter_stu=[]
    city= request.GET.get('city','hyd')

    for i in student_details:
        if i['city'] == city:
            filter_stu.append(i)
    return JsonResponse({'status':'success','data':filter_stu})