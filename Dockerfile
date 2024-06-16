# FROM node:14
# WORKDIR /app
# COPY . .
# RUN npm install
# CMD ["npm", "start"]
FROM nextcloud:stable-apache
RUN echo "Custom Dockerfile for Nextcloud"
