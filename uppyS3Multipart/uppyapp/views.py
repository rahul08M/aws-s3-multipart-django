# python imports
import boto3, random, string

# django imports
from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings

# drf imports
from rest_framework.views import APIView
from rest_framework.response import Response


class UploadUppyView(TemplateView):

    template_name = 'index.html'


class UppyMultiPart(APIView):

    bucket = settings.AWS_STORAGE_BUCKET_NAME
    secret_key = settings.AWS_SECRET_ACCESS_KEY
    region_name = settings.AWS_REGION_NAME
    access_key = settings.AWS_ACCESS_KEY_ID

    def client(self):

        """
        Configure AWS S3 Client object.
        """

        client = boto3.client('s3', aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key, region_name=self.region_name)
        return client

    def get(self, request, *args, **kwargs):

        client = self.client()

        if not kwargs.get('part'):
            try:
                parts = client.list_parts(Bucket=self.bucket, Key=request.GET.get('key'), UploadId=kwargs.get('upload_id'))
                return Response(parts['Parts'])
            except:
                return Response([])

        signed_url = client.generate_presigned_url(ClientMethod='upload_part', Params={'Bucket': self.bucket, 'Key': request.GET.get('key'), 'PartNumber': int(kwargs.get('part')), 'UploadId': kwargs.get('upload_id')})

        return Response({'url': signed_url})

    def post(self, request, *args, **kwargs):

        if kwargs.get('part') == 'complete':
            return self.complete_upload(request.data, request.GET.get('key'), kwargs.get('upload_id'))

        return self.create_upload_id(request.data)

    def create_upload_id(self, data):

        client = self.client()

        file_name = data.get('filename')
        file_extension = file_name.split('.')[-1]

        random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

        final_file_name = '%s.%s' % (random_string, file_extension)
        key = final_file_name

        response = client.create_multipart_upload(Bucket=self.bucket, Key=key)

        return Response({'key': response.get('Key'), 'uploadId': response.get('UploadId')})

    def complete_upload(self, data, key, upload_id):

        parts = []

        client = self.client()

        for part in client.list_parts(Bucket=self.bucket, Key=key, UploadId=upload_id)['Parts']:
            parts.append({'ETag': part.get('ETag'), 'PartNumber': part.get('PartNumber')})

        client.complete_multipart_upload(Bucket=self.bucket, Key=key, MultipartUpload={'Parts': parts}, UploadId=upload_id)

        return Response({'key': key, 'uploadId': upload_id})