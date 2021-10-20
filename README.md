# helloworld

Welcome to your first Khan project!
Khan is a library to turn your functions into web servers as quick as possible.
To learn more about the full feature set of Khan, check out the [Tutorial](https://github.com/stitchfix/khan/wiki/My-First-Khan-Service).
Coupled with portal, you'll be able to build a service and have it up and running in no time.

## Usage

```
 # To run inside a docker container
 $ igor portal open

 # To run outside a container
 $ uvicorn run:khan.server --reload --reload-dir . --host localhost
```

Then open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to see the Swagger console for your API.

## Deploying

```
 $ igor portal deploy
```

## Code Formatting

This project uses [black](https://black.readthedocs.io/en/stable/) code formatting.

## Tests

```
 $ pip install -r requirements-test.txt
 $ python -m pytest
```

