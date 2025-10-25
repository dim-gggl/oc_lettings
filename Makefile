# Image name (modifiable according to environment)
IMAGE_NAME=dgggl88/oc_lettings
TAG=latest

# Environment variables (modifiable at execution if needed)
ENV_FILE=.env
CONTAINER=oc_lettings_container
PORT=8000

# SQLite host file to bind-mount (must exist in repo root)
DB_FILE=oc-lettings-site.sqlite3
DB_HOST_PATH=$(shell pwd)/$(DB_FILE)

# Build local Docker image
build:
	docker build -t $(IMAGE_NAME):$(TAG) .

# Default run command
run: run-dev

# Ensure the SQLite file exists before running
db-check:
	@test -f "$(DB_HOST_PATH)" || (echo "ERROR: $(DB_FILE) not found at project root. Place your SQLite file to preserve data." >&2; exit 1)

# Run image locally in DEV (bind-mount the host SQLite file)
run-dev: build db-check
	docker run --rm \
		--name $(CONTAINER) \
		-e DJANGO_SECRET_KEY=$$(sed -n 's/^[[:space:]]*DJANGO_SECRET_KEY[[:space:]]*=[[:space:]]*//p' $(ENV_FILE) | tail -n 1) \
		-e ENV_MODE=dev \
		-p $(PORT):8000 \
		-v "$(DB_HOST_PATH):/app/oc-lettings-site.sqlite3" \
		$(IMAGE_NAME):$(TAG)

# Run image locally in PROD (bind-mount the host SQLite file)
run-prod: build db-check
	docker run --rm \
		--name $(CONTAINER) \
		-e DJANGO_SECRET_KEY=$$(sed -n 's/^[[:space:]]*DJANGO_SECRET_KEY[[:space:]]*=[[:space:]]*//p' $(ENV_FILE) | tail -n 1) \
		-e ENV_MODE=prod \
		-p $(PORT):8000 \
		-v "$(DB_HOST_PATH):/app/oc-lettings-site.sqlite3" \
		$(IMAGE_NAME):$(TAG)

# Pull image from Docker Hub then run local
pull-run: db-check
	docker pull $(IMAGE_NAME):$(TAG)
	docker run --rm \
		--name $(CONTAINER) \
		-e DJANGO_SECRET_KEY=$$(sed -n 's/^[[:space:]]*DJANGO_SECRET_KEY[[:space:]]*=[[:space:]]*//p' $(ENV_FILE) | tail -n 1) \
		-e ENV_MODE=dev \
		-p $(PORT):8000 \
		-v "$(DB_HOST_PATH):/app/oc-lettings-site.sqlite3" \
		$(IMAGE_NAME):$(TAG)

# Run tests with coverage locally (outside Docker)
test:
	coverage run -m pytest
	coverage report -m

# Push image to Docker Hub (multi-architecture)
push:
    # Ensure buildx builder exists (no-op if already present)
    docker buildx create --name oc_builder --use || true
    docker buildx inspect --bootstrap
    docker buildx build \
        --platform linux/amd64,linux/arm64 \
        -t $(IMAGE_NAME):$(TAG) \
        --push .


# Clean local image
clean:
	docker rmi $(IMAGE_NAME):$(TAG) || true
         