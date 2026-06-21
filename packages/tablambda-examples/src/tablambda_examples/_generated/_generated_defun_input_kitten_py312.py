# Generated, self-contained module: the import header is added at serialization time (see
# tablambda._defunctionalize.runnable_defun_module); the body is emitted by the DEFUN lambda
# term and content-addressed by compiled dataclass shape.
from tablambda._defun_runtime import Closure, Thunk, interned

@interned
class vg_1ab27c462fa47274(Closure):

    def __call__(self, a):
        return vg_72d8164d2bfa488c(a)

@interned
class vg_6ef54acf964332a2(Closure):

    def __call__(self, a):
        return vg_c083b33c5f0ef4ae(a)

@interned
class vg_72d8164d2bfa488c(Closure):
    cap_0: Closure

    def __call__(self, a):
        return self.cap_0

@interned
class vg_85418ccea6da692f(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return vg_9aa6f9e21f72dcd6(a, self.cap_0, self.cap_1)

@interned
class vg_9aa6f9e21f72dcd6(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, self.cap_1), self.cap_2)

@interned
class vg_aba1d9025faa3124(Closure):

    def __call__(self, a):
        return vg_fa2ecd93b3d53620()

@interned
class vg_c083b33c5f0ef4ae(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_85418ccea6da692f(self.cap_0, a)

@interned
class vg_fa2ecd93b3d53620(Closure):

    def __call__(self, a):
        return a
compiled = Thunk(Thunk(vg_6ef54acf964332a2(), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_aba1d9025faa3124()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_aba1d9025faa3124()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), vg_aba1d9025faa3124())))))))), Thunk(Thunk(vg_6ef54acf964332a2(), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_aba1d9025faa3124()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_aba1d9025faa3124()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_aba1d9025faa3124()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), vg_aba1d9025faa3124())))))))), Thunk(Thunk(vg_6ef54acf964332a2(), Thunk(Thunk(vg_6ef54acf964332a2(), vg_aba1d9025faa3124()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_aba1d9025faa3124()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_aba1d9025faa3124()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), vg_aba1d9025faa3124())))))))), Thunk(Thunk(vg_6ef54acf964332a2(), Thunk(Thunk(vg_6ef54acf964332a2(), vg_aba1d9025faa3124()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_aba1d9025faa3124()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_aba1d9025faa3124()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), vg_aba1d9025faa3124())))))))), Thunk(Thunk(vg_6ef54acf964332a2(), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_aba1d9025faa3124()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_aba1d9025faa3124()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_aba1d9025faa3124()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), vg_aba1d9025faa3124())))))))), Thunk(Thunk(vg_6ef54acf964332a2(), Thunk(Thunk(vg_6ef54acf964332a2(), vg_aba1d9025faa3124()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_aba1d9025faa3124()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), vg_aba1d9025faa3124())))))))), vg_aba1d9025faa3124()))))))