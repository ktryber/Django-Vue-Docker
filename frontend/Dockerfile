FROM node:alpine

WORKDIR '/app'

COPY ./package.json ./

RUN npm install

COPY . .

CMD ["npm", "run", "build"]

FROM nginx
EXPOSE 8080
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/build /usr/share/nginx/html