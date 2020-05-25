import environ

_ROOT_DIR = environ.Path(__file__) - 2

print("******** ENV PATH", _ROOT_DIR)

ENV = environ.Env(
    # set casting, default value
    DEBUG=(bool, True),
    DATABASE_URL=(
        str,
        'postgres://test_user:password@127.0.0.1:5432/iso_test'
    )
)

try:
    environ.Env.read_env(_ROOT_DIR('.env'))
except Exception as e:
    print("Unable to read .env file " + str(e))
