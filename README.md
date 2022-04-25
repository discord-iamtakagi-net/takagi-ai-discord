# takagi-ai-discord

## Install
`docker-compose.yml`
```yml
version: '3.8'

services:
  app:
    image: ghcr.io/discord-iamtakagi-net/takagi-ai-discord:latest
    environment:
      TOKEN: xxx
    restart: unless-stopped
```

## LICENSE
MIT License.
