given = [input() for x in range(int(input()))]

question = [input() for x in range(int(input()))]

#print(given)
#print(question)


help1 = False

answer = {}

for line in given:
    
    if line.count(':'):
        child, parents = line.split(':')
        
        child = child.split()
        
        parents = parents.strip().split()
        
        
        answer[child[0]] = set(parents)
        
    else:
        child = line.split()
        
        answer[child[0]] = []
        




# красивый вывод словаря
for i in answer.items():
    if help1:print('{} - {}'.format(i[0], ' '.join(i[1])))
if help1: print('--'*10)
    
def search_paren(parent, child):
    if parent == child: return True
    
    result = False
    for parent_or_not in answer[child]:
        if result: return True
        
        if help1:print('-\tparent:',parent, '\tchild:',child, '\tparent_or_not:',parent_or_not)
        
        if parent == parent_or_not:
            if help1:print('+\tparent:',parent, '\tchild:',child, '\tparent_or_not:',parent_or_not)
            return True
        else:
            result = search_paren(parent,parent_or_not)
    
    return result

    
    


for line in question:
    parent, child = line.split()
    
    if help1:print(parent, child, end=' : ')
    if search_paren(parent, child) == True:
        print('Yes')
    else:
        print('No')
