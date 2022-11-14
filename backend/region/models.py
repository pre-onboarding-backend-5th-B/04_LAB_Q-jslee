from django.db import models


class SeoulGu(models.Model):
    """
    서울 구 이름을 저장 하는 테이블

    강우량 CSV 파일과 하수관 수위 정보 CSV 에서 구 이름을 중복제거하여 저장함
    """
    name = models.CharField(max_length=16, unique=True)
    water_level_gu_code = models.CharField(max_length=16, blank=True, null=True)
