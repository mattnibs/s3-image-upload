from s3_upload import settings
import boto
from boto.s3.key import Key
import uuid
import os
import re

def getS3Bucket():
    conn = boto.connect_s3(
        settings.AWS_ACCESS_KEY_ID,
        settings.AWS_SECRET_ACCESS_KEY
    )

    return conn.get_bucket(settings.S3_BUCKET_NAME)

def uploadImage(imageFile):

    try:
        # create unqiue name and get extension
        unique_name = str(uuid.uuid1())
        fileName, fileExtension = os.path.splitext(imageFile.name)

        # validate fileExtension
        if not re.match('\.(gif|png|jpg|jpeg)$', fileExtension.lower()):
            raise Exception

        # get bucket and upload image file
        bucket = getS3Bucket()
        key = Key(bucket)
        key.key = unique_name + fileExtension
        key.size = imageFile.size # size must be set in order for this to work
        key.send_file(imageFile)

        return True, unique_name

    except Exception, e:
        print e
        return False, None

def getImage(imageID):
    try:
        bucket = getS3Bucket()
        key = next(k for k in bucket.list(imageID))
        return key
    except Exception, e:
        return None
