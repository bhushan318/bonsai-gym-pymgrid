import sys
import logging
from microsoft_bonsai_api.simulator.client import BonsaiClientConfig
from bonsai_gym_Pymgrid import GymSimulator3



log = logging.getLogger("gym_simulator")
log.setLevel(logging.DEBUG)


class PymGrid(GymSimulator3):
    # Environment name, from openai-gym
    # environment_name = "CartPole-v0"
    # Simulator name from Inkling
    simulator_name = "PymGridSimulator"

    def gym_to_state(self, observation):
        state = {
            "load": observation[0],
            'hour': observation[1],
            "pv": observation[2],
            "battery_soc": observation[3],
            "capatocharge": observation[4],
            'capa_to_discharge': observation[5],
            'grid_status': observation[6],
            'grid_co2': observation[7],
            'grid_price_import': observation[8],
            'grid_price_export': observation[9],
            'Extra' : observation[10]
        }
        return state
    # convert openai gym observation to our state type

    # convert our action type into openai gym action
    def action_to_gym(self, action):
        return action["command"]


if __name__ == "__main__":
    # create a brain, openai-gym environment, and simulator
    config = BonsaiClientConfig(argv=sys.argv)
    sim = PymGrid(config)
    sim.run_gym()