# This Python file uses the following encoding: utf-8
#数据库索引的作用，数据库索引其实就是查找问题，索引通过某种方式指向数据，就可以实现查找
#索引优点：1.可以提高系统性能
        #2.利用唯一索引，确定数据唯一
        #3.
#缺点：1.增加了存储空间，2.在插入数据和修改数据时，还要修改索引
#对于那些查找次数少，或者进场需要修改的就不要去加索引，定义为text/img/bit也不用，这些数据太大


#索引类型
#唯一索引，主键索引，聚集索引，


#i/o操作的读取，文件一般可以放在磁盘当中，或者内存当中，
# 而读取磁盘当中的数据会很慢，而顺序读取的效率很高，（局部性原理，一般一个数据被用时，他的其他需要数据都会很集中）所以我们可以才去预读，
#预读的大小一般为页，这是一个数据存储逻辑块，就是大小，一般我们会把文件切割成多个块，而每个块就叫做页
#如果数据不在主存中，就会发出一个缺页请求，然后磁盘中就会进行读取