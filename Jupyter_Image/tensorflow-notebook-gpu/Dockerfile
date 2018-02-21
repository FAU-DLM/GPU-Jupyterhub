# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
FROM base-notebook-gpu

MAINTAINER Samir Jabari <samir.jabari@fau.de>
#MAINTAINER aburnap@mit.edu
#MAINTAINER Jupyter Project <jupyter@googlegroups.com>

USER root

# Install all OS dependencies for fully functional notebook server
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    freeglut3-dev \
    libcupti-dev \
    libcurl3-dev \
    libfreetype6-dev \
    libpng12-dev \
    libzmq3-dev \
    pkg-config \
    unzip \
    python3 \
    python3-pip \
    python3-setuptools \
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
    libjasper-dev \
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
    python3-dev \
    python3-tk \
    ant \
    default-jdk \
    doxygen \
      && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y --no-install-recommends \
    bc \
    cmake \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
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
  apt-get autoremove && \
rm -rf /var/lib/apt/lists/*


# libav-tools for matplotlib anim
RUN apt-get update && \
    apt-get install -y --no-install-recommends libav-tools && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN pip3 install --upgrade pip


RUN pip3 --no-cache-dir install --upgrade ipython \
    Pillow \
    h5py \
    ipykernel \
    jupyter \
    matplotlib==2.0.2 \
    seaborn \
    numpy \
    pandas \
    scipy \
    sklearn \
    bcolz \
    Cython \
    path.py \
    six \
    sphinx \
    wheel \
    zmq \
    pygments \
    Flask \
    statsmodels \
    && \
python3 -m ipykernel.kernelspec



RUN conda install -c aaronzs tensorflow  && \
  fix-permissions $CONDA_DIR
RUN conda install -c aaronzs tensorflow-gpu && \
  fix-permissions $CONDA_DIR

RUN conda install -c anaconda keras && \
  fix-permissions $CONDA_DIR


# install pytorch
RUN conda install pytorch torchvision  cuda90 -c pytorch && \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR


# Install OpenSlide
RUN apt-get update && apt-get install -y openslide-tools
#RUN pip install --upgrade pip && pip install openslide-python
RUN apt-get update && apt-get install -y python3-openslide &&\
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN conda install -c conda-forge opencv  && \
    fix-permissions $CONDA_DIR
RUN  conda install -c conda-forge/label/broken opencv && \
    fix-permissions $CONDA_DIR


RUN apt update && apt install -y libvips libvips-dev libvips-tools libopenslide-dev

ENV CUDA_HOME /usr/local/cuda-9.0
ENV LD_LIBRARY_PATH /usr/local/cuda-9.0:/usr/local/cuda-9.0/lib64:$LD_LIBRARY_PATH
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
ENV LIBRARY_PATH $LD_LIBRARY_PATH

# Install facets which does not have a pip or conda package at the moment
RUN cd /tmp && \
    git clone https://github.com/PAIR-code/facets.git && \
    cd facets && \
    jupyter nbextension install facets-dist/ --sys-prefix && \
    rm -rf facets && \
    fix-permissions $CONDA_DIR


RUN conda install --yes \
    'matplotlib=2.0.*' \
    'jupyter' \
    'numpy=1.14.*' &&\
  fix-permissions /home/$NB_USER

# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \
    fix-permissions /home/$NB_USER

# -->jupyter-tensorboard does not work yet 
# RUN pip3 install --pre jupyter-tensorboard &&\
#     fix-permissions /home/$NB_USER


EXPOSE 5000 6006
USER $NB_USER


# cleanup
RUN apt-get autoremove -y && \
    apt-get autoclean && \
    apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
