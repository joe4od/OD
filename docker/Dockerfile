FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV TZ=Asia/Taipei

# Install basic tools: vi (vim), git, build tools, tzdata and libs needed for pycurl/pandas
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        tzdata \
        vim \
        git \
        ca-certificates \
        build-essential \
        gcc \
        curl \
        libcurl4-openssl-dev \
        libssl-dev \
        libffi-dev \
        pkg-config \
        python3-dev \
        procps \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && rm -rf /var/lib/apt/lists/*

# Copy helper scripts into image
COPY install_deps.sh /usr/local/bin/install_deps.sh
COPY detect_deps.py /usr/local/bin/detect_deps.py
RUN chmod +x /usr/local/bin/install_deps.sh /usr/local/bin/detect_deps.py

WORKDIR /workspace

# Default entry: run dependency installer (which inspects mounted /workspace) then drop to a shell
ENTRYPOINT ["bash", "-lc", "/usr/local/bin/install_deps.sh && exec bash"]
