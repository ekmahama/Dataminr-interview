def isMatch(s, p):
    m, n = len(s), len(p)
    lookup = [[False,]*(n+1) for _ in range(m+1)]

    # Empyt pattern matches empty string
    lookup[0][0]=True

    if p and p[0]=='*':
        lookup[0][1] = True

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1]==p[j-1] or p[j-1]=='?':
                lookup[i][j]=lookup[i-1][j-1]
            elif p[j-1]=='*':
                lookup[i][j]=lookup[i][j-1] or lookup[i-1][j]
    return lookup[m][n]

def removeDuplicates(p):
    if p == '':
        return p
    res = p[0]
    for c in p[1:]:
        if c != '*' or (c=='*' and res[-1]!='*'):
            res += c
    return res
