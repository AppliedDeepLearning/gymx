from concurrent import futures
from time import sleep
import gym
import grpc

from . import config
from .env_pb2 import Info, Observation, Transition
from .env_pb2_grpc import EnvServicer as Service, add_EnvServicer_to_server as register


def encode_observation(observation):
    return Observation(data=observation.ravel(), shape=observation.shape)


class Env(Service):

    def Make(self, name, _):
        name = name.value
        if not hasattr(self, 'env') or self.env.spec.id != name:
            self.env = gym.make(name)
        return Info(observation_shape=self.env.observation_space.shape,
                    num_actions=self.env.action_space.n,
                    max_episode_steps=self.env._max_episode_steps)

    def Reset(self, empty, _):
        return encode_observation(self.env.reset())

    def Step(self, action, _):
        observation, reward, done, _ = self.env.step(action.value)
        observation = encode_observation(observation)
        next_episode = encode_observation(self.env.reset()) if done else None
        return Transition(observation=observation,
                          reward=reward,
                          next_episode=next_episode)


def serve(address=config.address):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    register(Env(), server)
    server.add_insecure_port(address)
    server.start()
    try:
        while True:
            sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
