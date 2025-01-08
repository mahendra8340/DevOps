instances_info=[
    {
    "name":"Instance-001",
    "uptime":25,
    "downtime":11
    },
    {
    "name":"Instance-002",
    "uptime":26,
    "downtime":11
    },
    {
    "name":"Instance-003",
    "uptime":27,
    "downtime":11
    }
]

instances_info.append({ "name":"Instance-004",    "uptime":28,    "downtime":11})


for element in instances_info:
    print(element["uptime"])
