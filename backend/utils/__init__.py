import datetime
import os

import requests

URL = 'http://openapi.seoul.go.kr:8088'
API_KEY = os.environ.get('SEOUL_OPEN_API_KEY')
LIMIT_ROOF = 5
DT_FMT = '%Y%m%d%H'


def get_seoul_water_level(code, start_dt):
    request_num = 1  # HACK: 반복 요청을 막기 위한 flag

    def get_url(dt: datetime) -> str:
        """
        API 요청 URL 을 반환하는 함수
        :param dt: datetime
        :return: str 형태의 url
        """
        end_dt = dt + datetime.timedelta(hours=1)
        start = dt.strftime(DT_FMT)
        end = end_dt.strftime(DT_FMT)
        return f'{URL}/{API_KEY}/json/DrainpipeMonitoringInfo/1/5/{code}/{start}/{end}'

    def response(start_dt_: datetime) -> dict:
        """
        response 가 없을 경우 과거 데이터를 가져오기 위해 재귀 함수를 만듦
        :param start_dt_: 요청 시간
        :return: dict, 하수관 수위 response
        """
        nonlocal request_num
        if request_num > LIMIT_ROOF:
            raise Exception('요청이 반복 되고 있습니다.')
        request_num += 1  # HACK: 무한 루프를 돌지 않기 위해 만듦

        url = get_url(start_dt_)
        res = requests.get(url)
        result = res.json()
        result = result.get('DrainpipeMonitoringInfo') or result.get('RESULT').get('CODE')
        if '200' in result:
            dt = start_dt_ - datetime.timedelta(hours=1)
            return response(dt)
        return result.get('row')

    return response(start_dt)


def get_seoul_rainfall(gu_name):
    url = f'{URL}/{API_KEY}/json/ListRainfallService/1/50/{gu_name}'
    res = requests.get(url)
    result = res.json()  # type: dict
    result = result.get('ListRainfallService')
    return result.get('row')
