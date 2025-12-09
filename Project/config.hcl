ui = true
disable_mlock = true

storage "inmem" {}

listener "tcp" {
  address = "0.0.0.0:4646"
  tls_disable = true
}

api_addr = "http://127.0.0.1:8200"
