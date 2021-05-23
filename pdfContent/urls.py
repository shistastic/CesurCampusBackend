from django.urls import path
from django.urls import path
from pdfContent import views

app_name = 'pdf_reports'

urlpatterns = [
    path('', views.simple_upload, name='create_pdf'),
    path('showcontent/<int:id>/', views.show_image, name='show_image'),
]

