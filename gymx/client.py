import grpc
import numpy as np

from . import config
from .env_pb2 import Action, Empty, Name
from .env_pb2_grpc import EnvStub


def decode_observation(observation):
    if not observation.data:
        return
    return np.asarray(observation.data).reshape(observation.shape)


class Object:
    pass


class Env:

    def __init__(self, name, address=config.address):
        self.channel = grpc.insecure_channel(address)
        self.env = EnvStub(self.channel)
        self.make(name)

    def make(self, name):
        info = self.env.Make(Name(value=name))
        self.observation_space = Object()
        self.action_space = Object()
        self.observation_space.shape = tuple(info.observation_shape)
        self.action_space.n = info.num_actions
        self._max_episode_steps = info.max_episode_steps

    def reset(self):
        return decode_observation(self.env.Reset(Empty()))

    def step(self, action):
        transition = self.env.Step(Action(value=action))
        observation = decode_observation(transition.observation)
        next_episode = decode_observation(transition.next_episode)
        done = next_episode is not None
        return observation, transition.reward, done, next_episode

    def close(self):
        self.channel.close()
