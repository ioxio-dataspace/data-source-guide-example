from typing import Optional

import typer
import uvicorn

from tasks.common import uvicorn_common

cli = typer.Typer()


@cli.command()
def serve(port: Optional[int] = None):
    uvicorn_params = {**uvicorn_common()}
    if port:
        uvicorn_params["port"] = port

    server = uvicorn.Server(
        uvicorn.Config(reload=False, **uvicorn_params),
    )
    server.run()


if __name__ == "__main__":
    cli()
