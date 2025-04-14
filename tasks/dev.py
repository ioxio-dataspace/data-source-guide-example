from os import environ, system

import typer
import uvicorn
from uvicorn.supervisors import ChangeReload

from tasks.common import DEV_ENV, uvicorn_common

cli = typer.Typer()


@cli.command()
def dev():
    """Run the FastAPI app with Uvicorn."""
    system("poetry install")  # nosec

    environ.update(DEV_ENV)

    config = uvicorn.Config(
        log_level="debug",
        reload=True,
        **uvicorn_common(),
    )
    server = uvicorn.Server(config)

    supervisor = ChangeReload(config, target=server.run, sockets=[config.bind_socket()])
    supervisor.run()


if __name__ == "__main__":
    cli()
