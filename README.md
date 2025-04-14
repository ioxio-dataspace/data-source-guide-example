# Data Source Guide Example - Weather API

A simple weather API built with FastAPI. This API provides random weather data based on latitude and longitude coordinates.

## Requirements

- [Pre-commit](https://pre-commit.com/#install)
- [Python 3.11+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)

To set up the `pre-commit` hooks, run `pre-commit install` in the repo. After it you can
manually run `pre-commit` only for your changes or `pre-commit run --all-files` for all
files.

### Install Dependencies

To install dependencies, first set up your environment with Poetry:

```bash
# Using Poetry
poetry install

### Run the App

To run the app locally, execute the following command:

poetry run dev
```

### Docker

Make sure [Docker](https://docs.docker.com/install/) is installed.

```shell
docker build -t data-source-guide-example .
docker run -p 8000:8000 --rm -it data-source-guide-example
```

## License

This code is released under the BSD 3-Clause license. Details in the
[LICENSE.md](./LICENSE.md) file.

## Guides and help

[Written guide for how to build a data source](https://docs.ioxio.dev/guides/building-a-data-source/)

You can also check out our YouTube tutorial:

[![Defining Data Products for the IOXIO® Dataspace technology
](https://img.youtube.com/vi/f-f6P_-8zoQ/0.jpg)](http://www.youtube.com/watch?v=f-f6P_-8zoQ)

Also join our [IOXIO Community Slack](https://slack.ioxio.com/)
