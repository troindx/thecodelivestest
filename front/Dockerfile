FROM nginx:alpine
RUN rm -rf /usr/share/nginx/html/*
COPY ./ops/nginx.conf /etc/nginx/conf.d/default.conf
# Copy the built Angular files from the build stage
COPY ./www /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Command to run Nginx
CMD ["nginx", "-g", "daemon off;"]
