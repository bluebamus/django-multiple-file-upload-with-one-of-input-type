from django.shortcuts import render, redirect
import os
from .forms import UploadFileForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    form = UploadFileForm()
    if request.method == 'POST':
        print(os.getcwd())
        print("POST method")
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print("Valid")
            for count, x in enumerate(request.FILES.getlist("files")):
                def handle_uploaded_file(f):
                    with open(os.path.join(os.getcwd(),"media", f.name),'wb+') as destination:
                        for chunk in f.chunks():
                            destination.write(chunk)
                handle_uploaded_file(x)
                print(x.name)
                os.remove("media/"+str(x.name))
                print(str(x.name)+"삭제완료")
            context = {'form':form,}
            return render(request, 'testapp/index.html', context)
            # return HttpResponse(" File uploaded! ")
    else:
        form = UploadFileForm()

    return render(request, 'testapp/index.html', {'form': form})

# 이런 식으로도 가능하다
# ssw makes this for single file upload

# def upload(request):
#     flist = request.FILES.getlist('files')
#     for f in flist:
#         tmp = open(os.path.join(os.getcwd(), 'media', f.name), 'wb+')
#         for chunk in f.chunks():
#             tmp.write(chunk)
#     return HttpResponse( " File uploaded! ")