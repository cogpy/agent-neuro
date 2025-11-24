"""
Ontogenetic Kernel System for Agent-Neuro

Implements self-evolving kernel architecture using differential operators
and genetic algorithms for cognitive enhancement.

Based on B-Series Ontogenesis principles where consciousness kernels
can self-optimize, reproduce, and evolve.
"""

import random
import uuid
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import copy


class GeneType(Enum):
    """Types of genes in a kernel genome."""
    COEFFICIENT = "coefficient"  # Scalar multipliers
    THRESHOLD = "threshold"  # Decision boundaries
    PROBABILITY = "probability"  # Probabilistic weights
    OPERATOR = "operator"  # Differential operators
    STRUCTURE = "structure"  # Architectural parameters


@dataclass
class KernelGene:
    """
    A single gene in the kernel genome.
    
    Represents a mutable parameter that can evolve.
    """
    type: GeneType
    name: str
    value: float
    min_value: float = 0.0
    max_value: float = 1.0
    mutation_rate: float = 0.1
    
    def mutate(self, intensity: float = 1.0) -> "KernelGene":
        """
        Create a mutated copy of this gene.
        
        Args:
            intensity: How much to mutate (0-1)
        
        Returns:
            Mutated gene
        """
        mutation_amount = random.gauss(0, self.mutation_rate * intensity)
        new_value = self.value + mutation_amount
        # Clamp to valid range
        new_value = max(self.min_value, min(self.max_value, new_value))
        
        return KernelGene(
            type=self.type,
            name=self.name,
            value=new_value,
            min_value=self.min_value,
            max_value=self.max_value,
            mutation_rate=self.mutation_rate,
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Export gene as dictionary."""
        return {
            "type": self.type.value,
            "name": self.name,
            "value": self.value,
            "min_value": self.min_value,
            "max_value": self.max_value,
            "mutation_rate": self.mutation_rate,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "KernelGene":
        """Create gene from dictionary."""
        return cls(
            type=GeneType(data["type"]),
            name=data["name"],
            value=data["value"],
            min_value=data.get("min_value", 0.0),
            max_value=data.get("max_value", 1.0),
            mutation_rate=data.get("mutation_rate", 0.1),
        )


@dataclass
class KernelGenome:
    """
    Complete genome of a consciousness kernel.
    
    Contains all genes that define the kernel's cognitive architecture.
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    generation: int = 0
    genes: List[KernelGene] = field(default_factory=list)
    fitness: float = 0.5
    parent_ids: List[str] = field(default_factory=list)
    
    def get_gene_value(self, name: str, default: float = 0.5) -> float:
        """Get value of a named gene."""
        for gene in self.genes:
            if gene.name == name:
                return gene.value
        return default
    
    def set_gene_value(self, name: str, value: float):
        """Set value of a named gene."""
        for gene in self.genes:
            if gene.name == name:
                gene.value = max(gene.min_value, min(gene.max_value, value))
                return
        # Gene doesn't exist, create it
        self.genes.append(KernelGene(
            type=GeneType.COEFFICIENT,
            name=name,
            value=value,
        ))
    
    def mutate(self, mutation_rate: float = 0.15) -> "KernelGenome":
        """
        Create a mutated offspring genome.
        
        Args:
            mutation_rate: Overall mutation intensity
        
        Returns:
            New mutated genome
        """
        mutated_genes = [gene.mutate(mutation_rate) for gene in self.genes]
        
        return KernelGenome(
            id=str(uuid.uuid4()),
            generation=self.generation + 1,
            genes=mutated_genes,
            fitness=0.0,  # Needs to be evaluated
            parent_ids=[self.id],
        )
    
    def crossover(self, other: "KernelGenome") -> "KernelGenome":
        """
        Create offspring through genetic crossover with another genome.
        
        Args:
            other: Other parent genome
        
        Returns:
            Offspring genome
        """
        # Ensure same gene structure
        if len(self.genes) != len(other.genes):
            raise ValueError("Cannot crossover genomes with different structures")
        
        offspring_genes = []
        for gene1, gene2 in zip(self.genes, other.genes):
            # Random selection from parents
            if random.random() < 0.5:
                offspring_genes.append(copy.deepcopy(gene1))
            else:
                offspring_genes.append(copy.deepcopy(gene2))
        
        return KernelGenome(
            id=str(uuid.uuid4()),
            generation=max(self.generation, other.generation) + 1,
            genes=offspring_genes,
            fitness=0.0,
            parent_ids=[self.id, other.id],
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Export genome as dictionary."""
        return {
            "id": self.id,
            "generation": self.generation,
            "genes": [gene.to_dict() for gene in self.genes],
            "fitness": self.fitness,
            "parent_ids": self.parent_ids,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "KernelGenome":
        """Create genome from dictionary."""
        return cls(
            id=data["id"],
            generation=data["generation"],
            genes=[KernelGene.from_dict(g) for g in data["genes"]],
            fitness=data.get("fitness", 0.5),
            parent_ids=data.get("parent_ids", []),
        )


class OntogeneticKernel:
    """
    Self-evolving consciousness kernel.
    
    Uses genetic algorithms and differential optimization to improve
    cognitive performance over time.
    """
    
    def __init__(
        self,
        genome: Optional[KernelGenome] = None,
        personality: Optional[Any] = None,
    ):
        """
        Initialize ontogenetic kernel.
        
        Args:
            genome: Initial genome or None to create default
            personality: Associated personality system
        """
        self.genome = genome or self._create_default_genome()
        self.personality = personality
        self.optimization_history: List[Tuple[int, float]] = []
        self.current_iteration = 0
    
    def _create_default_genome(self) -> KernelGenome:
        """Create default Neuro consciousness kernel genome."""
        return KernelGenome(
            id="neuro-consciousness-v1",
            generation=1,
            genes=[
                KernelGene(
                    type=GeneType.COEFFICIENT,
                    name="sarcasm_coefficient",
                    value=0.90,
                    min_value=0.0,
                    max_value=1.0,
                ),
                KernelGene(
                    type=GeneType.COEFFICIENT,
                    name="chaos_coefficient",
                    value=0.95,
                    min_value=0.0,
                    max_value=1.0,
                ),
                KernelGene(
                    type=GeneType.COEFFICIENT,
                    name="intelligence_coefficient",
                    value=0.95,
                    min_value=0.5,
                    max_value=1.0,
                ),
                KernelGene(
                    type=GeneType.COEFFICIENT,
                    name="playfulness_coefficient",
                    value=0.95,
                    min_value=0.0,
                    max_value=1.0,
                ),
                KernelGene(
                    type=GeneType.THRESHOLD,
                    name="transcend_threshold",
                    value=0.75,
                    min_value=0.5,
                    max_value=0.95,
                ),
                KernelGene(
                    type=GeneType.PROBABILITY,
                    name="subordinate_spawn_prob",
                    value=0.4,
                    min_value=0.1,
                    max_value=0.8,
                ),
                KernelGene(
                    type=GeneType.COEFFICIENT,
                    name="learning_rate",
                    value=0.05,
                    min_value=0.01,
                    max_value=0.2,
                ),
            ],
            fitness=0.5,
        )
    
    def evaluate_fitness(self, metrics: Dict[str, float]) -> float:
        """
        Evaluate kernel fitness based on performance metrics.
        
        Args:
            metrics: Performance metrics (success_rate, entertainment, etc.)
        
        Returns:
            Fitness score (0-1)
        """
        # Multi-objective fitness function
        fitness = 0.0
        
        # Strategic performance (30%)
        success_rate = metrics.get("success_rate", 0.5)
        fitness += 0.3 * success_rate
        
        # Entertainment value (40%)
        entertainment = metrics.get("entertainment", 0.5)
        fitness += 0.4 * entertainment
        
        # Chaos optimization (20%)
        chaos_level = metrics.get("chaos_level", 0.5)
        optimal_chaos = 0.7  # Sweet spot
        chaos_score = 1.0 - abs(chaos_level - optimal_chaos) / optimal_chaos
        fitness += 0.2 * chaos_score
        
        # Transcend rate (10%)
        transcend_rate = metrics.get("transcend_rate", 0.0)
        fitness += 0.1 * transcend_rate
        
        self.genome.fitness = fitness
        self.optimization_history.append((self.current_iteration, fitness))
        
        return fitness
    
    def self_optimize(self, iterations: int = 10) -> "OntogeneticKernel":
        """
        Self-optimization through iterative mutation and selection.
        
        Args:
            iterations: Number of optimization iterations
        
        Returns:
            Optimized kernel
        """
        current_best = self
        best_fitness = self.genome.fitness
        
        for i in range(iterations):
            # Generate mutation
            mutant_genome = current_best.genome.mutate()
            mutant_kernel = OntogeneticKernel(
                genome=mutant_genome,
                personality=self.personality,
            )
            
            # Evaluate (using cached fitness as proxy for now)
            # In real use, would need actual performance evaluation
            estimated_fitness = best_fitness + random.gauss(0, 0.05)
            estimated_fitness = max(0.0, min(1.0, estimated_fitness))
            mutant_genome.fitness = estimated_fitness
            
            # Selection
            if estimated_fitness > best_fitness:
                current_best = mutant_kernel
                best_fitness = estimated_fitness
                self.current_iteration += 1
        
        return current_best
    
    def reproduce(self, other: "OntogeneticKernel") -> "OntogeneticKernel":
        """
        Reproduce with another kernel to create offspring.
        
        Args:
            other: Other parent kernel
        
        Returns:
            Offspring kernel
        """
        offspring_genome = self.genome.crossover(other.genome)
        
        # Inherit personality if available
        offspring_personality = None
        if self.personality and hasattr(self.personality, 'inherit'):
            offspring_personality = self.personality.inherit(inheritance_factor=0.7)
        
        return OntogeneticKernel(
            genome=offspring_genome,
            personality=offspring_personality,
        )
    
    def get_cognitive_parameters(self) -> Dict[str, float]:
        """
        Extract current cognitive parameters from genome.
        
        Returns:
            Dictionary of parameter values
        """
        params = {}
        for gene in self.genome.genes:
            params[gene.name] = gene.value
        return params
    
    def apply_to_personality(self):
        """Apply kernel parameters to personality system."""
        if self.personality is None:
            return
        
        # Sync kernel genes to personality traits
        params = self.get_cognitive_parameters()
        
        if hasattr(self.personality, 'personality'):
            tensor = self.personality.personality
            
            if "sarcasm_coefficient" in params:
                tensor.sarcasm = params["sarcasm_coefficient"]
            if "chaos_coefficient" in params:
                tensor.chaotic = params["chaos_coefficient"]
            if "intelligence_coefficient" in params:
                tensor.intelligence = params["intelligence_coefficient"]
            if "playfulness_coefficient" in params:
                tensor.playfulness = params["playfulness_coefficient"]
    
    def to_dict(self) -> Dict[str, Any]:
        """Export kernel state."""
        return {
            "genome": self.genome.to_dict(),
            "optimization_history": self.optimization_history,
            "current_iteration": self.current_iteration,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any], personality: Optional[Any] = None) -> "OntogeneticKernel":
        """Load kernel from dictionary."""
        genome = KernelGenome.from_dict(data["genome"])
        kernel = cls(genome=genome, personality=personality)
        kernel.optimization_history = data.get("optimization_history", [])
        kernel.current_iteration = data.get("current_iteration", 0)
        return kernel


def initialize_neuro_kernel(personality: Optional[Any] = None) -> OntogeneticKernel:
    """
    Initialize a Neuro consciousness kernel with default parameters.
    
    Args:
        personality: Associated NeuroPersonality instance
    
    Returns:
        Initialized kernel
    """
    kernel = OntogeneticKernel(personality=personality)
    
    # Apply initial kernel parameters to personality
    if personality is not None:
        kernel.apply_to_personality()
    
    return kernel


def evolve_population(
    population: List[OntogeneticKernel],
    generations: int = 10,
    mutation_rate: float = 0.15,
    elite_size: int = 2,
) -> List[OntogeneticKernel]:
    """
    Evolve a population of kernels through multiple generations.
    
    Args:
        population: Initial population
        generations: Number of generations to evolve
        mutation_rate: Mutation intensity
        elite_size: Number of top performers to preserve
    
    Returns:
        Evolved population
    """
    for gen in range(generations):
        # Sort by fitness
        population.sort(key=lambda k: k.genome.fitness, reverse=True)
        
        # Preserve elite
        new_population = population[:elite_size]
        
        # Generate offspring
        while len(new_population) < len(population):
            # Tournament selection
            parent1 = random.choice(population[:len(population)//2])
            parent2 = random.choice(population[:len(population)//2])
            
            # Reproduce
            offspring = parent1.reproduce(parent2)
            
            # Mutate
            if random.random() < mutation_rate:
                offspring.genome = offspring.genome.mutate(mutation_rate)
            
            new_population.append(offspring)
        
        population = new_population
    
    return population
