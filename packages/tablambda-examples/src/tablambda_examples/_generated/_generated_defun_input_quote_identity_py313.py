# Generated, self-contained module: the import header is added at serialization time (see
# tablambda._defunctionalize.runnable_defun_module); the body is emitted by the DEFUN lambda
# term and content-addressed by compiled dataclass shape.
from tablambda._defun_runtime import Closure, Thunk, interned

@interned
class vg_01093f6c55d01fb9(Closure):

    def __call__(self, a):
        return vg_ac313019883620b4(a)

@interned
class vg_1b6387f4c56929d6(Closure):

    def __call__(self, a):
        return a

@interned
class vg_22fda00779605656(Closure):

    def __call__(self, a):
        return vg_f8a9360db91cac99(a)

@interned
class vg_2ecb0322e9826d6f(Closure):

    def __call__(self, a):
        return vg_01093f6c55d01fb9()

@interned
class vg_ac313019883620b4(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, vg_22fda00779605656())

@interned
class vg_e322ad74fb7a27e0(Closure):

    def __call__(self, a):
        return vg_1b6387f4c56929d6()

@interned
class vg_e840d7fe5c77726d(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, vg_e322ad74fb7a27e0())

@interned
class vg_f8a9360db91cac99(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_e840d7fe5c77726d(self.cap_0)
compiled = vg_2ecb0322e9826d6f()