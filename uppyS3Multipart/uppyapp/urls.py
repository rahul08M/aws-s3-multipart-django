# django imports
from django.urls import path, include

# internal imports
from .views import *

urlpatterns = [
    path('upload/', UploadUppyView.as_view(), name='uppy-upload'),
    path('uppy/s3/multipart', UppyMultiPart.as_view(), name='uppy-part'),
    path('uppy/s3/multipart/<str:upload_id>/<str:part>', UppyMultiPart.as_view(), name='uppy-part'),
    path('uppy/s3/multipart/<str:upload_id>', UppyMultiPart.as_view(), name='uppy-part'),
]
