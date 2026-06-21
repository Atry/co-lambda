# Generated, self-contained module: the import header is added at serialization time (see
# tablambda._defunctionalize.runnable_defun_module); the body is emitted by the DEFUN lambda
# term and content-addressed by compiled dataclass shape.
from tablambda._defun_runtime import Closure, Thunk, interned

@interned
class vg_07fe30769a7d0b57(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, a), Thunk(vg_2b9e6be3fdcdc2db(), a))

@interned
class vg_089a575129b29bd7(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, Thunk(vg_2b9e6be3fdcdc2db(), a)), a)

@interned
class vg_0fc0c80aa37d5418(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return vg_c9ce625418bfa9fc(a, self.cap_0, self.cap_1)

@interned
class vg_108719df6dbc8e31(Closure):

    def __call__(self, a):
        return vg_07fe30769a7d0b57(a)

@interned
class vg_164851237114cf70(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, vg_83ce730a8f1095a7(a, self.cap_1, self.cap_2)), Thunk(Thunk(a, vg_37a22bcdaa7e80f0(self.cap_1, self.cap_2)), Thunk(Thunk(self.cap_1, Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), vg_9dd83a0b38353a6c())), vg_9dd83a0b38353a6c())))

@interned
class vg_1cf45aeaf14b8eb3(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return vg_164851237114cf70(a, self.cap_0, self.cap_1)

@interned
class vg_1d8e228ce8f1c29c(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure
    cap_3: Closure
    cap_4: Closure
    cap_5: Closure

    def __call__(self, a):
        return Thunk(Thunk(Thunk(Thunk(vg_65c40eeb813c6c26(), self.cap_0), self.cap_1), Thunk(Thunk(self.cap_2, self.cap_3), a)), Thunk(vg_5a62cb3a19e71727(), Thunk(Thunk(vg_50302ac7fb4731d2(), Thunk(Thunk(self.cap_2, self.cap_3), a)), Thunk(Thunk(vg_50302ac7fb4731d2(), Thunk(Thunk(self.cap_2, self.cap_3), self.cap_4)), Thunk(Thunk(self.cap_2, self.cap_5), a)))))

@interned
class vg_24214f20524fdf16(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, vg_c907a156d9f1c9a6(a, self.cap_1)), Thunk(Thunk(a, vg_58afd7fa88f586ef()), vg_439917b9df6b0880()))

@interned
class vg_2501989fcb79f05e(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_d29fa36a45476b9a(a, self.cap_0)

@interned
class vg_267c5a013e0be552(Closure):
    cap_0: Closure

    def __call__(self, a):
        return self.cap_0

@interned
class vg_2afc3067ea510b0b(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return Thunk(Thunk(vg_950f650a6f7f8132(), Thunk(Thunk(vg_73c269783328e5ed(), self.cap_0), self.cap_1)), Thunk(Thunk(vg_950f650a6f7f8132(), Thunk(Thunk(vg_73c269783328e5ed(), self.cap_0), a)), Thunk(Thunk(vg_73c269783328e5ed(), self.cap_1), a)))

@interned
class vg_2b9e6be3fdcdc2db(Closure):

    def __call__(self, a):
        return Thunk(Thunk(a, vg_9dd83a0b38353a6c()), vg_2f7005dfc64f22d3())

@interned
class vg_2f7005dfc64f22d3(Closure):

    def __call__(self, a):
        return vg_267c5a013e0be552(a)

@interned
class vg_32c060a3b019949a(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(Thunk(Thunk(Thunk(Thunk(vg_87807b7d77c0bc35(), vg_6356e238c4eae69a()), self.cap_0), a), self.cap_0), self.cap_0), a)

@interned
class vg_34ec91e0a7028d61(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, vg_6d4cf8e91ef7411f(self.cap_1, a, self.cap_2)), Thunk(Thunk(Thunk(Thunk(vg_87807b7d77c0bc35(), vg_cfae7f5eccd588ed()), Thunk(Thunk(vg_8063e79fbbf0b759(), self.cap_2), a)), vg_439917b9df6b0880()), vg_6e6aafd047ea9acf()))

@interned
class vg_37579a5d29d45af0(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(vg_5a62cb3a19e71727(), Thunk(self.cap_0, a))

@interned
class vg_37a22bcdaa7e80f0(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return vg_ad8c48a208685c5d(a, self.cap_0, self.cap_1)

@interned
class vg_439917b9df6b0880(Closure):

    def __call__(self, a):
        return vg_2f7005dfc64f22d3()

@interned
class vg_49f97b1b006e9074(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_0fc0c80aa37d5418(self.cap_0, a)

@interned
class vg_50302ac7fb4731d2(Closure):

    def __call__(self, a):
        return vg_32c060a3b019949a(a)

@interned
class vg_56a5e92339010f26(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_37579a5d29d45af0(self.cap_0)

@interned
class vg_572528f8c3e4385b(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(Thunk(Thunk(Thunk(Thunk(vg_87807b7d77c0bc35(), vg_6356e238c4eae69a()), self.cap_0), a), vg_9dd83a0b38353a6c()), vg_2f7005dfc64f22d3()), vg_9dd83a0b38353a6c())

@interned
class vg_5790a50754fc667f(Closure):

    def __call__(self, a):
        return a

@interned
class vg_58afd7fa88f586ef(Closure):

    def __call__(self, a):
        return vg_615a00b3f1e44e65(a)

@interned
class vg_59fac9142a1b43d5(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(a, vg_9ce4cc3bc06570e5(self.cap_0)), vg_2f7005dfc64f22d3())

@interned
class vg_5a62cb3a19e71727(Closure):

    def __call__(self, a):
        return Thunk(Thunk(vg_73cc4c88116472c8(), a), Thunk(Thunk(vg_8063e79fbbf0b759(), vg_2f7005dfc64f22d3()), vg_9dd83a0b38353a6c()))

@interned
class vg_615a00b3f1e44e65(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(Thunk(Thunk(vg_87807b7d77c0bc35(), vg_cfae7f5eccd588ed()), Thunk(Thunk(vg_8063e79fbbf0b759(), self.cap_0), a)), vg_439917b9df6b0880()), vg_8e257d4c73e89c62())

@interned
class vg_6356e238c4eae69a(Closure):

    def __call__(self, a):
        return vg_e77f1d10ec6ee1c1(a)

@interned
class vg_65c40eeb813c6c26(Closure):

    def __call__(self, a):
        return vg_572528f8c3e4385b(a)

@interned
class vg_67dda99bc366bfc7(Closure):

    def __call__(self, a):
        return vg_c3e9c656ab4f9937(a)

@interned
class vg_6c685142c1292ff0(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure
    cap_3: Closure
    cap_4: Closure

    def __call__(self, a):
        return vg_1d8e228ce8f1c29c(self.cap_0, a, self.cap_1, self.cap_2, self.cap_3, self.cap_4)

@interned
class vg_6ce5f545aa276ac7(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(a, vg_56a5e92339010f26(self.cap_0)), vg_9dd83a0b38353a6c())

@interned
class vg_6d4cf8e91ef7411f(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return vg_dbf3c09a64421247(self.cap_0, self.cap_1, self.cap_2, a)

@interned
class vg_6d7c5d43302710ae(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return vg_d027764473dfc419(self.cap_0, a, self.cap_1, self.cap_2)

@interned
class vg_6e6aafd047ea9acf(Closure):

    def __call__(self, a):
        return vg_9dd83a0b38353a6c()

@interned
class vg_73c269783328e5ed(Closure):

    def __call__(self, a):
        return vg_825b48edb2a1b909(a)

@interned
class vg_73cc4c88116472c8(Closure):

    def __call__(self, a):
        return vg_d4925a595c167951(a)

@interned
class vg_8063e79fbbf0b759(Closure):

    def __call__(self, a):
        return vg_49f97b1b006e9074(a)

@interned
class vg_825b48edb2a1b909(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, a), vg_9dd83a0b38353a6c())

@interned
class vg_83ce730a8f1095a7(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return vg_f0e3258f2ff87106(self.cap_0, a, self.cap_1, self.cap_2)

@interned
class vg_83ede87e1972aa4b(Closure):

    def __call__(self, a):
        return vg_964bc2304cceb6ce(a)

@interned
class vg_87807b7d77c0bc35(Closure):

    def __call__(self, a):
        return Thunk(vg_c3cf9e393305e4d5(a), vg_c3cf9e393305e4d5(a))

@interned
class vg_8e257d4c73e89c62(Closure):

    def __call__(self, a):
        return vg_b96f08cff84409ba(a)

@interned
class vg_950f650a6f7f8132(Closure):

    def __call__(self, a):
        return vg_f39525022c5c8f01(a)

@interned
class vg_964bc2304cceb6ce(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_2afc3067ea510b0b(self.cap_0, a)

@interned
class vg_9b872a8af2109e0e(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, vg_9dd83a0b38353a6c()), Thunk(self.cap_1, a))

@interned
class vg_9be975d359b54f2b(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure
    cap_3: Closure
    cap_4: Closure

    def __call__(self, a):
        return Thunk(Thunk(vg_8063e79fbbf0b759(), Thunk(Thunk(vg_d80f904b29ed6bc4(), Thunk(Thunk(vg_d80f904b29ed6bc4(), self.cap_0), self.cap_1)), self.cap_2)), Thunk(Thunk(Thunk(self.cap_3, Thunk(Thunk(Thunk(vg_83ede87e1972aa4b(), self.cap_0), self.cap_1), self.cap_2)), self.cap_4), a))

@interned
class vg_9ce4cc3bc06570e5(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_9b872a8af2109e0e(a, self.cap_0)

@interned
class vg_9dd83a0b38353a6c(Closure):

    def __call__(self, a):
        return vg_5790a50754fc667f()

@interned
class vg_ad8c48a208685c5d(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return Thunk(Thunk(vg_8063e79fbbf0b759(), Thunk(Thunk(vg_d80f904b29ed6bc4(), self.cap_0), self.cap_1)), Thunk(Thunk(Thunk(self.cap_2, Thunk(Thunk(vg_73c269783328e5ed(), self.cap_0), self.cap_1)), vg_9dd83a0b38353a6c()), a))

@interned
class vg_b2ad9a9c705a39fc(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure
    cap_3: Closure

    def __call__(self, a):
        return vg_9be975d359b54f2b(self.cap_0, a, self.cap_1, self.cap_2, self.cap_3)

@interned
class vg_b96f08cff84409ba(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_267c5a013e0be552(self.cap_0)

@interned
class vg_c3cf9e393305e4d5(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(self.cap_0, Thunk(a, a))

@interned
class vg_c3e9c656ab4f9937(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_1cf45aeaf14b8eb3(a, self.cap_0)

@interned
class vg_c907a156d9f1c9a6(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return vg_34ec91e0a7028d61(self.cap_0, self.cap_1, a)

@interned
class vg_c9441ef0670b8080(Closure):

    def __call__(self, a):
        return vg_2501989fcb79f05e(a)

@interned
class vg_c9ce625418bfa9fc(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, self.cap_1), self.cap_2)

@interned
class vg_cfae7f5eccd588ed(Closure):

    def __call__(self, a):
        return vg_59fac9142a1b43d5(a)

@interned
class vg_cfbda2abc1826f9a(Closure):

    def __call__(self, a):
        return vg_6ce5f545aa276ac7(a)

@interned
class vg_d027764473dfc419(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure
    cap_3: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, vg_6c685142c1292ff0(self.cap_1, self.cap_2, a, self.cap_0, self.cap_3)), Thunk(Thunk(vg_87807b7d77c0bc35(), vg_cfbda2abc1826f9a()), self.cap_3))

@interned
class vg_d29fa36a45476b9a(Closure):
    cap_0: Closure
    cap_1: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, vg_6d7c5d43302710ae(a, self.cap_1, self.cap_0)), Thunk(Thunk(vg_87807b7d77c0bc35(), vg_cfbda2abc1826f9a()), a))

@interned
class vg_d4925a595c167951(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(Thunk(Thunk(vg_87807b7d77c0bc35(), vg_67dda99bc366bfc7()), vg_9dd83a0b38353a6c()), self.cap_0), a)

@interned
class vg_d80f904b29ed6bc4(Closure):

    def __call__(self, a):
        return vg_089a575129b29bd7(a)

@interned
class vg_dbf3c09a64421247(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure
    cap_3: Closure

    def __call__(self, a):
        return Thunk(Thunk(Thunk(Thunk(Thunk(self.cap_0, self.cap_1), a), vg_8e257d4c73e89c62()), Thunk(Thunk(vg_f65e982d7f00bee3(), self.cap_2), self.cap_3)), vg_6e6aafd047ea9acf())

@interned
class vg_e77f1d10ec6ee1c1(Closure):
    cap_0: Closure

    def __call__(self, a):
        return vg_24214f20524fdf16(a, self.cap_0)

@interned
class vg_e99468c8fcf2802f(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(Thunk(Thunk(vg_108719df6dbc8e31(), self.cap_0), a), vg_439917b9df6b0880()), Thunk(Thunk(self.cap_0, vg_6e6aafd047ea9acf()), vg_8e257d4c73e89c62()))

@interned
class vg_f0e3258f2ff87106(Closure):
    cap_0: Closure
    cap_1: Closure
    cap_2: Closure
    cap_3: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, vg_b2ad9a9c705a39fc(self.cap_1, self.cap_2, self.cap_3, a)), Thunk(Thunk(vg_8063e79fbbf0b759(), Thunk(Thunk(vg_d80f904b29ed6bc4(), self.cap_1), self.cap_2)), Thunk(Thunk(Thunk(self.cap_3, Thunk(Thunk(vg_73c269783328e5ed(), self.cap_1), self.cap_2)), a), vg_9dd83a0b38353a6c())))

@interned
class vg_f39525022c5c8f01(Closure):
    cap_0: Closure

    def __call__(self, a):
        return Thunk(Thunk(self.cap_0, vg_2f7005dfc64f22d3()), a)

@interned
class vg_f65e982d7f00bee3(Closure):

    def __call__(self, a):
        return vg_e99468c8fcf2802f(a)
compiled = Thunk(vg_87807b7d77c0bc35(), vg_c9441ef0670b8080())