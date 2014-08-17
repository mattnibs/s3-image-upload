from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from core import ImageManager
from django.http import HttpResponse, Http404
from django.views.generic import View
import mimetypes

class ImageCreate(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        success, imageName = ImageManager.uploadImage(request.FILES['file'])
        return Response({
            'success': success,
            'image_name': imageName
        })

class GetImage(View):

    def get(self, request, uuid):
        s3Key = ImageManager.getImage(uuid)

        # if None raise 404 error
        if s3Key is None:
            raise Http404

        # create http response with appropriate mimetype
        response = HttpResponse(s3Key.read())
        response['Content-Type'] = mimetypes.guess_type(s3Key.key)[0]
        return response
