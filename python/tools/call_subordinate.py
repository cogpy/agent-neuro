from agent import Agent, UserMessage
from python.helpers.tool import Tool, Response


class Delegation(Tool):

    async def execute(self, message="", reset="", personality_inheritance=None, **kwargs):
        # create subordinate agent using the data object on this agent and set superior agent to his data object
        if (
            self.agent.get_data(Agent.DATA_NAME_SUBORDINATE) is None
            or str(reset).lower().strip() == "true"
        ):
            sub = Agent(
                self.agent.number + 1, self.agent.config, self.agent.context
            )
            sub.set_data(Agent.DATA_NAME_SUPERIOR, self.agent)
            self.agent.set_data(Agent.DATA_NAME_SUBORDINATE, sub)
            
            # Agent-Neuro: Inherit personality if enabled
            self._inherit_personality(sub, personality_inheritance, **kwargs)

        # add user message to subordinate agent
        subordinate: Agent = self.agent.get_data(Agent.DATA_NAME_SUBORDINATE)
        subordinate.hist_add_user_message(UserMessage(message=message, attachments=[]))
        # run subordinate monologue
        result = await subordinate.monologue()
        # result
        return Response(message=result, break_loop=False)
    
    def _inherit_personality(self, subordinate: Agent, personality_inheritance, **kwargs):
        """
        Agent-Neuro: Inherit personality from superior to subordinate.
        
        Args:
            subordinate: The subordinate agent
            personality_inheritance: Dict of personality overrides or None
            **kwargs: Additional configuration
        """
        # Check if parent has personality enabled
        parent_personality = self.agent.data.get("neuro_personality")
        parent_kernel = self.agent.data.get("ontogenetic_kernel")
        
        if not parent_personality:
            return  # Parent doesn't have personality, skip inheritance
        
        # Get inheritance factor from config or kwargs
        inheritance_factor = kwargs.get("inheritance_factor", 0.7)
        
        # Create child personality through inheritance
        from python.helpers.neuro_personality import NeuroPersonality
        from python.helpers.ontogenetic_kernel import OntogeneticKernel
        
        # Inherit personality tensor
        child_tensor = parent_personality.personality.inherit(
            inheritance_factor=inheritance_factor
        )
        
        # Apply any custom overrides from personality_inheritance param
        if personality_inheritance and isinstance(personality_inheritance, dict):
            for trait, value in personality_inheritance.items():
                if hasattr(child_tensor, trait):
                    setattr(child_tensor, trait, float(value))
        
        # Create child personality instance
        child_personality = NeuroPersonality(personality=child_tensor)
        
        # Inherit kernel if parent has one
        child_kernel = None
        if parent_kernel:
            # Create child through kernel reproduction
            from python.helpers.ontogenetic_kernel import initialize_neuro_kernel
            temp_kernel = initialize_neuro_kernel()  # Temporary second parent
            child_kernel = parent_kernel.reproduce(temp_kernel)
            child_kernel.personality = child_personality
            child_kernel.apply_to_personality()
        
        # Set personality in subordinate's data
        subordinate.data["neuro_personality"] = child_personality
        subordinate.data["ontogenetic_kernel"] = child_kernel
        
        # Log inheritance if verbose mode
        import os
        verbose = os.environ.get("NEURO_VERBOSE", "false").lower() == "true"
        if verbose:
            from python.helpers.print_style import PrintStyle
            PrintStyle(font_color="magenta", padding=False).print(
                f"🎭 Agent {subordinate.number} inherited personality from Agent {self.agent.number} "
                f"(factor: {inheritance_factor:.2f})"
            )
