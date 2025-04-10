from invoke import task


# Task to run the FastAPI app using Uvicorn
@task
def dev(ctx):
    """Run the FastAPI app with Uvicorn."""
    ctx.run("poetry run uvicorn app.app:app --reload", pty=True)
