FROM python:3.9-alpine3.13

RUN mkdir /app

WORKDIR /app

COPY ./* /app/

RUN addgroup user && adduser -D user -G user
USER user
RUN pip install -r requirements.txt

CMD [ "uvicorn", "main:app", "--host=0.0.0.0", "--port=${PORT:-5000}" ]