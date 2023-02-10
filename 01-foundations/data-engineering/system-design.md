# System Design

> Design the architecture, components and interfaces for big data systems

## How to Approach

- Scope the problem
  - Don’t make assumptions.
  - Ask clarifying questions to understand the constraints and use cases.
  - Steps
    - Requirements clarifications
    - System interface definition
- Sketch up an abstract design
  - Building blocks of the system
  - Relationships between them
  - Steps
    - Back-of-the-envelope estimation
    - Defining data model
    - High-level design
- Identify and address the bottlenecks
  - Use the fundamental principles of scalable system design
  - Steps
    - Detailed design
    - Identifying and resolving bottlenecks

## Distributed System Design Basics

### Key Characteristics of Distributed Systems

**Scalability**
- The capability of a system to grow and manage increased demand.
- A system that can continuously evolve to support growing amount of work is scalable.
- Horizontal scaling: by adding more servers into the pool of resources.
- Vertical scaling: by adding more resource (CPU, RAM, storage, etc) to an existing server. This approach comes with downtime and an upper limit.

**Reliability**
- Reliability is the probability that a system will fail in a given period.
- A distributed system is reliable if it keeps delivering its service even when one or multiple components fail.
- Reliability is achieved through redundancy of components and data (remove every single point of failure).

**Availability**
- Availability is the time a system remains operational to perform its required function in a specific period.
- Measured by the percentage of time that a system remains operational under normal conditions.
- A reliable system is available.
- An available system is not necessarily reliable.
  - A system with a security hole is available when there is no security attack.

**Efficiency**
- Latency: response time, the delay to obtain the first piece of data.
- Bandwidth: throughput, amount of data delivered in a given time.

**Serviceability / Manageability**
- Easiness to operate and maintain the system.
- Simplicity and spend with which a system can be repaired or maintained.

### Load Balancing (LB)

Help scale horizontally across an ever-increasing number of servers.

**LB locations**
- Between user and web server
- Between web servers and an internal platform layer (application servers, cache servers)
- Between internal platform layer and database

**Algorithms**
- Least connection
- Least response time
- Least bandwidth
- Round robin
- Weighted round robin
- IP hash

**Implementation**
- Smart clients
- Hardware load balancers
- Software load balancers

### Caching

- Take advantage of the locality of reference principle: recently requested data is likely to be requested again.
- Exist at all levels in architecture, but often found at the level nearest to the front end.

**Application server cache**
- Cache placed on a request layer node.
- When a request layer node is expanded to many nodes
  - Load balancer randomly distributes requests across the nodes.
  - The same request can go to different nodes.
  - Increase cache misses.
  - Solutions:
    - Global caches
    - Distributed caches

**Distributed cache**
- Each request layer node owns part of the cached data.
- Entire cache is divided up using a consistent hashing function.
- Pro
  - Cache space can be increased easily by adding more nodes to the request pool.
- Con
  - A missing node leads to cache lost.

**Global cache**
- A server or file store that is faster than original store, and accessible by all request layer nodes.
- Two common forms
  - Cache server handles cache miss.
    - Used by most applications.
  - Request nodes handle cache miss.
    - Have a large percentage of the hot data set in the cache.
    - An architecture where the files stored in the cache are static and shouldn’t be evicted.
    - The application logic understands the eviction strategy or hot spots better than the cache

**Content distributed network (CDN)**
- For sites serving large amounts of static media.
- Process
  - A request first asks the CDN for a piece of static media.
  - CDN serves that content if it has it locally available.
  - If content isn’t available, CDN will query back-end servers for the file, cache it locally and serve it to the requesting user.
- If the system is not large enough for CDN, it can be built like this:
  - Serving static media off a separate subdomain using lightweight HTTP server (e.g. Nginx).
  - Cutover the DNS from this subdomain to a CDN later.

**Cache invalidation**
- Keep cache coherent with the source of truth. Invalidate cache when source of truth has changed.
- Write-through cache
  - Data is written into the cache and permanent storage at the same time.
  - Pro
    - Fast retrieval, complete data consistency, robust to system disruptions.
  - Con
    - Higher latency for write operations.
- Write-around cache
  - Data is written to permanent storage, not cache.
  - Pro
    - Reduce the cache that is no used.
  - Con
    - Query for recently written data creates a cache miss and higher latency.
- Write-back cache
  - Data is only written to cache.
  - Write to the permanent storage is done later on.
  - Pro
    - Low latency, high throughput for write-intensive applications.
  - Con
    - Risk of data loss in case of system disruptions.

**Cache eviction policies**
- FIFO: first in first out
- LIFO: last in first out
- LRU: least recently used
- MRU: most recently used
- LFU: least frequently used
- RR: random replacement

### Sharding / Data Partitioning

**Partitioning methods**
- Horizontal partitioning
  - Range based sharding.
  - Put different rows into different tables.
  - Con
    - If the value whose range is used for sharding isn’t chosen carefully, the partitioning scheme will lead to unbalanced servers.
- Vertical partitioning
  - Divide data for a specific feature to their own server.
  - Pro
    - Straightforward to implement.
    - Low impact on the application.
  - Con
    - To support growth of the application, a database may need further partitioning.
- Directory-based partitioning
  - A lookup service that knows the partitioning scheme and abstracts it away from the database access code.
  - Allow addition of db servers or change of partitioning schema without impacting application.
  - Con
    - Can be a single point of failure.

**Partitioning criteria**
- Key or hash-based partitioning
  - Apply a hash function to some key attribute of the entry to get the partition number.
  - Problem
    - Adding new servers may require changing the hash function, which would need redistribution of data and downtime for the service.
    - Workaround: [consistent hashing](https://en.wikipedia.org/wiki/Consistent_hashing).
- List partitioning
  - Each partition is assigned a list of values.
- Round-robin partitioning
  - With `n` partitions, the `i` tuple is assigned to partition `i % n`.
- Composite partitioning
  - Combine any of above partitioning schemes to devise a new scheme.
  - Consistent hashing is a composite of hash and list partitioning.
    - Key -> reduced key space through hash -> list -> partition.

**Common problems of sharding**
Most of the constraints are due to the fact that operations across multiple tables or multiple rows in the same table will no longer run on the same server.

- Joins and denormalization
  - Joins will not be performance efficient since data has to be compiled from multiple servers.
  - Workaround: denormalize the database so that queries can be performed from a single table. But this can lead to data inconsistency.
- Referential integrity
  - Difficult to enforce data integrity constraints (e.g. foreign keys).
  - Workaround
    - Referential integrity is enforced by application code.
    - Applications can run SQL jobs to clean up dangling references.
- Rebalancing
  - Necessity of rebalancing
    - Data distribution is not uniform.
    - A lot of load on one shard.
  - Create more db shards or rebalance existing shards changes partitioning scheme and requires data movement.

### Indexes

- Improve the performance of search queries.
- Decrease the write performance. This performance degradation applies to all insert, update, and delete operation

### Proxies

- A proxy server is an intermediary piece of hardware / software sitting between client and backend server.
  - Filter requests
  - Log requests
  - Transform requests (encryption, compression, etc)
  - Batch requests
    - Collapsed forwarding: enable multiple client requests for the same URI to be processed as one request to the backend server
    - Collapse requests for data that is spatially close together in the storage to minimize the reads

### Queues

- Queues are used to effectively manage requests in a large-scale distributed system, in which different components of the system may need to work in an asynchronous way.
- It is an abstraction between the client’s request and the actual work performed to service it.
- Queues are implemente on the asynchronious communication protocol. When a client submits a task to a queue they are no longer required to wait for the results
- Queue can provide protection from service outages and failures.

### Redundancy

- Redundancy: **duplication of critical data or services** with the intention of increased reliability of the system.
- Server failover
  - Remove single points of failure and provide backups (e.g. server failover).
- Shared-nothing architecture
  - Each node can operate independently of one another.
  - No central service managing state or orchestrating activities.
  - New servers can be added without special conditions or knowledge.
  - No single point of failure.

### Client-Server Communication

**Standard HTTP Web Request**
1. Client opens a connection and requests data from server.
2. Server calculates the response.
3. Server sends the response back to the client on the opened request.

**Ajax Polling**
The client repeatedly polls (or requests) a server for data, and waits for the server to respond with data. If no data is available, an empty response is returned.

1. Client opens a connection and requests data from the server using regular HTTP.
2. The requested webpage sends requests to the server at regular intervals (e.g., 0.5 seconds).
3. The server calculates the response and sends it back, like regular HTTP traffic.
4. Client repeats the above three steps periodically to get updates from the server.

Problems
- Client has to keep asking the server for any new data.
- A lot of responses are empty, creating HTTP overhead.

**HTTP Long-Polling**
The client requests information from the server exactly as in normal polling, but with the expectation that the server may not respond immediately.

1. The client makes an initial request using regular HTTP and then waits for a response.
2. The server delays its response until an update is available, or until a timeout has occurred.
3. When an update is available, the server sends a full response to the client.
4. The client typically sends a new long-poll request, either immediately upon receiving a response or after a pause to allow an acceptable latency period.

Each Long-Poll request has a timeout. The client has to reconnect periodically after the connection is closed, due to timeouts.

**WebSockets**
- A persistent full duplex communication channels over a single TCP connection. Both server and client can send data at any time.
- A connection is established through WebSocket handshake.
- Low communication overhead.
- Real-time data transfer.

**Server-Sent Event (SSE)**
1. Client requests data from a server using regular HTTP.
2. The requested webpage opens a connection to the server.
3. Server sends the data to the client whenever there’s new information available.

- Use case:
  - When real-time traffic from server to client is needed.
  - When server generates data in a loop and sends multiple events to client.

## System Designs of Popular Services

### Ride-hailing Service

Ex: Uber, Lyft, Ola

- [Ace the System Design Interview — Uber/Lyft](https://towardsdatascience.com/ace-the-system-design-interview-uber-lyft-7e4c212734b3)
- [Uber System Design](https://www.karanpratapsingh.com/courses/system-design/uber)
- [[YouTube] Uber Data Engineer Interview: Design a Ride Sharing Schema](https://youtu.be/f7v_1UmkAoM)
- [Design Uber](https://medium.com/coders-mojo/day-15-of-system-design-case-studies-series-design-uber-2adc612701d?sk=d1c5481fcfd4f30e84074e5a5d7c548e)

### Food Delivery Service

Ex: Doordash, UberEats, Postmates

- [[YouTube] Design A Data Warehouse For a Food Delivery App](https://youtu.be/NPSQN9cRL3s)

### Music Streaming Service

Ex: Spotify, Amazon Music

- [[YouTube] Spotify Data Engineer System Design Interview Process](https://youtu.be/ukWwlnBizaM)

### Video Streaming Service

Ex: Netflix, Amazon Prime, Youtube

- [Design Netflix](https://www.karanpratapsingh.com/courses/system-design/netflix)
- [Design Youtube](https://medium.com/coders-mojo/day-10-of-system-design-case-studies-series-design-youtube-58bc4ad09c4b?sk=18560ffcc3d7174566d38d60c99d4914)
- [Design Tiktok](https://medium.com/coders-mojo/day-17-of-system-design-case-studies-series-design-tiktok-58e5a93bcfb5?sk=5eed7cbac7af8b6506951417514ec8e0)

### Online Messaging Service

Ex: Twitter, Whatsapp, Instagram

- [Design Twitter](https://www.karanpratapsingh.com/courses/system-design/twitter)
- [Design Twitter](https://medium.com/coders-mojo/day-7-of-system-design-case-studies-series-design-twitter-fd0722d7bb7c?sk=cdfc23d38edd5f48dc30efdcc0801c3e)
- [Design Whatsapp](https://www.karanpratapsingh.com/courses/system-design/whatsapp)
- [Design Whatsapp](https://medium.com/coders-mojo/day-18-of-system-design-case-studies-series-design-whatsapp-38ec39f32b44?sk=89cc7003e78917fd65330ad56a7ed8f0)
- [Design Instagram](https://medium.com/coders-mojo/day-4-of-system-design-case-studies-series-design-instagram-part-1-10943440f29c)
- [Design Messenger App](https://medium.com/coders-mojo/day-5-of-system-design-case-studies-series-design-messenger-app-7b73c589f4a?sk=4a53b122e8f02836c17fa35622aa0309)
- [Design Facebook’s Newsfeed](https://naina0412.medium.com/day-13-of-system-design-case-studies-series-design-facebooks-newsfeed-e96294c7d871?sk=f0956b536721902c7da6a1ec8e2f0880)

### Other Services

- [Design URL Shortner](https://www.karanpratapsingh.com/courses/system-design/url-shortener)
- [Design URL Shortner](https://medium.com/coders-mojo/day-8-of-system-design-case-studies-series-design-url-shortener-91c812a08e0b?sk=5e20d426c91ebaacfe43031bc43642da)
- [Design URL Shortener](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/designs/short-url.md)
- [Design Dropbox](https://medium.com/coders-mojo/day-9-of-system-design-case-studies-series-design-dropbox-ead523ccccfa?sk=03b3b4ea3633051f7a9a7d379b1066b8)
- [Design API Rate Limiter](https://medium.com/coders-mojo/day-11-of-system-design-case-studies-series-design-api-rate-limiter-8627993c5a92?sk=fad32cada40f414aef47b7928dfb7e67)
- [Design Web Crawler](https://medium.com/coders-mojo/day-12-of-system-design-case-studies-series-design-web-crawler-efba93f40030?sk=185e88e37fbc3d30dcaf41bc3863a868)
- [Design Yelp](https://medium.com/coders-mojo/day-14-of-system-design-case-studies-series-design-yelp-af432d13e838?sk=55e19b7d8ad43c4109e9b1694678c177)
- [Design Tinder](https://medium.com/coders-mojo/day-16-of-system-design-case-studies-series-design-tinder-a0867163f449?sk=6313f0b9760c3d78a17443a98bdb3330)

## System Design Interviews

### Distributed Message Queue

<iframe width="100%" height="480" src="https://www.youtube.com/embed/iJLL-KPqBpM" title="System Design Interview - Distributed Message Queue" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Notification Service

<iframe width="100%" height="480" src="https://www.youtube.com/embed/bBTPZ9NdSk8" title="System Design Interview - Notification Service" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Rate Limiting (local and distributed)

<iframe width="100%" height="480" src="https://www.youtube.com/embed/FU4WlwfS3G0" title="System Design Interview - Rate Limiting (local and distributed)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Distributed Cache

<iframe width="100%" height="480" src="https://www.youtube.com/embed/iuqZvajTOyA" title="System Design Interview - Distributed Cache" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Top K Problem (Heavy Hitters)

<iframe width="100%" height="480" src="https://www.youtube.com/embed/kx-XDoPjoHw" title="System Design Interview - Top K Problem (Heavy Hitters)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Step By Step Guide

<iframe width="100%" height="480" src="https://www.youtube.com/embed/bUHFg8CZFws" title="System Design Interview – Step By Step Guide" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Common System Design Questions

1. Design a Credit Card Authorization System
1. Design a chat service
1. Design a ride-sharing service
1. Design a URL shortening service
1. Design a social media service
1. Design a social message board
1. Design a system to store time series data
1. Design a concurrent Hashmap
1. Design an ATM Machine system which can support massive amount of transactions
1. Design Airport Baggage system
1. Design Flight Information Display system
1. Design a conference room booking system
1. Design newsfeed feature of Facebook
1. Design an efficient Mail delivery system
1. Design like/dislike feature at Youtube scale
1. Design Instagram
1. Design Tik-Tok
1. Design twitter
1. Design Uber
1. Design a logging system
1. Design Google Maps
1. Design a Video Conferencing System
1. Design a file storage service
1. Design a video streaming service
1. Design a smart meter system
Build Cart as a service
1. Design metas newsfeed with live posts
1. Design a Limited Time Deals
1. Design Twitter’s trending topics
1. Design a system that counts the number of clicks on YouTube videos
1. Design Gmail
1. Design a global system to upgrade software on a fleet of machines
1. Design a recommendation system
1. Design a food sharing application
1. Design an API for a tic tac toe game
1. Design payment module for Uber app
1. Design Truecaller type of system
1. Design performance management system (appraisal workflow system) that can be used across companies.
1. Design comment system
1. Design flight system
1. Design Tinder
1. Design survey site like surveymonkey
1. Design a geographically partitioned multi-player card game.
1. Design a kind of kindle fire application
1. Design a realtime Video chat like Google Duo
1. Design News paper & Magazine subscription system
1. Design a system like Hackerrank/Top Coder
1. Design an API Rate Limiter
1. Design a proximity server
1. Design a Type-Ahead service
1. Design a traffic control system
1. Design amazon’s frequently viewed product page
1. Design a toll system for highways.
1. Design URL Shortener.
1. Design Instant Messenger.
1. Design a CDN network
1. Design a Google document system
1. Design a random ID generation system
1. Design a key-value database
1. Design the Facebook news feed function
1. Design a forum-like systems like Quora, Reddit or HackerNews.
1. Design the Facebook timeline function
1. Design a function to return the top k requests during past time interval
1. Design an online multiplayer card game
1. Design an online poker game for multiplayer.
1. Design a graph search function
1. Design a picture sharing system
1. Design an API Rate Limiter system for GitHub or Firebase sites
1. Design a search engine
1. Design a recommendation system
1. Design What’s up
1. Design a garbage collection system.
1. Design a system to capture unique addresses in the entire world.
1. Design a recommendation system for products.
1. Design a tinyurl system
1. Design Paypal
1. Design Air traffic control system
1. Design Google Maps
1. Design Grammarly
1. Design AirBNB
1. Design a vending machine in Java
1. Design a traffic control system
1. Design a limit order book for trading systems
1. Design an elevator system?
1. Design an e-commerce website
1. Design an e-commerce website using microservices
1. Design a website like Pastebin.
1. Design Google’s Web Crawler
1. Design Zoom
1. Design Twitter
1. Design Online Examination Portal
1. Design RedBus
1. Design BookMyShow
1. Design Domain Backdooring system
1. Design Amazon Locker
1. Design Movies Review Aggregator System
1. Design offline caching system for Ecommerce platform
1. Design Amazon E-commerce
1. Design Online chess game/Multiplayer game
1. Design gaming platform.
1. Design a last-mile delivery platform
1. Design Foodpanda/Zomato/Swiggy/
1. Design Meeting Calendar system
1. Design Spotify
1. Design Promo Code API
1. Design Vending machine
1. Design splitwise
1. Design Google pay at scale
1. Design a Job schedular
1. Design Meeting Scheduler
1. Design Debugger
1. Design Automatic Parking System
1. Design malloc, free and garbage collection system.
1. Design a system for collaborating over a document
1. Design election commission architecture
1. Design a garbage collection system
1. Design a scalable web crawling system
1. Design the Facebook chat function
1. Design a trending topic system
1. Design a url compression system
1. Design Elevator system.
1. Design distributed caching system.
1. Design Amazon Locker Service.
1. Design Amazon Best Seller Item Service
1. Design a global chat service like Whatsapp or a facebook messenger.
1. Design dropbox’s architecture.
1. Design a picture sharing website.
1. Design a news feed
1. Design a product based on maps
1. Design commenting system
1. Design a ranking system.
1. Design Amazon Cart system
1. Design Google Search
1. Design Twitter
1. Design Facebook
1. Design Snapchat
1. Design Instagram
1. Design App-store
1. Design a music player application
1. Design a distributed LRU Cache
1. Design Dropbox or Google Drive
1. Design subscription based sports website
1. Design Netflix
1. Design a Latency Management System
1. Design a Library Management System
1. Design a Notification service
1. Design ESPN/Cricinfo/Cricbuzz
1. Design Uber
1. Design Whatsapp
1. Design Quora
1. Design Lookahead system
1. Design Google Docs/ Collaborative Editing service
1. Design URL Shortner service

## Resources

1. [https://github.com/Jeevan-kumar-Raj/Grokking-System-Design](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design)
2. [https://www.educative.io/courses/grokking-modern-system-design-interview-for-engineers-managers](https://www.educative.io/courses/grokking-modern-system-design-interview-for-engineers-managers)
3. [https://youtu.be/B22zwLIvoW0](https://youtu.be/B22zwLIvoW0)
4. [https://www.techshashank.com/data-warehousing/shipping-dimensional-modeling](https://www.techshashank.com/data-warehousing/shipping-dimensional-modeling)
5. [https://www.karanpratapsingh.com/courses/system-design/system-design-interviews](https://www.karanpratapsingh.com/courses/system-design/system-design-interviews)
6. [Most Popular System Design Questions](https://medium.com/coders-mojo/most-popular-system-design-questions-mega-compilation-45218129fe26?sk=6432dd01c067dd28bc81da1dfceccdab)
7. [Mega Compilation : Solved System Design Case studies](https://medium.com/coders-mojo/quick-roundup-solved-system-design-case-studies-6ad776d437cf?sk=e42f56968e1b592382f484c222e7c111)
9. [How to Prepare for System Design Interviews | Top System Design Interview Concepts](https://youtu.be/-m5cMzm9R-s)
11. [YouTube | Google Data Engineer Interview](https://youtu.be/rL2YASP04eQ)
12. https://igotanoffer.com/blogs/tech/system-design-interviews
13. https://blog.tryexponent.com/how-to-nail-the-system-design-interview/