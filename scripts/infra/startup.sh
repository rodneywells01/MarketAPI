# Installation / Configuration
yum update -y
yum install docker -y
service docker start

# Pull Code
docker pull rodneywells01/marketapi

# Birth
docker run -p 5000:5000 --name marketapi -d rodneywells01/marketapi