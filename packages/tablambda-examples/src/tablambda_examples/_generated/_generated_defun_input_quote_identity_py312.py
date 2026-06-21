# Generated, self-contained module: the import header is added at serialization time (see
# tablambda._defunctionalize.runnable_defun_module); the body is emitted by the DEFUN lambda
# term and content-addressed by compiled dataclass shape.
from tablambda._defun_runtime import Closure, Thunk, interned

@interned
class vg_0a65f83f04cd81b6(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_e73ebd7ced903053(self.cap_0)

@interned
class vg_202935e60239610c(Closure):

    def __call__(self, a):
        return vg_8e0012278c0a741b(a)

@interned
class vg_8e0012278c0a741b(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, vg_f2e6499880a78b37())

@interned
class vg_aba1d9025faa3124(Closure):

    def __call__(self, a):
        return vg_fa2ecd93b3d53620()

@interned
class vg_e73ebd7ced903053(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, vg_aba1d9025faa3124())

@interned
class vg_f2e6499880a78b37(Closure):

    def __call__(self, a):
        return vg_0a65f83f04cd81b6(a)

@interned
class vg_fa1a1c90b7ff9ec0(Closure):

    def __call__(self, a):
        return vg_202935e60239610c()

@interned
class vg_fa2ecd93b3d53620(Closure):

    def __call__(self, a):
        return a
compiled = vg_fa1a1c90b7ff9ec0()