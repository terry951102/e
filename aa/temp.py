f = float(input("請輸入華氏幾度："))

c = (f - 32) * 5 / 9
print("攝氏：", c, '度')
def f2c(f):
    c = (f - 32) * 5 / 9 # 先故意寫錯
    return c
 
f = float(input("請輸入華氏幾度："))
print("攝氏：", f2c(f), '度')
