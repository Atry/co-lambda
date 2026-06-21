# Generated, self-contained module: the import header is added at serialization time (see
# tablambda._defunctionalize.runnable_defun_module); the body is emitted by the DEFUN lambda
# term and content-addressed by compiled dataclass shape.
from tablambda._defun_runtime import Closure, Thunk, interned

@interned
class vg_02a5259214e98634(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return vg_56e39b445f76fecf(a, self.cap_0, self.cap_1)

@interned
class vg_03bb58a8563be495(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, Thunk(vg_72bff82b73855343(), a)), a)

@interned
class vg_055f0a43755dd116(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, a), vg_e322ad74fb7a27e0())

@interned
class vg_0aaa4ee57d0cc135(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(a, vg_313631720607360e(self.cap_0)), vg_e322ad74fb7a27e0())

@interned
class vg_11d48747095548bb(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_f0387a26bf5a44ff(a, self.cap_0)

@interned
class vg_1745280894292a15(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, a), Thunk(vg_72bff82b73855343(), a))

@interned
class vg_1b6387f4c56929d6(Closure):

    def __call__(self, a):
        return a

@interned
class vg_1dcf19523e1fc5a2(Closure):

    def __call__(self, a):
        return vg_055f0a43755dd116(a)

@interned
class vg_21fcc85a07128265(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return vg_7bf5b4a166edf5ce(a, self.cap_0, self.cap_1)

@interned
class vg_24075c19af81d502(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(Thunk(Thunk(vg_de0f2a5329dedd2e(), vg_2f7555bad683ee3d()), vg_e322ad74fb7a27e0()), self.cap_0), a)

@interned
class vg_292341ffdad781c7(Closure):

    def __call__(self, a):
        return vg_61d6aa4dd3126853(a)

@interned
class vg_2f362d2d44e871f0(Closure):

    def __call__(self, a):
        return vg_1745280894292a15(a)

@interned
class vg_2f7555bad683ee3d(Closure):

    def __call__(self, a):
        return vg_7afeec05e1e4ddec(a)

@interned
class vg_313631720607360e(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_9318429dee8b7320(self.cap_0)

@interned
class vg_37895e62928d32df(Closure):

    def __call__(self, a):
        return vg_f4f32717138ef876(a)

@interned
class vg_3798fcde86e9ac90(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, Thunk(a, a))

@interned
class vg_37a44230601df234(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return vg_af9530fecf861bac(self.cap_0, a, self.cap_1, self.cap_2)

@interned
class vg_4552e57f9762ab7d(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(Thunk(Thunk(vg_de0f2a5329dedd2e(), vg_b46165fc4e5bae10()), Thunk(Thunk(vg_acd263981d3d8fe7(), self.cap_0), a)), vg_4573cf6b321041fc()), vg_68a3d8c1b84d9ca5())

@interned
class vg_4573cf6b321041fc(Closure):

    def __call__(self, a):
        return vg_c6623de2fe71bbf7()

@interned
class vg_4f06c0ea5dff8133(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, self.cap_1), self.cap_2)

@interned
class vg_53f21d85476ce88c(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure
    cap_3: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, vg_cfd253982fc14c51(self.cap_1, self.cap_2, self.cap_3, a)), Thunk(Thunk(vg_acd263981d3d8fe7(), Thunk(Thunk(vg_e6aad4a0876ceadc(), self.cap_1), self.cap_2)), Thunk(Thunk(Thunk(self.cap_3, Thunk(Thunk(vg_1dcf19523e1fc5a2(), self.cap_1), self.cap_2)), a), vg_e322ad74fb7a27e0())))

@interned
class vg_55e18115e1854038(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure
    cap_3: Closure

    def __call__(self, a):
        return Thunk(Thunk(Thunk(Thunk(Thunk(self.cap_0, self.cap_1), a), vg_68a3d8c1b84d9ca5()), Thunk(Thunk(vg_292341ffdad781c7(), self.cap_2), self.cap_3)), vg_8b3cbcb29c3c4f60())

@interned
class vg_56e39b445f76fecf(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return Thunk(Thunk(vg_acd263981d3d8fe7(), Thunk(Thunk(vg_e6aad4a0876ceadc(), self.cap_0), self.cap_1)), Thunk(Thunk(Thunk(self.cap_2, Thunk(Thunk(vg_1dcf19523e1fc5a2(), self.cap_0), self.cap_1)), vg_e322ad74fb7a27e0()), a))

@interned
class vg_5de3337bc9df0e33(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, vg_878676346198d93e(self.cap_1, a, self.cap_2)), Thunk(Thunk(Thunk(Thunk(vg_de0f2a5329dedd2e(), vg_b46165fc4e5bae10()), Thunk(Thunk(vg_acd263981d3d8fe7(), self.cap_2), a)), vg_4573cf6b321041fc()), vg_8b3cbcb29c3c4f60()))

@interned
class vg_61d6aa4dd3126853(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(Thunk(Thunk(vg_2f362d2d44e871f0(), self.cap_0), a), vg_4573cf6b321041fc()), Thunk(Thunk(self.cap_0, vg_8b3cbcb29c3c4f60()), vg_68a3d8c1b84d9ca5()))

@interned
class vg_65b8add2c0babae9(Closure):

    def __call__(self, a):
        return vg_b02d70145ab88da8(a)

@interned
class vg_68a3d8c1b84d9ca5(Closure):

    def __call__(self, a):
        return vg_d270e95322b9511b(a)

@interned
class vg_6ca434712cd92a9a(Closure):

    def __call__(self, a):
        return Thunk(Thunk(vg_f845647e6cb2cebe(), a), Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), vg_e322ad74fb7a27e0()))

@interned
class vg_72bff82b73855343(Closure):

    def __call__(self, a):
        return Thunk(Thunk(a, vg_e322ad74fb7a27e0()), vg_c6623de2fe71bbf7())

@interned
class vg_775b1211b72a0631(Closure):

    def __call__(self, a):
        return vg_ea4779f777cb7c3f(a)

@interned
class vg_78caf05a50592e01(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_adfe3368c2ba9bdf(a, self.cap_0)

@interned
class vg_7afeec05e1e4ddec(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_21fcc85a07128265(a, self.cap_0)

@interned
class vg_7bf5b4a166edf5ce(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, vg_8733805ac8f8a620(a, self.cap_1, self.cap_2)), Thunk(Thunk(a, vg_02a5259214e98634(self.cap_1, self.cap_2)), Thunk(Thunk(self.cap_1, Thunk(Thunk(vg_acd263981d3d8fe7(), vg_c6623de2fe71bbf7()), vg_e322ad74fb7a27e0())), vg_e322ad74fb7a27e0())))

@interned
class vg_864cb759657c4bf5(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure
    cap_3: Closure
    cap_4: Closure

    def __call__(self, a):
        return Thunk(Thunk(vg_acd263981d3d8fe7(), Thunk(Thunk(vg_e6aad4a0876ceadc(), Thunk(Thunk(vg_e6aad4a0876ceadc(), self.cap_0), self.cap_1)), self.cap_2)), Thunk(Thunk(Thunk(self.cap_3, Thunk(Thunk(Thunk(vg_fa68c89a17b591ba(), self.cap_0), self.cap_1), self.cap_2)), self.cap_4), a))

@interned
class vg_8733805ac8f8a620(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return vg_53f21d85476ce88c(self.cap_0, a, self.cap_1, self.cap_2)

@interned
class vg_878676346198d93e(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return vg_55e18115e1854038(self.cap_0, self.cap_1, self.cap_2, a)

@interned
class vg_8b3cbcb29c3c4f60(Closure):

    def __call__(self, a):
        return vg_e322ad74fb7a27e0()

@interned
class vg_909e2b7cbbe0040c(Closure):
    cap_0: Closure

    def __call__(self, a):
        return self.cap_0

@interned
class vg_9318429dee8b7320(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(vg_6ca434712cd92a9a(), Thunk(self.cap_0, a))

@interned
class vg_a294b88d9bd370ce(Closure):

    def __call__(self, a):
        return vg_4552e57f9762ab7d(a)

@interned
class vg_acd263981d3d8fe7(Closure):

    def __call__(self, a):
        return vg_c15abec6e6e4bb6d(a)

@interned
class vg_ad151f0b90bd4036(Closure):

    def __call__(self, a):
        return vg_d317d9f645ef2398(a)

@interned
class vg_adfe3368c2ba9bdf(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, vg_dbef6d926df2512d(a, self.cap_1)), Thunk(Thunk(a, vg_a294b88d9bd370ce()), vg_4573cf6b321041fc()))

@interned
class vg_af9530fecf861bac(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure
    cap_3: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, vg_d23fe159a0bfac00(self.cap_1, self.cap_2, a, self.cap_0, self.cap_3)), Thunk(Thunk(vg_de0f2a5329dedd2e(), vg_c8554cb1bedcbe85()), self.cap_3))

@interned
class vg_b02d70145ab88da8(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_c28e69cc97e3d06b(a, self.cap_0)

@interned
class vg_b46165fc4e5bae10(Closure):

    def __call__(self, a):
        return vg_f7fae22c516e433b(a)

@interned
class vg_c15abec6e6e4bb6d(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_dcac5abcfd84665f(self.cap_0, a)

@interned
class vg_c28e69cc97e3d06b(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, vg_37a44230601df234(a, self.cap_1, self.cap_0)), Thunk(Thunk(vg_de0f2a5329dedd2e(), vg_c8554cb1bedcbe85()), a))

@interned
class vg_c31e0d8cb9750471(Closure):

    def __call__(self, a):
        return vg_78caf05a50592e01(a)

@interned
class vg_c6623de2fe71bbf7(Closure):

    def __call__(self, a):
        return vg_909e2b7cbbe0040c(a)

@interned
class vg_c8554cb1bedcbe85(Closure):

    def __call__(self, a):
        return vg_0aaa4ee57d0cc135(a)

@interned
class vg_cfd253982fc14c51(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure
    cap_3: Closure

    def __call__(self, a):
        return vg_864cb759657c4bf5(self.cap_0, a, self.cap_1, self.cap_2, self.cap_3)

@interned
class vg_d23fe159a0bfac00(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure
    cap_3: Closure
    cap_4: Closure

    def __call__(self, a):
        return vg_dfbb5ae473136f89(self.cap_0, a, self.cap_1, self.cap_2, self.cap_3, self.cap_4)

@interned
class vg_d270e95322b9511b(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_909e2b7cbbe0040c(self.cap_0)

@interned
class vg_d317d9f645ef2398(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(Thunk(Thunk(Thunk(Thunk(vg_de0f2a5329dedd2e(), vg_c31e0d8cb9750471()), self.cap_0), a), self.cap_0), self.cap_0), a)

@interned
class vg_dbef6d926df2512d(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return vg_5de3337bc9df0e33(self.cap_0, self.cap_1, a)

@interned
class vg_dcac5abcfd84665f(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return vg_4f06c0ea5dff8133(a, self.cap_0, self.cap_1)

@interned
class vg_de0f2a5329dedd2e(Closure):

    def __call__(self, a):
        return Thunk(vg_3798fcde86e9ac90(a), vg_3798fcde86e9ac90(a))

@interned
class vg_dfbb5ae473136f89(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure
    cap_3: Closure
    cap_4: Closure
    cap_5: Closure

    def __call__(self, a):
        return Thunk(Thunk(Thunk(Thunk(vg_775b1211b72a0631(), self.cap_0), self.cap_1), Thunk(Thunk(self.cap_2, self.cap_3), a)), Thunk(vg_6ca434712cd92a9a(), Thunk(Thunk(vg_ad151f0b90bd4036(), Thunk(Thunk(self.cap_2, self.cap_3), a)), Thunk(Thunk(vg_ad151f0b90bd4036(), Thunk(Thunk(self.cap_2, self.cap_3), self.cap_4)), Thunk(Thunk(self.cap_2, self.cap_5), a)))))

@interned
class vg_e322ad74fb7a27e0(Closure):

    def __call__(self, a):
        return vg_1b6387f4c56929d6()

@interned
class vg_e6aad4a0876ceadc(Closure):

    def __call__(self, a):
        return vg_03bb58a8563be495(a)

@interned
class vg_ea4779f777cb7c3f(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(Thunk(Thunk(Thunk(Thunk(vg_de0f2a5329dedd2e(), vg_c31e0d8cb9750471()), self.cap_0), a), vg_e322ad74fb7a27e0()), vg_c6623de2fe71bbf7()), vg_e322ad74fb7a27e0())

@interned
class vg_ef8d2f20d602508a(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return Thunk(Thunk(vg_37895e62928d32df(), Thunk(Thunk(vg_1dcf19523e1fc5a2(), self.cap_0), self.cap_1)), Thunk(Thunk(vg_37895e62928d32df(), Thunk(Thunk(vg_1dcf19523e1fc5a2(), self.cap_0), a)), Thunk(Thunk(vg_1dcf19523e1fc5a2(), self.cap_1), a)))

@interned
class vg_f0387a26bf5a44ff(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, vg_e322ad74fb7a27e0()), Thunk(self.cap_1, a))

@interned
class vg_f4f32717138ef876(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, vg_c6623de2fe71bbf7()), a)

@interned
class vg_f7fae22c516e433b(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(a, vg_11d48747095548bb(self.cap_0)), vg_c6623de2fe71bbf7())

@interned
class vg_f845647e6cb2cebe(Closure):

    def __call__(self, a):
        return vg_24075c19af81d502(a)

@interned
class vg_fa68c89a17b591ba(Closure):

    def __call__(self, a):
        return vg_feee433a19b16296(a)

@interned
class vg_feee433a19b16296(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_ef8d2f20d602508a(self.cap_0, a)
compiled = Thunk(vg_de0f2a5329dedd2e(), vg_65b8add2c0babae9())