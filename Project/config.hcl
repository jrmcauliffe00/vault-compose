ui = true
disable_mlock = true

storage "inmem" {}

# Note: In dev mode, the listener is configured via -dev-listen-address flag
# so we don't need a listener block here
api_addr = "http://0.0.0.0:8200"
