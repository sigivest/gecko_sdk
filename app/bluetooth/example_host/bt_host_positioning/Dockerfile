# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12.3-bookworm

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN adduser -u 5678 --disabled-password --gecos "" appuser

RUN apt update

RUN apt install -y mosquitto build-essential libmosquitto-dev git gdb
RUN > /etc/mosquitto/mosquitto.conf
RUN echo "listener 1883" >> /etc/mosquitto/mosquitto.conf
RUN echo "allow_anonymous true" >> /etc/mosquitto/mosquitto.conf

# # Install pip requirements
# COPY requirements.txt .
# RUN python -m pip install -r requirements.txt

WORKDIR /sigivest/app

RUN git clone https://github.com/sigivest/gecko_sdk.git --recursive
WORKDIR /sigivest/app/gecko_sdk/app/bluetooth/example_host/bt_aoa_host_locator
RUN make -j$(nproc)
WORKDIR /sigivest/app/gecko_sdk
RUN bash -l -c 'echo export GECKO_REMOTE="`git config --get remote.origin.url`" >> /home/appuser/.bashrc'
RUN bash -l -c 'echo export GECKO_COMMIT_HASH="`git rev-parse HEAD`" >> /home/appuser/.bashrc'
RUN mkdir /sigivest/bt_aoa_host_locator && cp ./app/bluetooth/example_host/bt_aoa_host_locator/exe/bt_aoa_host_locator /sigivest/bt_aoa_host_locator
RUN cp -r /sigivest/app/gecko_sdk/app/bluetooth/example_host/bt_aoa_host_locator/config /sigivest/bt_aoa_host_locator

# RUN rm -rf /sigivest/app/gecko_sdk

#COPY ./apis /sigivest/apis
#COPY ./app /sigivest/app
#COPY ./spawn.sh /sigivest

WORKDIR /sigivest/app
#RUN rm -rf sigivest_apis
#RUN rm -rf google
#RUN mkdir sigivest_apis
#RUN python -m grpc_tools.protoc -I ../apis --pyi_out=./sigivest_apis --python_out=./sigivest_apis --grpc_python_out=./sigivest_apis $(find ../apis -iname "*.proto") 
#RUN mv sigivest_apis/google .


# Creates a non-root user with an explicit UID and adds permission to access the /sigivest folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN chown -R appuser /sigivest
USER appuser




#EXPOSE 50001
WORKDIR /sigivest
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["/sigivest/bt_aoa_host_locator"]
