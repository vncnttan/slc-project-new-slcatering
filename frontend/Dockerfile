# Build image
FROM node:18 AS build

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . ./
RUN npm run build
RUN npm prune

# Getting the Environment Variables
ARG VITE_API_BASE_URL
ARG VITE_BACKEND_BASE_URL
ARG PUBLIC_FIREBASE_API_KEY
ARG PUBLIC_FIREBASE_AUTH_DOMAIN
ARG PUBLIC_FIREBASE_PROJECT_ID
ARG PUBLIC_FIREBASE_STORAGE_BUCKET
ARG PUBLIC_FIREBASE_MESSAGING_SENDER_ID
ARG PUBLIC_FIREBASE_APP_ID

# Production image
FROM node:18-alpine AS prod
COPY --from=build /app/build ./build
COPY --from=build /app/package.json .
RUN npm install --omit=dev

COPY ./static ./static

EXPOSE 3000
ENV HOST=0.0.0.0

CMD [ "node", "build/index.js" ]