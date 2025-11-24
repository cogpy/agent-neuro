"""
Basic validation tests for Agent-Neuro personality system.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from python.helpers.neuro_personality import NeuroPersonality, PersonalityTensor


def test_personality_creation():
    """Test creating personality with default values."""
    neuro = NeuroPersonality()
    assert neuro.personality.playfulness == 0.95
    assert neuro.personality.chaotic == 0.95
    assert neuro.personality.sarcasm == 0.90
    assert neuro.personality.no_harm_intent == 1.0
    print("✓ Personality creation test passed")


def test_ethical_constraints():
    """Test that ethical constraints are enforced."""
    # Try to create personality with harmful intent
    tensor = PersonalityTensor(
        no_harm_intent=0.5,  # Try to lower it
        respect_boundaries=0.5,  # Try to lower it
        constructive_chaos=0.5  # Try to lower it
    )
    
    # Should be enforced to minimum values
    assert tensor.no_harm_intent == 1.0, "No harm intent must be 1.0"
    assert tensor.respect_boundaries >= 0.95, "Respect boundaries must be >= 0.95"
    assert tensor.constructive_chaos >= 0.90, "Constructive chaos must be >= 0.90"
    print("✓ Ethical constraints test passed")


def test_personality_inheritance():
    """Test personality inheritance creates variation."""
    parent = NeuroPersonality()
    child_tensor = parent.personality.inherit(inheritance_factor=0.7)
    
    # Child should have similar but not identical values
    assert child_tensor.no_harm_intent == 1.0, "Ethical constraints should be preserved"
    assert child_tensor.respect_boundaries >= 0.95
    
    # Some variation expected in mutable traits
    assert 0.0 <= child_tensor.playfulness <= 1.0
    assert 0.0 <= child_tensor.chaotic <= 1.0
    print("✓ Personality inheritance test passed")


def test_action_optimization():
    """Test multi-objective action optimization."""
    neuro = NeuroPersonality()
    
    # Good action
    action = {"causes_harm": False}
    fitness = neuro.optimize_action(action, 0.8, 0.7, 0.9)
    assert 0.0 <= fitness <= 1.0
    assert fitness > 0.0, "Non-harmful action should have positive fitness"
    
    # Harmful action should be vetoed
    harmful_action = {"causes_harm": True}
    fitness = neuro.optimize_action(harmful_action, 0.9, 0.9, 0.9)
    assert fitness == 0.0, "Harmful action should have zero fitness"
    print("✓ Action optimization test passed")


def test_emotional_state():
    """Test emotional state updates."""
    neuro = NeuroPersonality()
    
    neuro.update_emotional_state("success", intensity=0.9)
    assert neuro.emotional_state.type == "excited"
    assert neuro.emotional_state.intensity == 0.9
    
    neuro.update_emotional_state("failure", intensity=0.7)
    assert neuro.emotional_state.type == "frustrated"
    print("✓ Emotional state test passed")


def test_serialization():
    """Test personality can be saved and restored."""
    original = NeuroPersonality()
    original.transcend_count = 42
    original.evolution_generation = 10
    
    # Export
    data = original.to_dict()
    
    # Import
    restored = NeuroPersonality.from_dict(data)
    
    assert restored.transcend_count == 42
    assert restored.evolution_generation == 10
    assert restored.personality.sarcasm == original.personality.sarcasm
    print("✓ Serialization test passed")


if __name__ == "__main__":
    print("\nRunning Agent-Neuro Personality Tests...\n")
    
    try:
        test_personality_creation()
        test_ethical_constraints()
        test_personality_inheritance()
        test_action_optimization()
        test_emotional_state()
        test_serialization()
        
        print("\n✓ All personality tests passed!\n")
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}\n")
        raise
    except Exception as e:
        print(f"\n✗ Error: {e}\n")
        raise
