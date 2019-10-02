# Django-Vue-Docker

# Steps to Deploy
1. Clone repo to new local directory

# AWS Instance
1. Login to AWS console and spin up a new elastic beanstalk instance
2. Create a new Elastic Beanstalk environment
3. Choose multi container platform
4. Create

# RDS Instance
1. Click services and find RDS
2. Create a database
3. Choose Postgresql
4. Create a username and password, write password down
5. Create database

# VPC Security Group
1. Click services and find VPC
2. On the left look for security and click security groups
3. Create new security group, give it a name and choose default VPC
4. Add an inbound rule, set port range to 5432-6379, in the box to the right of custom, 
start typing sg and look for the new security group, create rule
5. Once the DB is done initializing, click modify and look for security groups. Add the new security group.
6. Go back to the elastic beanstalk instance, click configuration and modify the instance. Check the new
security rule and apply.

# Set environment variables
1. Inside the EBS instance, click configuration, modify software.
2. Set your environment variables. These are examples but these would be any env's that are set inside
of the django or vue project that need to be read.
```
PG_USER = postgres
PG_PASSWORD = postgrespassword
PG_HOST = Find this under your RDS instance (url)
PG_DATABASE = DB name, find this inside of the RDS instance
PG_PORT = default port is 5432
```

# Create new IAM keys for deployment
1. Find IAM in AWS
2. Click users in the sidebar
3. Click add user
4. Create a username
5. Set access type to programmatic access
6. Click next and select Attach existing polices directly
7. Search for beanstalk and check all boxes
8. Create user
9. Copy keys and save for later. 
10. Add these keys to the travis CI environment variables
```
AWS_ACCESS_KEY
AWS_SECRET_KEY
```


