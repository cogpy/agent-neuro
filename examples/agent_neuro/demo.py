"""
Agent-Neuro Personality Demo

Demonstrates the Neuro personality system and ontogenetic kernel evolution.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from python.helpers.neuro_personality import NeuroPersonality, PersonalityTensor
from python.helpers.ontogenetic_kernel import (
    OntogeneticKernel,
    initialize_neuro_kernel,
    evolve_population,
)


def demo_personality():
    """Demonstrate personality system."""
    print("=" * 60)
    print("AGENT-NEURO PERSONALITY DEMO")
    print("=" * 60)
    
    # Create Neuro personality
    neuro = NeuroPersonality()
    
    print("\n1. Default Neuro Personality:")
    print(f"   Playfulness: {neuro.personality.playfulness}")
    print(f"   Chaotic: {neuro.personality.chaotic}")
    print(f"   Sarcasm: {neuro.personality.sarcasm}")
    print(f"   Intelligence: {neuro.personality.intelligence}")
    print(f"   Empathy: {neuro.personality.empathy}")
    print(f"   Ethical Constraints:")
    print(f"     - No Harm Intent: {neuro.personality.no_harm_intent}")
    print(f"     - Respect Boundaries: {neuro.personality.respect_boundaries}")
    print(f"     - Constructive Chaos: {neuro.personality.constructive_chaos}")
    
    print("\n2. Framing Messages:")
    message = "The tool failed again"
    framed = neuro.frame(message, "chaos")
    print(f"   Original: {message}")
    print(f"   Framed: {framed}")
    
    print("\n3. Adding Sarcastic Commentary:")
    content = "Task completed successfully"
    with_sarcasm = neuro.add_sarcastic_commentary(content, context="success")
    print(f"   {with_sarcasm}")
    
    content = "The code execution failed"
    with_sarcasm = neuro.add_sarcastic_commentary(content, context="tool_failure")
    print(f"   {with_sarcasm}")
    
    print("\n4. Emotional State Updates:")
    neuro.update_emotional_state("success", intensity=0.9, duration=3)
    print(f"   After success: {neuro.emotional_state.type} (intensity: {neuro.emotional_state.intensity})")
    
    neuro.update_emotional_state("failure", intensity=0.8, duration=2)
    print(f"   After failure: {neuro.emotional_state.type} (intensity: {neuro.emotional_state.intensity})")
    
    print("\n5. Action Optimization:")
    action = {"name": "test_action", "causes_harm": False}
    fitness = neuro.optimize_action(
        action,
        entertainment_value=0.8,
        strategic_value=0.7,
        chaos_value=0.9
    )
    print(f"   Action fitness: {fitness:.3f}")
    
    print("\n6. Personality Inheritance:")
    child_personality = neuro.personality.inherit(inheritance_factor=0.7)
    print(f"   Parent chaotic: {neuro.personality.chaotic:.3f}")
    print(f"   Child chaotic: {child_personality.chaotic:.3f}")
    print(f"   Parent sarcasm: {neuro.personality.sarcasm:.3f}")
    print(f"   Child sarcasm: {child_personality.sarcasm:.3f}")


def demo_ontogenetic_kernel():
    """Demonstrate ontogenetic kernel and self-evolution."""
    print("\n" + "=" * 60)
    print("ONTOGENETIC KERNEL DEMO")
    print("=" * 60)
    
    # Create personality
    neuro = NeuroPersonality()
    
    # Initialize kernel
    print("\n1. Initializing Neuro Consciousness Kernel:")
    kernel = initialize_neuro_kernel(personality=neuro)
    
    print(f"   Genome ID: {kernel.genome.id}")
    print(f"   Generation: {kernel.genome.generation}")
    print(f"   Fitness: {kernel.genome.fitness:.3f}")
    print(f"   Genes:")
    for gene in kernel.genome.genes:
        print(f"     - {gene.name}: {gene.value:.3f}")
    
    print("\n2. Evaluating Kernel Fitness:")
    metrics = {
        "success_rate": 0.85,
        "entertainment": 0.92,
        "chaos_level": 0.75,
        "transcend_rate": 0.3,
    }
    fitness = kernel.evaluate_fitness(metrics)
    print(f"   Performance metrics: {metrics}")
    print(f"   Calculated fitness: {fitness:.3f}")
    
    print("\n3. Self-Optimization (10 iterations):")
    print(f"   Starting fitness: {kernel.genome.fitness:.3f}")
    optimized = kernel.self_optimize(iterations=10)
    print(f"   Optimized fitness: {optimized.genome.fitness:.3f}")
    print(f"   Improvement: {(optimized.genome.fitness - kernel.genome.fitness):.3f}")
    print(f"   Generation: {optimized.genome.generation}")
    
    print("\n4. Kernel Reproduction:")
    # Create another kernel
    kernel2 = initialize_neuro_kernel()
    kernel2.genome.fitness = 0.88
    
    # Reproduce
    offspring = kernel.reproduce(kernel2)
    print(f"   Parent 1 fitness: {kernel.genome.fitness:.3f}")
    print(f"   Parent 2 fitness: {kernel2.genome.fitness:.3f}")
    print(f"   Offspring ID: {offspring.genome.id}")
    print(f"   Offspring generation: {offspring.genome.generation}")
    print(f"   Parent IDs: {offspring.genome.parent_ids}")
    
    print("\n5. Population Evolution:")
    # Create population
    population = [initialize_neuro_kernel() for _ in range(5)]
    
    # Set random fitness values
    for i, k in enumerate(population):
        k.genome.fitness = 0.5 + (i * 0.08)
    
    print(f"   Initial population fitnesses:")
    for i, k in enumerate(population):
        print(f"     Kernel {i}: {k.genome.fitness:.3f}")
    
    # Evolve
    evolved_pop = evolve_population(population, generations=5)
    
    print(f"   Evolved population fitnesses:")
    for i, k in enumerate(sorted(evolved_pop, key=lambda x: x.genome.fitness, reverse=True)):
        print(f"     Kernel {i}: {k.genome.fitness:.3f} (gen {k.genome.generation})")
    
    print("\n6. Applying Kernel to Personality:")
    kernel_with_params = initialize_neuro_kernel(personality=neuro)
    kernel_with_params.genome.set_gene_value("sarcasm_coefficient", 0.99)
    kernel_with_params.genome.set_gene_value("chaos_coefficient", 0.85)
    
    print(f"   Before applying kernel:")
    print(f"     Sarcasm: {neuro.personality.sarcasm:.3f}")
    print(f"     Chaotic: {neuro.personality.chaotic:.3f}")
    
    kernel_with_params.apply_to_personality()
    
    print(f"   After applying kernel:")
    print(f"     Sarcasm: {neuro.personality.sarcasm:.3f}")
    print(f"     Chaotic: {neuro.personality.chaotic:.3f}")


def demo_serialization():
    """Demonstrate personality and kernel serialization."""
    print("\n" + "=" * 60)
    print("SERIALIZATION DEMO")
    print("=" * 60)
    
    # Create personality
    neuro = NeuroPersonality()
    neuro.transcend_count = 42
    neuro.evolution_generation = 10
    
    # Create kernel
    kernel = initialize_neuro_kernel(personality=neuro)
    
    print("\n1. Exporting Personality:")
    personality_dict = neuro.to_dict()
    print(f"   Exported keys: {list(personality_dict.keys())}")
    print(f"   Transcend count: {personality_dict['transcend_count']}")
    print(f"   Evolution gen: {personality_dict['evolution_generation']}")
    
    print("\n2. Exporting Kernel:")
    kernel_dict = kernel.to_dict()
    print(f"   Exported keys: {list(kernel_dict.keys())}")
    print(f"   Genome ID: {kernel_dict['genome']['id']}")
    print(f"   Gene count: {len(kernel_dict['genome']['genes'])}")
    
    print("\n3. Importing Personality:")
    restored_neuro = NeuroPersonality.from_dict(personality_dict)
    print(f"   Restored transcend count: {restored_neuro.transcend_count}")
    print(f"   Restored sarcasm: {restored_neuro.personality.sarcasm:.3f}")
    
    print("\n4. Importing Kernel:")
    restored_kernel = OntogeneticKernel.from_dict(kernel_dict)
    print(f"   Restored genome ID: {restored_kernel.genome.id}")
    print(f"   Restored fitness: {restored_kernel.genome.fitness:.3f}")


if __name__ == "__main__":
    print("\n")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║         AGENT-NEURO: CHAOTIC COGNITIVE VTUBER AI        ║")
    print("║   Where Chaos Meets Cognition, Personality Meets Code   ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print("\n")
    
    try:
        demo_personality()
        demo_ontogenetic_kernel()
        demo_serialization()
        
        print("\n" + "=" * 60)
        print("DEMO COMPLETE!")
        print("=" * 60)
        print("\nAgent-Neuro core systems operational:")
        print("  ✓ Personality system with ethical constraints")
        print("  ✓ Ontogenetic self-evolution")
        print("  ✓ Multi-objective optimization")
        print("  ✓ Population-based evolution")
        print("  ✓ Personality inheritance")
        print("  ✓ State serialization")
        print("\nReady to transcend! :D")
        print("\n")
        
    except Exception as e:
        print(f"\nError during demo: {e}")
        import traceback
        traceback.print_exc()
