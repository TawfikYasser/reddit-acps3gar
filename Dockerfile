# FROM apache/airflow:2.7.1-python3.9

# USER root

# # Create the log directory and set appropriate permissions
# RUN mkdir -p /opt/airflow/logs \
#     && chown -R airflow: /opt/airflow/logs \
#     && chmod -R 775 /opt/airflow/logs

# # Add the airflow user to the sudo group
# RUN usermod -aG sudo airflow

# COPY requirements.txt /opt/airflow/

# RUN apt-get update && apt-get install -y gcc python3-dev sudo

# USER airflow

# RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

# FROM apache/airflow:2.7.1-python3.9

# USER root

# RUN mkdir -p /opt/airflow/logs/scheduler/2024-04-20

# # Create the log directory and set appropriate permissions
# RUN mkdir -p /opt/airflow/logs \
#     && chown -R airflow:root /opt/airflow/logs \
#     && chmod -R 775 /opt/airflow/logs

# COPY requirements.txt /opt/airflow/

# RUN apt-get update && apt-get install -y gcc python3-dev

# USER airflow

# RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

# FROM apache/airflow:2.7.1-python3.9

# USER root

# # Create the log directory and set appropriate permissions
# RUN mkdir -p /opt/airflow/logs \
#     && chown -R airflow:root /opt/airflow/logs \
#     && chmod -R 775 /opt/airflow/logs

# COPY requirements.txt /opt/airflow/

# RUN apt-get update && apt-get install -y gcc python3-dev

# USER airflow

# RUN mkdir -p /opt/airflow/logs/dag_processor_manager \
#     && chown -R airflow:root /opt/airflow/logs/dag_processor_manager \
#     && chmod -R 775 /opt/airflow/logs/dag_processor_manager \
#     && pip install --no-cache-dir -r /opt/airflow/requirements.txt


FROM apache/airflow:2.7.1-python3.9

USER root

# Set permissions on directories where Airflow needs to write
RUN mkdir -p /opt/airflow/{data,logs,pipelines}
RUN chown -R airflow: /opt/airflow/{data,logs,pipelines}

# Install additional dependencies
RUN apt-get update && apt-get install -y gcc python3-dev

USER airflow

COPY requirements.txt /opt/airflow/

RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

