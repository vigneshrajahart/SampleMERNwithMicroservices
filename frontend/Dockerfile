# Stage 1: build React app
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci --production=false
COPY . ./
RUN npm run build


# Stage 2: serve with nginx
FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf # optional: custom config
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]