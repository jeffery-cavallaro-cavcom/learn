# KAFKA COUCHBASE CONNECTOR

## Basic Installation

1. Get the current zip file and extract it to the desired location.

1. In couchbase, create a DCP reader user for the connector.

1. Copy the quickstart properties file:

``` bash
cp $CONNECTOR_HOME/etc/quickstart-couchbase-source.properties \
	$CONNECTOR_LOCAL/config/couchbase-source.properties
```

1. In the properties file:

	- Set the couchbase seed nodes property to a comma-separated list of
	  couchbase cluster nodes.

	- Set the couchbase bucket, username and password properties.  These should
	  match the created DCP reader user.
   
    - Set the destination kafka topic.  Note that the topic string recognizes
	  `${bucket}`, `${scope}`, and `${collection}` macros.  The default is
	  `${bucket}.${scope}.${collection}`.
	  
	- Set the `couchbase.scope` or `couchbase.collections` properties to
	  limit what collections are uploaded to kafka.
	
	- Set the offset storage file to something not in /tmp.
	
	- Make any other desired changes.

1. Set the `CLASSPATH` so it can find the connector jars:

``` bash
export CLASSPATH=$CONNECTOR_HOME/lib/*
```

1. Start the connector:

``` bash
$KAFKA_HOME/bin/connect-standalone \
	$KAFKA_HOME/config/connect-standalone.properties \
	$CONNECTOR_LOCAL/config/couchbase-source.properties
```

## Alternate Installation

Instead of using the `connect-standalone.properties` file directly, copy it
and change the `plugin.path` property to include `$CONNECTOR_HOME`.
Alternatively, copy the `$CONNECTOR_HOME/lib` directory to an existing
directory already on the path.
