FROM alliancecostarica/climmob_base:20200815

MAINTAINER Alliance Bioversity-CIAT

WORKDIR /opt
RUN mkdir climmob_repository
VOLUME /opt/climmob_repository

RUN mkdir climmob_log
VOLUME /opt/climmob_log

RUN mkdir climmob_celery
VOLUME /opt/climmob_celery

RUN mkdir climmob_plugins
VOLUME /opt/climmob_plugins

RUN mkdir climmob_gunicorn
RUN python3 -m venv climmob_env

RUN git clone https://github.com/qlands/FormShare.git -b stable-2.6.8 formshare
RUN . ./formshare_env/bin/activate && pip install wheel && pip install -r /opt/formshare/requirements.txt && python /opt/formshare/download_nltk_packages.py

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.6.0/wait /wait
RUN chmod +x /wait

WORKDIR /opt
RUN mkdir formshare_config
VOLUME /opt/formshare_config

COPY docker_files/etc/default/celery_climmob /etc/default/celery_formshare
COPY docker_files/etc/init.d/celery_climmob /etc/init.d/celery_formshare
COPY ./docker_files/run_server.sh /opt/formshare_gunicorn
COPY ./docker_files/docker-entrypoint.sh /

EXPOSE 5900

RUN chmod +x /docker-entrypoint.sh
RUN chmod +x /etc/init.d/celery_formshare
RUN chmod +x /opt/formshare_gunicorn/run_server.sh
RUN chmod 640 /etc/default/celery_formshare
RUN ldconfig
ENTRYPOINT ["/docker-entrypoint.sh"]