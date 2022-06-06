# This file defines the Docker container that will contain the Flask app.

# From the source image
FROM python:3.6-slim


# Set the default working directory
WORKDIR /docker-flask-model/

# Copy requirements.txt outside the container
# to /app/ inside the container
COPY requirements.txt /docker-flask-model/

# Install required packages
RUN pip install -r ./requirements.txt

# Copy app.py and__init__.py outside the container
# to /app/ inside the container
COPY app.py /docker-flask-model/

# Copy model.pkl outside the container
# to /app/ inside the container
COPY model_perc.pkl /docker-flask-model/

# Expose the container's port 3333
EXPOSE 5001

# When the container starts, run this
ENTRYPOINT python ./app.py