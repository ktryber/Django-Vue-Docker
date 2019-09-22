
# production stage
FROM nginx
EXPOSE 8080
COPY ./prod.conf /etc/nginx/nginx.conf

CMD ["nginx", "-g", "daemon off;"]