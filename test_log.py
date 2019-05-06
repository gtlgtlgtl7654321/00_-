import logging
logging.basicConfig(level=logging.DEBUG)
'''
logging的好处，它允许你指定记录信息的级别，有debug，info，warning，
error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。
同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以
放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
'''
s = '0'
n = int(s)
logging.debug('n = %d' % n)
logging.info('n = %d' % n)
logging.warning('n = %d' % n)
logging.error('n = %d' % n)

print(10 / n)