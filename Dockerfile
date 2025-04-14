# ---- BUILD ENVIRONMENT ----- #

FROM ghcr.io/ioxiocom/python-base:ubuntu24.04-python3.13 AS build

WORKDIR /src/data-source-guide-example

ADD docker/build-prepare.sh /src/docker/build-prepare.sh
RUN bash /src/docker/build-prepare.sh

ADD pyproject.toml poetry.lock ./
ADD docker/build-setup.sh /src/docker/build-setup.sh
RUN --mount=type=cache,uid=2000,gid=2000,target=/home/${USER}/.cache bash /src/docker/build-setup.sh


# ---- RUNTIME ENVIRONMENT ----- #

FROM ghcr.io/ioxiocom/python-base:ubuntu24.04-python3.13 AS runtime

COPY --from=build ${WORKON_HOME} ${WORKON_HOME}

WORKDIR /src/data-source-guide-example
ADD . ./

RUN bash docker/runtime-prepare.sh

USER ${USER}
EXPOSE 8000
ENTRYPOINT ["bash", "docker/runtime-entrypoint.sh"]
