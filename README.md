# S3 Image Upload & Retrieve

Simple server (written in Python/Django) for uploading images to a designated
AWS S3 Bucket

## Installation Steps

    1. Clone repository on your computer
    2. Make sure python and pip are installed on your machine
    3. From the project root, use pip to install requirements

    $ pip install -r requirements.txt

    4. Set the AWS S3 Access Information in environment variables

    $ export S3_BUCKET_NAME=DESIREDBUCKETNAME
    $ export AWS_ACCESS_KEY_ID=AWSACCESSKEYID
    $ export AWS_SECRET_ACCESS_KEY=AWSSECRETACCESSKEY

    5. Run the project:

    $ python s3_upload/manage.py runserver

    6. Navigate to 127.0.0.1:8000 in your browser (tested on Safari desktop and Chrome).
There's a small page on the index that can be used to test the server endpoints

## Server Endpoints

    'POST: /api/images/' - Posts the submitted images to the specifed S3 bucket
    'GET: /api/images/[image_id]' - Retrieves the specified image from S3 and serves the image
