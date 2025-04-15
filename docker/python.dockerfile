# uses image
FROM python:3.9-slim

# indicates work directory inside the container
WORKDIR /app
# copies requirements.txt to the container
COPY requirements.txt /app/

# updates pip and installs dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# copies the rest of the app code
COPY . /app

# expose port 80
EXPOSE 80

# defines the command to run the app
CMD ["python", "app.py"]
