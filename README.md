Role Name
=========

Bootstrap role to update our alfresco config

Requirements
------------

None

Role Variables
--------------

```yaml
- bucket_name # Name of our s3 content bucket
- bucket_encrypt_type # should be kms
- bucket_key_id # kms key id
- db_user # rds user name
- db_password # rds password
- db_name #rds db name
- db_host # rds url
- server_mode # Default is TEST
- cluster_name # alfresco cluster name
- cluster_subnet # alfresco cluster subnet
- monitoring_server_url # ingest node url for elasticsearch
- monitoring_cluster_name # name of elasticsearch cluster
- logstash_index #defaults to alfresco-logstash, used for reading and writing of audit events
```
