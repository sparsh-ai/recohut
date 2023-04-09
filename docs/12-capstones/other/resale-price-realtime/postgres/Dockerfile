FROM postgres:10.4
COPY ./sql/* /docker-entrypoint-initdb.d/
CMD ["postgres", "-c", "wal_level=logical"]