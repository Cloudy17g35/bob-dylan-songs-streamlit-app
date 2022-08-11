FROM python:3.8

WORKDIR /api

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN [ "python3", "-c", "import nltk; nltk.download('stopwords', download_dir='/usr/local/nltk_data')" ]

COPY . .

RUN chmod +x run.sh

CMD ["./run.sh"]