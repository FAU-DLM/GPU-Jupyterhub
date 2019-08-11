# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# Configuration file for JupyterHub
import os
import requests
from oauthenticator.github import LocalGitHubOAuthenticator
from oauthenticator.google import LocalGoogleOAuthenticator
c = get_config()
docker_personal_network_folder=os.environ.get('DOCKER_PERSONAL_NETWORK_FOLDER')
docker_shared_network_folder=os.environ.get('DOCKER_SHARED_NETWORK_FOLDER')
host_personal_network_folder=os.environ.get('HOST_PERSONAL_NETWORK_FOLDER')
host_shared_network_folder=os.environ.get('HOST_SHARED_NETWORK_FOLDER')
#print('{username}')
def create_dir_hook(spawner):
    username =  spawner.escaped_name # get the escaped!!! username
    volume_path = os.path.join(host_personal_network_folder, username)
    if not os.path.exists(volume_path):
        # create a directory with umask 0755
        # hub and container user must have the same UID to be writeable
        # still readable by other users on the system
        os.mkdir(volume_path,0o755)
        os.chown(volume_path, 1000, 100)
        # now do whatever you think your user needs
        pass

#attach the hook function to the spawner
c.DockerSpawner.pre_spawn_hook = create_dir_hook


#os.environ['LD_LIBRARY_PATH'] = '/usr/local/cuda-9.0/lib64:usr/local/cuda-9.0/lib64/libcudart.so.9.0'
#c.Spawner.env.update('LD_LIBRARY_PATH')
# We rely on environment variables to configure JupyterHub so that we
# avoid having to rebuild the JupyterHub container every time we change a
# configuration parameter.

token = os.environ['CONFIGPROXY_AUTH_TOKEN']

c.ConfigurableHTTPProxy.auth_token= token
# Spawn single-user servers as Docker containers
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
# Spawn containers from this image
c.DockerSpawner.container_image = os.environ['DOCKER_NOTEBOOK_IMAGE']
# JupyterHub requires a single-user instance of the Notebook server, so we
# default to using the `start-singleuser.sh` script included in the
# jupyter/docker-stacks *-notebook images as the Docker run command when
# spawning containers.  Optionally, you can override the Docker run command
# using the DOCKER_SPAWN_CMD environment variable.
spawn_cmd = os.environ.get('DOCKER_SPAWN_CMD', "start-singleuser.sh")


c.DockerSpawner.extra_create_kwargs.update({ 'command': spawn_cmd } )
#create_kwargs['host_config']['PortBindings']['8888/tcp'] == [{'HostIp': '127.0.0.1', 'HostPort': ''}]
#c.DockerSpawner.host_ip='127.0.0.1'
#c.Spawner.port=6006
# Connect containers to this Docker network
network_name = os.environ['DOCKER_NETWORK_NAME']
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name
# Pass the network name as argument to spawned containers
c.DockerSpawner.extra_host_config = {
                    'network_mode': network_name,
                    'runtime': 'nvidia',
                    'shm_size' : '16G',
                    # 'devices': [ '/dev/nvidia-uvm:/dev/nvidia-uvm:mrw',
                    #             # '/dev/nvidia-uvm-tools:/dev/nvidia-uvm-tools:mrw',
                    #              '/dev/nvidia-modeset:/dev/nvidia-modeset:mrw',
                    #              '/dev/nvidia0:/dev/nvidia0:mrw',
                    #              #'/dev/nvidia1:/dev/nvidia1:mrw',
                    #              '/dev/nvidiactl:/dev/nvidiactl:mrw'
                    # ]
                    }
# Explicitly set notebook directory because we'll be mounting a host volume to
# it.  Most jupyter/docker-stacks *-notebook images run the Notebook server as
# user `jovyan`, and set the notebook directory to `/home/jovyan/work`.
# We follow the same convention.
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/Deep_Learner/private/local/'
#base_network_folder = os.environ.get('BASE_NETWORK_FOLDER')


c.DockerSpawner.notebook_dir = notebook_dir
# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container
#c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

c.DockerSpawner.volumes = {
    #'nvidia_driver_387.34':'/usr/local/nvidia',
    'jupyterhub-user-{username}': notebook_dir,
    host_personal_network_folder+'{username}':  docker_personal_network_folder,
    host_shared_network_folder:  docker_shared_network_folder
}


# Remove containers once they are stopped
c.DockerSpawner.remove_containers = True
# For debugging arguments passed to spawned containers
c.DockerSpawner.debug = True
c.Spawner.mem_guarantee = 17179869184
c.Spawner.cpu_guarantee = 10.0

# User containers will access hub by container name on the Docker network
# User containers will access hub by container name on the Docker network
#c.JupyterHub.hub_ip = '0.0.0.0'
#c.JupyterHub.hub_port = 8081
#c.JupyterHub.hub_connect_ip = public_ips()[0]
#c.DockerSpawner.container_ip = '172.22.0.10'

c.JupyterHub.hub_ip = 'jupyterhub'
c.JupyterHub.hub_port = 8080
#hub_ip='0.0.0.0'
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.proxy_api_ip = '0.0.0.0'

c.DockerSpawner.hub_ip_connect = "jupyterhub"
#os.environ['DOCKER_HOST'] = hub_ip + ':6006'
#c.DockerSpawner.links = {"jupyterhub" : "jupyterhub"}



# TLS config
c.JupyterHub.port = 8000
c.JupyterHub.ssl_key = os.environ['SSL_KEY']
c.JupyterHub.ssl_cert = os.environ['SSL_CERT']


# Authenticate users with GitHub OAuth
#c.JupyterHub.authenticator_class = 'oauthenticator.GitHubOAuthenticator'
#c.GitHubOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']

# Persist hub data on volume mounted inside container
data_dir = os.environ.get('DATA_VOLUME_CONTAINER', '/data')

c.JupyterHub.cookie_secret_file = os.path.join(data_dir,
    'jupyterhub_cookie_secret')

#c.JupyterHub.db_url = "mysql://{}:{}@mysql/jupyter".format("root", os.environ['MYSQL_ROOT_PASSWORD'])

c.JupyterHub.db_url = 'postgresql://postgres:{password}@{host}/{db}'.format(
    host=os.environ['POSTGRES_HOST'],
    password=os.environ['POSTGRES_PASSWORD'],
    db=os.environ['POSTGRES_DB'],
)
#for var in os.environ:
#    c.Spawner.env_keep.append(var)

#c.JupyterHub.logo_file = '/opt/conda/share/jupyterhub/static/images/dlm_logo.jpg'
# Whitlelist users and admins
#c.LocalAuthenticator.create_system_users = True
c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator
c.LocalGitHubOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']
c.LocalGitHubOAuthenticator.client_secret = os.environ['GITHUB_CLIENT_SECRET']
c.LocalGitHubOAuthenticator.client_id = os.environ['GITHUB_CLIENT_ID']
#c.LocalGitHubOAuthenticator.login_service = 'Deep Learning Mophology'


# For Google OAuth Authentication
#c.JupyterHub.authenticator_class = LocalGoogleOAuthenticator
#c.LocalGoogleOAuthenticator.create_system_users = True
#c.LocalGoogleOAuthenticator.hosted_domain = [ 'gmail.com', 'googlemail.com']
#c.LocalGoogleOAuthenticator.login_service = 'Deep Learning Mophology'
#c.LocalGoogleOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']
#c.LocalGoogleOAuthenticator.client_id = os.environ['GOOGLE_CLIENT_ID']
#c.LocalGoogleOAuthenticator.client_secret = os.environ['GOOGLE_CLIENT_SECRET']
#c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/jupyterhub_cookie_secret'


c.Authenticator.add_user_cmd = ['adduser', '-q', '--gecos', '""', '--disabled-password', '--force-badname']
#c.Authenticator.add_user_cmd = ['adduser', '--force-badname', '-q', '--gecos', '""', '--ingroup', 'jupyter', '--disabled-password']
c.LocalGitHubOAuthenticator.create_system_users = True
#c.LocalGoogleOAuthenticator.create_system_users = True
c.Authenticator.whitelist = whitelist = set()
c.Authenticator.admin_users = admin = set()
c.JupyterHub.admin_access = True
pwd = os.path.dirname(__file__)
with open(os.path.join(pwd, 'userlist')) as f:
    for line in f:
       if not line:
           continue
       parts = line.split()
       name = parts[0]
       whitelist.add(name)
       if len(parts) > 1 and parts[1] == 'admin':
           admin.add(name)
