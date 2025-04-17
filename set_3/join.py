"""
write a function that take two parameter of list of dict

"""

food_name=[
    {
        "id":1,
        "name":"pizza"
    },
    {
        "id":2,
        "name":"watermelon"
    },
    {
        "id":3,
        "name":"pepsi"
    }
]

food_info=[
    {
        "id":1,
        "calories":1054
    },
    {
        "id":3,
        "calories":217
    }
]

"""
return an diction that join both list base on id
if no data to join, mark the join field with None

ex
"""

food = [
    {
        "id":1,
        "name":"pizza",
        "calories":1054
    },
    {
        "id":2,
        "name":"watermelon",
        "calories":None
    },
    {
        "id":3,
        "name":"pepsi",
        "calories":217
    }
]