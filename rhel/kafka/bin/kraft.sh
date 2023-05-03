#!/bin/bash

export KAFKA_HOME=/opt/kafka
export KAFKA_LOCAL=/data/kafka
export LOG_DIR=${KAFKA_LOCAL}/kraft-logs

export PATH=$PATH:$KAFKA_HOME/bin
