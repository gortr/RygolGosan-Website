# Imports the Web Application APP Initialization file for Usage
from RygolGosan import app

# EOF Application Run Time Code
if __name__ == '__main__':
    #app.secret_key = secret_key = 'GP17535HYS01WGMS'
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)