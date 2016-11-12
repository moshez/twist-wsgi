FROM python:2.7.12
COPY twist.pex /
RUN /twist.pex 2>/dev/null || true
ENTRYPOINT ["/twist.pex", "sayhello", "--port", "lets:/srv/www/certs:tcp:443"]
