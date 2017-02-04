FROM ubuntu:16.04

# Set up to use apt-cacher-ng
RUN echo 'Acquire::HTTP::Proxy "http://172.17.0.1:3142";' >> /etc/apt/apt.conf.d/01proxy \
 && echo 'Acquire::HTTPS::Proxy "false";' >> /etc/apt/apt.conf.d/01proxy

RUN apt-get update \
 && apt-get install -y \
    git \
    python \
    python-pip \
    vim

RUN pip install --upgrade pip

RUN pip install \
    markdown \
    pelican

RUN apt-get update \
 && apt-get install -y \
    libssl-dev \
 && pip install \
    fabric \
    ghp-import

EXPOSE 8000
CMD bash
