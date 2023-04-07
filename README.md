
## Simple working demo for [AWS S3](https://aws.amazon.com/s3/) Multipart using Uppy

This is a simple demo of how to use [Uppy](https://uppy.io/docs/aws-s3-multipart/) to upload files to AWS S3 in multiple parts. Here are the setup instructions:

#### [Uppy AWS S3 Multipart](https://uppy.io/docs/aws-s3-multipart/)

## Setup

Following are the setup instruction

##### 1. Clone the repository by running the following command:
```buildoutcfg
git clone https://github.com/rahul08M/aws-s3-multipart-django.git
```
##### 2. Create a Python 3.8 virtual environment:

```bash
python3.8 -m venv <env-name>
```
##### 3. Install all required packages:

```bash
pip install -r requirements.txt
```
##### 4. Configure your AWS settings in `settings.py`:

```bash
AWS_ACCESS_KEY_ID = '<AWS_ACCESS_KEY>'
AWS_SECRET_ACCESS_KEY = '<AWS_SECRET_ACCESS_KEY>'
AWS_STORAGE_BUCKET_NAME = '<AWS_STORAGE_BUCKET_NAME>'
AWS_REGION_NAME = '<AWS_REGION_NAME>'
```
##### 5. Migrate and run the server:

```bash
python manage.py migrate   # migrate db models
python manage.py runserver  # run server on default port 8000
python manage.py runserver 0.0.0.0:<port> # run server on default port custom port
http://127.0.0.1:8000/upload/
```
##### 6. Access the demo at `http://127.0.0.1:8000/upload/`.
That's it! With these steps, you should be able to successfully upload files to AWS S3 using Uppy's multipart feature.
