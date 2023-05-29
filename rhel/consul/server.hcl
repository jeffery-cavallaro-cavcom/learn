# Enable the service mesh.
connect {
  enabled = true
}

# Listen to this port for gRPC.
ports {
  grpc = 8502
}

# Run as a server.
server = true

# Number of expected servers that must join this cluster prior to start.
bootstrap_expect = 2

# Enable the UI.
ui_config {
  enabled = true
}

# HTTP API port.
client_addr = "0.0.0.0"

# Internal cluster communications.
bind_addr = "0.0.0.0"
advertise_addr = "10.0.0.129"

# Cluster nodes.
retry_join = ["10.0.0.128"]
