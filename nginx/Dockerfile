FROM node:alpine as builder
WORKDIR /app/

COPY frontend/package.json frontend/package-lock.json /app/
RUN npm install
COPY frontend /app/
RUN npm run build

# production stage
FROM nginx
EXPOSE 8080
COPY ./nginx/prod.conf /etc/nginx/nginx.conf
COPY --from=builder /app/dist /dist/

CMD ["nginx", "-g", "daemon off;"]