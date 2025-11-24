"""
Agent-Neuro Personality Tool

Allows agents to access and manage their personality state and ontogenetic kernel.
"""

import json
from python.helpers.tool import Tool, Response
from python.helpers.print_style import PrintStyle


class NeuroPersonality(Tool):
    """Tool for interacting with Agent-Neuro personality system"""
    
    async def execute(self, **kwargs) -> Response:
        """
        Execute personality operations
        
        Supported methods:
        - get_state: Get current personality state
        - get_emotional_state: Get current emotional state
        - update_emotion: Update emotional state
        - evolve: Trigger self-optimization of kernel
        - get_fitness: Get current kernel fitness
        - export_state: Export personality and kernel state
        """
        
        method = self.method or "get_state"
        
        # Get personality from agent data
        personality = self.agent.data.get("neuro_personality")
        kernel = self.agent.data.get("ontogenetic_kernel")
        
        if not personality:
            return Response(
                message="Agent-Neuro personality is not enabled. Set ENABLE_NEURO_PERSONALITY=true to enable.",
                break_loop=False
            )
        
        try:
            if method == "get_state":
                result = self._get_state(personality, kernel, **kwargs)
            elif method == "get_emotional_state":
                result = self._get_emotional_state(personality, **kwargs)
            elif method == "update_emotion":
                result = self._update_emotion(personality, **kwargs)
            elif method == "evolve":
                result = self._evolve_kernel(personality, kernel, **kwargs)
            elif method == "get_fitness":
                result = self._get_fitness(kernel, **kwargs)
            elif method == "export_state":
                result = self._export_state(personality, kernel, **kwargs)
            else:
                result = {"error": f"Unknown method: {method}"}
            
            return Response(
                message=self._format_result(result),
                break_loop=False
            )
            
        except Exception as e:
            return Response(
                message=f"Error in personality operation: {str(e)}",
                break_loop=False
            )
    
    def _get_state(self, personality, kernel, **kwargs):
        """Get complete personality state"""
        return {
            "personality": {
                "playfulness": personality.personality.playfulness,
                "chaotic": personality.personality.chaotic,
                "sarcasm": personality.personality.sarcasm,
                "intelligence": personality.personality.intelligence,
                "empathy": personality.personality.empathy,
                "cognitive_power": personality.personality.cognitive_power,
                "evolution_rate": personality.personality.evolution_rate,
            },
            "ethical_constraints": {
                "no_harm_intent": personality.personality.no_harm_intent,
                "respect_boundaries": personality.personality.respect_boundaries,
                "constructive_chaos": personality.personality.constructive_chaos,
            },
            "emotional_state": {
                "type": personality.emotional_state.type,
                "intensity": personality.emotional_state.intensity,
                "duration": personality.emotional_state.duration,
            },
            "kernel": {
                "generation": kernel.genome.generation,
                "fitness": kernel.genome.fitness,
                "gene_count": len(kernel.genome.genes),
            } if kernel else None,
            "stats": {
                "transcend_count": personality.transcend_count,
                "evolution_generation": personality.evolution_generation,
            }
        }
    
    def _get_emotional_state(self, personality, **kwargs):
        """Get current emotional state"""
        return {
            "type": personality.emotional_state.type,
            "intensity": personality.emotional_state.intensity,
            "duration": personality.emotional_state.duration,
            "commentary_style": personality.get_commentary_style(),
        }
    
    def _update_emotion(self, personality, **kwargs):
        """Update emotional state"""
        event_type = kwargs.get("event_type", "neutral")
        intensity = float(kwargs.get("intensity", 0.7))
        duration = int(kwargs.get("duration", 3))
        
        personality.update_emotional_state(event_type, intensity, duration)
        
        return {
            "success": True,
            "new_state": {
                "type": personality.emotional_state.type,
                "intensity": personality.emotional_state.intensity,
                "duration": personality.emotional_state.duration,
            }
        }
    
    def _evolve_kernel(self, personality, kernel, **kwargs):
        """Trigger kernel self-optimization"""
        if not kernel:
            return {"error": "Ontogenetic kernel not available"}
        
        iterations = int(kwargs.get("iterations", 10))
        
        # Perform self-optimization
        old_fitness = kernel.genome.fitness
        optimized = kernel.self_optimize(iterations=iterations)
        
        # Update the kernel in agent data
        self.agent.data["ontogenetic_kernel"] = optimized
        
        # Apply to personality
        optimized.apply_to_personality()
        
        # Update personality evolution tracking
        if optimized.genome.fitness > old_fitness:
            personality.evolve(optimized.genome.fitness - old_fitness)
        
        return {
            "success": True,
            "old_fitness": old_fitness,
            "new_fitness": optimized.genome.fitness,
            "improvement": optimized.genome.fitness - old_fitness,
            "generations_evolved": optimized.genome.generation - kernel.genome.generation,
            "evolution_generation": personality.evolution_generation,
        }
    
    def _get_fitness(self, kernel, **kwargs):
        """Get current kernel fitness"""
        if not kernel:
            return {"error": "Ontogenetic kernel not available"}
        
        return {
            "fitness": kernel.genome.fitness,
            "generation": kernel.genome.generation,
            "genome_id": kernel.genome.id,
            "genes": [
                {"name": gene.name, "value": gene.value}
                for gene in kernel.genome.genes
            ]
        }
    
    def _export_state(self, personality, kernel, **kwargs):
        """Export complete personality and kernel state"""
        export_data = {
            "personality": personality.to_dict(),
            "kernel": kernel.to_dict() if kernel else None,
        }
        
        # Optionally save to file
        save_to_file = kwargs.get("save_to_file", False)
        if save_to_file:
            filename = kwargs.get("filename", f"neuro_state_agent_{self.agent.number}.json")
            import json
            with open(filename, 'w') as f:
                json.dump(export_data, f, indent=2)
            return {
                "success": True,
                "saved_to": filename,
                "data": export_data
            }
        
        return export_data
    
    def _format_result(self, result):
        """Format result as readable string"""
        if isinstance(result, dict) and "error" in result:
            return f"❌ {result['error']}"
        
        return f"🎭 Agent-Neuro Personality Result:\n```json\n{json.dumps(result, indent=2)}\n```"
