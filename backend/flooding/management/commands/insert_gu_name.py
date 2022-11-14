import pandas as pd
from django.core.management import BaseCommand

from config.settings import BASE_DIR
from flooding.models import SeoulGu

CSV_DIR = f'{BASE_DIR}/../res/csv'


class Command(BaseCommand):
    """
    강우량 API 와 하수관 수위 query parameter 를 매핑하기 위해
    미리 서울 오픈 API 에서 csv 파일을 pkl 로 변환 후 (용량이 커서 중복을 제거한 pkl 파일)
    SeoulGu Model 에 insert 함

    """

    def handle(self, *args, **options):
        """
        pkl 파일에서 서울시 구 이름을 읽어들여서
        SeoulGu DB 에 insert 시킨다.
        """
        df_water_level = pd.read_pickle(f'{CSV_DIR}/seoul_water_level_unique.pkl')
        df_water_level = df_water_level.sort_values(by=['구분명'])
        for row in df_water_level.itertuples(index=False):
            name = row.구분명 + '구'
            SeoulGu.objects.get_or_create(name=name, water_level_gu_code=row.구분코드)
