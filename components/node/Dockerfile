# Use the standard node LTS image
FROM node:23.11.0 AS base
RUN mkdir -p /tmp/.cache/npm
RUN chown -R node:node /tmp/.cache/npm

# enable corepack
ENV COREPACK_ENABLE_DOWNLOAD_PROMPT=0
RUN corepack enable

# Install npm v3
RUN corepack prepare npm@latest
RUN npm set version 3.x

# Continue with the development stage
FROM base AS dev
# Update the package list and install dependencies with apt-get
RUN apt-get update && apt-get install -y python3 openssl ca-certificates
# Install build dependencies
RUN apt-get install -y build-essential

# Building stage
FROM base AS builder

WORKDIR /app

# GitHub Token als Build-Argument übergeben
ARG GITHUB_TOKEN
ARG VITE_BACKEND_API_URL
ENV VITE_BACKEND_API_URL=$VITE_BACKEND_API_URL
ARG VITE_BASE_URL
ENV VITE_BASE_URL=$VITE_BASE_URL

# Füge temporäres .npmrc für private Packages hinzu
RUN echo "@your-org:registry=https://npm.pkg.github.com/" > .npmrc \
 && echo "//npm.pkg.github.com/:_authToken=${GITHUB_TOKEN}" >> .npmrc

# Installiere Dependencies
COPY ./components/web-app/package*.json ./
RUN npm install

# Kopiere Rest der App
COPY ./components/web-app .

# Baue das Projekt
RUN npm run build

# Production stage
FROM nginx:alpine AS production

COPY --from=builder /app/dist /usr/share/nginx/html
COPY ./components/node/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
