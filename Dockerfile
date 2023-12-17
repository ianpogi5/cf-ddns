FROM python:3.12-alpine

# Create WORKDIR
ENV WORKDIR=/cflare-ddns
RUN mkdir "$WORKDIR"
WORKDIR "$WORKDIR"

# Prepare codes
ARG CFLARE_DDNS_VERSION
COPY ./cflare_ddns cflare_ddns/
COPY README.md .
COPY setup.py .
RUN sed -i "s/{{VERSION_PLACEHOLDER}}/${CFLARE_DDNS_VERSION}/g" setup.py

# Install self
RUN pip install .

# Do not buffer stdout and stderr
ENV PYTHONUNBUFFERED=true

# Run cflare-ddns
CMD ["cflare-ddns"]

