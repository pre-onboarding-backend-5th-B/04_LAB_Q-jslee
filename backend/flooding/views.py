import datetime

from django.shortcuts import get_object_or_404
from django.utils.timezone import make_aware
from rest_framework.decorators import api_view
from rest_framework.response import Response

import utils
from region.models import SeoulGu


@api_view(['GET'])
def get_flooding(requests, gu_name):
    """
    서울 하수관로 수위와 강우량을 알려준다.
    이를 토대로 침수 레벨을 알려준다.

    :param requests:
    :param gu_name:
    :return:
    """

    start_dt = make_aware(datetime.datetime.now())
    inst = get_object_or_404(SeoulGu, name=gu_name)
    water_level_res = utils.get_seoul_water_level(inst.water_level_gu_code, start_dt)
    rainfall_res = utils.get_seoul_rainfall(gu_name)
    result = {
        'water_level': water_level_res,
        'rainfall': rainfall_res
    }
    return Response(result)
