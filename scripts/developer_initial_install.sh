# Install Mongodb - https://docs.mongodb.com/manual/tutorial/install-mongodb-enterprise-on-ubuntu/
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
echo "deb [ arch=amd64,arm64,ppc64el,s390x ] http://repo.mongodb.com/apt/ubuntu xenial/mongodb-enterprise/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-enterprise.list
apt-get update # <-- This will take a while to execute
apt-get install -y mongodb-enterprise