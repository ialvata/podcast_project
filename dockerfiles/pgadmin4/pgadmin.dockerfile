FROM dpage/pgadmin4
COPY ["server.json","/pgadmin4"]
ENTRYPOINT ["/bin/sh", "-c"]
# The <src> path must be inside the context of the build;