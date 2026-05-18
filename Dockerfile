# start w a base image that already has pip installed
FROM python:3.13-slim 

# all future cmds run inside the /app folder (create it if dne)
WORKDIR /app

# copies config file into the container
COPY pyproject.toml /app/

# install dependencies
RUN pip install .

# copies the rest of the project files (i.e. main.py) into the container (after installing dependencies)
COPY . /app/

# app listens on point 8000
EXPOSE 8000

# cmd that runs when the container starts
# --host 0.0.0.0 means accept connections from outside the container
CMD ["fastapi", "dev", "--host", "0.0.0.0", "--port", "8000"]