# UCU Software Architecture Lab Assignments

## Lab 2 Protocol

### Download and set up Hazelcast

Hazelcast has been used via Docker. A network needed to be created. The following commands were used:
```
docker run  -e JAVA_OPTS="-Dhazelcast.config=/opt/hazelcast/config_ext/hazelcast.yaml" -v /Users/dmytrolopushanskyy/ucu/architecture/microservices-interaction:/opt/hazelcast/config_ext -it --network hazelcast-network --rm -e HZ_CLUSTERNAME=hz-cluster -p 5701:5701 hazelcast/hazelcast
docker run --network hazelcast-network -p 8080:8080 hazelcast/management-center
```



## Lab 1 Protocol

### POST request to Facade / with message payload
![image1](https://user-images.githubusercontent.com/25267308/158078093-94e88045-13c5-48c1-8dce-6dde2f54d92f.png)
![image2](https://user-images.githubusercontent.com/25267308/158078091-e40c7616-a314-4727-ad14-ff71d4af499e.png)

### GET request to Facade /
![image3](https://user-images.githubusercontent.com/25267308/158078089-14c0c9c1-3da1-41d4-beed-0da57f7c9a23.png)

### Console output of the logger
![image4](https://user-images.githubusercontent.com/25267308/158078086-4b4c5125-2de6-4b0a-9bda-49fd90ba037e.png)
