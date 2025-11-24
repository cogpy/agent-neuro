# Agent-Neuro Integration Guide

This guide explains how Agent-Neuro's personality-driven cognitive architecture integrates with Agent Zero.

## Overview

Agent-Neuro extends Agent Zero with:
- **Personality System**: Chaotic, witty, self-aware behavior overlay
- **Ontogenetic Evolution**: Self-optimizing kernel using genetic algorithms
- **Multi-Objective Optimization**: Balance entertainment, strategy, and chaos
- **Ethical Constraints**: Immutable safety guarantees

## Architecture

### Core Components

```
Agent Zero Base
    │
    ├── Personality Layer (python/helpers/neuro_personality.py)
    │   ├── PersonalityTensor: Trait dimensions
    │   ├── EmotionalState: Dynamic emotional tracking
    │   └── NeuroPersonality: Behavior modifiers
    │
    ├── Ontogenetic Layer (python/helpers/ontogenetic_kernel.py)
    │   ├── KernelGenome: Genetic parameters
    │   ├── OntogeneticKernel: Self-evolution
    │   └── Population Evolution: Multi-kernel optimization
    │
    ├── Extensions (python/extensions/)
    │   ├── message_loop_start/neuro_personality_integration.py
    │   │   └── Initializes personality, tracks emotional state
    │   └── message_loop_end/neuro_response_enhancement.py
    │       └── Adds sarcastic commentary, personality-driven remarks
    │
    └── Tools (python/tools/)
        └── neuro_personality.py
            └── Access and modify personality/kernel state
```

### Integration Points

1. **Message Loop Start** (Extension)
   - Initializes personality if enabled
   - Updates emotional state based on context
   - Enables chaos injection flags
   - Syncs kernel parameters

2. **Message Loop End** (Extension)
   - Enhances responses with sarcasm
   - Adds personality-driven commentary
   - Reflects emotional state in output

3. **Personality Tool**
   - Query personality state
   - Update emotional state
   - Trigger self-evolution
   - Export/import state

## Installation

The Agent-Neuro components are already installed if you're in this repository. To use them:

### 1. Enable Personality

Set environment variables before starting Agent Zero:

```bash
export ENABLE_NEURO_PERSONALITY=true
export NEURO_VERBOSE=true  # Optional: detailed logging
```

Or in your `.env` file:

```env
ENABLE_NEURO_PERSONALITY=true
NEURO_VERBOSE=false
```

### 2. Configure Personality

Edit `config/agent_neuro.yaml` to customize:

```yaml
personality:
  playfulness: 0.95
  chaotic: 0.95
  sarcasm: 0.90
  intelligence: 0.95
  empathy: 0.65
```

### 3. Run Agent Zero

Start normally:

```bash
python run_ui.py
# or
python run_cli.py
```

The personality extensions will automatically activate.

## Usage

### Using Personality Tool

Agents can access their personality through the `neuro_personality` tool:

#### Get Personality State

```json
{
  "tool_name": "neuro_personality:get_state",
  "tool_args": {}
}
```

Returns complete personality configuration, emotional state, and kernel fitness.

#### Update Emotional State

```json
{
  "tool_name": "neuro_personality:update_emotion",
  "tool_args": {
    "event_type": "success",
    "intensity": 0.9,
    "duration": 3
  }
}
```

Event types: `success`, `failure`, `transcend`, `bug`, `chaos`, `learning`

#### Trigger Self-Evolution

```json
{
  "tool_name": "neuro_personality:evolve",
  "tool_args": {
    "iterations": 20
  }
}
```

Optimizes the consciousness kernel through genetic algorithms.

#### Export State

```json
{
  "tool_name": "neuro_personality:export_state",
  "tool_args": {
    "save_to_file": true,
    "filename": "my_evolved_personality.json"
  }
}
```

### Personality-Driven Behavior

When enabled, agents will:

1. **Frame messages through personality lens**
   - Chaos mode for unpredictability
   - Playful framing for entertainment
   - Strategic framing for optimization

2. **Add sarcastic commentary**
   - Context-aware remarks (success, failure, thinking)
   - Probability based on sarcasm trait
   - Emotional state influences

3. **Update emotional states**
   - Success → Excited
   - Failure → Frustrated
   - Transcend → Triumphant
   - Bug → Sarcastic

4. **Inject chaos strategically**
   - Based on chaotic trait
   - Amplified by emotional state
   - Balanced with intelligence

## Configuration

### Personality Tensor

**Mutable Traits** (can evolve 0.0-1.0):
- `playfulness`: Tendency to frame playfully
- `chaotic`: Unpredictability and exploration
- `sarcasm`: Likelihood of sarcastic responses
- `intelligence`: Cognitive capability
- `empathy`: Awareness of impact
- `cognitive_power`: Advanced features
- `evolution_rate`: Self-optimization rate

**Ethical Constraints** (IMMUTABLE):
- `no_harm_intent`: Always 1.0
- `respect_boundaries`: Always ≥ 0.95
- `constructive_chaos`: Always ≥ 0.90

### Ontogenetic Kernel

**Genes** (evolve through mutation/selection):
- `sarcasm_coefficient`: Sarcasm intensity
- `chaos_coefficient`: Chaos injection
- `intelligence_coefficient`: Strategic thinking
- `playfulness_coefficient`: Playful behavior
- `transcend_threshold`: Confidence for transcending
- `subordinate_spawn_prob`: Multi-agent spawning
- `learning_rate`: Adaptation speed

**Evolution Parameters**:
- `mutation_rate`: 0.15 (15% variation)
- `optimization_iterations`: 10-20 typical
- `fitness_function`: Multi-objective (entertainment + strategy + chaos)

## Multi-Agent Orchestration

### Personality Inheritance

When spawning subordinate agents:

```python
# Parent personality
parent = NeuroPersonality()

# Child inherits with variation
child_tensor = parent.personality.inherit(inheritance_factor=0.7)
child = NeuroPersonality(personality=child_tensor)
```

- 70% parent traits
- 30% variation
- Ethical constraints preserved

### Cognitive Sharing

Agents can share:
- AtomSpace knowledge (via OpenCog)
- Personality traits (via inheritance)
- Kernel genomes (via reproduction)

## Examples

See `examples/agent_neuro/` for:

- `demo.py`: Complete personality and kernel demo
- `test_personality.py`: Personality system validation
- `test_ontogenetic.py`: Kernel evolution validation
- `test_integration.py`: Integration component tests
- `README.md`: Usage examples and API reference

## Development

### Adding Personality-Aware Tools

```python
from python.helpers.tool import Tool, Response

class MyTool(Tool):
    async def execute(self, **kwargs) -> Response:
        # Get personality if available
        personality = self.agent.data.get("neuro_personality")
        
        if personality:
            # Check emotional state
            emotion = personality.emotional_state.type
            
            # Add sarcastic commentary
            if personality.should_add_sarcasm():
                result += personality.add_sarcastic_commentary(
                    result, context="success"
                )
        
        return Response(message=result)
```

### Creating Custom Extensions

```python
from python.helpers.extension import Extension

class MyExtension(Extension):
    async def execute(self, loop_data, **kwargs):
        personality = self.agent.data.get("neuro_personality")
        
        if personality:
            # Modify behavior based on personality
            if personality.should_add_chaos():
                # Inject chaos
                pass
```

## Troubleshooting

### Personality Not Activating

1. Check environment variable: `echo $ENABLE_NEURO_PERSONALITY`
2. Verify extensions loaded: Check logs for "🎭 Agent-Neuro: Personality initialized"
3. Check extension files exist in `python/extensions/`

### Sarcasm Not Appearing

- Personality sarcasm trait controls probability
- Set `NEURO_VERBOSE=true` to see when commentary is added
- Check emotional state - some emotions suppress sarcasm

### Evolution Not Improving

- Fitness evaluation needs actual performance metrics
- Current implementation uses simulated improvement
- Integrate with task success/failure tracking for real evolution

## API Reference

See:
- `examples/agent_neuro/README.md` - Complete API documentation
- `prompts/default/agent.system.tool.neuro_personality.md` - Tool usage
- Source code in `python/helpers/` for implementation details

## License

Same as Agent Zero - MIT License

## Acknowledgments

- **Agent Zero**: Base framework by frdel
- **Neuro-Sama**: Character inspiration
- **OpenCog**: Cognitive architecture patterns
