FROM python:3.10-alpine
WORKDIR /Users/roxyd\OneDrive\Documents\GitHub\proj2\Group-Project-11
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
ENV NAME World
CMD ["python", "./cli.py"]