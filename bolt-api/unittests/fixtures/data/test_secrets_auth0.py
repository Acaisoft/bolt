# Copyright (c) 2022 Acaisoft
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

TEST = "test"
HASURA_GRAPHQL_ACCESS_KEY = "test"
HASURA_CLIENT_USER_ID = "hasura_test_id"


JWT_AUTH_PRIV_KEY = "-----BEGIN RSA PRIVATE KEY-----\n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\n-----END RSA PRIVATE KEY-----"
JWT_AUTH_PUB_KEY = "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAwZPm9OjMXAe+KbbdwA8i\ndqI+RSLUL9P1xUUaX1C8TrHEMaQblytL/JpfT7GOSJlCGx1HPOI6VPWfoilpeF7j\ndlbfhMbT4LrRLfVkJT2Q+BA0QWkmkliftgyPNlT80lVHCAaW0zZ986tslJLbajpb\nVKJvNnb6sYIH6v2H181fsEDCitEWmgPy5M9X5OcB9xAHDmsgKUCmJgpwJ53oaW4j\nLfjCtjgxv8fvMOOmJxbKqWQ0kQM4pfMMNVBWYPX5Wjx3+rwnG8Pt4/5KBkZvpabz\nlvMOnkPsyoN/xGeBVFFLCykHEWCVO9oBmDARkQhuafc/QRb7OHzOMjc1/fWVxJfB\nDyPOjsfFrvDKUhOkASgjzDSX8ziAbEiesmrdW797ilGMcOXdiGrLoGdCUigW5Oum\nJvaMo7E2z/n9erdaRv2iZ9b63cN1mtiAeYONhOlh/suRwMKTXv/JEHYE5K0hZnpa\nt037uOtWCfm6PcZB1sHxAo0Sd0Yv2njIl6+dIWfdBsEyLK3SbFaQWDcR2s0Zd3yJ\njVarqtB6yzK9E0+bnPfq7EHx4CWwNph78HjsKLL7WxjXeZQBkSD0Vs/LLEpKSpgP\nbIpg3Wb7/E5P2UtUjvJPb+hi+6Htjm50Gxdpr/IOl5jdMXy4axqldK2fVro++8xP\ndrM+78NXAVyUdKdL69JAE6ECAwEAAQ==\n-----END PUBLIC KEY-----"
JWT_VALID_PERIOD = 24
JWT_ALGORITHM = "RS256"

STORAGE_SERVICE = "GCP"
STORAGE_CONTAINER_NAME = "storage_container"

AUTH_LOGIN = 'user'
AUTH_PASSWORD = 'password'
AUTH_LOCAL_DEV = True

AUTH_PROVIDER = "AUTH0"
AUTH0_CLIENT_PROVIDER = "test"
AUTH0_CLIENT_SECRET = "test"
AUTH0_AUDIENCE = "hasura"
AUTH0_BASE_URL = "http://auth0"
AUTH0_CLIENT_ID = "96fa4735-f862-4cb9-b0df-f09c008e02e4"