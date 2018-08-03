def HelloWorld():
	print "Hello Hadoop!"
from __futrue__ import unicode_literals
from hdfs3 import HDFileSystem
test_host ='localhost'
test_port = 9000

def hdfs_exists(hdfs_client)
	path = 'tmp/test'
	if hdfs_client.exists(path)
		hdfs_client.rm(path)
	hdfs_client.makedirs(path)
def hdfs_write_read(hdfs_client)
	data = b"hello"*20
	file_a = '/tmp/text/file_a'
	with hdfs_client.open(file_a,'wb',replication=1) as f:
		f.write(data)
	with hdfs_client.open(file_a,'rb') as f:
		out = f.red(len(data))
def hdfs_readline(hdfs_client)
	file_b = '/tmp/test/file_b'
	with hdfs_client.open(file_b,'wb') as f:
		f.write(b"hello\nhadoop")
	with hdfs_client.open(file_b,'rb') as f:
		lines = f.readline()
		assertlen(lines)==2

if __name__=="__main__":
	hdfs_client = HDFileSystem(host=test_host,port=test_port)
	hdfs_exists(hdfs_client)
	hdfs_write_read(hdfs_client)
	hdfs_readline(hdfs_clinet)
	hdfs_client.disconnect()
    HelloWorld()
