# Generated, self-contained module: the import header is added at serialization time (see
# tablambda._defunctionalize.runnable_defun_module); the body is emitted by the DEFUN lambda
# term and content-addressed by compiled dataclass shape.
from tablambda._defun_runtime import Closure, Thunk, interned

@interned
class vg_001de8094153c9bc(Closure):

    def __call__(self, a):
        return vg_e8a15ff2b3e9e014()

@interned
class vg_00b848ccf081017b(Closure):

    def __call__(self, a):
        return vg_9f09aeb1245f6b46(a)

@interned
class vg_0fa721213d1ceba2(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, vg_64dc9d3f59112ac0())

@interned
class vg_162a429821072deb(Closure):

    def __call__(self, a):
        return vg_89b8f5ba6b88aaf0(a)

@interned
class vg_177ad524ed9cf471(Closure):

    def __call__(self, a):
        return vg_ea9a45bd7100360e()

@interned
class vg_19e4b8ed23c83cdf(Closure):

    def __call__(self, a):
        return vg_6bcab5c6a9fa2425()

@interned
class vg_1b6387f4c56929d6(Closure):

    def __call__(self, a):
        return a

@interned
class vg_1fc75c8fb08ecd57(Closure):

    def __call__(self, a):
        return vg_001de8094153c9bc()

@interned
class vg_22fda00779605656(Closure):

    def __call__(self, a):
        return vg_f8a9360db91cac99(a)

@interned
class vg_44e5470ea6c51ee0(Closure):

    def __call__(self, a):
        return vg_c2dbdf05c75fda70()

@interned
class vg_4f06c0ea5dff8133(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, self.cap_1), self.cap_2)

@interned
class vg_64dc9d3f59112ac0(Closure):

    def __call__(self, a):
        return vg_44e5470ea6c51ee0()

@interned
class vg_6bcab5c6a9fa2425(Closure):

    def __call__(self, a):
        return vg_0fa721213d1ceba2(a)

@interned
class vg_7807af998f8215ca(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), vg_e322ad74fb7a27e0()))

@interned
class vg_89b8f5ba6b88aaf0(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, vg_19e4b8ed23c83cdf())

@interned
class vg_909e2b7cbbe0040c(Closure):
    cap_0: Closure

    def __call__(self, a):
        return self.cap_0

@interned
class vg_9b63dc0d5e5e0f6e(Closure):

    def __call__(self, a):
        return vg_162a429821072deb()

@interned
class vg_9ec804f2bfb0cfef(Closure):

    def __call__(self, a):
        return vg_d8e3dc706abd2447()

@interned
class vg_9f09aeb1245f6b46(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_c47714d4f24e4827(self.cap_0)

@interned
class vg_a3f7f2196cfc3293(Closure):

    def __call__(self, a):
        return vg_fcdb384f03be631d(a)

@interned
class vg_aaf6ad8f57ad131d(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, vg_9b63dc0d5e5e0f6e())

@interned
class vg_acd263981d3d8fe7(Closure):

    def __call__(self, a):
        return vg_c15abec6e6e4bb6d(a)

@interned
class vg_af5f12698fc532a4(Closure):

    def __call__(self, a):
        return Thunk(Thunk(a, vg_00b848ccf081017b()), vg_22fda00779605656())

@interned
class vg_c15abec6e6e4bb6d(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_dcac5abcfd84665f(self.cap_0, a)

@interned
class vg_c2dbdf05c75fda70(Closure):

    def __call__(self, a):
        return Thunk(Thunk(a, vg_177ad524ed9cf471()), vg_1fc75c8fb08ecd57())

@interned
class vg_c47714d4f24e4827(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, Thunk(Thunk(vg_acd263981d3d8fe7(), vg_e322ad74fb7a27e0()), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), vg_e322ad74fb7a27e0())))

@interned
class vg_c6623de2fe71bbf7(Closure):

    def __call__(self, a):
        return vg_909e2b7cbbe0040c(a)

@interned
class vg_d8e3dc706abd2447(Closure):

    def __call__(self, a):
        return vg_aaf6ad8f57ad131d(a)

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

@interned
class vg_e840d7fe5c77726d(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, vg_e322ad74fb7a27e0())

@interned
class vg_e8a15ff2b3e9e014(Closure):

    def __call__(self, a):
        return Thunk(Thunk(a, vg_a3f7f2196cfc3293()), vg_22fda00779605656())

@interned
class vg_ea9a45bd7100360e(Closure):

    def __call__(self, a):
        return vg_af5f12698fc532a4()

@interned
class vg_f8a9360db91cac99(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_e840d7fe5c77726d(self.cap_0)

@interned
class vg_fcdb384f03be631d(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_7807af998f8215ca(self.cap_0)
compiled = vg_9ec804f2bfb0cfef()