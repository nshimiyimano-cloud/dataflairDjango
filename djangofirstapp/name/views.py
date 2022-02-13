from django.http import HttpResponse
from django.shortcuts import render


names={
   "firstname":"nshimiyimana"
}
students={
   "student":['nshimiyimana','isingizwe','patient','dukuze']
}
#djangofirstapp/name/templates/footer.html

def index(request):
       return HttpResponse('<h1>hello index</h1>')

def htmlpage(request):
    return render(request, 'htmlpage.html',students)
 
 #about cookie
def setCookie(request):
    html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
    if request.COOKIES.get('visits'):
        html.set_cookie('studentMIS', 'Welcome Back')
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits', value + 1)
    else:
        value = 1
        text = "Welcome for the first time"
        html.set_cookie('visits', value)
        html.set_cookie('studentMIS', text)
    return html
 
 
def showCookie(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('studentMIS')
        html = HttpResponse("<center><h1>{0}<br>You have requested this page {1} times</h1></center>".format(text, value))
        html.set_cookie('visits', int(value) + 1)
        return html
    else:
        return redirect('/setcookie')
     
def delete_co(request):
    if request.COOKIES.get('visits'):
       response = HttpResponse("<h1>studentMIS<br>Cookie deleted</h1>")
       response.delete_cookie("visits")
    else:
        response = HttpResponse("<h1>studentMIS</h1>need to create cookie before deleting")
    return response
 
 

def create_session(request):
       request.session['name'] = 'username'
       request.session['password'] = 'password123'
       return HttpResponse("<h1> schoolMIS<br> the session is set </h1>")

def access_session(request):
       response="<h1> Welcome to Sessions of schoolMIS </h1><br>"
       if request.session.get('name'):
              response +="Name : {0} <br> ".format(request.session.get('name'))
       if request.session.get('password'):
              response+= "password : {0} <br>".format(request.session.get('password'))
              return HttpResponse(response)
       else:
              return redirect('create-session/')
def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except  KeyError:
        pass
    return HttpResponse("<h1>studentMIS<br>Session Data cleared</h1>")

           
 

   
