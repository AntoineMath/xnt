FROM python:3.11.2-alpine
WORKDIR /xnt
ENV FLASK_RUN_HOST=0.0.0.0 \
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt /xnt
RUN pip3 install -r requirements.txt
EXPOSE 5001
COPY . .
CMD ["python3","-m", "flask", "--app", "xnt", "run", "--host=0.0.0.0", "-p", "5001"]
