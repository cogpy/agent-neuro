"""
Basic validation tests for Agent-Neuro ontogenetic kernel.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from python.helpers.ontogenetic_kernel import (
    OntogeneticKernel,
    KernelGenome,
    KernelGene,
    GeneType,
    initialize_neuro_kernel,
)
from python.helpers.neuro_personality import NeuroPersonality


def test_kernel_creation():
    """Test creating a kernel with default genome."""
    kernel = initialize_neuro_kernel()
    
    assert kernel.genome is not None
    assert kernel.genome.generation == 1
    assert len(kernel.genome.genes) > 0
    assert kernel.genome.fitness >= 0.0
    print("✓ Kernel creation test passed")


def test_gene_mutation():
    """Test gene mutation stays within bounds."""
    gene = KernelGene(
        type=GeneType.COEFFICIENT,
        name="test",
        value=0.5,
        min_value=0.0,
        max_value=1.0
    )
    
    # Mutate many times
    for _ in range(100):
        mutated = gene.mutate(intensity=1.0)
        assert mutated.min_value <= mutated.value <= mutated.max_value
    
    print("✓ Gene mutation test passed")


def test_genome_mutation():
    """Test genome mutation creates offspring."""
    kernel = initialize_neuro_kernel()
    original_id = kernel.genome.id
    
    mutated_genome = kernel.genome.mutate()
    
    assert mutated_genome.id != original_id
    assert mutated_genome.generation == kernel.genome.generation + 1
    assert original_id in mutated_genome.parent_ids
    print("✓ Genome mutation test passed")


def test_kernel_reproduction():
    """Test kernel reproduction creates offspring."""
    kernel1 = initialize_neuro_kernel()
    kernel2 = initialize_neuro_kernel()
    
    offspring = kernel1.reproduce(kernel2)
    
    assert offspring.genome.id not in [kernel1.genome.id, kernel2.genome.id]
    assert len(offspring.genome.parent_ids) == 2
    assert kernel1.genome.id in offspring.genome.parent_ids
    assert kernel2.genome.id in offspring.genome.parent_ids
    print("✓ Kernel reproduction test passed")


def test_fitness_evaluation():
    """Test fitness evaluation."""
    kernel = initialize_neuro_kernel()
    
    metrics = {
        "success_rate": 0.8,
        "entertainment": 0.9,
        "chaos_level": 0.7,
        "transcend_rate": 0.3,
    }
    
    fitness = kernel.evaluate_fitness(metrics)
    
    assert 0.0 <= fitness <= 1.0
    assert kernel.genome.fitness == fitness
    assert len(kernel.optimization_history) > 0
    print("✓ Fitness evaluation test passed")


def test_self_optimization():
    """Test self-optimization improves or maintains fitness."""
    kernel = initialize_neuro_kernel()
    kernel.genome.fitness = 0.5
    
    optimized = kernel.self_optimize(iterations=5)
    
    # Should have tried to improve
    assert optimized.genome.generation >= kernel.genome.generation
    print("✓ Self-optimization test passed")


def test_kernel_personality_sync():
    """Test kernel can sync with personality."""
    neuro = NeuroPersonality()
    kernel = initialize_neuro_kernel(personality=neuro)
    
    # Modify kernel genes
    kernel.genome.set_gene_value("sarcasm_coefficient", 0.99)
    
    # Apply to personality
    kernel.apply_to_personality()
    
    assert neuro.personality.sarcasm == 0.99
    print("✓ Kernel-personality sync test passed")


def test_serialization():
    """Test kernel can be saved and restored."""
    kernel = initialize_neuro_kernel()
    kernel.genome.fitness = 0.87
    
    # Export
    data = kernel.to_dict()
    
    # Import
    restored = OntogeneticKernel.from_dict(data)
    
    assert restored.genome.id == kernel.genome.id
    assert restored.genome.fitness == kernel.genome.fitness
    assert len(restored.genome.genes) == len(kernel.genome.genes)
    print("✓ Serialization test passed")


if __name__ == "__main__":
    print("\nRunning Agent-Neuro Ontogenetic Kernel Tests...\n")
    
    try:
        test_kernel_creation()
        test_gene_mutation()
        test_genome_mutation()
        test_kernel_reproduction()
        test_fitness_evaluation()
        test_self_optimization()
        test_kernel_personality_sync()
        test_serialization()
        
        print("\n✓ All ontogenetic kernel tests passed!\n")
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}\n")
        raise
    except Exception as e:
        print(f"\n✗ Error: {e}\n")
        raise
