> ./messages-service.env

echo "HOST=127.0.0.1" > ./messages-service.env
echo "PORT=${1}" >> ./messages-service.env

uvicorn api:app --workers 2 --reload --port ${1}
