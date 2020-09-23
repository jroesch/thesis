import tensorflow as tf
from tvm import relay
from tvm.relay.frontend.tensorflow import from_tensorflow

graph = tf.Graph()
with graph.as_default():
    i = tf.constant(1)
    j = tf.constant(1)
    k = tf.constant(5)

    def c(i, j, k): return \
        tf.equal(tf.not_equal(tf.less(i + j, 10),
                              tf.less(j * k, 100)),
                              tf.greater_equal(k, i + j))

    def b(i, j, k): return [i+j, j+k, k+1]

    r = tf.while_loop(c, b, loop_vars=[i, j, k])

    with tf.Session() as sess:
        writer = tf.summary.FileWriter("graph_viz", graph)
        sess.run(r)
        writer.close()

        expr, params = from_tensorflow(graph.as_graph_def(add_shapes=True))
        binds = {}
        for p in expr.params:
            binds[p] = relay.Constant(params[p.name_hint])
        expr = relay.bind(expr.body, binds)

        print(params)
        print("Relay", expr)

