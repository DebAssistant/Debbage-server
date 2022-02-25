FROM python:3.9

EXPOSE 4563

COPY . .

RUN pip install -r reqr.txt

RUN prisma generate

CMD ["python", "main.py"]