# Design System of High-Scale Product Application(POC)

Given a real-world problem to scale the applications to read and save products inside a controlled environment I decided to create a POC (Prove of Concepts) about the approach to delivering a good performance and high availability design.

This application backend is responsible by save and read products over the HTTP protocol using a RESTFull approach, the user makes a read or write request, the service does processing, stores data, then returns the results.

The service needs to envolve from serving a small amount of requests to millions of requests.

## How use
Its a POC that you can test it in your development enviroment.
To init the application you need to have a docker and docker-compose installed in your computer.

```console
docker-compose up -d
```

With the all containers running you can call the request to use the application:

### Create a Product
To create a new product execute a POST in our API:

**Schema**

```json
{
  "description": "string",
  "value": "float"
}
```
Execute the below command to create with *201* status:

```console
curl -X POST -H "Content-Type: application/json" -d '{ "description": "Awesome Product", "value": 10.0}' http://localhost/products
```

### Get all Products
Route only available to get all:
```console
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
### Create a Comment
To create a new comment to product execute a POST in our API:

****Schema****

```json
{
  "comment": "string",
  "author": "string",
  "id_product": "int"
}
```
Execute the below command to create with *201* status:

```console
curl -X POST -H "Content-Type: application/json" -d '{ "id_product": 1, "comment": "Hello!!!", "author": "Hattori" } ' http://localhost/comments
```

##  High Level Design

![image](https://user-images.githubusercontent.com/2198233/188327644-87d47124-5e28-4a1e-b097-a5eb3d804473.png)


* **Client** using a brower, mobile, or any device to access to application
* **DNS** translate a domain name to an IP address
* **Web Server** is a proxy that centralizes internal services and provides unifield inrterfaces
* The Application Servers **Product_Write** and **Product_Read** handling the requets, with this separation we can scale both layers independently, the  **Product_Write** is reponsable for insert new data while  **Product_Read**  read all data from storage.
* **Tax** is a small microservice responsable by calculate all tax to some product, as a internal service that use over gRPC protocol to communicate with others.
* The database choised was the **Postgres** and *Redis* as cache the Comments_Worker uses as queue broker too, in production enviroment it's not a good approach.
* **Comments_Write_Async** is a bach service that is responsable by create asynchronously Comments, the client send request to async API than pubisher messase to Redis broker, the **Comments_Worker** receive message and process to save to No-SQL database(MongoDB) 
