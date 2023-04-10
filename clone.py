#Alunos: Francisco Wernke (11221870) e Luis Vitor Zerkowski (9837201)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def A():
    wB='def B(wB):\n    print(f"#Alunos: Francisco Wernke (11221870) e Luis Vitor Zerkowski (9837201)")\n    print(f"#!/usr/bin/env python3\\n# -*- coding: utf-8 -*-")\n    print(f"def A():\\n    wB=%s\\n    return wB"%repr(wB))\n    print(wB)\n    print("wB=A()\\nB(wB)")'
    return wB
def B(wB):
    print(f"#Alunos: Francisco Wernke (11221870) e Luis Vitor Zerkowski (9837201)")
    print(f"#!/usr/bin/env python3\n# -*- coding: utf-8 -*-")
    print(f"def A():\n    wB=%s\n    return wB"%repr(wB))
    print(wB)
    print("wB=A()\nB(wB)")
wB=A()
B(wB)
