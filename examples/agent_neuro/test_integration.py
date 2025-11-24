"""
Test Agent-Neuro integration components
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))


def test_personality_module():
    """Test personality module can be imported."""
    from python.helpers.neuro_personality import NeuroPersonality, PersonalityTensor
    print("✓ Personality module imported")
    
    # Create instance
    neuro = NeuroPersonality()
    assert neuro.personality.playfulness == 0.95
    print("✓ Personality instance created")


def test_kernel_module():
    """Test ontogenetic kernel module can be imported."""
    from python.helpers.ontogenetic_kernel import (
        OntogeneticKernel,
        initialize_neuro_kernel,
    )
    print("✓ Ontogenetic kernel module imported")
    
    # Create kernel
    kernel = initialize_neuro_kernel()
    assert kernel.genome is not None
    print("✓ Kernel instance created")


def test_extension_files_exist():
    """Test that extension files exist."""
    import os
    
    extensions_dir = os.path.join(os.path.dirname(__file__), '../..', 'python', 'extensions')
    
    # Check personality integration extension
    personality_ext = os.path.join(extensions_dir, 'message_loop_start', 'neuro_personality_integration.py')
    assert os.path.exists(personality_ext), f"Extension not found: {personality_ext}"
    print(f"✓ Found: {personality_ext}")
    
    # Check response enhancement extension
    response_ext = os.path.join(extensions_dir, 'message_loop_end', 'neuro_response_enhancement.py')
    assert os.path.exists(response_ext), f"Extension not found: {response_ext}"
    print(f"✓ Found: {response_ext}")


def test_tool_file_exists():
    """Test that personality tool exists."""
    import os
    
    tools_dir = os.path.join(os.path.dirname(__file__), '../..', 'python', 'tools')
    tool_file = os.path.join(tools_dir, 'neuro_personality.py')
    
    assert os.path.exists(tool_file), f"Tool not found: {tool_file}"
    print(f"✓ Found: {tool_file}")


def test_config_exists():
    """Test that configuration file exists."""
    import os
    
    config_file = os.path.join(os.path.dirname(__file__), '../..', 'config', 'agent_neuro.yaml')
    assert os.path.exists(config_file), f"Config not found: {config_file}"
    print(f"✓ Found: {config_file}")


if __name__ == "__main__":
    print("\nTesting Agent-Neuro Integration Components...\n")
    
    try:
        test_personality_module()
        test_kernel_module()
        test_extension_files_exist()
        test_tool_file_exists()
        test_config_exists()
        
        print("\n✓ All integration component tests passed!\n")
        print("Agent-Neuro core systems are installed and ready.")
        print("\nIntegration with Agent Zero:")
        print("  • Extensions in: python/extensions/")
        print("  • Tool in: python/tools/neuro_personality.py")
        print("  • Config in: config/agent_neuro.yaml")
        print("\nTo enable personality:")
        print("  export ENABLE_NEURO_PERSONALITY=true")
        print("  export NEURO_VERBOSE=true  # Optional")
        print("\n")
    except Exception as e:
        print(f"\n✗ Integration test failed: {e}\n")
        import traceback
        traceback.print_exc()
        raise
