# from .models import Todo, Category
from rest_framework import viewsets, permissions, exceptions
from ipware import get_client_ip
from core.models import licenss,mg
from order.models import Order
from work.models import employees, posting
from .serializers import EmployeesSerializer, LizSerializer, OrderSerializer,mgSerializer, postingSerializer
from rest_framework import generics

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

    permission_classes = [permissions.IsAdminUser]


class employeesPOST(viewsets.ModelViewSet):
    serializer_class = EmployeesSerializer

    queryset = employees.objects.all()

    permission_classes = [permissions.IsAdminUser]

    def post_queryset(self):
        return self.kwargs["pk"]


class mgPOST(viewsets.ModelViewSet):
    serializer_class = mgSerializer

    queryset = mg.objects.all()

    def perform_create(self, serializer):
        # Получение IP-адреса из запроса
        ip_address = self.get_client_ip()
        # Сохранение объекта с IP-адресом
        serializer.save(ip_address=ip_address)

    def get_client_ip(self):
        """Получить IP-адрес клиента из запроса"""
        x_forwarded_for = self.request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = self.request.META.get("REMOTE_ADDR")
        return ip

    # def create(self, request, *args, **kwargs):
    #     client_ip, is_routable = get_client_ip(request)
    #     # print(f"IP клиента: {client_ip}, Доступен извне: {is_routable}")
    #     self.kwargs["ip_address"] = client_ip
    #     return super().create(request, *args, **kwargs)

    permission_classes = [
        permissions.IsAdminUser
    ]

class OrderPOST(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    queryset = Order.objects.all()
    
    permission_classes = [
        permissions.IsAdminUser
    ]

class OrderViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrderSerializer
    def get_queryset(self):
        ggg = self.kwargs['guid']

        queryset = Order.objects.filter(guid=ggg)
        return queryset  


class empViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.AllowAny]
    serializer_class = EmployeesSerializer

    def get_queryset(self):
        ggg = self.kwargs["guid"]

        queryset = employees.objects.filter(guid=ggg)
        return queryset


class posViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.AllowAny]
    serializer_class = postingSerializer

    def get_queryset(self):
        ggg = self.kwargs["guid"]

        queryset = posting.objects.filter(guid=ggg)
        return queryset


class empDW(generics.RetrieveUpdateDestroyAPIView):
    queryset = employees.objects.all()
    serializer_class = EmployeesSerializer


class postingPOST(viewsets.ModelViewSet):
    serializer_class = postingSerializer

    queryset = posting.objects.all()

    permission_classes = [permissions.IsAdminUser]

    def post_queryset(self):
        return self.kwargs["pk"]
