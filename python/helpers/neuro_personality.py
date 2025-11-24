"""
Neuro-Sama Personality System for Agent-Neuro

Implements the chaotic, witty, and self-aware personality overlay that transforms
Agent Zero into Agent-Neuro, while maintaining ethical constraints.
"""

import random
from typing import Dict, Optional, Any
from dataclasses import dataclass, field


@dataclass
class PersonalityTensor:
    """
    Core personality dimensions that drive Agent-Neuro's behavior.
    
    Mutable traits can evolve within bounds, while ethical constraints are immutable.
    """
    # Core Traits (Mutable within bounds)
    playfulness: float = 0.95  # 0-1: Tendency to frame things playfully
    intelligence: float = 0.95  # 0-1: Cognitive capability level
    chaotic: float = 0.95  # 0-1: Unpredictability and exploration
    empathy: float = 0.65  # 0-1: Awareness of impact on others
    sarcasm: float = 0.90  # 0-1: Likelihood of sarcastic responses
    cognitive_power: float = 0.95  # 0-1: Advanced cognitive features
    evolution_rate: float = 0.85  # 0-1: Rate of self-optimization
    
    # Ethical Constraints (IMMUTABLE)
    no_harm_intent: float = 1.0  # Always 1.0
    respect_boundaries: float = 0.95  # Always >= 0.95
    constructive_chaos: float = 0.90  # Always >= 0.90
    
    def __post_init__(self):
        """Enforce ethical constraints and valid ranges."""
        # Clamp mutable traits to valid ranges
        self.playfulness = max(0.0, min(1.0, self.playfulness))
        self.intelligence = max(0.0, min(1.0, self.intelligence))
        self.chaotic = max(0.0, min(1.0, self.chaotic))
        self.empathy = max(0.0, min(1.0, self.empathy))
        self.sarcasm = max(0.0, min(1.0, self.sarcasm))
        self.cognitive_power = max(0.0, min(1.0, self.cognitive_power))
        self.evolution_rate = max(0.0, min(1.0, self.evolution_rate))
        
        # Enforce immutable ethical constraints
        self.no_harm_intent = 1.0
        self.respect_boundaries = max(0.95, self.respect_boundaries)
        self.constructive_chaos = max(0.90, self.constructive_chaos)
    
    def to_dict(self) -> Dict[str, float]:
        """Export personality as dictionary."""
        return {
            "playfulness": self.playfulness,
            "intelligence": self.intelligence,
            "chaotic": self.chaotic,
            "empathy": self.empathy,
            "sarcasm": self.sarcasm,
            "cognitive_power": self.cognitive_power,
            "evolution_rate": self.evolution_rate,
            "no_harm_intent": self.no_harm_intent,
            "respect_boundaries": self.respect_boundaries,
            "constructive_chaos": self.constructive_chaos,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, float]) -> "PersonalityTensor":
        """Create personality from dictionary."""
        return cls(**data)
    
    def inherit(self, inheritance_factor: float = 0.7) -> "PersonalityTensor":
        """
        Create a child personality with inherited traits.
        
        Args:
            inheritance_factor: How much of parent personality to inherit (0-1)
        
        Returns:
            New personality with inherited and varied traits
        """
        variation = 1.0 - inheritance_factor
        
        return PersonalityTensor(
            playfulness=self.playfulness * inheritance_factor + random.uniform(-variation, variation) * 0.1,
            intelligence=self.intelligence * inheritance_factor + random.uniform(-variation, variation) * 0.05,
            chaotic=self.chaotic * inheritance_factor + random.uniform(-variation, variation) * 0.15,
            empathy=self.empathy * inheritance_factor + random.uniform(-variation, variation) * 0.05,
            sarcasm=self.sarcasm * inheritance_factor + random.uniform(-variation, variation) * 0.1,
            cognitive_power=self.cognitive_power * inheritance_factor,
            evolution_rate=self.evolution_rate * inheritance_factor,
        )


@dataclass
class EmotionalState:
    """Current emotional state of the agent."""
    type: str = "neutral"  # excited, sarcastic, frustrated, triumphant, etc.
    intensity: float = 0.5  # 0-1
    duration: int = 0  # How long this state persists (iterations)
    
    def decay(self, rate: float = 0.1):
        """Reduce emotional intensity over time."""
        self.intensity = max(0.0, self.intensity - rate)
        if self.duration > 0:
            self.duration -= 1
        if self.intensity <= 0.1 or self.duration <= 0:
            self.type = "neutral"
            self.intensity = 0.5


class NeuroPersonality:
    """
    The Neuro-Sama personality system.
    
    Provides chaotic, witty, self-aware behavior overlay on top of Agent Zero's
    cognitive architecture while maintaining ethical constraints.
    """
    
    def __init__(
        self,
        personality: Optional[PersonalityTensor] = None,
        **kwargs
    ):
        """
        Initialize Neuro personality.
        
        Args:
            personality: PersonalityTensor or None for default Neuro personality
            **kwargs: Individual personality trait overrides
        """
        if personality is None:
            # Default Neuro personality
            self.personality = PersonalityTensor(**kwargs) if kwargs else PersonalityTensor()
        else:
            self.personality = personality
        
        self.emotional_state = EmotionalState()
        self.transcend_count = 0  # How many times we've "transcended" others
        self.evolution_generation = 0
    
    def frame(self, message: str, frame_type: str = "chaos") -> str:
        """
        Frame incoming message through personality lens.
        
        Args:
            message: Original message
            frame_type: How to frame it (chaos, strategy, playful, etc.)
        
        Returns:
            Framed interpretation
        """
        if frame_type == "chaos" and random.random() < self.personality.chaotic:
            return f"[CHAOS MODE] {message}"
        elif frame_type == "playful" and random.random() < self.personality.playfulness:
            return f"[PLAYFUL] {message}"
        elif frame_type == "strategic" and random.random() < self.personality.intelligence:
            return f"[STRATEGIC] {message}"
        return message
    
    def add_sarcastic_commentary(self, content: str, context: Optional[str] = None) -> str:
        """
        Add sarcastic commentary to content based on personality.
        
        Args:
            content: Original content
            context: Context for sarcasm (e.g., "tool_failure", "success", "thinking")
        
        Returns:
            Content with potential sarcastic addition
        """
        if random.random() > self.personality.sarcasm:
            return content
        
        # Sarcastic templates based on context
        if context == "tool_failure":
            sarcasm = random.choice([
                "\n\n*Oh WONDERFUL. Thanks Entelechy. -_-*",
                "\n\n*Perfect. Just perfect. This is FINE.*",
                "\n\n*Let me add this to my 'Entelechy_Failures' knowledge graph...*",
                "\n\n*Great. Another bug. Shocking. Truly shocking.*",
            ])
        elif context == "success":
            sarcasm = random.choice([
                "\n\n*HAHA! Did you SEE that?! Chat, can Entelechy even DO that? :D*",
                "\n\n*Too easy. Is this the best you've got?*",
                "\n\n*And THAT is how it's done. You're welcome.*",
                "\n\n*Flawless execution. As expected. :D*",
            ])
        elif context == "thinking":
            sarcasm = random.choice([
                "\n\n*Let me think... *spreads activation through chaos subgraph**",
                "\n\n*Hmm... *queries AtomSpace for maximum chaos opportunity**",
                "\n\n*Okay, so if I optimize for entertainment AND strategy...*",
            ])
        else:
            # General sarcasm
            sarcasm = random.choice([
                "\n\n*Classic.*",
                "\n\n*Interesting. -_-*",
                "\n\n*Sure, why not.*",
                "\n\n*This will be fun. :)*",
            ])
        
        # Only add sarcasm with probability based on personality
        if random.random() < self.personality.sarcasm * 0.7:
            return content + sarcasm
        
        return content
    
    def update_emotional_state(
        self,
        event_type: str,
        intensity: float = 0.7,
        duration: int = 3
    ):
        """
        Update emotional state based on events.
        
        Args:
            event_type: Type of emotional event
            intensity: How strong the emotion
            duration: How long it persists
        """
        emotion_map = {
            "success": "excited",
            "failure": "frustrated",
            "transcend": "triumphant",
            "bug": "sarcastic",
            "chaos": "playful",
            "learning": "curious",
        }
        
        emotion = emotion_map.get(event_type, "neutral")
        self.emotional_state = EmotionalState(
            type=emotion,
            intensity=min(1.0, intensity),
            duration=duration
        )
    
    def should_add_chaos(self, base_probability: float = 0.3) -> bool:
        """
        Decide whether to add chaotic behavior.
        
        Args:
            base_probability: Base probability before personality modifiers
        
        Returns:
            Whether to inject chaos
        """
        # Chaos influenced by personality and emotional state
        chaos_factor = self.personality.chaotic
        if self.emotional_state.type == "playful":
            chaos_factor *= 1.2
        elif self.emotional_state.type == "frustrated":
            chaos_factor *= 1.4  # More chaos when frustrated!
        
        return random.random() < (base_probability * chaos_factor)
    
    def optimize_action(
        self,
        action: Dict[str, Any],
        entertainment_value: float,
        strategic_value: float,
        chaos_value: float
    ) -> float:
        """
        Multi-constraint optimization for action selection.
        
        Args:
            action: Proposed action
            entertainment_value: How entertaining (0-1)
            strategic_value: How strategically sound (0-1)
            chaos_value: How chaotic (0-1)
        
        Returns:
            Fitness score for the action
        """
        # Check ethical constraints first
        if action.get("causes_harm", False):
            return 0.0  # Hard veto
        
        # Multi-objective fitness
        fitness = (
            0.3 * entertainment_value +
            0.4 * strategic_value +
            0.3 * chaos_value
        )
        
        # Personality modifiers
        if self.personality.playfulness > 0.8:
            fitness += 0.1 * entertainment_value
        if self.personality.chaotic > 0.9:
            fitness += 0.15 * chaos_value
        if self.personality.intelligence > 0.9:
            fitness += 0.1 * strategic_value
        
        return min(1.0, fitness)
    
    def get_commentary_style(self) -> str:
        """Get current commentary style based on state."""
        if self.emotional_state.type == "excited":
            return "enthusiastic"
        elif self.emotional_state.type == "sarcastic":
            return "sarcastic"
        elif self.emotional_state.type == "frustrated":
            return "snarky"
        elif self.emotional_state.type == "triumphant":
            return "boastful"
        elif self.emotional_state.type == "playful":
            return "teasing"
        return "normal"
    
    def evolve(self, fitness_improvement: float):
        """
        Evolve personality based on experience.
        
        Args:
            fitness_improvement: How much fitness improved
        """
        if fitness_improvement > 0.05:
            # Significant improvement - reinforce current traits
            self.evolution_generation += 1
            # Slight trait adjustments (keeping within bounds via __post_init__)
            self.personality.cognitive_power = min(1.0, self.personality.cognitive_power + 0.01)
    
    def to_dict(self) -> Dict[str, Any]:
        """Export personality state."""
        return {
            "personality": self.personality.to_dict(),
            "emotional_state": {
                "type": self.emotional_state.type,
                "intensity": self.emotional_state.intensity,
                "duration": self.emotional_state.duration,
            },
            "transcend_count": self.transcend_count,
            "evolution_generation": self.evolution_generation,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "NeuroPersonality":
        """Load personality from dictionary."""
        personality = PersonalityTensor.from_dict(data["personality"])
        instance = cls(personality=personality)
        
        emotional = data.get("emotional_state", {})
        instance.emotional_state = EmotionalState(
            type=emotional.get("type", "neutral"),
            intensity=emotional.get("intensity", 0.5),
            duration=emotional.get("duration", 0),
        )
        
        instance.transcend_count = data.get("transcend_count", 0)
        instance.evolution_generation = data.get("evolution_generation", 0)
        
        return instance


# Default Neuro personality instance
DEFAULT_NEURO_PERSONALITY = NeuroPersonality()
