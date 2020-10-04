import os
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .forms import ImageForm
from .models import ImageModel
from rest_framework.routers import DefaultRouter
from .serializers import FileSerializer
from rest_framework import status
import io
import PIL.Image as Image
import random
import keras
from keras.models import model_from_json
import numpy as np
from skimage import transform

# Create your views here.


def model_form_upload(request):
    imagemodel = ImageModel.objects.get(id=1)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("form received")

            text = handle_image(form.cleaned_data["image"].image)
            return HttpResponse(text)
    else:
        form = ImageForm()
    return render(request, 'index.html', {
        'form': form, 'model': imagemodel
    })


class ImageUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            resp = handle_image(request.data["image"].file.file)
            return Response(resp, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# handles_image returns text
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("Trained.h5")


def handle_image(imgio):
    img = Image.open(io.BytesIO(imgio.read()))

    print(type(img))
    np_image = np.array(img).astype('float32')/255
    np_image = transform.resize(np_image, (224, 224, 3))
    np_image = np.expand_dims(np_image, axis=0)

    print(np_image.shape)
    return str(loaded_model.predict(np_image)[0][0])
