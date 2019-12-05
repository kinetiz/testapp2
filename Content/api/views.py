from ..models import Content
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response

class ContentListView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = serializers.ContentSerializer

class ContentCreateView(generics.CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = serializers.ContentSerializer

    # def create(self, request, *args, **kwargs):
    #     super(ContentCreateView, self).create(request, args, kwargs)
    #     response = {"status_code": status.HTTP_200_OK,
    #                 "message": "Successfully created",
    #                 "result": request.data}
    #     return Response(response)

class ContentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = serializers.ContentSerializer

    def retrieve(self, request, *args, **kwargs):
        super(ContentDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(ContentDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(ContentDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)