# UCU Software Architecture Lab Assignments

## Lab 2 Protocol

### Download and set up Hazelcast

Hazelcast has been used via Docker. A network needed to be created. The following commands were used:
```
docker run  -e JAVA_OPTS="-Dhazelcast.config=/opt/hazelcast/config_ext/hazelcast.yaml" -v /Users/dmytrolopushanskyy/ucu/architecture/microservices-interaction:/opt/hazelcast/config_ext -it --network hazelcast-network --rm -e HZ_CLUSTERNAME=hz-cluster -p 5701:5701 hazelcast/hazelcast
docker run --network hazelcast-network -p 8080:8080 hazelcast/management-center
```

### Launch 3 HZ instances

Here's the view of the cluster from the managament center:
![cluster](https://user-images.githubusercontent.com/25267308/172974363-07e148fc-1ca8-4e8b-b43e-60bcc3c17deb.png)

### Distributed Map

![1](https://user-images.githubusercontent.com/25267308/172973551-ba2da114-17e3-469f-9f43-00d7650c6408.png)
![2](https://user-images.githubusercontent.com/25267308/172973550-44b27c8b-2b28-4d48-8023-ea22b0a083d0.png)
![3](https://user-images.githubusercontent.com/25267308/172973548-cecab8b0-ff96-498d-b9a3-6fc02f786e44.png)

### Distributed Map with locks

The first run is racy. It is the fastest but we can clearly see a race. The last value 1218 whereas it should be 3000.
![1](https://user-images.githubusercontent.com/25267308/172974122-0e5bf98e-f610-4e3b-a45e-8c6857e13491.png)


The second run (pessimistic) is not racy. The last value is correct, but it takes 21 seconds to run, which is qute long.
![3](https://user-images.githubusercontent.com/25267308/172974124-2af842ad-313b-4e9c-b671-b789944c4250.png)

THe last run (optimistic) is also not racy. The value is correct and it is twice as fast as the previous one.
![2](https://user-images.githubusercontent.com/25267308/172974126-8a4891f5-63b2-4593-a89e-0bdeb540831b.png)


### Bounded Queue

To create a bounded queue, I needed to update Hazelcast configurations. The YAML file is provided.

#### One node writes, two others read.
The read happens faster than write so the values are retrieved from the queue almost immediately.

#### No reading, queue is full.
The writing stops and waits until a value is taken out.

#### How values are read if there are many readers?
The values are read randomly by either reader, there is no rule which reader gets which value.


## Lab 1 Protocol

### POST request to Facade / with message payload
![image1](https://user-images.githubusercontent.com/25267308/158078093-94e88045-13c5-48c1-8dce-6dde2f54d92f.png)
![image2](https://user-images.githubusercontent.com/25267308/158078091-e40c7616-a314-4727-ad14-ff71d4af499e.png)

### GET request to Facade /
![image3](https://user-images.githubusercontent.com/25267308/158078089-14c0c9c1-3da1-41d4-beed-0da57f7c9a23.png)

### Console output of the logger
![image4](https://user-images.githubusercontent.com/25267308/158078086-4b4c5125-2de6-4b0a-9bda-49fd90ba037e.png)
