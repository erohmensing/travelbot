FROM rasa/rasa-sdk:1.7.0

WORKDIR /app

COPY ./actions.py /app/actions.py

CMD ["start"]
