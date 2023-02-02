from logging import NullHandler
from logging.config import valid_ident
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from .models import *
import openpyxl

def index(request):
    if request.user.is_authenticated==False:
        books = Books.objects.all().values()
        template = loader.get_template('main.html')
        context = {
            'books': books,
        }
        return HttpResponse(template.render(context, request))
    else:
        books = Books.objects.all().values()
        template = loader.get_template('main.html')
        context = {
            'books': books,
        }
        return render(request,'login.html',context)
    
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        books = Books.objects.all().values()
        template = loader.get_template('main.html')
        if request.method=="POST":
            name=request.POST.get('username')
            buyers = Buyers.objects.all().values()
            for x in buyers:
                if x["firstname"]==name:
                    print("Authenticated")
                    user=authenticate(request,username=name,password="123")
        if user is not None:
            login(request,user)
            return redirect('main') 
            return render(request,'login.html')

        '''pwd=request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('home') 
       return redirect('login')'''


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        Form=UserCreationForm()
        if request.method=='POST':
            Form=UserCreationForm(request.POST)
            if Form.is_valid():
                currUser=Form.save()
                Buyers.objects.create(user=currUser,firstname=currUser.username)
                return redirect('login')
        context={
            'form':Form
        }
        return render(request,'register.html',context)


def add(request, id):
    books = Books.objects.get(id=id)
    #request.session['bookinfo'] = books
    template = loader.get_template('add.html')
    context = {
            'books': books,
    }
    global val
    def val():
        return books
    return render(request,'add.html',context)


def addtocart(request):
    #buyername = request.POST['first']
    buyername=""
    #book = request.session['bookinfo']
    bookinfo = val()
    bookcheckout = Checkout(bookname=bookinfo.bookname , bookauthor=bookinfo.bookauthor,  price=bookinfo.price, buyer_name=buyername, )
    bookcheckout.save()
    return HttpResponseRedirect(reverse('index'))

def viewcart(request):
    bookcart = Checkout.objects.all().values()
    cost = 0
    for row in bookcart:
        print(row)
        cost =cost + row['price']
        print("Cost is ",cost)
    template = loader.get_template('viewcart.html')
    context = {
            'bookcart': bookcart,
            'total':cost
        }
    return HttpResponse(template.render(context, request))
    #return render(request,'viewcart.html')

def delete(request, id):
    book_to_delete = Checkout.objects.get(id=id)
    print(book_to_delete.bookname)
    book_to_delete.delete()
    return HttpResponseRedirect('/viewcart')

def uploadapps(request):
    if "GET" == request.method:
        return render(request, 'main.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet2"]
        print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows(2):
            row_data = list()
            
            for cell in row:
                row_data.append(str(cell.value))
            bookauth = row_data[0]
            pr = (int(row_data[1]))
            bookn= row_data[2]
            seller = row_data[3]
            book = Books(bookauthor=bookauth, price=pr, bookname=bookn, seller_name_id=1)
            book.save()
            excel_data.append(row_data)

        return render(request, 'main.html', {"excel_data":excel_data})
    return render(request,'viewcart.html')
