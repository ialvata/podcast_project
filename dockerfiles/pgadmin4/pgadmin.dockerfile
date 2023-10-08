FROM dpage/pgadmin4
COPY ["servers.json","/pgadmin4"]
ENTRYPOINT ["/entrypoint.sh", "-c"]
# The <src> path must be inside the context of the build;