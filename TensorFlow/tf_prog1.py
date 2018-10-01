import tensorflow as tf 
hello = tf.constant("Hello world")
a = tf.placeholder("float",shape=[None,3], name="a")
b = tf.placeholder("float",shape=[None,3], name = "b")
x = tf.Variable(0,dtype="float")
output = tf.Variable(0,dtype="float")
x = a*b
output = x*x
sess = tf.Session()
print(sess.run(output,feed_dict={a : [[1 , 2, 3]], b : [[5 ,6 ,7]]}))

