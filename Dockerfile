FROM nginx:stable-alpine
EXPOSE 9090
ENV PYTHONUNBUFFERED=1

RUN apk update \
    && apk add --virtual build-deps gcc python3 python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg
RUN ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

WORKDIR /app
COPY ./sources /app

ENV PATH_IMAGES="/var/www/images"
RUN mkdir -p $PATH_IMAGES
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf

#CMD nginx -g 'daemon off;'
CMD sh -c "python3 /app/main.py & nginx -g 'daemon off;'"
