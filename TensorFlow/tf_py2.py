import tensorflow as tf
Input = tf.placeholder("float" , shape=[None,2], name="Input")
target = tf.placeholder("float" , shape=[None,1], name="target")
input_biased = tf.Variable(initial_value=tf.random_normal(shape=[3], stddev=0.4),name='input_biased' , dtype='float')

Weight = tf.Variable(initial_value=tf.random_normal(shape=[2,3], stddev=0.4),name="Weight" , dtype='float')
Biased_weight = tf.Variable(initial_value=tf.random_normal(shape=[1], stddev=0.4),name="Weight_biased" , dtype='float')
tf.summary.histogram(name="Weights_1", values=Weight)

outputWeight = tf.Variable(initial_value=tf.random_normal(shape=[3,1], stddev=0.4),name="Weight" , dtype='float')
tf.summary.histogram(name="Weights_1",values = outputWeight)
hiddenLayer = tf.matmul(Input,Weight) + input_biased
hiddenLayer = tf.sigmoid(hiddenLayer , name= "hidden_activation")

output = tf.matmul(hiddenLayer,outputWeight) + Biased_weight
output = tf.sigmoid(output , name= "output_activation")

cost = tf.squared_difference(target,output)
cost = tf.reduce_mean(cost)
tf.summary.scalar("error",cost)


optimizer = tf.train.AdamOptimizer().minimize(cost)
inp = [[1,0] ,[0,1],[1,1],[0,0]]
out = [[0],[1],[1],[0]]
epochs = 6000
import datetime
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    mergedSummary = tf.summary.merge_all()
    fileName = './summary_log/run'+datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%s")
    writer = tf.summary.FileWriter(fileName,sess.graph)
    for i in range(epochs):
        err, _,summaryOutput = sess.run([cost,optimizer,mergedSummary],feed_dict={Input : inp , target : out})
        print(err,i)
        writer.add_summary(summaryOutput,i)

    while True:
        inp = [[0,0]]
        inp[0][0]=input("type first input")
        inp[0][1]=input("type second input")
        print(sess.run([output],feed_dict={Input : inp})[0][0])

