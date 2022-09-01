FROM zenika/alpine-chrome:with-node

WORKDIR /usr/app

USER root

RUN apk update && apk add git \
    # && apk add build-essential \
    && apk add curl \
    && apk add python3 py3-pip py3-setuptools
    # && apk add --no-install-recommends \
    # python3 python3-pip python3-setuptools

COPY requirements.txt .

RUN pip3 install \
    --no-cache-dir \
    --no-warn-script-location \
    -r requirements.txt

RUN rm requirements.txt

# RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -
# RUN apk update && apk add -y nodejs
RUN npm install --production single-file-cli
# RUN npm install selenium-webdriver

# RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
# ENV PATH="$PATH:/root/.cargo/bin"
# RUN cargo install geckodriver
# RUN apk add -y firefox
# ENV PUPPETEER_PRODUCT="firefox"
# RUN npm i puppeteer

COPY webserver.py .

WORKDIR /usr/app/out

ENTRYPOINT ["/usr/app/node_modules/single-file/cli/single-file", "--browser-executable-path=/usr/bin/chromium-browser", "--browser-args='[\"--no-sandbox\"]'", "--dump-content"]
