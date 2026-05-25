-- ltc_engine.lua
-- Liquid Time-Constant (LTC) Engine for continuous-time state inference.

local LTCEngine = {}
LTCEngine.__index = LTCEngine

function LTCEngine.new(state_dim, tau)
    local self = setmetatable({}, LTCEngine)
    self.state = {}
    for i = 1, state_dim do self.state[i] = 0.0 end
    self.tau = tau or 1.0  -- Time constant
    return self
end

-- Update state based on input and elapsed time (dt)
-- Following a simplified ODE: dS/dt = (Input - S) / tau
function LTCEngine:update(input_vector, dt)
    for i = 1, #self.state do
        local input = input_vector[i] or 0.0
        local delta = (input - self.state[i]) / self.tau
        self.state[i] = self.state[i] + delta * dt
    end
end

function LTCEngine:get_state()
    return self.state
end

-- Boilerplate for standalone test
local function test()
    local engine = LTCEngine.new(2, 0.5)
    print("Initial State: " .. table.concat(engine:get_state(), ", "))

    -- Simulate update with input [1.0, 0.5] over 0.1s
    engine:update({1.0, 0.5}, 0.1)
    print("State after 0.1s: " .. table.concat(engine:get_state(), ", "))
end

-- Uncomment to run test if executed directly
-- test()

return LTCEngine
