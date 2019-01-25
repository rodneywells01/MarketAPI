# Kill
docker kill market_api 
docker rm market_api 

# Rebirth
docker build -t market_api . 
docker run -p 5000:5000 --name market_api -d market_api 