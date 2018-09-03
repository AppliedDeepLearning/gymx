FROM python:3.7-slim as base

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python-numpy python-dev cmake zlib1g-dev libjpeg-dev xvfb libav-tools xorg-dev python-opengl libboost-all-dev libsdl2-dev swig \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv /venv && \
    /venv/bin/pip install gym gym[all] gymx

FROM python:3.7-slim

COPY --from=base /venv /venv

EXPOSE 54321

CMD ["/venv/bin/python", "-m", "gymx"]
