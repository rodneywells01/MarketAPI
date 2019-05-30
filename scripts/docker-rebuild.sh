# Kill
docker kill marketapi 
docker rm marketapi 

# Rebirth
docker build -t rodneywells01/marketapi . 
docker run -p 5000:5000 --name marketapi -d rodneywells01/marketapi 