# UCU Software Architecture Lab Assignments

## Lab 4 Protocol

### Launch Kafka

To launch Kafka, we need to download the archive, start Zookeeper first, then Kafka, and finally create a topic:
```
./bin/zookeeper-server-start.sh config/zookeeper.properties
./bin/kafka-server-start.sh config/server.properties
./bin/kafka-topics.sh --zookeeper 127.0.0.1:2181 --topic messages --create --partitions 3 --replication-factor 1
```

After that, three logging service and two messages services have been launched.

To start messages service, the following command needs to be used:
```
uvicorn api:app --workers 1 --reload --port 5030
```

### Write msg1-msg10

Facade service logs:
![img](https://user-images.githubusercontent.com/25267308/173257074-8ca79738-2333-4275-831e-83b9a57aede7.png)

### Logging Logs

Logging 1 logs:
![img](https://user-images.githubusercontent.com/25267308/173257134-dc133b0e-4dcb-4ce2-9e9b-452d24003868.png)

Logging 2 logs:
![img](https://user-images.githubusercontent.com/25267308/173257143-4a253c6f-5e87-4a60-80b4-f059b481ed41.png)

Logging 3 logs:
![img](https://user-images.githubusercontent.com/25267308/173257146-758185c1-592c-46fc-8b8b-58edfff948b0.png)

### Messages Logs

Messages 1 logs:
![img](https://user-images.githubusercontent.com/25267308/173257239-14350383-2537-4511-b142-e963ca819e3d.png)

Logging 2 logs:
![img](https://user-images.githubusercontent.com/25267308/173257227-4d98ef20-e5b3-4f84-8058-d06baa3e09b1.png)

### Get Data

GET request to the Facade service returns different responses based on which Messages instance is called.

Response 1:
![img](https://user-images.githubusercontent.com/25267308/173257447-c2d79337-e2d9-497e-bd87-5c89c498361c.png)

Response 2
![img](https://user-images.githubusercontent.com/25267308/173257429-8c880b5d-d6b3-4f3c-af72-69de48af268f.png)

## Lab 3 Protocol

### Launch three logging-services and write msg1-msg10 through facade-service

![1](https://user-images.githubusercontent.com/25267308/172979982-c7c82048-dce7-402c-930e-2c70a513b72f.png)

### Show logging-service logs

Instance 1 logs:
![1](https://user-images.githubusercontent.com/25267308/172980751-a5dc1b74-0ea2-4bf4-8b3d-f0d690becb44.png)
Instance 2 logs:
![2](https://user-images.githubusercontent.com/25267308/172980773-7e721c5a-7a16-4e86-85cd-9fa6d9edbf76.png)
Instance 3 logs:
![3](https://user-images.githubusercontent.com/25267308/172980785-87bfac6f-67d7-4d9d-aba1-a3bbe5401c9f.png)

### Read through facade-service

![4](https://user-images.githubusercontent.com/25267308/172981456-eaaf5c32-9ca9-4110-adcb-06d1be59e8f4.png)

### Shut down two logging-services instances.

Two out of three times we get an error:
![4](https://user-images.githubusercontent.com/25267308/172981576-8ec19cb1-44dd-49cd-a4f3-21caced986fe.png)

But it is also possible to read our messages:
![5](https://user-images.githubusercontent.com/25267308/172981590-e3965da0-ea50-432e-8add-6b7502c42404.png)

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
