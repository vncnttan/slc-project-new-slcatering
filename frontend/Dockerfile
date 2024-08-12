# Build image
FROM node:18 AS build

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . ./
RUN npm run build
RUN npm prune

# Production image
FROM node:18-alpine AS prod
COPY --from=build /app/build ./build
COPY --from=build /app/package.json .
RUN npm install --omit=dev

COPY ./static ./static

FROM nginx:1.19-alpine
COPY --from=build /app/build /usr/share/nginx/html