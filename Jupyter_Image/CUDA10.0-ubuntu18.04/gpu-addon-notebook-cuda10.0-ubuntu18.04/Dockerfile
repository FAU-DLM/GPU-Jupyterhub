FROM digitalanatomist/gpu-notebook-cuda10.0-ubuntu18.04:latest
MAINTAINER samir.jabari@fau.de
USER root
#SOS
RUN     python3 -m pip install pip --upgrade
RUN     python3 -m pip install xlrd docker
RUN     python3 -m pip install markdown wand graphviz imageio pillow

RUN     conda install -y feather-format -c conda-forge
RUN     python3 -m pip install nbformat --upgrade
## trigger rerun for sos updates
ARG	    DUMMY=unknown
RUN     DUMMY=${DUMMY} python3 -m pip install sos sos-notebook sos-r sos-julia sos-python sos-matlab sos-javascript sos-bash sos-bioinfo --upgrade
RUN     python3 -m sos_notebook.install
RUN     python3 -m pip install jupyterlab
RUN     jupyter labextension install jupyterlab-sos

COPY --chown=1000:100 docker/custom.css /opt/conda/lib/python3.7/site-packages/notebook/static/custom/
RUN     fix-permissions $CONDA_DIR &&\
        fix-permissions /home/$NB_USER

USER $NB_USER
