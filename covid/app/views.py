from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.contrib import messages
from .models import Contact
from django.core import mail
from django.core.mail.message import EmailMessage




# Create your views here.
def index(request):
    return render(request,'index.html')
    
def about(request):
    return render(request,'about.html')

def handleBlog(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    posts=BlogPosts.objects.all()
    context= {'posts':posts}
    return render(request,'handleBlog.html',context)

def services(request):
    return render(request,'services.html')

    
def contact(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        phone=request.POST.get('num')
        description=request.POST.get('desc')
        contact_query=Contact(name=fullname,email=email,number=phone,description=description)
        contact_query.save()
        from_email=settings.EMAIL_HOST_USER
        # email starts here
        connection=mail.get_connection()
        connection.open()
        email_mesge=mail.EmailMessage(f'Website Email from : {fullname}',f'Email from: {email}\nPhone Number : {phone}\nUser Query : {description}',from_email,['snsathhya7411@gmail.com'],connection=connection)
        email_user=mail.EmailMessage('kavya website',f'Hello {fullname}\nThanks for Contacting Us! We will resolve your query ASAP!\nThank You.',from_email,[email],connection=connection)
        connection.send_messages([email_mesge,email_user])
        connection.close()
        messages.info(request,"Thanks for Contacting Us")
        return redirect('/contact')
        


    

    return render(request,'contact.html')
    

def signup(request):

    if request.method=="POST":
            username=request.POST['username']
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            email=request.POST['email']
            pass1=request.POST['pass1']
            pass2=request.POST['pass2']
            if pass1!=pass2:

                messages.info("Password not match")


            try:
                 if User.objects.get(username=username):
                     messages.info("username is taken")

            except Exception as identifier:
                 pass

            myuser=User.objects.create_user(username,email,pass1) 
            myuser.first_name=firstname
            myuser.last_name=lastname
            myuser.save()
            messages.info(request,"signup successful")  

    return render(request,'auth/signup.html')

def handlelogin(request):
    if request.method=="POST":
        handleusername=request.POST['username']
        handlepassword=request.POST['pass1']
        user=authenticate(username=handleusername,password=handlepassword)
        if user is not None:
            login(request,user)
            messages.info(request,"welcome to my website")
            return redirect('/')
        else:
            messages.warning(request,"Invalid Credentials")
            return redirect('/login')
            
   
    return render(request,'auth/login.html')

def handlelogout(request):
    logout(request)
    messages.success(request,"logout succesfull")
    return redirect('/login')

def add(request):
    if request.method == 'POST':

        title=request.POST.get('title')
        content=request.POST.get('desc')
        name=request.POST.get('name')
        file=request.FILES['file']
        query=BlogPosts(title=title,content=content, author=name,img=file)
        query.save()
        messages.info(request,'Your Post Has Been Saved')
        return redirect('/handleBlog')


    return render(request,'add.html')

def search(request):
    #query=request.GET['search']
    query=request.POST.get('search',False)
    print (query)

    if len(query)>80:
        
        allPosts = BlogPost.objects.none()
    else:
        allPostsTitle=BlogPost.objects.filter(title__icontains=query)
        allPostsContent=BlogPost.objects.filter(content__icontains=query)
        allPosts=allPostsTitle.union(allPostsContent)
    if allPosts.count() == 0:
        messages.warning(request,"No Search Results")
    params={'allPosts':allPosts,'query':query}        

    return render(request,'search.html',params)    



def msme(request):
    return render(request,'msme.html')

def real(request):
    return render(request,'real.html')

def avi(request):
    return render(request,'avi.html')

def txt(request):
    return render(request,'txt.html')

def txtd(request):
    return render(request,'txtd.html')

def d(request):
    return render(request,'d.html')

def s(request):
    return render(request,'s.html')

def f(request):
    return render(request,'f.html')

def a(request):
    return render(request,'a.html')

def b(request):
    return render(request,'b.html')

def c(request):
    return render(request,'c.html')

def p(request):
    return render(request,'p.html')

def q(request):
    return render(request,'q.html')

def r(request):
    return render(request,'r.html')
    
