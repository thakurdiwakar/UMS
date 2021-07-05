
from django.contrib import admin
from django.urls import path
from mycrud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_show,name="addandshow"),
    path('delete/<int:id>/', views.delete_data,name="deletedata"),
    path('<int:id>/', views.update_data,name="updatedata"),
    path('mycrud/forms.html', views.form_data,name="formdata"),
    
    
]
