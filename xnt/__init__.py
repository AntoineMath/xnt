from flask import Flask
from opensearchpy import OpenSearch


app = Flask(__name__)
app.config.from_object('config.DevConfig')

osearch = OpenSearch(
    hosts = [{'host': app.config['DEV_OSEARCH_HOST'], 'port': app.config['DEV_OSEARCH_PORT']}],
    http_compress = True, # enables gzip compression for request bodies
    http_auth = app.config['DEV_OSEARCH_AUTH'], 
    # client_cert = client_cert_path,
    # client_key = client_key_path,
    use_ssl = True,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False,
    ca_certs = app.config['DEV_CA_CERTS_PATH']
)


import xnt.views, xnt.article