FROM nginx:stable-alpine
EXPOSE 9090
ENV PYTHONUNBUFFERED=1
ENV PATH_IMAGES = "/usr/share/nginx/html"

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

WORKDIR /www/app
COPY ./requirements.txt /www/backend/requirements.txt
RUN pip3 install -r /www/backend/requirements.txt

COPY ./sources /www/app
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf



CMD sh -c "python3 /app/main.py & nginx -g 'daemon off;'"
