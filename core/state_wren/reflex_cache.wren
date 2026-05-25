/*
 * reflex_cache.wren
 * Wren State Machine & Reflex Cache (CAG layer).
 */

class ReflexCache {
  construct new() {
    _states = {}
    _currentState = "idle"
  }

  addState(name, action) {
    _states[name] = action
  }

  transition(newState) {
    if (_states.containsKey(newState)) {
      _currentState = newState
      System.print("Transitioned to: " + _currentState)
    } else {
      System.print("State not found: " + newState)
    }
  }

  execute() {
    if (_states.containsKey(_currentState)) {
      _states[_currentState].call()
    }
  }

  currentState { _currentState }
}

/*
var cache = ReflexCache.new()
cache.addState("idle") { System.print("Resting...") }
cache.addState("acting") { System.print("Executing O.D.A. cycle...") }

cache.execute()
cache.transition("acting")
cache.execute()
*/
