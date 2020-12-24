def find_content(content, sting_to_find):  #輸入lis跟要找到的關鍵字
    mp = content.find(sting_to_find)    #找出關鍵字在list中的位置
    fcontent = content[mp+8:-5:]    #產生一個關鍵字後開始的list
    return fcontent

file = open('source.txt')   #讀檔
content = file.read()
file.close
new_content = find_content(content, 'member')   #呼叫find_content函式
print(new_content)


