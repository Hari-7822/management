"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.contrib.auth import urls
from students.views.auth import user_signup, user_login
from students.views.students import *

urlpatterns = []

admin_urls = [
    path('admin/', admin.site.urls),
]

index=[
    path('/', list, name='index'),
    # path('student/', list )
]

forms = [
    # path('user/', include('django.contrib.auth.urls')),
    path('user/login/', user_login, name="user_login" ),
    path("user/add_user/", user_signup,name="user_register")
]

students = [
    path("student/add",Add_Student, name='add_student'),
    path("student/Edit/",Add_Student, name='add_student'),
]
temp = [
    path('list/', list, name='list')
]

urlpatterns.extend(admin_urls)
urlpatterns.extend(forms)
urlpatterns.extend(students)
urlpatterns.extend(temp) 