FROM codeiai/auto-learner-base:2.1.2
WORKDIR /app
COPY models /app/models
COPY __main__.py /app/__main__.py
RUN mkdir /app/training_data
RUN mkdir /app/vectors
ENTRYPOINT ["python", "/app/__main__.py"]