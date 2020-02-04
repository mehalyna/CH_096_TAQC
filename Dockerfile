FROM python:3.7

RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A6DCF7707EBC211F \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

RUN apt-get update\
    && apt-get install -y software-properties-common git python3-pip build-essential libssl-dev libffi-dev python3.7-dev \
    && apt-get install -y unixodbc-dev
RUN ACCEPT_EULA=Y apt-get install msodbcsql17
RUN ACCEPT_EULA=Y apt-get install mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
# RUN source ~/.bashrc
RUN rm -rf /var/lib/apt/lists/*
    
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
ENTRYPOINT ["py.test", "--alluredir=/CH_096_TAQC/Reports_Allure", "$TEST_COLLECTION", "-k", "$SELECTED"]
#CMD ["py.test", "--alluredir=/CH_096_TAQC/Reports_Allure", "$TEST_COLLECTION", "-k", "$SELECTED"]
