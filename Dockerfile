FROM python:3.12-alpine

RUN pip install --no-cache-dir --upgrade pip
RUN pip install cflare-ddns

CMD ["python3", "-u", "-m", "cflare_ddns"]