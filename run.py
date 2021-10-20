import khan
import random

from typing import Dict, List

#
# Khan is just a thin wrapper around FastAPI
#
#    https://fastapi.tiangolo.com
#    https://github.com/stitchfix/khan/tree/v3
#
# Checkout the documentation to see what it possible. All Khan does is setup
# the server for you automatically with some platform defaults such as structured
# logging, distributed tracing, and plugins
#


#
# Simply expose a function to khan and it'll build a REST API around it
#
# You can request data from it by,
#   $ curl -XGET http://localhost:5000/my_func?a=2&b=4
#
@khan.get("/my_func")
async def my_func(a: int, b: str):
    return b * random.randint(1, a)


#
# Now and example with other HTTP verbs
#
# You can request data from it by,
#   $ curl -XPOST http://localhost:5000/my_other_func -d '{ "a" : { "b" : 3 } }'
#
@khan.post("/my_other_func")
async def my_other_func(a: Dict[str, int]) -> int:
    val = 0
    for k, v in a.items():
        val += v
    return val


#
# Finally let's request some resources from the real world!
#
http = khan.client("http")


@khan.post("/external")
async def get_external():
    # Inside a request, we use the async version of the API, all
    # you have to do is drop the sync and add the await!
    bing = await http.get("http://bing.com")
    return bing.text


@khan.post('/foo/bar')
async def create_foobar():
    return 'foobar'
