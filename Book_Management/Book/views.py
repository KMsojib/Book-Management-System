from django.shortcuts import render, redirect
from Book.forms import BookStoreForm
from Book.models import BookStoreModel

# Create your views here.
def home(request):
    return render(request,'upload_book.html')


def StoreBook(request):
    if request.method == 'POST':
        book = BookStoreForm(request.POST)
        if book.is_valid():
            book.save()
            print(book.cleaned_data)
            return redirect('ShowBooks')
    else:
        book = BookStoreForm()    
    return render(request,'upload_book.html',{'Book': book})

def ShowBooks(request):
    book = BookStoreModel.objects.all()
    print(book)
    return render(request, 'show_book.html',{'Data': book})