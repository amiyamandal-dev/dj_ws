### ws test django

requirements for the projects

1. python 3.9
2. docker

#### to run server

1. install docker
2. run the below command to build the image

```dockerfile
docker build -t dj_ws .
```

2. running the below command will make server up and running

```dockerfile
docker run -p 8000:8000 dj_ws
```

Now server is up at port 8000

3. Run client.py the use the server

```bash
python client.py
```

4. fill the info and will show the result

NOTE:- want to update key just update the .env file