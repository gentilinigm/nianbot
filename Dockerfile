FROM python:3.10-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install python3-dev libpq-dev build-essential -y

RUN pip install poetry

# Install project dependencies
WORKDIR /bot
COPY pyproject.toml poetry.lock ./
RUN poetry install --without dev

# Copy the source code in last to optimize rebuilding the image
COPY . .

ENTRYPOINT ["poetry"]
CMD ["run", "python", "-m", "bot"]
