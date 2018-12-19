FROM digitalanatomist/tensorflow-notebook-gpu-CUDA10-ubuntu18.04:latest
MAINTAINER samir.jabari@fau.de
USER root
# create a deep_learning_python2 environment (for OMERO-PY compatibility)
ADD docker/environment-python2-omero.yml .setup/
RUN conda env update -n deep_learning_python2 -q -f .setup/environment-python2-omero.yml
# Don't use this:
#RUN /opt/conda/envs/deep_learning_python2/bin/python -m ipykernel install --user --name deep_learning_python2 &&\
  #  fix-permissions /home/$NB_USER &&\
  #  fix-permissions $CONDA_DIR
#COPY --chown=1000:100 docker/logo-32x32.png docker/logo-64x64.png .local/share/jupyter/kernels/deep_learning_python2/
#COPY --chown=1000:100 docker/deep_learning_python2-kernel.json .local/share/jupyter/kernels/deep_learning_python2/kernel.json

#RUN /opt/conda/envs/deep_learning_python2/bin/pip install ipykernel --user --name deep_learning_python2 --display-name 'OMERO Python 2'&&\

# R-kernel and R-OMERO prerequisites
ADD docker/environment-r-omero.yml .setup/
RUN conda env update -n r-omero -q -f .setup/environment-r-omero.yml && \
    /opt/conda/envs/r-omero/bin/Rscript -e "IRkernel::installspec(displayname='OMERO R')"

RUN mkdir /opt/romero /opt/omero && \
    fix-permissions /opt/romero /opt/omero
# R requires these two packages at runtime
RUN apt-get install -y -q \
    libxrender1 \
    libsm6


# install rOMERO
ENV _JAVA_OPTIONS="-Xss2560k -Xmx2g"
ARG ROMERO_VERSION=v0.4.2
RUN cd /opt/romero && \
    curl -sf https://raw.githubusercontent.com/ome/rOMERO-gateway/$ROMERO_VERSION/install.R --output install.R && \
    bash -c "source activate r-omero && Rscript install.R --version=$ROMERO_VERSION --quiet"

# OMERO full CLI
# This currently uses the deep_learning_python2 environment, should we move it to its own?
ARG OMERO_VERSION=5.4.9
RUN cd /opt/omero && \
    /opt/conda/envs/deep_learning_python2/bin/pip install -q omego && \
    /opt/conda/envs/deep_learning_python2/bin/omego download -q --sym OMERO.server server --release $OMERO_VERSION && \
    rm OMERO.server-*.zip
ADD docker/omero-bin.sh /usr/local/bin/omero

#SOS
RUN     python3.6 -m pip install pip --upgrade
RUN     python3.6 -m pip install xlrd docker
RUN     python3.6 -m pip install markdown wand graphviz imageio pillow

RUN     conda install -y feather-format -c conda-forge
RUN     python3.6 -m pip install nbformat --upgrade
## trigger rerun for sos updates
ARG	    DUMMY=unknown
RUN     DUMMY=${DUMMY} python3.6 -m pip install sos sos-notebook sos-r sos-julia sos-python sos-matlab sos-javascript sos-bash sos-bioinfo --upgrade
RUN     python3.6 -m sos_notebook.install
#RUN     pip install jupyterlab
RUN     jupyter labextension install jupyterlab-sos



RUN     fix-permissions /home/$NB_USER
        #fix-permissions $CONDA_DIR


# For CUDA profiling, TensorFlow requires CUPTI.
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
ENV CUDA_HOME=/usr/local/cuda
ENV CUDA_ROOT=$CUDA_HOME
ENV PATH=$PATH:$CUDA_ROOT/bin:$HOME/bin
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CUDA_ROOT/lib64

#USER root
USER $NB_USER

CMD ["start-notebook.sh", "--allow-root"]

#COPY start-notebook.sh /usr/local/bin


# Clone the source git repo into notebooks (keep this at the end of the file)
#COPY --chown=1000:100 . notebooks
