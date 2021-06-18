def check_par(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
         return True
    if start not in graph:
         return False
    for node in graph[start]:
         if node not in path:
            newpath = check_par(graph, node, end, path)
            if newpath: return newpath
    return False
cls = {}
for _ in range(int(input('n = '))):
    cls_str = input('ch:par  ')
    cls_nod = cls_str.split(':')[0].strip(' ')
    if cls_str == cls_nod:
        cls_par = []
    else:
        cls_par = cls_str.split(':')[1].split()
    cls.update({cls_nod:cls_par})
for _ in range(int(input('m= '))):
    cls_str = input('par chr ')
    end = cls_str.split()[0]
    start = cls_str.split()[1]
    if check_par(cls, start, end):
        print('Yes')
    else:
        print('No')