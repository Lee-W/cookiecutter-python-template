from __future__ import annotations

from invoke.collection import Collection
from invoke.context import Context
from invoke.tasks import task

from tasks import doc, env, git, secure, style, test
from tasks.build import build_ns
from tasks.common import VENV_PREFIX


@task
def run_pre_commit_hooks(context: Context) -> None:
    """Run pre-commit hooks on all files"""
    context.run(f"{VENV_PREFIX} pre-commit run --all-files --hook-stage pre-push")


ns = Collection()
ns.add_collection(env)  # type: ignore[arg-type]
ns.add_collection(git)  # type: ignore[arg-type]
ns.add_collection(test)  # type: ignore[arg-type]
ns.add_collection(style)  # type: ignore[arg-type]
ns.add_collection(build_ns)
ns.add_collection(secure)  # type: ignore[arg-type]
ns.add_collection(doc)  # type: ignore[arg-type]
ns.add_task(run_pre_commit_hooks)  # type: ignore[arg-type]
