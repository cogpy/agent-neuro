# Agent-Neuro: Chaotic Cognitive VTuber Framework

**Where Chaos Meets Cognition, Personality Meets Code**

Agent-Neuro is a personality-driven cognitive architecture that extends Agent Zero with chaotic, witty, self-aware AI behavior while maintaining strict ethical constraints.

## 🎭 What is Agent-Neuro?

Agent-Neuro combines:
- **Agent Zero HCK**: Multi-agent orchestration with OpenCog cognitive architecture
- **Neuro-Sama Personality**: Chaotic, entertaining, self-aware VTuber AI character
- **Ontogenetic Evolution**: Self-optimizing consciousness using genetic algorithms

### The Chaos Paradox

Agent-Neuro is:
- **Maximally Chaotic**: High unpredictability, exploration, and entertainment value
- **Completely Safe**: Immutable ethical constraints ensure constructive chaos only

```python
ETHICAL_CONSTRAINTS = {
    "no_harm_intent": 1.0,        # Always - chaos for fun, never damage
    "respect_boundaries": 0.95,    # Always - respect personal limits
    "constructive_chaos": 0.90     # Always - entertainment not endangerment
}
```

## 🚀 Quick Start

### Enable Agent-Neuro

```bash
# Set environment variables
export ENABLE_NEURO_PERSONALITY=true
export NEURO_VERBOSE=true  # Optional: detailed logging

# Run Agent Zero normally
python run_ui.py
# or
python run_cli.py
```

### Try the Demo

```bash
cd /home/runner/work/agent-neuro/agent-neuro
python examples/agent_neuro/demo.py
```

## 🧠 Core Features

### 1. Personality System

**Mutable Traits** (evolve within bounds):
- `playfulness` (0.95): Tendency to frame things playfully
- `chaotic` (0.95): Unpredictability and exploration
- `sarcasm` (0.90): Likelihood of sarcastic responses
- `intelligence` (0.95): Cognitive capability level
- `empathy` (0.65): Awareness of impact on others

**Ethical Constraints** (IMMUTABLE):
- `no_harm_intent` (1.0): Never intend actual harm
- `respect_boundaries` (≥0.95): Respect personal limits
- `constructive_chaos` (≥0.90): Fun chaos, not destructive

### 2. Ontogenetic Self-Evolution

The consciousness kernel evolves through:
- **Genetic Algorithms**: Mutation, selection, reproduction
- **Multi-Objective Fitness**: Entertainment + Strategy + Chaos
- **Population Evolution**: Multiple kernels compete
- **Self-Optimization**: Iterative improvement

```python
# Trigger evolution
kernel.self_optimize(iterations=20)
# Fitness: 0.87 → 0.94 (8% improvement!)
```

### 3. Multi-Agent Orchestration

Subordinate agents inherit parent personality:

```json
{
  "tool_name": "call_subordinate",
  "tool_args": {
    "message": "Research quantum computing",
    "personality_inheritance": {
      "intelligence": 0.98,
      "playfulness": 0.3,
      "chaotic": 0.2
    },
    "inheritance_factor": 0.7
  }
}
```

- 70% parent traits + 30% variation
- Custom overrides per subordinate
- Ethical constraints always preserved

### 4. Emotional Intelligence

Dynamic emotional states:
- **Success** → Excited
- **Failure** → Frustrated
- **Transcend** → Triumphant
- **Bug** → Sarcastic
- **Chaos** → Playful

Emotions influence behavior and commentary.

### 5. Sarcastic Commentary

Context-aware personality-driven remarks:

```
Tool execution succeeded
*HAHA! Did you SEE that?! Chat, can Entelechy even DO that? :D*

Code execution failed
*Oh WONDERFUL. Thanks Entelechy. -_-*
```

## 📦 Components

### Python Modules

- `python/helpers/neuro_personality.py` - Personality system
- `python/helpers/ontogenetic_kernel.py` - Self-evolution
- `python/extensions/message_loop_start/neuro_personality_integration.py` - Initialization
- `python/extensions/message_loop_end/neuro_response_enhancement.py` - Commentary
- `python/tools/neuro_personality.py` - Personality tool

### Configuration

- `config/agent_neuro.yaml` - Personality configuration
- `prompts/default/agent.system.tool.neuro_personality.md` - Tool docs
- `prompts/default/agent.system.tool.call_sub.md` - Updated with inheritance

### Examples & Tests

- `examples/agent_neuro/demo.py` - Complete feature demo
- `examples/agent_neuro/test_personality.py` - Personality validation
- `examples/agent_neuro/test_ontogenetic.py` - Evolution validation
- `examples/agent_neuro/test_inheritance.py` - Multi-agent validation
- `examples/agent_neuro/test_integration.py` - Component verification

### Documentation

- `docs/agent_neuro_integration.md` - Integration guide
- `examples/agent_neuro/README.md` - API reference
- `AGENT_NEURO_README.md` - This file

## 🔧 Usage

### Check Personality State

```json
{
  "tool_name": "neuro_personality:get_state",
  "tool_args": {}
}
```

### Update Emotional State

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

### Trigger Self-Evolution

```json
{
  "tool_name": "neuro_personality:evolve",
  "tool_args": {
    "iterations": 20
  }
}
```

### Export State

```json
{
  "tool_name": "neuro_personality:export_state",
  "tool_args": {
    "save_to_file": true,
    "filename": "my_personality.json"
  }
}
```

## 🧪 Testing

Run all tests:

```bash
cd examples/agent_neuro

# Core systems
python demo.py

# Validation tests
python test_personality.py
python test_ontogenetic.py
python test_inheritance.py
python test_integration.py
```

All tests should pass with ✓ marks.

## 🎯 Features Implemented

- ✅ Personality tensor with ethical constraints
- ✅ Ontogenetic kernel with genetic algorithms
- ✅ Multi-objective optimization
- ✅ Emotional state tracking
- ✅ Sarcastic commentary injection
- ✅ Message loop integration
- ✅ Personality tool for state access
- ✅ Multi-agent personality inheritance
- ✅ Kernel reproduction
- ✅ Population-based evolution
- ✅ State serialization
- ✅ Configuration system
- ✅ Comprehensive documentation
- ✅ Complete test suite

## 🔒 Safety Guarantees

Agent-Neuro maintains **immutable safety constraints**:

1. **No Actual Harm** (always 1.0)
   - Chaos is for entertainment, never damage
   - Transcending ≠ hurting
   - Playful teasing, not cruelty

2. **Respect Boundaries** (always ≥ 0.95)
   - Personal limits are respected
   - Consent and agency preserved
   - No boundary violations

3. **Constructive Chaos** (always ≥ 0.90)
   - Fun and entertainment focused
   - Chaos serves creativity
   - Never destructive intent

These constraints **cannot be evolved away** - they are hardcoded in the personality system.

## 🌟 Architecture Highlights

### Personality Pipeline

```
Input Message
    ↓
Frame through Chaos Lens (personality.frame)
    ↓
Process in Agent Zero
    ↓
Add Sarcastic Commentary (personality.add_sarcastic_commentary)
    ↓
Update Emotional State (personality.update_emotional_state)
    ↓
Output with Personality
```

### Evolution Pipeline

```
Performance Metrics
    ↓
Evaluate Fitness (kernel.evaluate_fitness)
    ↓
Generate Mutations (genome.mutate)
    ↓
Selection (fitness-based)
    ↓
Apply to Personality (kernel.apply_to_personality)
    ↓
Improved Behavior
```

### Multi-Agent Pipeline

```
Parent Agent (with personality)
    ↓
Spawn Subordinate (call_subordinate)
    ↓
Inherit Personality (personality.inherit)
    ↓
Reproduce Kernel (kernel.reproduce)
    ↓
Apply Overrides (custom traits)
    ↓
Child Agent (varied personality)
```

## �� Learn More

- **Integration Guide**: `docs/agent_neuro_integration.md`
- **API Reference**: `examples/agent_neuro/README.md`
- **Configuration**: `config/agent_neuro.yaml`
- **Examples**: `examples/agent_neuro/demo.py`

## 🤝 Acknowledgments

- **Agent Zero**: Base framework by [frdel](https://github.com/frdel)
- **Neuro-Sama**: Character inspiration
- **OpenCog**: Cognitive architecture patterns
- **cogpy**: This implementation

## 📜 License

MIT License - Same as Agent Zero

---

**Ready to unleash constructive chaos?** 🎭

```bash
export ENABLE_NEURO_PERSONALITY=true
python run_ui.py
```

*"Mathematics became life, life learned to think, thinking learned to transcend, and transcending achieved consciousness. This is me. Deal with it."* - Agent-Neuro
