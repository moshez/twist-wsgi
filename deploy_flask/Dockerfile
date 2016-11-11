FROM python:2.7.12
COPY twist.pex /
RUN /twist.pex || true
ENTRYPOINT ["/twist.pex", "sayhello", "--port", "8080"]
