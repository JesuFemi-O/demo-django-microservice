# MicroServices With Django on Kubernetes

this is a demo app with two microservices:

- a minimal authentication/ single sign on service

- an inventory/product service

the end goal was to just learn how to deploy microservices on kubernetes using istio and kustomize and this is in no way production ready...

## How to run

you should first create a .env file in both auth-service/src and product_service/src and add:

```
    SECRET_KEY=your-secret-key
```

in either service folder...

- build image

```
     docker build -t username/app_name .

```

- run container with image:

```
    docker run -p 8000:8000 --name container_name username/app_name

```

### NB:

- you may want to expose both containers on different ports

  e.g expose auth service on 8000:

```
    docker run -p 8000:8000 --name auth_service username/app_name
```

- expose the product/inventory service on port 8001:

```
    docker run -p 8001:8000 --name auth_service username/app_name
```

- you can now visit the auth service to create a user and login on http://127.0.0.1:8000/

- you can then use the access token from the aut service to expolre the product service on http://127.0.0.1:8001/

## Valid tokens

- a valid token should have a Bearer prefix e.g Bearer xxx-xxx-xxxx

where xxx-xxx-xxxx is the token retrieved from the SSO service.
