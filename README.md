# Smart Home Backend

## References

* https://www.emqx.com/en/blog/how-to-use-mqtt-in-python
* https://fastapi.tiangolo.com/de/

## Setup

```bash
git clone https://github.com/MadMax2506/smarthome-backend.git smarthome-backend
cd smarthome-backend
pip install -r requirements.txt
uvicorn main:app --reload
```

## Deployment

```bash
bash .scriptbox/build-docker.sh
cd .docker
docker-compose up
```

IMPORTANT: If you want to run the image on a raspberry pi you need to build it on a raspberry pi.
