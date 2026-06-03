#!/bin/bash

# Ensure to insert your correct host, port, and password
mysqldump --host=172.21.51.80 --port=3306 --user=root --password=bTutU0W14RwkGZIJoYLeKGE0 sales sales_data > sales_data.sql
