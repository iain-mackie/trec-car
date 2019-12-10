# check command line inputs and map to dockerfile paths
if [ "$1" = "cpu" ]; then
  DOCKER_PATH="./Dockerfile.cpu"
  echo "Building cpu dockerfile from: " DOCKER_PATH;

elif [ "$1" = "gpu" ]; then
  DOCKER_PATH="./Dockerfile.gpu"

else
  echo "Error - please need to enter 'cpu' or 'gpu'";
  exit 0;

fi

# build docker
echo "Trying to build docker image on" $1 "from:" $DOCKER_PATH;

if [ -f "$DOCKER_PATH" ]; then
  echo "file exits"
  sudo docker build -t trec_car_img -f $DOCKER_PATH .
  sudo docker run -it -v $PWD/../:/my_shared/ --name trec_car_container trec_car_img bash

else
  echo "Error - path to file not found:" $DOCKER_PATH;
  exit 0;

fi


