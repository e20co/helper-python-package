FROM e20co/base-python:bionic

RUN pip3 install --upgrade pip

COPY helper_python /run/helper_python/
RUN chmod +x /run/helper_python/test.sh
WORKDIR /run/helper_python

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

ADD run.sh /
RUN chmod +x /run.sh

# Run application
CMD ["/run.sh"]
