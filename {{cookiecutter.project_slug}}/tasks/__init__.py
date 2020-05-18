from invoke import Collection

from tasks import doc, env, git, secure, style, test
from tasks.build import build_ns

ns = Collection()
ns.add_collection(env)
ns.add_collection(git)
ns.add_collection(test)
ns.add_collection(style)
ns.add_collection(build_ns)
ns.add_collection(doc)
ns.add_collection(secure)
