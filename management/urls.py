from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.urls import path, include
from django.conf import settings as st
from django.conf.urls.static import static

from students.views.auth import user_signup, user_login
from students.views.students import *
from students.views.user import *

from students.API import views as api_view

urlpatterns = [] + static(st.MEDIA_URL, document_root=st.MEDIA_ROOT)


admin_urls = [
    path('admin', admin.site.urls, name='admin'),
]

main=[
    path('', index, name='index'),
    path('info/', info, name="user_informatics"),
    path('perms/', perms, name="user_perms"),
    path('settings/', user_settings, name="user_settings"),
]

forms = [
    path('user/login/', LoginView.as_view(template_name='./forms/login.j2'), name="user_login"),
    path("user/add_user/", user_signup,name="user_register"),
    path("user/logout/", LogoutView.as_view(), name="user_logout")
]

students = [
    path("student/add",Add_Student, name='add_student'),
    path("student/Edit/",Add_Student, name='add_student'),
    path("student/list/",Student_View, name='student_list'),
]

users= [
    path(r"user/<str:username>", user_view, name="user_view")
]

user_list=api_view.UserViewset.as_view({'get':'list'})
student_list=api_view.StudentViewset.as_view({'get':'list'})
group_list=api_view.GroupViewset.as_view({'get':'list'})

api = [
    path('api/', api_view.api_root, name='api_root'),
    path('api/users/', user_list, name='Api_users'),
    path('api/users/register/', api_view.UserRegistrationViewset.as_view(), name="Api_user_registration"),
    path('api/students/', student_list, name='Api_students'),
    path('api/groups/', group_list, name='Api_groups')
]


urlpatterns.extend(admin_urls)
urlpatterns.extend(forms)
urlpatterns.extend(students)
urlpatterns.extend(main) 
urlpatterns.extend(users) 
urlpatterns.extend(api) 
