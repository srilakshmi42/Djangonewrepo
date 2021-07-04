from django.urls import path
from common import views

urlpatterns=[
    path('',views.showCommonPage,name='common_page'),
    path('student/',views.showStudentPage,name='student_page'),
    path('student_Registration/',views.studentRegistration,name='student_registration'),

    path('student_Otp/',views.openStudentOtp,name='student_otp'),
    path('student_login_check/',views.studentLoginCheck,name='student_login_check'),
    path('validate_otp/',views.validateOtp,name='validate_otp'),

]