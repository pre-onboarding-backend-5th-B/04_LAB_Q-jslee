from rest_framework.generics import ListAPIView

from region.models import SeoulGu
from region.serializers import SeoulGuSerializer


class SeoulGuListView(ListAPIView):
    """
    서울 구 이름을 보여주는 List View
    """
    queryset = SeoulGu.objects.all()
    serializer_class = SeoulGuSerializer
