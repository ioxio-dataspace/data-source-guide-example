from os import environ

import uvicorn
from invoke import task
from uvicorn.supervisors import ChangeReload


# Task to run the FastAPI app using Uvicorn
@task
def dev(ctx, port=8000):
    """Run the FastAPI app with Uvicorn."""
    host = "0.0.0.0"  # nosec, it's not a mistake
    port = environ.get("PORT", port)

    config = uvicorn.Config(
        app="app.app:app",
        host=host,
        port=int(port),
        reload=True,
        log_level="debug",
    )
    server = uvicorn.Server(config)

    supervisor = ChangeReload(config, target=server.run, sockets=[config.bind_socket()])
    supervisor.run()


@task
def serve(ctx, port=8000):
    host = "0.0.0.0"  # nosec
    port = environ.get("PORT", port)
    server = uvicorn.Server(
        uvicorn.Config(app="app.app:app", host=host, port=int(port)),
    )
    server.run()
