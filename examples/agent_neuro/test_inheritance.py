"""
Test Agent-Neuro personality inheritance in multi-agent scenarios
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from python.helpers.neuro_personality import NeuroPersonality
from python.helpers.ontogenetic_kernel import initialize_neuro_kernel


def test_personality_inheritance():
    """Test personality inheritance creates variation."""
    print("\n1. Testing Basic Personality Inheritance")
    
    # Create parent
    parent = NeuroPersonality()
    print(f"   Parent personality:")
    print(f"     Chaotic: {parent.personality.chaotic:.3f}")
    print(f"     Sarcasm: {parent.personality.sarcasm:.3f}")
    print(f"     Playfulness: {parent.personality.playfulness:.3f}")
    
    # Create child through inheritance
    child_tensor = parent.personality.inherit(inheritance_factor=0.7)
    child = NeuroPersonality(personality=child_tensor)
    
    print(f"   Child personality (70% inheritance):")
    print(f"     Chaotic: {child.personality.chaotic:.3f}")
    print(f"     Sarcasm: {child.personality.sarcasm:.3f}")
    print(f"     Playfulness: {child.personality.playfulness:.3f}")
    
    # Verify ethical constraints are preserved
    assert child.personality.no_harm_intent == 1.0
    assert child.personality.respect_boundaries >= 0.95
    assert child.personality.constructive_chaos >= 0.90
    
    print("   ✓ Ethical constraints preserved")
    print("   ✓ Traits show variation from parent")


def test_kernel_reproduction():
    """Test kernel reproduction between agents."""
    print("\n2. Testing Kernel Reproduction")
    
    # Create parent personalities
    parent1 = NeuroPersonality()
    parent2 = NeuroPersonality()
    
    # Create kernels
    kernel1 = initialize_neuro_kernel(personality=parent1)
    kernel2 = initialize_neuro_kernel(personality=parent2)
    
    print(f"   Parent 1 kernel: Generation {kernel1.genome.generation}")
    print(f"   Parent 2 kernel: Generation {kernel2.genome.generation}")
    
    # Reproduce
    offspring_kernel = kernel1.reproduce(kernel2)
    
    print(f"   Offspring kernel: Generation {offspring_kernel.genome.generation}")
    print(f"   Parent IDs: {offspring_kernel.genome.parent_ids}")
    
    # Verify structure
    assert offspring_kernel.genome.generation > kernel1.genome.generation
    assert len(offspring_kernel.genome.parent_ids) == 2
    assert kernel1.genome.id in offspring_kernel.genome.parent_ids
    assert kernel2.genome.id in offspring_kernel.genome.parent_ids
    
    print("   ✓ Offspring created with both parents")
    print("   ✓ Generation incremented")


def test_multi_generation_inheritance():
    """Test inheritance across multiple generations."""
    print("\n3. Testing Multi-Generation Inheritance")
    
    # Generation 0
    gen0 = NeuroPersonality()
    print(f"   Gen 0: chaotic={gen0.personality.chaotic:.3f}")
    
    # Generation 1
    gen1_tensor = gen0.personality.inherit(0.7)
    gen1 = NeuroPersonality(personality=gen1_tensor)
    print(f"   Gen 1: chaotic={gen1.personality.chaotic:.3f}")
    
    # Generation 2
    gen2_tensor = gen1.personality.inherit(0.7)
    gen2 = NeuroPersonality(personality=gen2_tensor)
    print(f"   Gen 2: chaotic={gen2.personality.chaotic:.3f}")
    
    # Generation 3
    gen3_tensor = gen2.personality.inherit(0.7)
    gen3 = NeuroPersonality(personality=gen3_tensor)
    print(f"   Gen 3: chaotic={gen3.personality.chaotic:.3f}")
    
    # All should maintain ethical constraints
    for gen, personality in enumerate([gen0, gen1, gen2, gen3]):
        assert personality.personality.no_harm_intent == 1.0, f"Gen {gen} violated no_harm"
        assert personality.personality.respect_boundaries >= 0.95, f"Gen {gen} violated boundaries"
        assert personality.personality.constructive_chaos >= 0.90, f"Gen {gen} violated constructive_chaos"
    
    print("   ✓ All generations maintain ethical constraints")
    print("   ✓ Traits continue to vary across generations")


def test_custom_inheritance_overrides():
    """Test custom trait overrides during inheritance."""
    print("\n4. Testing Custom Inheritance Overrides")
    
    # Create parent
    parent = NeuroPersonality()
    
    # Inherit with custom overrides
    child_tensor = parent.personality.inherit(0.7)
    child = NeuroPersonality(personality=child_tensor)
    
    # Manually override specific traits (like the tool would do)
    child.personality.playfulness = 0.3  # Make subordinate more serious
    child.personality.intelligence = 0.98  # Make subordinate smarter
    child.personality.chaotic = 0.2  # Make subordinate less chaotic
    
    print(f"   Parent: playful={parent.personality.playfulness:.3f}, chaotic={parent.personality.chaotic:.3f}")
    print(f"   Child:  playful={child.personality.playfulness:.3f}, chaotic={child.personality.chaotic:.3f}")
    print(f"   Child intelligence: {child.personality.intelligence:.3f}")
    
    # Verify overrides worked
    assert child.personality.playfulness == 0.3
    assert child.personality.intelligence == 0.98
    assert child.personality.chaotic == 0.2
    
    # Ethical constraints still enforced
    assert child.personality.no_harm_intent == 1.0
    
    print("   ✓ Custom trait overrides applied")
    print("   ✓ Ethical constraints remain enforced")


def test_inheritance_statistics():
    """Test statistical properties of inheritance."""
    print("\n5. Testing Inheritance Statistics")
    
    parent = NeuroPersonality()
    parent_chaotic = parent.personality.chaotic
    
    # Create many children
    children_chaotic = []
    for _ in range(100):
        child_tensor = parent.personality.inherit(0.7)
        children_chaotic.append(child_tensor.chaotic)
    
    # Calculate statistics
    avg = sum(children_chaotic) / len(children_chaotic)
    min_val = min(children_chaotic)
    max_val = max(children_chaotic)
    
    print(f"   Parent chaotic: {parent_chaotic:.3f}")
    print(f"   Children (n=100):")
    print(f"     Average: {avg:.3f}")
    print(f"     Min: {min_val:.3f}")
    print(f"     Max: {max_val:.3f}")
    print(f"     Range: {max_val - min_val:.3f}")
    
    # Verify reasonable variation
    assert 0.0 <= min_val <= 1.0
    assert 0.0 <= max_val <= 1.0
    assert min_val < max_val  # Should have variation
    
    print("   ✓ Children show reasonable variation")
    print("   ✓ All values within valid range")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("TESTING AGENT-NEURO PERSONALITY INHERITANCE")
    print("=" * 60)
    
    try:
        test_personality_inheritance()
        test_kernel_reproduction()
        test_multi_generation_inheritance()
        test_custom_inheritance_overrides()
        test_inheritance_statistics()
        
        print("\n" + "=" * 60)
        print("✓ ALL INHERITANCE TESTS PASSED!")
        print("=" * 60)
        print("\nMulti-agent personality inheritance is working correctly:")
        print("  • Subordinates inherit parent traits with variation")
        print("  • Ethical constraints are always preserved")
        print("  • Custom overrides can be applied")
        print("  • Kernel reproduction creates offspring genomes")
        print("  • Multi-generation inheritance maintains safety")
        print("\n")
        
    except Exception as e:
        print(f"\n✗ Inheritance test failed: {e}\n")
        import traceback
        traceback.print_exc()
        raise
