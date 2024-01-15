FROM python:3.12.1

WORKDIR /app_workdir

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "main_run.py"]