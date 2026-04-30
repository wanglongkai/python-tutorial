import sys as _sys
import os as _os
import importlib as _importlib

# The local "fastapi" directory shadows the installed fastapi package.
# Re-export everything from the real fastapi and merge package paths
# so that subpackages (fastapi.templating, etc.) resolve correctly.
_here = _os.path.dirname(_os.path.abspath(__file__))
_parent = _os.path.dirname(_here)

# Pop this module from cache temporarily so we can import the real one
_self = _sys.modules.pop(__name__, None)

# Hide the local directory so the real fastapi is found
_path_filtered = [p for p in _sys.path if _os.path.abspath(p) != _parent]
_orig_path = _sys.path[:]
_sys.path[:] = _path_filtered

# Import the real fastapi from site-packages
_real = _importlib.import_module("fastapi")

# Restore sys.path
_sys.path[:] = _orig_path

# Merge __path__ so subpackages (templating, etc.) resolve in both locations
__path__[:] = list(__path__) + [p for p in _real.__path__ if p not in __path__]

# Restore our module in the cache
_sys.modules[__name__] = _self

# Merge real fastapi's public namespace into ours
for _attr in dir(_real):
    if not _attr.startswith("_"):
        globals()[_attr] = getattr(_real, _attr)

del _sys, _os, _importlib, _here, _parent, _self, _path_filtered, _orig_path, _real, _attr
