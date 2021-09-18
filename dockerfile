FROM python:3.9-alpine3.13

RUN mkdir /app

WORKDIR /app

COPY ./* /app/

RUN pip install -r requirements.txt \
&& adduser -DH user -G user

USER user

CMD [ "uvicorn", "main:app", "--host=0.0.0.0", "--port=${PORT:-5000}" ]