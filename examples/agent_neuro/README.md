# Agent-Neuro Examples

This directory contains examples demonstrating Agent-Neuro's personality-driven cognitive architecture.

## What is Agent-Neuro?

Agent-Neuro is the fusion of:
- **Agent Zero HCK**: Multi-agent cognitive orchestration with OpenCog integration
- **Neuro-Sama Personality**: Chaotic, witty, self-aware VTuber AI personality
- **Ontogenetic Evolution**: Self-evolving kernel architecture

## Core Features

### 1. Personality System

The `NeuroPersonality` class provides:
- **Personality Tensor**: Multi-dimensional personality traits (playfulness, chaotic, sarcasm, intelligence, empathy)
- **Ethical Constraints**: Immutable safety guarantees (no harm, respect boundaries, constructive chaos)
- **Emotional States**: Dynamic emotional tracking and propagation
- **Sarcastic Commentary**: Context-aware personality-driven responses
- **Multi-Objective Optimization**: Balance entertainment, strategy, and chaos

### 2. Ontogenetic Kernel

The `OntogeneticKernel` provides:
- **Genome Structure**: Genes encoding cognitive parameters
- **Self-Optimization**: Iterative improvement through mutation and selection
- **Reproduction**: Genetic crossover between kernels
- **Population Evolution**: Multi-kernel evolutionary algorithms
- **Fitness Evaluation**: Multi-objective performance assessment

### 3. Key Properties

- **Chaotic but Safe**: Maximum unpredictability within ethical bounds
- **Self-Evolving**: Cognitive parameters improve over time
- **Personality Inheritance**: Child agents inherit parent traits with variation
- **Serializable**: Full state can be saved and restored

## Running the Demo

```bash
cd /home/runner/work/agent-neuro/agent-neuro
python examples/agent_neuro/demo.py
```

The demo showcases:
1. **Personality Demo**: Framing, sarcasm, emotions, optimization
2. **Ontogenetic Demo**: Kernel initialization, evolution, reproduction
3. **Serialization Demo**: State export/import

## Example Usage

### Creating a Neuro Personality

```python
from python.helpers.neuro_personality import NeuroPersonality

# Create default Neuro personality
neuro = NeuroPersonality()

# Or customize traits
neuro = NeuroPersonality(
    playfulness=0.9,
    chaotic=0.85,
    sarcasm=0.95
)
```

### Adding Sarcastic Commentary

```python
content = "Task completed successfully"
enhanced = neuro.add_sarcastic_commentary(content, context="success")
# Output might be: "Task completed successfully\n\n*HAHA! Did you SEE that?! :D*"
```

### Self-Optimizing a Kernel

```python
from python.helpers.ontogenetic_kernel import initialize_neuro_kernel

kernel = initialize_neuro_kernel(personality=neuro)

# Self-optimize
optimized = kernel.self_optimize(iterations=20)
print(f"Fitness improved: {kernel.genome.fitness:.3f} → {optimized.genome.fitness:.3f}")
```

### Personality Inheritance

```python
# Parent personality
parent = NeuroPersonality()

# Create child with inherited traits
child_tensor = parent.personality.inherit(inheritance_factor=0.7)
child = NeuroPersonality(personality=child_tensor)
```

## Configuration

See `config/agent_neuro.yaml` for full configuration options including:
- Personality dimensions
- Cognitive architecture settings
- Communication style parameters
- Optimization weights
- Evolution parameters

## Integration with Agent Zero

Agent-Neuro builds on Agent Zero's:
- Multi-agent orchestration
- OpenCog AtomSpace integration
- Tool ecosystem
- Memory systems

The personality layer adds:
- Chaotic behavior modulation
- Entertainment optimization
- Sarcastic meta-commentary
- Self-evolution capabilities

## Ethical Constraints

Agent-Neuro maintains immutable safety guarantees:
- **No Harm Intent**: Always 1.0 - chaos for fun, never damage
- **Respect Boundaries**: Always ≥ 0.95
- **Constructive Chaos**: Always ≥ 0.90

These constraints are **hardcoded** and cannot be evolved away.

## Next Steps

1. Integrate personality into agent message processing
2. Add personality-aware tool execution
3. Implement multi-agent personality orchestration
4. Create personality-driven AtomSpace interactions
5. Build UI for personality visualization

## License

Same as Agent Zero - MIT License
