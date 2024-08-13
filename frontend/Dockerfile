# Build image
FROM node:18 AS build

WORKDIR /app

RUN cat .env

COPY package.json ./
COPY package-lock.json ./
COPY .env ./.env
RUN npm install
COPY . ./
RUN npm run check
RUN npm run build
RUN npm prune

# Production image
FROM node:18-alpine AS prod
COPY --from=build /app/build ./build
COPY --from=build /app/package.json .
RUN npm install --omit=dev

COPY ./static ./static

EXPOSE 3000
ENV HOST=0.0.0.0

CMD [ "node", "build/index.js" ]