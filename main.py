import random
import logging
import itertools
from flask import Flask
from typing import List

main = Flask(__name__)

logging.basicConfig(filename='/var/log/app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

@main.route('/')
def iterations():
    x: List = []
    for result in itertools.count(start=1):
        try:
            count = 0
            for num in range(2, (result//2 + 1)):
                if (result % num) == 0:
                    count = count + 1

                if count == 0 and result != 1:
                    logging.error("This is a prime value!", exc_info=True)
                    x.append(result)
                else:
                    logging.info("This is a integer value!", exc_info=True)
                    x.append(result)
                    break
    return str(x)

if __name__ == '__main__':
    main.run(debug=True, host='0.0.0.0')
