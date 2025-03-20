from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login, PasswordChangeView
from django.urls import path, include
from django.conf import settings as st
from django.conf.urls.static import static

from Users.views.auth import UserSignup, UserLogin
from students.views.students import *
from Users.views.main import *

from API import views as api_view

urlpatterns = [] + static(st.MEDIA_URL, document_root=st.MEDIA_ROOT)

# handler404="students.views.defaults.NotFound"

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
    path("user/add_user/", UserSignup, name="user_register"),
    path("user/logout/", LogoutView.as_view(), name="user_logout"),
    path("user/change_password/", PasswordChangeView.as_view(), name="change_user_passord"),
]

students = [
    path("student/add", Add_Student, name='add_student'),
    path("student/Edit/", Add_Student, name='add_student'),
    path("student/list/", Student_View, name='student_list'),
]

users= [
    path(r"user/<str:username>", user_view, name="user_view")
]

#API
user_list=api_view.UserViewset.as_view({'get':'list'})
student_list=api_view.StudentViewset.as_view({'get':'list'})
group_list=api_view.GroupViewset.as_view({'get':'list'})


get_routes=[
    #user
    path('api/users/', user_list, name='Api_users'),
    path('api/user/<int:pk>', api_view.UserCreateRetrieveUpdateDestroy.as_view(), name='user_profile'),
    
    #students
    path('api/students/', student_list, name='Api_students'),
    path('api/student/<int:roll_number>', api_view.StudentRetrieveUpdateDestroy.as_view(), name='Api_students'),
    
    path('api/groups/', group_list, name='Api_groups')
]

post_routes=[
    path('api/user/register/', api_view.UserRegistrationViewset.as_view(), name="Api_user_registration"),
    path('api/students/add', student_list, name='Api_students_Registration'),
]

patch_routes=[]

delete_routes=[
    path('api/user/delete/<int:pk>', api_view.UserCreateRetrieveUpdateDestroy.as_view(), name="Api_user_deletion"),
    path('api/user/delete/<int:roll_number>', api_view.StudentRetrieveUpdateDestroy.as_view(), name="Api_Student_deletion")
]


api = [
    path('api/', api_view.api_root, name='api_root'),    
]

api.extend(get_routes)
api.extend(post_routes)
api.extend(patch_routes)
api.extend(delete_routes)



urlpatterns.extend(admin_urls)
urlpatterns.extend(forms)
urlpatterns.extend(students)
urlpatterns.extend(main) 
urlpatterns.extend(users) 
urlpatterns.extend(api) 
