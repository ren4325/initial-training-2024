#予想:[6, 7, 8][1, 2, 3, 1]と表示される
def f(a):
    a = [6, 7, 8]
    print(a)

def g(a):
    a.append(1)

def somefunction():
    a0 = [1, 2, 3]
    f(a0)
    print(a0)

    a1 = [1, 2, 3]
    g(a1)
    print(a1)

somefunction()

#考察
#関数内で代入をするとローカル変数として関数内でしか扱えないため。関数外には影響しない。
#関数内のappend()はa1そのものを参照する。
