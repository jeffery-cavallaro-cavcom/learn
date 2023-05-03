# KAFKA

## Kraft

As of v3.3.1, Kraft is deemed production-ready, meaning that zookeeper is
now deprecated.

## Installation

1. Install Java 11:

``` bash
yum install java-11-openjdk
yum install java-11-openjdk-devel
```

1. If the `JAVA_HOME` environment variable needs to be set, then it can be
   set to `/etc/alternatives/jre_11`.

1. Download the Kafka binaries from the
   [Kafka website](http://kafka.apache.org).

1. Extract the tarball into the desired location.

1. Add the new bin location to your PATH.

## Start with Zookeeper

1. Copy the `zookeeper.properties` and `server.properties` files from
   `$KAFKA_HOME/config` to a local directory and edit the files to change the
   data/log file locations as desired.

1. Start zookeeper (listens on port 2181 by default):

``` bash
zookeeper-server-start.sh $KAFKA_LOCAL/config/zookeeper.properties
```

1. Start Kafka:

``` bash
kafka-server-start.sh $KAFKA_LOCAL/config/server.properties
```

## Start with Kraft

1. Copy the `server.properties` files from `$KAFKA_HOME/config/kraft` to a
   local directory and edit the files to change the data/log file locations as
   desired.  The LOG_DIR environment variable also needs to be set.

1. Generate a random UUID for the cluster:

``` bash
kafka-storage.sh random-uuid
```

1. Initialize the storage:

``` bash
kafka-storage.sh format -t <uuid> -c $KAFKA_LOCAL/config/kraft/server.properties
```

1. Start Kafka (listens on port 9092:client, 9093:zoo by default):

``` bash
kafka-server-start.sh $KAFKA_LOCAL/config/kraft/server.properties
```

## Topics

### List:

``` bash
kafka-topics --bootstrap-server localhost:9092 --list
```

### Create:

``` bash
kafka-topics --bootstrap-server localhost:9092 --create --topic <name> \
	[--partitions n] [--replication-factor m]
```

### Describe:

``` bash
kafka-topics --bootstrap-server localhost:9092 --describe [--topic <name>]
```

### Delete:

``` bash
kafka-topics --bootstrap-server localhost:9092 --delete --topic <name>
```

## Console Producer

### Without Keys

``` bash
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic <name> \
	--property parse.key=false
```

### With Keys

``` bash
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic <name> \
	--property parse.key=true --property key.separator=:
```

## Console Consumer

### From End

``` bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <name>
```

### From Beginning

``` bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <name> \
	--from-beginning
```

### With Formatter

``` bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <name> \
	--formatter kafka.tools.DefaultMessageFormatter \
	--property print.timestamp=true \
	--property print.key=true \
	--propert print.value=true \
	[--from-beginning]
```

### In a Group

This is supposed to write to the various partitions using the sticky
partitioner and/or keying; however, using the CLI and producing data without
keys always seems to go to the same partition.  A python producer using the
aiokafka package seems to partition as expected.

``` bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <name> \
	--group <group-name> [--from-beginning]
```

## Consumer Groups

### List

``` bash
kafka-consumer-groups --bootstrap-server localhost:9092 --list
```

### Describe

``` bash
kafka-consumer-groups --bootstrap-server localhost:9092 --describe \
	--group <name>
```
