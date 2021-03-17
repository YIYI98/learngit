def toTxtFile(fn):  #函数定义
    with open(fn,'w') as fp:
        for i in range(10):
            if i%3==0 or i%7==0:
                fp.write(str(i)+'\n')
            else:
                fp.write('ignored\n')
        fp.write('finished\n')
    print('all job done')
toTxtFile('text.txt')