import logging


logging.basicConfig(filename='/var/log/app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
a = 2
b = 0
try:
   c = a/b
   if c != 0:
   	print = logging.info("c is not equal to 0!!", exc_info=True)
   else:
       print = logging.critical("c is equal to 0!", exc_info=True)
except Exception as e:
  logging.error("denominator must not be zero", exc_info=True)
   
#logging.debug('This is a debug message')
#logging.info('This is an info message')
#logging.warning('This is a warning message')
#logging.error('This is an error message')
#logging.critical('This is a critical message')
