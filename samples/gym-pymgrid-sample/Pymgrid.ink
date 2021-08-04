
inkling "2.0"

using Number

type SimState {
	load: Number.Float32,
	hour: Number.Float32,
	pv: Number.Float32,
	battery_soc: Number.Float32,
	capatocharge: Number.Float32,
	capa_to_discharge: Number.Float32,
	grid_status: Number.Float32,	
	grid_co2: Number.Float32,
	grid_price_import: Number.Float32,
	grid_price_export: Number.Float32,
	Extra: Number.Float32,
	_gym_reward: number,
	_gym_terminal: number
}


type GameState {
	load: Number.Float32,
	hour: Number.Float32,
	pv: Number.Float32,
	battery_soc: Number.Float32,
	capatocharge: Number.Float32,
	capa_to_discharge: Number.Float32,
	grid_status: Number.Float32,	
	grid_co2: Number.Float32,
	grid_price_import: Number.Float32,
	grid_price_export: Number.Float32,
	Extra: Number.Float32,
}

type Action {
    command: Number.Int8<0..4 step 1>
}

type PymgridConfig {
    episode_length: Number.Int8,
    deque_size: Number.UInt8
}

function Reward(ss: SimState) {
    return ss._gym_reward
}

function Terminal(ss: SimState) {
    return ss._gym_terminal
}

simulator PymGridSimulator(action: Action, config: PymgridConfig ): SimState {
}

graph (input: GameState): Action {
    concept Maxreward(input): Action {
        curriculum {
            reward Reward
            terminal Terminal
            source PymGridSimulator
            lesson Randomstart{
                scenario {
                    episode_length: -1,
                    deque_size: 1
                }
            }
        }
    }
    output Maxreward
}
