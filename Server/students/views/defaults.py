from django.shortcuts import render
from django.template import RequestContext

def NotFound(request, exception, *args, **kwargs):
    return render('404.html', status = 404)

def Unauthorised(request, exception):
    pass
    
def InternalServerError(request, exception):
    pass


#DB-Errors
def IntegrityError(request, exception):
    pass

def DataError(request, exception):
    pass