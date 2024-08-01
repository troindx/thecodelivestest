# Cat Navigator
Cat Navitagor is a small test that allows for an interface to perform CRUD operations over a Cat registry, with their information as well as information on their vaccines.

The idea behind this project is to act as a showcase of how I develop as a full stack engineer. In this repository you will find
- A Backend developed in python, using fastAPI and a mongo database to store information.
- A frontend developed in ionic framework + Angular, that allows for deployment of electron apps, android + iOS apps and web applications using angular's powerful PWA elements
- A docker container to expose any of the services through your own network , and to keep each of the services containerized
- A github actions workflow that launches after every push to main branch, that ensures stability of the system and preventing regressions.

Start by cloning this repository and explore the work to see how I develop full stack services. You will need nodejs at least v20 and python 3.12+ installed in your system for this environment to work.

## Preparation after cloning.
### Backend
Preparation of Backend
````
cp .env.dist /back/.env
cd ./back
pip install -r requirements.txt
````
### Frontend
Preparation of Frontend
````
cd ./front
npm install -g @angular/cli
npm install -g @ionic/cli
npm i
ionic build
````
### Backend Integration Testing
Integration tests are provided. In order to execute them, in back folder, you can run `docker compose -f db.docker-compose.yaml up -d` from CLI. Once database service is up and running, execute `pytest` to execute tests

### Backend Development mode
Launching the command `uvicorn app.main:app --reload` will launch the application with hot reloading of modules. The Database service needs to be up and running.

## Frontend e2e Testing
In order for e2e tests from frontend, backend must be up and running. Then, in front folder,  execute `npm run e2e`.

### Frontend Development mode
In front folder, executing the command `ionic serve` will launch the application on a small testing service in port 8100.
Execute `ionic build --prod` to build for production and release.
You can also run `npm run watch`for the compiler to recompile everything into the www folder on changes. This can be useful if you are using docker to expose your service

## Docker
Services can be started by launching `docker compose up` in root folder. This will deploy the backend service, a small nginx service containing the frontend application built in /www file, and the database service, all connected in a network with adecuate ports exposed.  
- This docker is made for development purposes, but it could be used for production if what is built into the front/www folder is built with the --prod tag when using ionic build.
- The frontend service only uses the www folder (mounted), so changes made into the build are straightly published.

## ENV files for frontend and backend
Make sure that the variables and env are properly set in .env.dist for the backend. and in /front/src/environments for the frontend. When testing with docker, remember to use the docker strings assigned in the docker compose file. If you are testing each service independently maybe you need to alter the strings to localhost when not using docker containers