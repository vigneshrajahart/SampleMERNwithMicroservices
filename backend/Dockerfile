FROM node:18-alpine
WORKDIR /usr/src/app

# Install dependencies
COPY package*.json ./
RUN npm install --only=production

# Copy source code
COPY . .

EXPOSE 3000
CMD ["node", "server.js"]  # change if your entry file is different