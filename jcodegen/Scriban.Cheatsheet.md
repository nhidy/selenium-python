# Scriban Cheatsheet

---

## 1. Toán tử So sánh

| Toán tử | Ví dụ    | Ý nghĩa           |
| :------ | :------- | :---------------- |
| `==`    | `x == 2` | So sánh bằng      |
| `!=`    | `x != 2` | So sánh khác      |
| `>`     | `x > 2`  | Lớn hơn           |
| `<`     | `x < 2`  | Nhỏ hơn           |
| `>=`    | `x >= 2` | Lớn hơn hoặc bằng |
| `<=`    | `x <= 2` | Nhỏ hơn hoặc bằng |

---

## 2. Toán tử Logic

| Toán tử | Ví dụ              | Ý nghĩa        |
| :------ | :----------------- | :------------- |
| `and`   | `x > 1 and x < 10` | Và             |
| `or`    | `x == 1 or x == 2` | Hoặc           |
| `not`   | `not x`            | Phủ định       |
| `!`     | `!empty array`     | Phủ định nhanh |

---

## 3. Toán tử Điều Kiện

| Toán tử | Ví dụ                | Ý nghĩa                   |
| :------ | :------------------- | :------------------------ |
| `? :`   | `x == 2 ? "a" : "b"` | Toán tử ba ngôi (ternary) |

---

## 4. Kiểm tra chuỗi, danh sách

| Toán tử    | Ví dụ                | Ý nghĩa                     |
| :--------- | :------------------- | :-------------------------- |
| `contains` | `"abc" contains "a"` | Kiểm tra chuỗi con          |
| `in`       | `"a" in array`       | Kiểm tra phần tử trong mảng |
| `empty`    | `empty array`        | Mảng/chuỗi rỗng             |
| `blank`    | `blank str`          | Chuỗi trắng                 |

---

## 5. Xử lý mảng

| Hàm       | Ví dụ             | Ý nghĩa                        |                            |
| :-------- | :---------------- | :----------------------------- | -------------------------- |
| `size`    | `array.size`      | Đếm số phần tử                 |                            |
| `first`   | `array.first`     | Phần tử đầu tiên               |                            |
| `last`    | `array.last`      | Phần tử cuối                   |                            |
| `where`   | \`array           | where "x" "x.type == 'bool'"\` | Lọc theo điều kiện         |
| `sort_by` | \`array           | sort\_by "name"\`              | Sắp xếp theo field         |
| `join`    | \`array           | array.join ", "\`              | Ghép danh sách thành chuỗi |
| `reverse` | `array.reverse`   | Đảo ngược mảng                 |                            |
| `slice`   | `array.slice 0 2` | Cắt 2 phần tử từ vị trí 0      |                            |

---

## 6. Các thực hành nhỏ

**Kiểm tra mảng rỗng:**

```scriban
{{ if array.empty }}
Empty!
{{ else }}
Has Data.
{{ end }}
```

**Sắp xếp danh sách field theo name:**

```scriban
{% for prop in private_properties | sort_by "name" %}
private {{ prop.type }} {{ prop.name }};
{% end %}
```

**Chọn field theo điều kiện:**

```scriban
{% assign bool_fields = private_properties | where "x" "x.type == 'bool'" %}

{% for field in bool_fields %}
private bool {{ field.name }};
{% end %}
```

---

# Kết luận

* Scriban rất gần gũi C#/JS.
* Dễ học, dễ xây dựng template sinh code phức tạp.

> Để hiệu quả hơn, nên kèm theo tài liệu này bên project khi phát triển template.
