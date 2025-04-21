# Roter Kompass

## Setup

Make sure to install the dependencies:
```
just
docker
docker-compose
```

```bash
# docker-compose needs to be running on your machine
just install
```

Create .env of the Project
```
NAME={z.B. roter-kompass}
PORT_WEB_APP={z.B. 5173}
GITHUB_TOKEN={github token for solid-ui package}

PORT_BACKEND={z.B. 8080}

PORT_PG_DB={z.B. 5432}
PG_ADMIN={z.B. dev}
PG_PASSWORD={z.B. dev}
PG_DB_NAME={z.B. dev}
```

Create .env of the Web-App
```
VITE_BACKEND_API_URL={z.B. http://localhost:8080/api}
VITE_BASE_URL={z.B. http://localhost:5173}
```

Create .npmrc for the Web-App
```
//npm.pkg.github.com/:_authToken=${GITHUB_TOKEN}
@linkebonn:registry=https://npm.pkg.github.com
```

Create .env of the Backend
```
PORT={z.B. 5000}
DATABASE_URL={z.B. postgresql://dev:dev@host.docker.internal:5432/dev}
```

## Development

The environment starts the web-app.

```bash
# npm
just start
```