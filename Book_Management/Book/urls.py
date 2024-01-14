from django.urls import path
from Book.views import home,StoreBook,ShowBooks

urlpatterns = [
    path('',home),
    path('StoreBook/',StoreBook,name="Uploadbook"),
    path('ShowBooks/',ShowBooks,name="ShowBooks"),
    
]

#class="bg-white border-gray-200 dark:bg-gray-900"
# upload,show book,about us, contact