#from .models import Todo, Category
from rest_framework import viewsets, permissions, exceptions

from core.models import licenss
from .serializers import LizSerializer



class LizViewSet(viewsets.ModelViewSet):
    
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LizSerializer
    def get_queryset(self):
       ggg = self.kwargs['guid']
     
       queryset = licenss.objects.filter(guid=ggg)
       return queryset
    
class LizViewSet2(viewsets.ModelViewSet):
    
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LizSerializer
    def get_queryset(self):
       ggg = self.kwargs['okpo']
       queryset = licenss.objects.filter(okpo=ggg)
       return queryset
 
class LizPOST(viewsets.ModelViewSet):
    serializer_class = LizSerializer

    queryset = licenss.objects.all()
    
    permission_classes = [
        permissions.IsAdminUser
    ]
   
