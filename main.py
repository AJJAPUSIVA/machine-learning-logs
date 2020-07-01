import random
import logging
from flask import Flask
from typing import List

main = Flask(__name__)

logging.basicConfig(filename='/var/log/app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


@main.route('/')
def division():
    results: List = []
    for i in range(10):
        try:
            num1 = random.randint(0, 30)
            num2 = random.randint(0, 30)
            result = num1 / num2
            if result == 0:
                logging.error("result is equal to zero!", exc_info=True)
            else:
                logging.info("result is not equal to zero!", exc_info=True)
                results.append(result)
        except ZeroDivisionError:
            logging.critical("Denominator must not be Zero!", exc_info=True)
    return str(results)


# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

if __name__ == '__main__':
    main.run(debug=True, host='0.0.0.0')
