FROM mokari94/spark-base:latest

##### SPARK FIX #####

# Because we're not using the defaut start-up routine, we manually need to add a name to Spark's UID 
# (which, yes, I hereby hardcode to the default of 185)
# If you don't do this, you'll have hours of debugging a 
# javax.security.auth.login.LoginException: java.lang.NullPointerException: invalid null input: name
# exception ahead of you.
RUN echo '185:x:185:0:anonymous uid:/opt/spark:/bin/false' >> /etc/passwd 

##### CONDA #####
# Prepare installation as root
USER 0

RUN apt-get update -y && \
    apt-get install -y \
        wget

RUN chmod 777 /opt
    
# Back to the default UID for Spark
USER 185

# Install
RUN wget --progress=dot:mega https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3

ENV PATH="/opt/miniconda3/bin:${PATH}"
ENV PATH="/opt/miniconda3/condabin:${PATH}"

##### PYTHON PACKAGE DEPENDENCIES #####
WORKDIR /opt/spark/work-dir

COPY env.yml env.yml
RUN conda env update -f env.yml --name base

##### APP #####
ENV PYTHONUNBUFFERED=.

COPY app.py app.py

ENTRYPOINT [ "/opt/entrypoint.sh" ]