FROM node:18-alpine
WORKDIR /usr/src/app


# Install dependencies
COPY package*.json ./
RUN npm ci --only=production


# Copy source
COPY . .


# If you use environment variables for DB_URL, PORT, etc., they should be provided at runtime
ENV NODE_ENV=production
EXPOSE 3000
CMD ["node", "server.js"] # adjust to your app entry point (app.js/index.js)