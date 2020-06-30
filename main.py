import logging
from flask import Flask

main = Flask(__name__)

logging.basicConfig(filename='/var/log/app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

@main.route('/')

def return_div():
  a = 2
  b = 2
  c = a/b

  try:
    if c != 0:
      print = logging.info("c is not equal to 0!", exc_info=True)
      return str(c)
    else:
      print = logging.error("c is equal to 0!", exc_info=True)
      return str(c)
  except ZeroDivisionError as error:
    print = logging.critical("denominator must not be zero", exc_info=True)
#logging.debug('This is a debug message')
#logging.info('This is an info message')
#logging.warning('This is a warning message')
#logging.error('This is an error message')
#logging.critical('This is a critical message')

if __name__ == '__main__':
    main.run(debug=True,host='0.0.0.0')