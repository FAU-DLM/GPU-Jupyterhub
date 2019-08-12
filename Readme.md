This repo contains the docker-compose.yml for defining the dependencies to run the Jupyter Notebook Images described in the Dockerfiles under Jupyter_Images.
There is one Jupyter Notebook image, CUDA10.0 and Ubuntu18.04 based.
It will be spwaned from a Jupyterhub which is defined in the Dockerfile.jupyterhub under the folder Jupyterhub_Image.
For more details visit our website https://www.dlm.med.fau.de/setting-jupyterhub-deep-learning/

Edited the repo:
- removed the cuda 9 image
- restructured the docker-compose.yml
--> you will need a folder called secets containing the env_files mentioned in the yml-env_file
--> will need a folder under Jupyterhub_Image called ssl containing your ssl certs for building and running the Jupyterhub.

The Jupyter_Image (jupyternotebook) has new features and some removed features:
Python2 is gone
R is available
Python3 is available
SOS is available

The workhorse for deep-learning is Python3 based.
It contains Tensorflow-GPU 1.14, Keras 2.2.4 Pytorch 1.0 and Fastai 1

-Jupyterhub Image definition with DockerSpawner for spawning Jupyternotebooks.
    Localauthentication is removed and replaced by OAuth with Github
   - Data is persisted:
     --> -locally (Docker-Volume --> cookie secrets)
     --> host machine and pesronal data is mapped into the container for pre spwan hook (see into jupyterhub_config.py)

 -Spawned Images run in single Docker-Containers        
    - Data is persisted:
     --> user based:
         -locally on nvme/ssd (Docker-Volume bind mount--> host_path:/home/Deep_Learner/private/local) and per network associated folder       
          (host_path:/home/Deep_Learner/private/network).
      --> commonly shared:
         - per network associated folder (net_share:/home/Deep_Learner/shared).

Added ftp server mapping to an uploads folder in host_path/uploads:/home/Deep_Learner/shared/uploads
