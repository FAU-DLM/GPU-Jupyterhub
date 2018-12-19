# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

FROM digitalanatomist/base-notebook-CUDA10-ubuntu18.04:latest


MAINTAINER Samir Jabari <samir.jabari@fau.de>
#MAINTAINER aburnap@mit.edu
#MAINTAINER Jupyter Project <jupyter@googlegroups.com>

# For CUDA profiling, TensorFlow requires CUPTI.
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
ENV CUDA_HOME=/usr/local/cuda
ENV CUDA_ROOT=$CUDA_HOME
ENV PATH=$PATH:$CUDA_ROOT/bin:$HOME/bin
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CUDA_ROOT/lib64

USER root
RUN apt-get update

RUN ln -sf /usr/bin/python3.6 /usr/local/bin/python3 &&\
    ln -sf /usr/local/bin/pip /usr/local/bin/pip3

# Install all OS dependencies for fully functional notebook server
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    freeglut3-dev \
    libcupti-dev \
    libcurl3-dev \
    libfreetype6-dev \
    libzmq3-dev \
    pkg-config \
    unzip \
    rsync \
    software-properties-common \
    inkscape \
    jed \
    libsm6 \
    libxext-dev \
    libxrender1 \
    lmodern \
    pandoc \
    vim \
    libpng-dev \
    g++ \
    gfortran \
    libffi-dev \
    libhdf5-dev \
    libjpeg-dev \
    liblcms2-dev \
    libopenblas-dev \
    liblapack-dev \
    libssl-dev \
    libtiff5-dev \
    libwebp-dev \
    nano \
    libopenslide-dev \
    wget \
    zlib1g-dev \
    qt5-default \
    libvtk6-dev \
    libopenexr-dev \
    libgdal-dev \
    libdc1394-22-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libtheora-dev \
    libvorbis-dev \
    libxvidcore-dev \
    libx264-dev \
    yasm \
    libopencore-amrnb-dev \
    libopencore-amrwb-dev \
    libv4l-dev \
    libxine2-dev \
    libtbb-dev \
    libeigen3-dev \
    ant \
    default-jdk \
    doxygen \
    bc \
    cmake \
    python-dev \
    python-tk \
    python-setuptools \
    python-numpy \
    python-scipy \
    python-nose \
    python-h5py \
    python-skimage \
    python-matplotlib \
    python-pandas \
    python-sklearn \
    python-sympy \
    python3-dev \
    python3-tk \
    python3-setuptools \
    python3-numpy \
    python3-scipy \
    python3-nose \
    python3-h5py \
    python3-skimage \
    python3-matplotlib \
    python3-pandas \
    python3-sklearn \
    python3-sympy \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Installing OpenSlide
RUN apt-get update && apt-get install -y openslide-tools
RUN apt-get update && apt-get install -y python3-openslide &&\
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Installing Libvips
RUN apt update && apt install -y libvips libvips-dev libvips-tools libopenslide-dev


RUN /opt/conda/envs/deep_learning_python3/bin/python -m pip install  \
    scikit-image \
    pandas \
    tqdm \
    imgaug \
    kaggle \
    pydicom \
    tensorboardX \
    tensorflow-tensorboard \
    sklearn \
    plotly \
    pretrainedmodels \
    seaborn \
    keras \
    skorch \
    ignite  \
    graphviz \
    sklearn_pandas \
    isoweek \
    pandas_summary \
    spacy\
    pypng \
    torchtext \
    Pillow \
    h5py \
    ipykernel \
    jupyter \
    matplotlib \
    numpy \
    scipy \
    bcolz \
    Cython \
    path.py \
    six \
    sphinx \
    wheel \
    pygments \
    Flask \
    statsmodels \
    ipython \
    scikit-learn \
    zmq \
    openslide-python \
    jupyter-tensorboard &&\
    fix-permissions $CONDA_DIR &&\
    fix-permissions /home/$NB_USER

RUN /opt/conda/envs/deep_learning_python2/bin/python -m pip install  \
    scikit-image \
    pandas \
    tqdm \
    imgaug \
    kaggle \
    pydicom \
    tensorboardX \
    tensorflow-tensorboard \
    sklearn \
    plotly \
    pretrainedmodels \
    seaborn \
    keras \
    skorch \
    ignite  \
    graphviz \
    sklearn_pandas \
    isoweek \
    pandas_summary \
    spacy\
    pypng \
    torchtext \
    Pillow \
    h5py \
    ipykernel \
    jupyter \
    matplotlib \
    numpy \
    scipy \
    bcolz \
    Cython \
    path.py \
    six \
    sphinx \
    wheel \
    pygments \
    Flask \
    statsmodels \
    ipython \
    scikit-learn \
    zmq \
    openslide-python \
    jupyter-tensorboard &&\
    fix-permissions $CONDA_DIR &&\
    fix-permissions /home/$NB_USER

# Installing OpenCV TensorFlow Kerasand Pytorch into the environments
RUN conda install -n deep_learning_python2 -y  \
    opencv \
    tensorboard \
    tensorflow-gpu=1.12.0 \
    keras \
    pytorch torchvision  cuda100 -c pytorch &&\
    fix-permissions $CONDA_DIR &&\
    fix-permissions /home/$NB_USER

RUN conda install -n deep_learning_python3   \
      opencv \
      tensorboard \
      tensorflow-gpu=1.12.0 \
      keras \
      pytorch torchvision  cuda100 -c pytorch &&\
      fix-permissions $CONDA_DIR &&\
      fix-permissions /home/$NB_USER

RUN conda install --yes \
    'tensorflow-gpu==1.11.0' &&\
    fix-permissions $CONDA_DIR &&\
    fix-permissions /home/$NB_USER

# Import matplotlib the first time to build the font cache.
#ENV XDG_CACHE_HOME /home/$NB_USER/.cache/
#RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \
    #fix-permissions /home/$NB_USER

# Install facets which does not have a pip or conda package at the moment
#RUN cd /tmp && \
#    git clone https://github.com/PAIR-code/facets.git && \
#    cd facets && \
#    /opt/conda/envs/deep_learning_python2/bin/ jupyter nbextension install facets-dist/ --sys-prefix && \
#    /opt/conda/envs/deep_learning_python3/bin/ jupyter nbextension install facets-dist/ --sys-prefix && \
#    rm -rf facets && \
#    fix-permissions $CONDA_DIR &&\
#    fix-permissions /home/$NB_USER

RUN python3.6 -m pip install --upgrade --force-reinstall --no-cache-dir --ignore-installed  --pre \
   jupyter-tensorboard &&\
   fix-permissions $CONDA_DIR &&\
   fix-permissions /home/$NB_USER


EXPOSE 5000 6006

USER root

# Autodetects jupyterhub and standalone modes
#COPY jupyter_notebook_config.py /root/.jupyter/
#COPY run_jupyter.sh /usr/local/bin/

#RUN chmod +x /usr/local/bin/run_jupyter.sh

#CMD ["/usr/local/bin/run_jupyter.sh", "--allow-root"]


USER $NB_USER
CMD ["start-notebook.sh"]

#COPY start-notebook.sh /usr/local/bin/


#USER $NB_USER

# cleanup
 #RUN 	apt-get autoremove -y && \
  # apt-get autoclean && \
  # apt-get clean && \
 #rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
