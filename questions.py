# -*- coding: utf8 -*-

from typing_extensions import ParamSpec


Câu 1: What is the lambda function in Python? Why does it exist in Python?

Lambda trong python là hàm được định nghĩa mà không có tên (hàm vô danh).
Lambda có thể nhận vào nhiều tham số nhưng chỉ có một biểu thức.

    Lambda tồn tại để gọi ra 1 hàm vô danh trong 1 hàm khác.
    Nói chung là để đỡ mất công gọi nhiều dễ loạn và tiết kiệm tài nguyên phần cứng.


Câu 2: What is pass in Python?

Pass được dùng như một lệnh để giữ chỗ cho các hàm tương lai.
Nó được dùng để tránh gặp phải những lỗi cũ pháp không được để trống.

    if, class, loop và function không được phép để trống.


Câu 3: What is *args, **kwargs in function definition?

Cú pháp *args và **kwargs cho phép định nghĩa hàm có thể nhận số lượng tham số tuỳ ý.
Ngoài ra, cú pháp này còn có thể được sử dụng để unpack khi gọi hàm cũng như trong nhiều trường hợp khác.
    <*Unpack giúp tách độc lập các phần từ có trong object list ra>

    *args sự dụng với hàm không có từ khóa.
    **kwargs sử dụng với hàm có từ khóa (ví dụ như dict)


Câu 4: What is docstring in Python? How to write them? Are they required?

Docstring là:
    Một dạng chú thích nhiều dòng.
        Hay xuất hiện ở đầu một file Python, sau một dòng định nghĩa lớp, hàm.

Cách viết :
'''
Hê lô anh em !
Ahihi
'''

Không bắt buộc nhưng đây là một trong những chuẩn quy ước về định dạng, trình bày code Python (luật bất thành văn).


Câu 5: What are the built-in data types that Python provides? Which of them are mutable, which are immutable?

Python có các dạng data được tích hợp sẵn là int, bool, float, str, bytes, bytearray, dict, list, tuple, set và frozenset.
Những đối tượng thuộc loại sau là mutable (có thể thay đổi giá trị):
    list
    dict
    set
    bytearray

Những đối tượng thuộc loại sau là immutable (không thể thay đổi giá trị):
    tuple
    frozenset
    bytes
    str
    float
    bool
    int


Câu 6: What is the difference between list and tuple types in Python?

list là dạng dữ liệu có thể thay đổi giá trị (mutable) còn tuple thuộc dạng không thể thay đổi giá trị (immutable).


Câu 7: What keywords can be used in conjunction with the for keyword?

Các từ khóa có thể dùng với for là break, continue, range(), else, for trong for, pass.


Câu 8: What's the difference between globals(), locals(), and vars()?

Biến globals() có thể được gọi ở trong mọi function trong trường trình.

Biến locals() chỉ có thể gọi được ở trong function mà nó được gọi ra.

Biến vars() để gọi ra các thuộc tính của __dict__ được truyền vào.
    Nếu không có đối số nào được truyền vào thì vars() hoạt động như locals().


Câu 9: Is it possible to have a negative index in iterative types in Python?

Vòng lặp for n in range(start, stop, step) có nhận giá trị âm với điều kiện (start > stop).


Câu 10: What is the __init__.py module? What it's for?

__init__ là hàm khởi tạo dùng để khởi tạo trạng thái của object đồng thời cũng gán giá trị cho các dữ liệu trong class.

Nó cho phép người dùng định nghĩa một biến ở cấp độ đóng gói.


Câu 11: How can I swap values of variables in Python? Please give an example

Dùng 1 biến làm trung gian.

Ví dụ :
x = 5
y = 10

temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


Câu 12:  How do I view object methods? Please give an example

Sử dụng dir(object) để xem các phương thức của object.

Ví dụ :
object_methods = [method_name for method_name in dir(object)
                  if callable(getattr(object, method_name))]


Câu 13: What is a module in python? What is a package?
        What is the difference between packages and modules in Python?
        Please give an example module and package

Module là một đối tượng với các thuộc tính được đặt tên tùy ý mà người viết có thể liên kết và tham chiếu.
1 Module có thể định nghĩa các hàm, lớp và biến và cũng có thể tự hoạt động độc lập được.

Package là cấu trúc phân cấp các Module của chương trình. Nó giúp ta dễ quản lí và tránh xung đột giữa các Module.

Ví dụ:
Trong 1 directory có tên "pkg" gồm 2 module "mod1.py" và "mod2.py".

Trong "mod1.py" có :
def foo():
    print('[mod1] foo()')

class Foo:
    pass

Trong "mod2.py" có :
def bar():
    print('[mod2] bar()')

class Bar:
    pass

Ta có thể gọi ra ở 1 file mới như sau

import pkg.mod1, pkg.mod2
pkg.mod1.foo()
[mod1] foo()
x = pkg.mod2.Bar()


Câu 14: What is the __init__ function used for?

__init__ function được dùng để khởi tạo và gán giá trị cho các đối tượng trong class.


Câu 15: Explain how to make a Python script executable on Unix?

Thêm : #!/usr/bin/env python3
    vào dòng đâu tiên trong script.

Trong cmd prompt, đánh :
    $ chmod +x myscript.py (myscript là tên file cần chạy)


Câu 16: What is the output of -12 % 10 and -12 // 10.

Output của -12 % 10 là 8
Output của -12 // 10 là -2


Câu 17: Why shouldn't you make the default arguments an empty list?

