# Python错误处理

```python
print("请输入两个数")
print("我们将计算第一个数除以第二个数的商")

num1=input("\n第1个数：")
num2=input("\n第2个数：")

try:
    answer = int(num1)/int(num2)
except ZeroDivisionError:
    print("除数不能为0！")
else:
    print(answer)
```

