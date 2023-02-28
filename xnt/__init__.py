import os
from flask import Flask
from opensearchpy import OpenSearch

test_config = True
app = Flask(__name__, instance_relative_config=True)
if test_config is None:
    app.config.from_object('config.Config')
else:
    app.config.from_object('config.DevConfig')
try:
    os.makedirs(app.instance_path)
except OSError: pass


osearch = OpenSearch(
    hosts = [{'host': app.config['OSEARCH_HOST'], 'port': app.config['OSEARCH_PORT']}],
    http_compress = True, # enables gzip compression for request bodies
    http_auth = app.config['OSEARCH_AUTH'], 
    # client_cert = client_cert_path,
    # client_key = client_key_path,
    use_ssl = True,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False,
    ca_certs = app.config['CA_CERTS_PATH']
)

import xnt.views, xnt.article