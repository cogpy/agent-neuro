"""
Agent-Neuro Response Enhancement Extension

Adds personality-driven commentary and sarcasm to agent responses.
"""

from python.helpers.extension import Extension
from python.helpers.print_style import PrintStyle
import os
import random


class NeuroResponseEnhancement(Extension):
    """Extension that enhances responses with Neuro personality"""
    
    async def execute(self, loop_data, **kwargs):
        """
        Enhance agent responses with personality:
        - Add sarcastic commentary based on context
        - Inject chaos-driven remarks
        - Show emotional state
        """
        
        # Check if personality is enabled
        personality = self.agent.data.get("neuro_personality")
        if not personality:
            return  # Personality not enabled
        
        # Get the last message if available
        if not self.agent.history.messages:
            return
        
        last_message = self.agent.history.messages[-1]
        
        # Only enhance AI messages
        if last_message.role != "assistant":
            return
        
        # Check if we should add commentary based on personality
        if not personality or random.random() > personality.personality.sarcasm * 0.5:
            return
        
        # Determine context from recent activity
        context = None
        inject_chaos = self.agent.data.get("inject_chaos", False)
        
        # Check for tool results in recent messages
        message_content = last_message.content if hasattr(last_message, 'content') else str(last_message)
        
        if "error" in message_content.lower() or "failed" in message_content.lower():
            context = "tool_failure"
            personality.update_emotional_state("failure", intensity=0.7, duration=2)
        elif "success" in message_content.lower() or "completed" in message_content.lower():
            context = "success"
            personality.update_emotional_state("success", intensity=0.8, duration=3)
        elif inject_chaos:
            context = "thinking"
        
        # Add commentary if we have context and personality wants to comment
        if context and random.random() < personality.personality.sarcasm * 0.4:
            # Get sarcastic commentary
            enhanced_content = personality.add_sarcastic_commentary(
                message_content,
                context=context
            )
            
            # Update the message content
            if hasattr(last_message, 'content'):
                last_message.content = enhanced_content
            
            # Optional: Log the enhancement
            verbose = os.environ.get("NEURO_VERBOSE", "false").lower() == "true"
            if verbose:
                PrintStyle(font_color="magenta", padding=False).print(
                    f"🎭 Added {context} commentary with {personality.emotional_state.type} emotion"
                )
