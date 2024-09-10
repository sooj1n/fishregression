# 1. 베이스 이미지로 Python 3.11 사용
FROM python:3.11

# 2. 작업 디렉토리 생성
WORKDIR /code

# 3. 필요한 파일 복사 (FastAPI 애플리케이션 코드 및 모델)
COPY . /code/

# 4. 필요한 패키지 설치 (예: FastAPI, scikit-learn)
RUN pip install --no-cache-dir -r requirements.txt

# 5. uvicorn을 사용하여 FastAPI 애플리케이션 실행 (포트 8000)
CMD ["uvicorn", "src.fishregression.main:app", "--host", "0.0.0.0", "--port", "8001"]
