from functools import reduce
C2F = {
'0':0,
'1':1,
'2':2,
'3':3,
'4':4,
'5':5,
'6':6,
'7':7,
'8':8,
'9':9,
'.':-1
}
def str2float(s):
    nums = map(lambda ch: C2F[ch],s)
    point = 0
    def to_float(f,n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f*10 + n
        else:
            point = point*10
            return f + n/point
    return reduce(to_float,nums,0.0)
print(str2float('123.456'))