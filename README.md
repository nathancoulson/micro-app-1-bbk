# micro-app-1-bbk
Microservice app_1 of web app for MSc Data Science project repo (microservice auto-scaling system)

# Description
Application summary as part of test microservice based web application (seen in 2019 N C Coulson paper: "Adaptive microservice scaling for elastic web applications")

App 1 is the simplest microservice. Like all the microservices, the root domain returns a hello world statement, what makes it unique is that all requests are sent from the NGINX reverse proxy server to App 1 first and then the request is routed to the next microservice specified in the url.

# Deployment
This github repo is linked to a DockerHub repo (https://cloud.docker.com/u/certainnathan/repository/docker/certainnathan/micro-app-1-bbk) which is referenced in the Swarm deployment YAML config file. Any accepted changes will be automatically incorporated into the latest Docker image used in the main application.
