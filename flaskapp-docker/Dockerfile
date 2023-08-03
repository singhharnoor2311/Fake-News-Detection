# Stage 1: Base
FROM ubuntu:22.04 AS base

RUN apt-get update -y && \
    apt-get install python3-pip -y

COPY requirements.txt .

# Stage 2: Builder
FROM base AS builder

RUN apt-get install gcc -y && \
    pip3 install --user -r requirements.txt

# Stage 3: Final
FROM base

COPY --from=builder /root/.local /root/.local
COPY flask-app /opt/

# Make sure scripts in .local are usable:
ENV PATH=/root/.local:$PATH

WORKDIR /opt/

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]
