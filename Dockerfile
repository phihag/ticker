FROM python:3.6

WORKDIR /sclive
ADD requirements.txt ./
RUN pip3 install -r requirements.txt

EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000

# Run with  docker build -t sclive . && docker run -v $(pwd):/sclive --rm -it -p 8001:8000 sclive
