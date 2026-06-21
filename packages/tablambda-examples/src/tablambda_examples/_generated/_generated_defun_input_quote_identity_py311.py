# Generated, self-contained module: the import header is added at serialization time (see
# tablambda._defunctionalize.runnable_defun_module); the body is emitted by the DEFUN lambda
# term and content-addressed by compiled dataclass shape.
from tablambda._defun_runtime import Closure, Thunk, interned

@interned
class vg_23c02d03a51f842e(Closure):

    def __call__(self, a):
        return vg_eab3e33b86d031f1()

@interned
class vg_3186342fbb3bc969(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_96ace814564870ef(self.cap_0)

@interned
class vg_54dc8207c20e7d33(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, vg_e43a8b0f1b4bed47())

@interned
class vg_5790a50754fc667f(Closure):

    def __call__(self, a):
        return a

@interned
class vg_96ace814564870ef(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, vg_9dd83a0b38353a6c())

@interned
class vg_9dd83a0b38353a6c(Closure):

    def __call__(self, a):
        return vg_5790a50754fc667f()

@interned
class vg_e43a8b0f1b4bed47(Closure):

    def __call__(self, a):
        return vg_3186342fbb3bc969(a)

@interned
class vg_eab3e33b86d031f1(Closure):

    def __call__(self, a):
        return vg_54dc8207c20e7d33(a)
compiled = vg_23c02d03a51f842e()