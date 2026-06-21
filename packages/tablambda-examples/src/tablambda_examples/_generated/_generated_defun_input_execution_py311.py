# Generated, self-contained module: the import header is added at serialization time (see
# tablambda._defunctionalize.runnable_defun_module); the body is emitted by the DEFUN lambda
# term and content-addressed by compiled dataclass shape.
from tablambda._defun_runtime import Closure, Thunk, interned

@interned
class vg_0fc0c80aa37d5418(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return vg_c9ce625418bfa9fc(a, self.cap_0, self.cap_1)

@interned
class vg_267c5a013e0be552(Closure):
    cap_0: Closure

    def __call__(self, a):
        return self.cap_0

@interned
class vg_2f7005dfc64f22d3(Closure):

    def __call__(self, a):
        return vg_267c5a013e0be552(a)

@interned
class vg_49f97b1b006e9074(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_0fc0c80aa37d5418(self.cap_0, a)

@interned
class vg_5790a50754fc667f(Closure):

    def __call__(self, a):
        return a

@interned
class vg_8063e79fbbf0b759(Closure):

    def __call__(self, a):
        return vg_49f97b1b006e9074(a)

@interned
class vg_9dd83a0b38353a6c(Closure):

    def __call__(self, a):
        return vg_5790a50754fc667f()

@interned
class vg_c9ce625418bfa9fc(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, self.cap_1), self.cap_2)
compiled = Thunk(Thunk(vg_8063e79fbbf0b759(), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), vg_9dd83a0b38353a6c())))))))), Thunk(Thunk(vg_8063e79fbbf0b759(), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), vg_9dd83a0b38353a6c())))))))), Thunk(Thunk(vg_8063e79fbbf0b759(), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), vg_9dd83a0b38353a6c())))))))), Thunk(Thunk(vg_8063e79fbbf0b759(), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), vg_9dd83a0b38353a6c())))))))), Thunk(Thunk(vg_8063e79fbbf0b759(), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), vg_9dd83a0b38353a6c())))))))), Thunk(Thunk(vg_8063e79fbbf0b759(), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), vg_9dd83a0b38353a6c())))))))), Thunk(Thunk(vg_8063e79fbbf0b759(), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), vg_9dd83a0b38353a6c())))))))), Thunk(Thunk(vg_8063e79fbbf0b759(), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), vg_9dd83a0b38353a6c())))))))), Thunk(Thunk(vg_8063e79fbbf0b759(), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_9dd83a0b38353a6c()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), vg_9dd83a0b38353a6c())))))))), vg_9dd83a0b38353a6c())))))))))