from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from drf_yasg.utils import swagger_auto_schema

from resume import serializers, models



class ResumeView(APIView):
    model = models.Resume
    serializer_class = serializers.ResumeSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    http_method_names = ['get', 'patch']

    def get_object(self) -> model:
        return self.model.objects.get_or_create(owner=self.request.user)[0]

    @swagger_auto_schema(responses={200: serializer_class()})
    def get(self, request: Request):
        resume = self.get_object()
        serializer = self.serializer_class(resume)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={200: serializer_class(), 400: {}})
    def patch(self, request: Request):
        resume = self.get_object()
        serializer = self.serializer_class(resume, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

