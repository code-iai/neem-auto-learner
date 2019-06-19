# NEEM Auto Learner

## Prerequisites

1. A collection of NEEMs stored on your local computer or accessible via network.
2. Docker installed on your computer with support for Linux containers.

## How to use it
1. Create a volume for storing the trained models via: 
    ```bash
   docker volume create learning-models
   ```
2. To learn models from your NEEMs for the first time just execute the following command: 
   ```bash
   docker run --name auto-learner --mount source=learning-models,target=/app/models --mount type=bind,source=<PATH_TO_YOUR_NARRATIVES>,target=/app/narratives codeiai/auto-learner:1.0.1
   ```   
3. If you started the container once with the "docker run" command, please use the following command for future usage: 
    ```bash
    docker start auto-learner --attach
    ```    



