# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

FROM digitalanatomist/base-notebook-cuda10-ubuntu18.04:latest

MAINTAINER Samir Jabari <samir.jabari@fau.de>
#MAINTAINER aburnap@mit.edu
#MAINTAINER Jupyter Project <jupyter@googlegroups.com>

# For CUDA profiling, TensorFlow requires CUPTI.
#ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
#ENV CUDA_HOME=/usr/local/cuda
#ENV CUDA_ROOT=$CUDA_HOME
#ENV PATH=$PATH:$CUDA_ROOT/bin:$HOME/bin
#ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CUDA_ROOT/lib64

# For CUDA profiling, TensorFlow requires CUPTI.
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:/usr/local/cuda/lib64:$LD_LIBRARY_PATH


USER root
RUN apt-get update

RUN ln -sf /usr/bin/python3.7 /usr/local/bin/python3 &&\
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


RUN python3 -m pip install  \
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
    jupyter-tensorboard \
    jupyter_contrib_nbextensions \
    torchsummary \
    dataclasses \
    fastprogress \
    opencv-python \
    ipywidgets \
    nvidia-ml-py3 \
    scikit-multilearn \
    keras-lr-finder \
    keras-lr-multiplier \
    feature-selector \
    mlens \
    xgboost \
    vecstack \
    &&\
    fix-permissions $CONDA_DIR &&\
    fix-permissions /home/$NB_USER

RUN conda install -c defaults -c anaconda -c conda-forge -c pytorch -c fastai -y   \
      tensorboard \
      tensorflow-gpu=1.14.0 \
      keras \
      fastai \
      libjpeg-turbo &&\
      fix-permissions $CONDA_DIR &&\
      fix-permissions /home/$NB_USER

RUN python3 -m pip uninstall -y pillow pil jpeg libtiff libjpeg-turbo
RUN conda uninstall -y --force pillow pil jpeg libtiff libjpeg-turbo
RUN conda install -c conda-forge libjpeg-turbo
RUN CC="cc -mavx2" python3 -m pip install --no-cache-dir -U --force-reinstall pillow-simd
#RUN CFLAGS="${CFLAGS} -mavx2"  /opt/conda/bin/python -m pip install --upgrade --no-cache-dir --force-reinstall --no-binary :all: --compile pillow-simd
RUN conda install  -c zegami  -y   \
            libtiff-libjpeg-turbo &&\
            fix-permissions $CONDA_DIR &&\
            fix-permissions /home/$NB_USER

RUN conda install -y \
            jpeg \
            libtiff &&\
            fix-permissions $CONDA_DIR &&\
            fix-permissions /home/$NB_USER
            
RUN conda install pytorch torchvision cudatoolkit=10.0 -c pytorch &&\
    fix-permissions $CONDA_DIR &&\
    fix-permissions /home/$NB_USER            

EXPOSE 5000 6006

USER $NB_USER

# cleanup
 #RUN 	apt-get autoremove -y && \
  # apt-get autoclean && \
  # apt-get clean && \
 #rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
