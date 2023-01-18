# aws-s3-multipart-django

![Django Hacks](https://i.ibb.co/r5tVzLx/uppy-Untitled.png)

## Simple working demo for AWS S3 Multipart using Uppy
#### [Uppy AWS S3 Multipart](https://uppy.io/docs/aws-s3-multipart/)
## Setup

Following are the setup instruction

##### Clone the repo
```buildoutcfg
git clone https://github.com/rahul08M/aws-s3-multipart-django.git
```
##### Create python3.8 Virtual Env

```bash
python3.8 -m venv <env-name>
```
##### Install all required packages

```bash
pip install -r requirements.txt
```
##### Configure AWS Settings in settings.py

```bash
AWS_ACCESS_KEY_ID = '<AWS_ACCESS_KEY>'
AWS_SECRET_ACCESS_KEY = '<AWS_SECRET_ACCESS_KEY>'
AWS_STORAGE_BUCKET_NAME = '<AWS_STORAGE_BUCKET_NAME>'
AWS_REGION_NAME = '<AWS_REGION_NAME>'
```
##### Migrate and runserver

```bash
python manage.py migrate   # migrate db models
python manage.py runserver  # run server on default port 8000
python manage.py runserver 0.0.0.0:<port> # run server on default port custom port
http://127.0.0.1:8000/upload/
```
