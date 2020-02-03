FROM python:3.7

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A6DCF7707EBC211F

RUN apt-get update\
    && apt-get install -y software-properties-common git python3-pip build-essential libssl-dev libffi-dev python3.7-dev \
    && apt-get install -y unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*
    
# Install Firefox browser
RUN apt-add-repository "deb http://ppa.launchpad.net/ubuntu-mozilla-security/ppa/ubuntu bionic main"
RUN apt update && apt install -y firefox

# Get POM and tests from git
RUN git clone https://github.com/mehalyna/CH_096_TAQC.git

# Attach credentials to the cloned code
WORKDIR $WORKSPACE/CH_096_TAQC
COPY credentials.py $WORKSPACE/CH_096_TAQC

# Create venv
RUN pip install -r requirements.txt

# Create required service dirs
RUN mkdir Reports_Allure && mkdir Logs
# Set environment variables to be passed from outside a container
ENV TEST_COLLECTION="Tests"
ENV SELECTED="all"
# ENTRYPOINT ["/bin/bash"]
CMD ["py.test", "$TEST_COLLECTION", "-k", "$SELECTED", "--alluredir=/CH_096_TAQC/Reports_Allure"]
