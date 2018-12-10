This repo contains the docker-compose.yml for defining the dependencies to run the Jupyter Notebook Images described in the Dockerfiles under Jupyter_Images.
There are two sets of images. CUDA10 and Ubuntu18.04 or CUDA9.2 and Ubuntu16.04 based ones.
They will be spwaned from a Jupyterhub which is defined in the Dockerfile.jupyterhub under the folder Jupyterhub_image.
For more details visit our website https://www.dlm.med.fau.de/setting-jupyterhub-deep-learning/

Just in short some features:
-Jupyterhub Image definition with DockerSpawner for spawning Jupyternotebooks.
   - Data is persisted:
     --> -locally (Docker-Volume --> cookie secrets) 
         
 -Spawned Images run in single Docker-Containers        
    - Data is persisted:
     --> user based:
         -locally (Docker-Volume--> :/home/Deep_Learner/work/local) and per network associated folder       
          (:/home/Deep_Learner/work/network).
      --> commonly shared:
         - per network associated folder (:/home/Deep_Learner/shared).
     - They contain either CUDA10 and Ubuntu18.04 (needs Nvidia Driver v. >410) or CUDA9.2 and Ubuntu16.04 (needs Nvidia Driver 
       v. >390) (choose what suits you best)
       Installed:
       Virtual Environments (Conda env.) for (DeepLearning)Python3, (DeepLearning)Python2, (local Python3), OmeroR, SOS 
       Notebook:
         The workhorses are (DeepLearning)Python3, (DeepLearning)Python2:
         They include (and many others--> see Dockerfiles)
           
           Tensorflow-GPU 1.12 and
           Pytorch-GPU 1.0.0
       
        

