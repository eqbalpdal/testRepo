#import logging
#logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
#logging.warning('This is a Warning')

#import logging
#logging.basicConfig(format='%(asctime)s - %(message)s',
#        level=logging.INFO)
#logging.info('Admin logged in')

import logging
logging.basicConfig(format='%(asctime)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Admin logged out')
