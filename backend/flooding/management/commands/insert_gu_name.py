from django.core.management import BaseCommand
import pandas as pd
from flooding.models import SeoulGu

from config.settings import BASE_DIR

CSV_DIR = f'{BASE_DIR}/../res/csv'


class Command(BaseCommand):
    """
    강우량 API 와 하수관 수위 query parameter 를 매핑하기 위해
    미리 서울 오픈 API 에서 csv 파일을 pkl 로 변환 후 (용량이 커서 중복을 제거한 pkl 파일)
    SeoulGu Model 에 insert 함

    """

    def handle(self, *args, **options):
        """
        pkl 파일을 읽어들여 서울시 구 이름을 읽어들인다.
        """
        df_water_level = pd.read_pickle(f'{CSV_DIR}/seoul_water_level_unique.pkl')
        df_water_level = df_water_level.sort_values(by=['구분명'])

        df_rainfall = pd.read_pickle(f'{CSV_DIR}/seoul_rainfall_unique.pkl')
        df_rainfall = df_rainfall.sort_values(by=['구청명'])
        df_rainfall_rename = df_rainfall.rename(columns={'구청 코드': 'gu_code'})

        for row in df_water_level.itertuples(index=False):
            name = row.구분명 + '구'
            SeoulGu.objects.get_or_create(name=name, water_level_gu_code=row.구분코드)

        for row in df_rainfall_rename.itertuples(index=False):
            code = row.gu_code
            SeoulGu.objects.update_or_create(
                name=row.구청명,
                defaults={
                    'rainfall_gu_code': code
                }
            )