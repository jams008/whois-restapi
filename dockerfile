FROM python:3.9-alpine3.13

RUN mkdir /app

WORKDIR /app

COPY ./* /app/

RUN addgroup user && adduser -s /bin/sh -D user -G user
USER user
RUN mkdir -p /home/user/.local/bin && pip install -r requirements.txt

EXPOSE 5000

CMD ["/home/user/.local/bin/uvicorn", "main:app", "--host=0.0.0.0", "--port=5000"]