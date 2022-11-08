# 04_LAB_Q-jslee

## 원티드 4주차 과제 랩큐

- **서울시 하수관로 수위 현황**과 **서울시 강우량 정보**를 활용하여 사용자에게 필요한 정보를 주는 REST API 개발을 목표로 하고 있습니다.

# 사용 기술 스택

<div align="center">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white" alt="파이썬" />
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white" alt="장고" />
    <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=Postgresql&logoColor=white" alt="PostgreSQL" />
</div>

# 기능 구현

## Query Parameter

- Gubn: 구분코드
- dateType(?): 일간, 시간, 분, 초 등등 시간 타입을 넣는다.

## 기본요구사항

1. 서울시 하수관로 수위 현황을 사용자에게 제공해줌
2. 강수량 데이터를 사용자에게 제공해줌
3. 두 데이터를 결합하여 사용자에게 제공해줌

## 추가될 기능

1. Dokcer
2. Aws

# API 목록

| METHOD | URL                       | QUERY_STRING | DESCRIPTION |
|--------|---------------------------|--------------|-------------|
| GET    | /api/flooding/water-level | GUBN_NAM     | 서울 하수관로     |
| GET    | /api/flooding/rainfall    | GU_NAME      | 서울 강우량      |
