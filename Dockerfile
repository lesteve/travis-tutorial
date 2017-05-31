FROM continuumio/miniconda

ARG numpy_version

RUN conda install pytest numpy=$numpy_version --yes
