FROM python:3.7

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A6DCF7707EBC211F

RUN apt-get update\
    && apt-get install -y software-properties-common git python3-pip build-essential libssl-dev libffi-dev python3.7-dev\
    && apt-get install -y unixodbc-dev
    && rm -rf /var/lib/apt/lists/*
    
# Install Firefox browser
RUN apt-add-repository "deb http://ppa.launchpad.net/ubuntu-mozilla-security/ppa/ubuntu bionic main"
RUN apt update && apt install -y firefox

ENV GIT_URL https://github.com/mehalyna/CH_096_TAQC.git
# ENV PATH_PROJECT /CH_096_TAQC

# Get POM and tests from git
RUN git clone $GIT_URL
WORKDIR $WORKSPACE/CH_096_TAQC

# RUN apt-get install build-essential libssl-dev libffi-dev python3-dev
# Create venv
RUN pip install -r requirements.txt

#Set "root" of CH_096_TAQC project
WORKDIR $WORKSPACE/CH_096_TAQC
RUN ls Tests
RUN pwd

# ENTRYPOINT ["/bin/bash"]
CMD ["py.test", "-v", "--rootdir=Tests", "--alluredir=/CH_096_TAQC/Reports_Allure"]
