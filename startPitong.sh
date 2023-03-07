#/bin/bash 

podman run -itd --name codeserver -p 3080:3080 -v /home/redhat/storage/projetos/python:/projetos --privileged localhost/codeserver-python:1
