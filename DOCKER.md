# Docker Build Instructions

## Using Docker to Run the Application

### Prerequisites
- Docker Desktop installed (https://www.docker.com/products/docker-desktop)
- Docker running in the background

### Option 1: Using Docker (Single Container)

1. Build the image:
```bash
docker build -t malayalam-story-creator .
```

2. Run the container:
```bash
docker run -p 8000:8000 \
  -e GEMINI_API_KEY=your-api-key \
  -e AI_API_PROVIDER=gemini \
  malayalam-story-creator
```

3. Open browser: http://localhost:8000

### Option 2: Using Docker Compose (Recommended)

1. Create `.env` file with your API keys:
```
GEMINI_API_KEY=your-api-key
AI_API_PROVIDER=gemini
```

2. Start services:
```bash
docker-compose up
```

3. In another terminal, run migrations:
```bash
docker-compose exec web python manage.py migrate
```

4. Create superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

5. Open browser: http://localhost:8000

6. Stop services:
```bash
docker-compose down
```

### Useful Docker Commands

```bash
# View running containers
docker ps

# View logs
docker logs container-id

# Execute command in container
docker exec -it container-id python manage.py shell

# Stop container
docker stop container-id

# Remove container
docker rm container-id
```

### Troubleshooting

**Port already in use:**
```bash
docker run -p 8001:8000 malayalam-story-creator
# Then access: http://localhost:8001
```

**Container not starting:**
```bash
docker logs container-id
# Check the error message
```

**Permission denied:**
On Linux, you may need:
```bash
sudo docker build -t malayalam-story-creator .
```
