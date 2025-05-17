FROM node:18

WORKDIR /app

# Copy dependency files first and install
COPY package*.json ./
RUN npm install

# Copy the rest of the Angular app
COPY . .

# Serve the app
CMD ["sh", "-c", "npx ng serve --host 0.0.0.0 --port ${FRONTEND_PORT:-4200}"]
