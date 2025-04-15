# builds
FROM node:14 AS build

# work directory inside de container
WORKDIR /app

# copy dependencies
COPY package*.json ./
# executes the command to install dependencies
RUN npm install

# copy the rest of the application code
COPY . .

# builds the app
RUN npm run build

# builds web server image
FROM nginx:alpine

# copy build artifacts from the build stage to the nginx dir
COPY --from=build /app/build /usr/share/nginx/html

# expose port
EXPOSE 80

# execute nginx
CMD ["nginx", "-g", "daemon off;"]
