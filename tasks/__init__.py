from invoke import Collection

from tasks import doc, env, git, secure, style, test
from tasks.build import build_ns

ns = Collection()
ns.add_collection(env)  # type: ignore[arg-type]
ns.add_collection(git)  # type: ignore[arg-type]
ns.add_collection(test)  # type: ignore[arg-type]
ns.add_collection(style)  # type: ignore[arg-type]
ns.add_collection(build_ns)
ns.add_collection(secure)  # type: ignore[arg-type]
ns.add_collection(doc)  # type: ignore[arg-type]
