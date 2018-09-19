'''
Implement with PoC base
The base source code:
 A logistic regression learning algorithm example using TensorFlow library.
 Code: https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/2_BasicModels/logistic_regression.py
'''

from framework.tasks import BaseTask
from framework import Context
from typing import Any

import warnings
warnings.filterwarnings(action='ignore', category=RuntimeWarning)

import tensorflow as tf
tf.logging.set_verbosity(tf.logging.ERROR)

# Import mnist data
from tensorflow.examples.tutorials.mnist import input_data

class Task(BaseTask):
    """
    Concrete task class.
    """
    SAVED_MODEL_PATH = 'saved_models/model'

    def __init__(self, context: Context) -> None:
        super().__init__(context)

    def execute(self) -> Any:
        """
        Concrete execute method.

        Notes
        -----
        1. Logging:
            You can output logs with `self.context.logger`.
            (e.g.) self.context.logger.debug("logging output")
        2. Command Line Arguments:
            You can access to arguments through `self.args` after set your arguments
            through `set_arguments` method.
            (e.g.) self.context.config.get('model_path')
        3. File Path:
            You can get absolute path under `data` directory by `self.context.file.get_path`.
            Please put your files (data set or any necessary files) under `data` directory.
            (e.g.) self.context.file.get_path('sample.csv')
        """
        self.context.logger.debug("logging output")

        # Logger
        logger = self.context.logger

        # Parameters
        learning_rate = self.context.config.get('learning_rate')
        training_epochs = self.context.config.get('training_epochs')
        batch_size = self.context.config.get('batch_size')
        display_step = self.context.config.get('display_step')
        use_saved_model = self.context.config.get('use_saved_model')

        # Download dataset to /data/tmp
        mnist = input_data.read_data_sets(self.context.file.get_path("tmp"), one_hot=True)

        # tf Graph Input
        x = tf.placeholder(tf.float32, [None, 784])  # mnist data image of shape 28*28=784
        y = tf.placeholder(tf.float32, [None, 10])  # 0-9 digits recognition => 10 classes

        # Set model weights
        W = tf.Variable(tf.zeros([784, 10]))
        b = tf.Variable(tf.zeros([10]))

        # Construct model
        pred = tf.nn.softmax(tf.matmul(x, W) + b)  # Softmax

        # Minimize error using cross entropy
        cost = tf.reduce_mean(-tf.reduce_sum(y * tf.log(pred), reduction_indices=1))
        # Gradient Descent
        optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

        # Initialize the variables (i.e. assign their default value)
        init = tf.global_variables_initializer()

        # Start training
        with tf.Session() as sess:

            # Run the initializer
            sess.run(init)
            saver = tf.train.Saver()

            if self.to_bool(use_saved_model):
                logger.info("Use saved model...")
                # Restore model
                saver.restore(sess, self.context.file.get_path(self.SAVED_MODEL_PATH))
            else:
                logger.info("Start training...")
                # Training cycle
                for epoch in range(training_epochs):
                    avg_cost = 0.
                    total_batch = int(mnist.train.num_examples / batch_size)
                    # Loop over all batches
                    for i in range(total_batch):
                        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
                        # Run optimization op (backprop) and cost op (to get loss value)
                        _, c = sess.run([optimizer, cost], feed_dict={x: batch_xs,
                                                                      y: batch_ys})
                        # Compute average loss
                        avg_cost += c / total_batch
                    # Display logs per epoch step
                    if (epoch + 1) % display_step == 0:
                        #logger.info("Epoch: %04d cost=", epoch + 1, "{:.9f}".format(avg_cost))
                        msg = "Epoch: " + str(epoch + 1) + "cost= " + "{:.9f}".format(avg_cost)
                        logger.info(msg)

                logger.info("Optimization Finished!")
                # Save model
                saver.save(sess, self.context.file.get_path(self.SAVED_MODEL_PATH))

            # Test model
            correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
            # Calculate accuracy
            accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
            #logger.info("Accuracy:", accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))
            msg = "Accuracy: " + str(accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))
            logger.info(msg)

    def set_arguments(self) -> None:
        """
        Set your command line arguments if necessary.

        Notes
        -----
        Adding command line arguments.
        (e.g.) `self.context.config.set_argument('--model', dest="model_path", help='set model path')`
        """

        learning_rate = 0.01
        training_epochs = 25
        batch_size = 100
        display_step = 1
        use_saved_model = 'True'

        self.context.config.set_argument('--learning_rate', dest="learning_rate", default=learning_rate, help='set learning rate')
        self.context.config.set_argument('--training_epochs', dest="training_epochs", default=training_epochs, help='set training epochs')
        self.context.config.set_argument('--batch_size', dest="batch_size", default=batch_size, help='set batch size')
        self.context.config.set_argument('--display_step', dest="display_step", default=display_step, help='set display step')
        self.context.config.set_argument('--use_saved_model', dest="use_saved_model", default=use_saved_model, help='Use saved model')


    def to_bool(self, str: str) -> bool:
        if str.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif str.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise ValueError
