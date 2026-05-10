FROM node:20-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

# Commande pour le développement avec hot-reloading
CMD ["npm", "run", "dev"]
