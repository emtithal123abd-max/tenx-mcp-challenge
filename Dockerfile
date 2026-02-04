FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -U pip && pip install pytest
CMD ["pytest", "-q"]
