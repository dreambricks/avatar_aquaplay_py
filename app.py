from flask import Flask

app = Flask(__name__)

# configuration
app.secret_key = 'db_secret'

# init apps


# register blueprints




def main():
    context = ('static/certificate.crt', 'static/privateKey.key')
    app.run(host='0.0.0.0', port=443, ssl_context=context)

if __name__ == '__main__':
    main()