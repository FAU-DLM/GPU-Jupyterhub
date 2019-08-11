# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# Ubuntu 18.04

FROM nvidia/cuda:10.0-cudnn7-runtime-ubuntu18.04


MAINTAINER Samir Jabari <samir.jabari@fau.de>

USER root

ENV  DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
          apt-get -y install software-properties-common --fix-missing &&\
          apt-get update


# Install all OS dependencies for notebook server that starts but lacks all
# features (e.g., download as all possible file formats)

RUN apt-get update && apt-get -yq dist-upgrade \
 && apt-get install -yq --no-install-recommends \
    wget \
    bzip2 \
    ca-certificates \
    sudo \
    locales \
    fonts-liberation \
    python3.7 \
    curl \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen


RUN ln -sf /usr/bin/python3.6 /usr/local/bin/python3 &&\
         ln -sf /usr/local/bin/pip /usr/local/bin/pip3

# Install Tini
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.10.0/tini && \
    echo "1361527f39190a7338a0b434bd8c88ff7233ce7b9a4876f3315c22fce7eca1b0 *tini" | sha256sum -c - && \
    mv tini /usr/local/bin/tini && \
    chmod +x /usr/local/bin/tini

# Configure environment
ENV CONDA_DIR=/opt/conda \
    SHELL=/bin/bash \
    NB_USER=Deep_Learner \
    NB_UID=1000 \
    NB_GID=100 \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8
ENV PATH=$CONDA_DIR/bin:$PATH \
    HOME=/home/$NB_USER

ADD fix-permissions /usr/local/bin/fix-permissions
# Create Deep_Learner user with UID=1000 and in the 'users' group
# and make sure these dirs are writable by the `users` group.
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    mkdir -p $CONDA_DIR && \
    chown $NB_USER:$NB_GID $CONDA_DIR && \
    fix-permissions $HOME && \
    fix-permissions $CONDA_DIR

USER $NB_USER

# Install conda as Deep_Learner and check the md5 sum provided on the download site
ENV MINICONDA_VERSION latest
RUN cd /tmp && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh && \
    #echo "a946ea1d0c4a642ddf0c3a26a18bb16d *Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh" | md5sum -c - && \
    /bin/bash Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh && \
    $CONDA_DIR/bin/conda config --system --prepend channels conda-forge && \
    $CONDA_DIR/bin/conda config --system --set auto_update_conda false && \
    $CONDA_DIR/bin/conda config --system --set show_channel_urls true && \
    $CONDA_DIR/bin/conda update --all --quiet --yes && \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR



# Install Python, Jupyter Notebook and Hub
RUN conda install -y \
    'notebook' \
    'jupyterhub' \
    'jupyter' \
    'six' \
     &&\
    fix-permissions $CONDA_DIR

# R-kernel
RUN conda create  -n r-kernel \
     -c r r-irkernel \
        &&\
        fix-permissions $CONDA_DIR

ADD docker/environment-r.yml .setup/
RUN conda env update -n r-kernel -q -f .setup/environment-r.yml && \
    /opt/conda/envs/r-kernel/bin/Rscript -e "IRkernel::installspec(displayname='R')" \
    &&\
    fix-permissions $CONDA_DIR
USER root
RUN apt-get update && apt-get upgrade
RUN apt-get install -y -q \
    libxrender1 \
    libsm6
USER $NB_USER
#RUN /opt/conda/envs/r-kernel/bin/pip install ipykernel --user --name deep_learning_python2 --display-name 'R'

# Setup work directory for backward-compatibility
RUN mkdir /home/$NB_USER/private && \
    fix-permissions /home/$NB_USER
RUN mkdir /home/$NB_USER/private/local && \
    fix-permissions /home/$NB_USER

RUN python3 -m ipykernel install --user --display-name 'DLM Py3'

#COPY --chown=1000:100 logo-64x64.png /home/Deep_Learner/.local/share/jupyter/kernels/python3/
#COPY --chown=1000:100 logo-32x32.png /home/Deep_Learner/.local/share/jupyter/kernels/python3/

#COPY --chown=1000:100 logo-32x32.png /opt/conda/share/jupyter/kernels/python3/
#COPY --chown=1000:100 logo-64x64.png /opt/conda/share/jupyter/kernels/python3/

COPY --chown=1000:100 docker/logo.png /opt/conda/lib/python3.7/site-packages/notebook/static/custom/
COPY --chown=1000:100 docker/custom.css /opt/conda/lib/python3.7/site-packages/notebook/static/custom/


RUN   fix-permissions $CONDA_DIR &&\
      fix-permissions /home/$NB_USER

USER root


EXPOSE 8888
WORKDIR $HOME

# Configure container startup
ENTRYPOINT ["tini", "--"]
CMD ["start-notebook.sh"]

# Add local files as late as possible to avoid cache busting
COPY start.sh /usr/local/bin/
COPY start-notebook.sh /usr/local/bin/
COPY start-singleuser.sh /usr/local/bin/
#COPY ~/jupyterhub/jupyter_notebook_config.py /etc/jupyter/
#RUN fix-permissions /etc/jupyter/

# Switch back to Deep_Learner to avoid accidental container runs as root
USER $NB_USER
