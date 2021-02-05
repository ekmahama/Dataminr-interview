"""
Given an input string (s) and a pattern (p),
implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
"""

def isMatch(s,p):
    m,n = len(s),len(p)
    lookup =[[False]*(n+1) for _ in range(m)]
    lookup[0][0]=True

    for j in range(2, n+1):
        if p[j-1]=='*':
            lookup[0][j-1]=lookup[0][j-2]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1]==p[j-1] or p[j-1]=='.':
                lookup[i][j]=lookup[i-1][j-1]
            elif j > 1 and p[j-1]=='*':
                if p[j-2]=='*' or s[i-1]==s[i-2]:
                    lookup[i][j]=lookup[i-1][j] or lookup[i][j-2]
                else:
                    lookup[i][j]=lookup[i][j-2]
    return lookup[m][n]
