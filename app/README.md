## Instruction how to deploy your web service in docker container
Go to the working direcory with Dockerfile.

[Build](https://docs.docker.com/engine/reference/commandline/build/) Docker image from a Dockerfile:
```sh
docker build -t <image_name>
```
[Run](https://docs.docker.com/language/nodejs/run-containers/) your image as a container:
```sh
docker run -p 5000:5000 <image_name>
```
Inspired by [this](https://docs.docker.com/language/python/build-images/) article.
