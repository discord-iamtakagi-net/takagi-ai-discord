# takagi.AI.discord

## Install
`docker-compose.yml`
```yml
version: '3.8'

services:
  app:
    image: ghcr.io/iamtakagi/takagi.ai.discord
    environment:
      TOKEN: xxx
    restart: unless-stopped
```

## LICENSE
MIT License.