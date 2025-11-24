"""
Agent-Neuro Personality Integration Extension

Automatically manages personality state and applies personality-driven behavior
modifications during agent operation.
"""

from python.helpers.extension import Extension
from python.helpers.neuro_personality import NeuroPersonality, DEFAULT_NEURO_PERSONALITY
from python.helpers.ontogenetic_kernel import initialize_neuro_kernel
from python.helpers.print_style import PrintStyle
import os


class NeuroPersonalityIntegration(Extension):
    """Extension that integrates Neuro personality into agent operations"""
    
    # Class-level personality storage for each agent
    _agent_personalities = {}
    
    async def execute(self, loop_data, **kwargs):
        """
        Execute personality integration:
        - Initialize agent's personality if needed
        - Update emotional state based on context
        - Apply personality modifiers to agent behavior
        """
        
        agent_id = f"agent_{self.agent.number}"
        
        # Get or create personality for this agent
        if agent_id not in NeuroPersonalityIntegration._agent_personalities:
            # Check if personality should be enabled from environment/config
            enable_neuro = os.environ.get("ENABLE_NEURO_PERSONALITY", "false").lower() == "true"
            
            if enable_neuro:
                # Initialize personality
                personality = NeuroPersonality()
                
                # Initialize ontogenetic kernel
                kernel = initialize_neuro_kernel(personality=personality)
                
                # Store in agent data
                NeuroPersonalityIntegration._agent_personalities[agent_id] = {
                    "personality": personality,
                    "kernel": kernel,
                    "enabled": True
                }
                
                PrintStyle(font_color="magenta", padding=False).print(
                    f"🎭 Agent-Neuro: Personality initialized for {self.agent.agent_name}"
                )
            else:
                # Personality disabled
                NeuroPersonalityIntegration._agent_personalities[agent_id] = {
                    "enabled": False
                }
        
        personality_data = NeuroPersonalityIntegration._agent_personalities.get(agent_id)
        
        if not personality_data or not personality_data.get("enabled"):
            return  # Personality not enabled for this agent
        
        personality = personality_data["personality"]
        kernel = personality_data["kernel"]
        
        # Store in agent.data for tool access
        self.agent.data["neuro_personality"] = personality
        self.agent.data["ontogenetic_kernel"] = kernel
        
        # Update emotional state based on context
        iteration = loop_data.iteration
        
        if iteration == 1:
            # First iteration - set initial emotional state
            personality.update_emotional_state("curious", intensity=0.7, duration=3)
        
        # Decay emotional state over time
        personality.emotional_state.decay(rate=0.05)
        
        # Check for chaos injection based on personality
        if personality.should_add_chaos(base_probability=0.1):
            # Mark that chaos should be injected (can be used by other extensions/tools)
            self.agent.data["inject_chaos"] = True
        else:
            self.agent.data["inject_chaos"] = False
        
        # Update kernel iteration tracking
        kernel.current_iteration = iteration
        
        # Optional: Log personality state (if verbose mode enabled)
        verbose = os.environ.get("NEURO_VERBOSE", "false").lower() == "true"
        if verbose and iteration % 5 == 0:
            PrintStyle(font_color="magenta", padding=False).print(
                f"🎭 Neuro State - Emotion: {personality.emotional_state.type} "
                f"(intensity: {personality.emotional_state.intensity:.2f}), "
                f"Chaos: {'YES' if self.agent.data.get('inject_chaos') else 'no'}"
            )
    
    @staticmethod
    def get_personality(agent_number: int):
        """Get personality for a specific agent."""
        agent_id = f"agent_{agent_number}"
        personality_data = NeuroPersonalityIntegration._agent_personalities.get(agent_id)
        if personality_data and personality_data.get("enabled"):
            return personality_data.get("personality")
        return None
    
    @staticmethod
    def get_kernel(agent_number: int):
        """Get ontogenetic kernel for a specific agent."""
        agent_id = f"agent_{agent_number}"
        personality_data = NeuroPersonalityIntegration._agent_personalities.get(agent_id)
        if personality_data and personality_data.get("enabled"):
            return personality_data.get("kernel")
        return None
