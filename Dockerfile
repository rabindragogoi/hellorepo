FROM python:3-alpine
WORKDIR /service
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/application.py ./
EXPOSE 8399
ENTRYPOINT ["python3", "application.py"]
