FROM node:alpine

WORKDIR '/app'

COPY ./package.json ./

RUN npm install

COPY . .

CMD ["npm", "run", "build"]

FROM nginx
EXPOSE 8080
COPY ./nginx/prod.conf /etc/nginx/nginx.conf
COPY --from=builder /app/build /usr/share/nginx/html