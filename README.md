Run OpenAI Gym environments on an external process or remote machine using gRPC.

## Installation

[Install Gym] (not required if using [Docker]) and run:

```sh
pip install gymx
```

It is recommended to use a [virtual environment].

## Usage

### Server

To start the server run:

```sh
python -m gymx
```

To use a different port run:

```sh
python -m gymx --port=54321
```

You can also run the server using [Docker]:

```sh
docker run -p 54321:54321 album/gymx
```

### Client

Inside your application use:

```py
from gymx import Env

env = Env('CartPole-v0')
```

To specify the server address use:

```py
env = Env('CartPole-v0', address='localhost:54321')
```

#### API

-   `env.reset()`: Reset the environment's state. Returns `observation`.
-   `env.step(action)`: Step the environment by one timestep. Returns `observation`, `reward`, `done`, `next_episode`. Unlike the original gym API, it automatically resets the environment when done and returns next episode's observation instead of `info`.

[virtual environment]: https://docs.python.org/3/library/venv.html
[install gym]: https://github.com/openai/gym#installation
[docker]: https://docs.docker.com/
