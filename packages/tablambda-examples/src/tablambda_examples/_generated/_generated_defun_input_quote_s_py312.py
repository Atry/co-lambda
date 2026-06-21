# Generated, self-contained module: the import header is added at serialization time (see
# tablambda._defunctionalize.runnable_defun_module); the body is emitted by the DEFUN lambda
# term and content-addressed by compiled dataclass shape.
from tablambda._defun_runtime import Closure, Thunk, interned

@interned
class vg_095db32799f551ac(Closure):

    def __call__(self, a):
        return vg_3ac33600b8fe1c42()

@interned
class vg_0a65f83f04cd81b6(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_e73ebd7ced903053(self.cap_0)

@interned
class vg_0da44de306d3394b(Closure):

    def __call__(self, a):
        return Thunk(Thunk(a, vg_4de6719312a26452()), vg_095db32799f551ac())

@interned
class vg_11d2669c19b8252f(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), vg_aba1d9025faa3124()))

@interned
class vg_1ab27c462fa47274(Closure):

    def __call__(self, a):
        return vg_72d8164d2bfa488c(a)

@interned
class vg_1dde68526cfe9481(Closure):

    def __call__(self, a):
        return vg_48c79dd87187420c()

@interned
class vg_256d51530c773a26(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, Thunk(Thunk(vg_6ef54acf964332a2(), vg_aba1d9025faa3124()), Thunk(Thunk(vg_6ef54acf964332a2(), vg_1ab27c462fa47274()), vg_aba1d9025faa3124())))

@interned
class vg_32867555f1d4e09f(Closure):

    def __call__(self, a):
        return vg_42326288205e8b2e(a)

@interned
class vg_341e066408f87d35(Closure):

    def __call__(self, a):
        return vg_c603a3dc0bc7f9dc(a)

@interned
class vg_3972b5d2313adc9b(Closure):

    def __call__(self, a):
        return vg_dcb7769a4e0f0900(a)

@interned
class vg_3ac33600b8fe1c42(Closure):

    def __call__(self, a):
        return vg_edb8582874d5adbc()

@interned
class vg_42326288205e8b2e(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_11d2669c19b8252f(self.cap_0)

@interned
class vg_48c79dd87187420c(Closure):

    def __call__(self, a):
        return vg_0da44de306d3394b()

@interned
class vg_4de6719312a26452(Closure):

    def __call__(self, a):
        return vg_6e46e3f2bc23eaa7()

@interned
class vg_4e606180c620e9a6(Closure):

    def __call__(self, a):
        return vg_ecef9d0db9a8b976(a)

@interned
class vg_62f18526c8bf9d3c(Closure):

    def __call__(self, a):
        return vg_be9cd4b756983565(a)

@interned
class vg_6e46e3f2bc23eaa7(Closure):

    def __call__(self, a):
        return vg_e9d1efb3979b8d3b()

@interned
class vg_6ef54acf964332a2(Closure):

    def __call__(self, a):
        return vg_c083b33c5f0ef4ae(a)

@interned
class vg_6f47e38d8666184b(Closure):

    def __call__(self, a):
        return vg_4e606180c620e9a6()

@interned
class vg_72d8164d2bfa488c(Closure):
    cap_0: Closure

    def __call__(self, a):
        return self.cap_0

@interned
class vg_80448c783eefcd2f(Closure):

    def __call__(self, a):
        return vg_341e066408f87d35()

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
class vg_be9cd4b756983565(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, vg_80448c783eefcd2f())

@interned
class vg_c083b33c5f0ef4ae(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_85418ccea6da692f(self.cap_0, a)

@interned
class vg_c603a3dc0bc7f9dc(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, vg_6f47e38d8666184b())

@interned
class vg_d5d86ea87a500212(Closure):

    def __call__(self, a):
        return vg_62f18526c8bf9d3c()

@interned
class vg_dcb7769a4e0f0900(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_256d51530c773a26(self.cap_0)

@interned
class vg_e73ebd7ced903053(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, vg_aba1d9025faa3124())

@interned
class vg_e9d1efb3979b8d3b(Closure):

    def __call__(self, a):
        return Thunk(Thunk(a, vg_3972b5d2313adc9b()), vg_f2e6499880a78b37())

@interned
class vg_ecef9d0db9a8b976(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, vg_1dde68526cfe9481())

@interned
class vg_edb8582874d5adbc(Closure):

    def __call__(self, a):
        return Thunk(Thunk(a, vg_32867555f1d4e09f()), vg_f2e6499880a78b37())

@interned
class vg_f2e6499880a78b37(Closure):

    def __call__(self, a):
        return vg_0a65f83f04cd81b6(a)

@interned
class vg_fa2ecd93b3d53620(Closure):

    def __call__(self, a):
        return a
compiled = vg_d5d86ea87a500212()