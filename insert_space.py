s = "aoxjyomdymtbsdkfmitbsddtxjyozgep gsxjkf zkoklfymgoigsdokzk sdhzdtzg mgokzgzgtbmdok zgkflflfokzgzglkkfmimigoep estbzg yoxjsd sdxjxj zkdtlklkdtlfkfmisd okdtsdhzokymmz qdtbzg dtsdhd esokmimimz mdxjxjzk ruxjceep twyosdokym sdhzdtzg nzokgoqdxjymzk tbzg zgxjmikfsddtxjyomf xjigmiigzgcezglfmdmgzkmiep"
t = ""
i = 0
while i < len(s):
    if s[i] == " ":
        i += 3
        continue
    t += s[i] + s[i+1] + " "
    i += 2
'''for i in range(0, len(s), 2):
    if s[i] == " ":
        i -= 1
        continue
    
    t += s[i] + s[i+1] + " "'''
print(t)
    
