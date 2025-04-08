"""
List
"""

"""
List สามารถเก็บข้อมูลหลายๆ อย่างได้ด้วยกัน
"""
items = [1,2,6,"AAA",[1,15],{"name":"honny"},True]

print(items[1])
print(items[3])
print(items[4])
print(items[4][1]) # Guess hows its work
print(items[5]["name"]) # Guess hows its work

if(items[6]):
    print("true")

"""
เราสามารถรู้ความยาวของ list ได้ด้วย function len() ( python มีมาให้)
"""

list_length = len(items)
print(list_length)


"""
เราสามารถ loop ได้ผ่าน for in
"""
for item in items:
    print(item)