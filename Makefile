# Image name (modifiable according to environment)
IMAGE_NAME=dgggl88/oc_lettings_site
TAG=latest

# Environment variables (modifiable at execution if needed)
ENV_FILE=.env
PORT=8000

# Build local Docker image
build:
	docker build -t $(IMAGE_NAME):$(TAG) .

# Run local built image
run:
	docker run --rm \
		-e DJANGO_SECRET_KEY=$$(grep DJANGO_SECRET_KEY $(ENV_FILE) | cut -d '=' -f2) \
		-e ALLOWED_HOSTS=localhost \
		-p $(PORT):8000 \
		$(IMAGE_NAME):$(TAG)

# Pull image from Docker Hub then run local
pull-run:
	docker pull $(IMAGE_NAME):$(TAG)
	docker run --rm \
		-e DJANGO_SECRET_KEY=$$(grep DJANGO_SECRET_KEY $(ENV_FILE) | cut -d '=' -f2) \
		-e ALLOWED_HOSTS=localhost \
		-p $(PORT):8000 \
		$(IMAGE_NAME):$(TAG)

# Run tests with coverage locally (outside Docker)
test:
	coverage run -m pytest
	coverage report -m

# Push image to Docker Hub
push:
	docker buildx build --platform linux/amd64 -t $(IMAGE_NAME):$(TAG) --push .


# Clean local image
clean:
	docker rmi $(IMAGE_NAME):$(TAG) || true
