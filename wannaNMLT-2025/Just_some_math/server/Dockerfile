FROM ubuntu:22.04

RUN apt-get update -q \
    && apt-get install -q -y --no-install-recommends \
        python3 \
        python3-pip \
        socat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install pycryptodome

RUN useradd -m math

WORKDIR /home/math

COPY chall.py .
COPY flag.txt .

RUN chown -R root:math /home/math \
    && chmod -R 750 /home/math \
    && chmod 550 chall.py \
    && chmod 440 flag.txt

USER math

CMD socat -T 60 -d -d TCP-LISTEN:3636,reuseaddr,fork EXEC:'python3 -u chall.py'