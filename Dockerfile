FROM python:3.9-slim-bullseye

WORKDIR /app

COPY fetch_jwks.py .

RUN pip install requests

CMD ["python", "fetch_jwks.py"]
