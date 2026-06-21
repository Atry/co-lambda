# Generated, self-contained module: the import header is added at serialization time (see
# tablambda._defunctionalize.runnable_defun_module); the body is emitted by the DEFUN lambda
# term and content-addressed by compiled dataclass shape.
from tablambda._defun_runtime import Closure, Thunk, interned

@interned
class vg_1b6387f4c56929d6(Closure):

    def __call__(self, a):
        return a

@interned
class vg_4f06c0ea5dff8133(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, self.cap_1), self.cap_2)

@interned
class vg_909e2b7cbbe0040c(Closure):
    cap_0: Closure

    def __call__(self, a):
        return self.cap_0

@interned
class vg_acd263981d3d8fe7(Closure):

    def __call__(self, a):
        return vg_c15abec6e6e4bb6d(a)

@interned
class vg_c15abec6e6e4bb6d(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_dcac5abcfd84665f(self.cap_0, a)

@interned
class vg_c6623de2fe71bbf7(Closure):

    def __call__(self, a):
        return vg_909e2b7cbbe0040c(a)

@interned
class vg_dcac5abcfd84665f(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return vg_4f06c0ea5dff8133(a, self.cap_0, self.cap_1)

@interned
class vg_e322ad74fb7a27e0(Closure):

    def __call__(self, a):
        return vg_1b6387f4c56929d6()
compiled = Thunk(Thunk(vg_acd263981d3d8fe7(), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), vg_e322ad74fb7a27e0())))))))), Thunk(Thunk(vg_acd263981d3d8fe7(), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), vg_e322ad74fb7a27e0())))))))), Thunk(Thunk(vg_acd263981d3d8fe7(), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), vg_e322ad74fb7a27e0())))))))), Thunk(Thunk(vg_acd263981d3d8fe7(), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), vg_e322ad74fb7a27e0())))))))), Thunk(Thunk(vg_acd263981d3d8fe7(), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), vg_e322ad74fb7a27e0())))))))), Thunk(Thunk(vg_acd263981d3d8fe7(), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), vg_e322ad74fb7a27e0())))))))), Thunk(Thunk(vg_acd263981d3d8fe7(), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), vg_e322ad74fb7a27e0())))))))), vg_e322ad74fb7a27e0())))))))