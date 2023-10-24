from rest_framework import viewsets
from forms.models import Form
from forms.serializers import FormSerializer
# Create your views here.

class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    