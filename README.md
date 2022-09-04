# Design System of High-Scale Product Application(POC)

Given a real-world problem to scale the applications to read and save products inside a controlled environment I decided to create a POC (Prove of Concepts) about the approach to delivering a good performance and high availability design.

This application backend is responsible by save and read products over the HTTP protocol using a RESTFull approach, the user makes a read or write request, the service does processing, stores data, then returns the results.

The service needs to envolve from serving a small amount of requests to millions of requests.

## How use
Its a POC that you can test it in your development enviroment.
To init the application you need to have a docker and docker-compose installed in your computer.

```
docker-compose up -d
```

With the all containers running you can call the request to use the application:

### Create a Product
To create a new product execute a POST in our API:

### Schema

```json
{
	description: string,
	value: float
}
```
Execute the below command to create with *201* status:

```
curl -X POST -H "Content-Type: application/json" -d '{ "description": "Prod", "value": 10.0}' http://localhost/products
```

### Get all Products
Route only available to get all:
```
curl -X GET http://localhost/products
```

Returns 200 status:

```json
{
  "products": [
    {
      "description": "Awesome Product",
      "id": 6,
      "tax": 12.5,
      "value": 12.5
    }
  ]
}
```

##  High Level Design


* **Client** using a brower, mobile, or any device to access to application
* **DNS** translate a domain name to an IP address
* **Web Server** is a proxy that centralizes internal services and provides unifield inrterfaces
* The Application Servers **Product_Write** and **Product_Read** handling the requets, with this separation we can scale both layers independently, the  **Product_Write** is reponsable for insert new data while  **Product_Read**  read all data from storage.
* **Tax** is a small microservice responsable by calculate all tax to some product, as a internal service that use gRPC  to communicate with others.
* The database choised was th Postgres and I'm using  Redis as cache and queue broker
* **Comments_Write_Async** is a bach service that is responsable by create asynchronously Comments 
