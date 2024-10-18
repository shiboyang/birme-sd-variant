FROM nginx:1.24.0-alpine

COPY --chmod=0777 . /usr/share/nginx/html/

COPY nginx/default.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]