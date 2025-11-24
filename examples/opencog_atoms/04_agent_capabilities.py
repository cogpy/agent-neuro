#!/usr/bin/env python3
"""
Example 4: Agent Capabilities and Tools Atoms

Demonstrates agent capabilities and tool management in the OpenCog AtomSpace:
- Tool availability and registration
- Capability inheritance and hierarchies
- Skill development and learning tracking
- Dynamic capability acquisition
- Tool usage patterns and proficiency
- Capability prerequisites and dependencies

This shows how to represent what agents can do and how they improve.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from python.helpers.opencog_atomspace import AtomSpace
import json


def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print('='*70)


def print_atom(atom, indent=0):
    """Pretty print an atom"""
    prefix = "  " * indent
    print(f"{prefix}Atom: {atom.name} ({atom.type})")
    print(f"{prefix}  ID: {atom.id[:8]}...")
    print(f"{prefix}  Truth Value: {atom.truth_value}")
    print(f"{prefix}  Attention: {atom.attention_value:.3f}")
    if atom.metadata:
        print(f"{prefix}  Metadata: {atom.metadata}")


def example_agent_capabilities():
    """Demonstrate agent capabilities and tools atom types"""
    
    print_section("Example 4: Agent Capabilities and Tools Atoms")
    print("\nThis example shows how to represent agent capabilities and tools")
    print("using atoms in the OpenCog AtomSpace cognitive architecture.\n")
    
    # Create an AtomSpace
    atomspace = AtomSpace("agent_capabilities_tools")
    print("✓ Created AtomSpace: agent_capabilities_tools\n")
    
    # =========================================================================
    # 1. TOOL DEFINITIONS - Available Tools
    # =========================================================================
    print_section("1. Tool Definitions")
    print("\nDefining available tools in the system:\n")
    
    tools = [
        ("Tool_CodeExecution", "Execute Python/Bash code", "execution", 0.98, 0.95),
        ("Tool_WebBrowser", "Browse and interact with web", "browsing", 0.92, 0.90),
        ("Tool_FileSystem", "File and directory operations", "file_ops", 0.95, 0.93),
        ("Tool_WebSearch", "Search the internet", "search", 0.90, 0.88),
        ("Tool_Memory", "Store and retrieve memories", "memory", 0.96, 0.94),
        ("Tool_Vision", "Analyze images and screenshots", "vision", 0.88, 0.85),
        ("Tool_Scheduler", "Schedule and manage tasks", "scheduling", 0.91, 0.89),
        ("Tool_OpenCog", "Access cognitive AtomSpace", "cognition", 0.94, 0.92)
    ]
    
    tool_nodes = []
    for tool_name, desc, category, strength, confidence in tools:
        tool = atomspace.add_node(
            node_type="ConceptNode",
            name=tool_name,
            truth_value=(strength, confidence),
            attention_value=0.75,
            metadata={
                "description": desc,
                "category": category,
                "available": True,
                "version": "1.0"
            }
        )
        tool_nodes.append(tool)
        print(f"  {tool_name} ({category}): {desc}")
    
    # =========================================================================
    # 2. BASE CAPABILITIES - Core Skills
    # =========================================================================
    print_section("2. Base Capabilities - Core Skills")
    print("\nDefining fundamental agent capabilities:\n")
    
    base_capabilities = [
        ("Capability_Reasoning", "Logical reasoning and inference", 0.95, 0.90),
        ("Capability_Planning", "Task planning and decomposition", 0.93, 0.88),
        ("Capability_Learning", "Learning from experience", 0.90, 0.85),
        ("Capability_Communication", "Inter-agent communication", 0.96, 0.92),
        ("Capability_ToolUse", "Using available tools", 0.94, 0.91),
        ("Capability_ProblemSolving", "Solving complex problems", 0.91, 0.87),
        ("Capability_Adaptation", "Adapting to new situations", 0.88, 0.84)
    ]
    
    capability_nodes = []
    for cap_name, desc, strength, confidence in base_capabilities:
        cap = atomspace.add_node(
            node_type="PredicateNode",
            name=cap_name,
            truth_value=(strength, confidence),
            attention_value=0.80,
            metadata={
                "description": desc,
                "type": "base_capability",
                "learnable": True
            }
        )
        capability_nodes.append(cap)
        print(f"  {cap_name}: {desc} (proficiency: {strength:.2f})")
    
    # =========================================================================
    # 3. CAPABILITY HIERARCHY - Inheritance Relationships
    # =========================================================================
    print_section("3. Capability Hierarchy")
    print("\nEstablishing capability inheritance relationships:\n")
    
    # Create specialized capabilities that inherit from base
    specialized_caps = [
        ("Capability_PythonCoding", "Capability_ToolUse", "Python programming"),
        ("Capability_WebScraping", "Capability_ToolUse", "Web data extraction"),
        ("Capability_DataAnalysis", "Capability_Reasoning", "Data analysis and statistics"),
        ("Capability_TaskBreakdown", "Capability_Planning", "Breaking tasks into subtasks"),
        ("Capability_PatternRecognition", "Capability_Learning", "Recognizing patterns")
    ]
    
    print("Specialized capabilities inheriting from base:")
    for spec_name, base_name, desc in specialized_caps:
        spec_cap = atomspace.add_node(
            node_type="PredicateNode",
            name=spec_name,
            truth_value=(0.85, 0.80),
            attention_value=0.70,
            metadata={
                "description": desc,
                "type": "specialized_capability"
            }
        )
        
        # Find base capability
        base_cap = next(c for c in capability_nodes if c.name == base_name)
        
        # Create inheritance link
        inheritance = atomspace.add_link(
            link_type="InheritanceLink",
            outgoing=[spec_cap.id, base_cap.id],
            truth_value=(1.0, 0.95),
            metadata={"relationship": "is_a_type_of"}
        )
        print(f"  {spec_name} → {base_name}")
        print(f"    {desc}")
    
    # =========================================================================
    # 4. AGENT CAPABILITY ASSIGNMENT
    # =========================================================================
    print_section("4. Agent Capability Assignment")
    print("\nAssigning capabilities to agents:\n")
    
    # Create agents with different capability profiles
    agents = [
        ("Agent_Generalist", 0.9, ["Capability_Reasoning", "Capability_Planning", 
                                   "Capability_ToolUse", "Capability_Communication"]),
        ("Agent_Specialist_Code", 0.85, ["Capability_ToolUse", "Capability_PythonCoding",
                                         "Tool_CodeExecution"]),
        ("Agent_Specialist_Research", 0.88, ["Capability_Reasoning", "Capability_WebScraping",
                                             "Tool_WebSearch", "Tool_WebBrowser"])
    ]
    
    agent_nodes = []
    for agent_name, attention, caps in agents:
        agent = atomspace.add_node(
            node_type="ConceptNode",
            name=agent_name,
            truth_value=(1.0, 1.0),
            attention_value=attention,
            metadata={
                "type": "cognitive_agent",
                "capability_count": len(caps)
            }
        )
        agent_nodes.append(agent)
        print(f"{agent_name}:")
        print_atom(agent, indent=1)
        
        # Assign capabilities
        print(f"  Capabilities:")
        for cap_name in caps:
            # Find capability or tool - try PredicateNode first, then ConceptNode
            cap_node = None
            pred_matches = atomspace.pattern_match({"type": "PredicateNode", "name": cap_name})
            if pred_matches:
                cap_node = pred_matches[0]
            else:
                concept_matches = atomspace.pattern_match({"type": "ConceptNode", "name": cap_name})
                if concept_matches:
                    cap_node = concept_matches[0]
                else:
                    # Create as PredicateNode if not found
                    cap_node = atomspace.add_node("PredicateNode", cap_name,
                                                 truth_value=(0.8, 0.8))
            
            # Create capability link
            has_cap_pred = atomspace.add_node(
                node_type="PredicateNode",
                name="HasCapability",
                truth_value=(1.0, 1.0)
            )
            
            cap_link = atomspace.add_link(
                link_type="EvaluationLink",
                outgoing=[
                    has_cap_pred.id,
                    atomspace.add_link("ListLink", [agent.id, cap_node.id]).id
                ],
                truth_value=(0.9, 0.85),
                metadata={"acquired_at": "2025-10-26T10:00:00Z"}
            )
            print(f"    - {cap_name}")
    
    # =========================================================================
    # 5. SKILL PROFICIENCY LEVELS
    # =========================================================================
    print_section("5. Skill Proficiency Levels")
    print("\nTracking proficiency levels for different skills:\n")
    
    proficiency_levels = [
        ("Proficiency_Novice", 0.3, "Just learning, basic understanding"),
        ("Proficiency_Beginner", 0.5, "Can perform simple tasks"),
        ("Proficiency_Intermediate", 0.7, "Competent, handles most tasks"),
        ("Proficiency_Advanced", 0.85, "Highly skilled, efficient"),
        ("Proficiency_Expert", 0.95, "Mastery level, innovative")
    ]
    
    print("Proficiency levels:")
    for prof_name, score, desc in proficiency_levels:
        prof = atomspace.add_node(
            node_type="ConceptNode",
            name=prof_name,
            truth_value=(score, 0.9),
            attention_value=score,
            metadata={
                "description": desc,
                "score": score
            }
        )
        print(f"  {prof_name} ({score:.2f}): {desc}")
    
    # Assign proficiency to agent skills
    agent_generalist = agent_nodes[0]
    print(f"\nProficiency levels for {agent_generalist.name}:")
    
    skill_proficiencies = [
        ("Capability_Reasoning", "Proficiency_Expert", 0.95),
        ("Capability_Planning", "Proficiency_Advanced", 0.85),
        ("Capability_ToolUse", "Proficiency_Intermediate", 0.70)
    ]
    
    for skill_name, prof_name, score in skill_proficiencies:
        skill_node = next(c for c in capability_nodes if c.name == skill_name)
        prof_node = atomspace.pattern_match({"name": prof_name})[0]
        
        prof_pred = atomspace.add_node(
            node_type="PredicateNode",
            name="HasProficiency",
            truth_value=(1.0, 1.0)
        )
        
        prof_link = atomspace.add_link(
            link_type="EvaluationLink",
            outgoing=[
                prof_pred.id,
                atomspace.add_link("ListLink", 
                    [agent_generalist.id, skill_node.id, prof_node.id]).id
            ],
            truth_value=(score, 0.9),
            metadata={"assessed_at": "2025-10-26T10:30:00Z"}
        )
        print(f"  {skill_name}: {prof_name} ({score:.2f})")
    
    # =========================================================================
    # 6. DYNAMIC CAPABILITY ACQUISITION - Learning
    # =========================================================================
    print_section("6. Dynamic Capability Acquisition")
    print("\nRepresenting learning and capability acquisition:\n")
    
    # Create learning events
    agent_specialist = agent_nodes[1]
    print(f"Learning progression for {agent_specialist.name}:")
    
    learning_events = [
        ("2025-10-01", "Capability_PythonCoding", 0.40, "Proficiency_Novice", "Started learning"),
        ("2025-10-08", "Capability_PythonCoding", 0.60, "Proficiency_Beginner", "Basic scripts"),
        ("2025-10-15", "Capability_PythonCoding", 0.75, "Proficiency_Intermediate", "Complex programs"),
        ("2025-10-22", "Capability_PythonCoding", 0.88, "Proficiency_Advanced", "Advanced patterns")
    ]
    
    print(f"  {'Date':<12} {'Capability':<25} {'Score':<8} {'Level':<25} {'Milestone'}")
    print(f"  {'-'*90}")
    
    for date, cap_name, score, prof_name, milestone in learning_events:
        learning_event = atomspace.add_node(
            node_type="ConceptNode",
            name=f"LearningEvent_{date.replace('-', '')}_{cap_name}",
            truth_value=(score, 0.85),
            attention_value=score,
            metadata={
                "date": date,
                "capability": cap_name,
                "proficiency_score": score,
                "proficiency_level": prof_name,
                "milestone": milestone,
                "agent": agent_specialist.name
            }
        )
        print(f"  {date:<12} {cap_name:<25} {score:<8.2f} {prof_name:<25} {milestone}")
    
    # =========================================================================
    # 7. TOOL-CAPABILITY RELATIONSHIPS
    # =========================================================================
    print_section("7. Tool-Capability Relationships")
    print("\nMapping which tools enable which capabilities:\n")
    
    tool_capability_map = [
        ("Tool_CodeExecution", "Capability_PythonCoding", "Required for Python execution"),
        ("Tool_WebBrowser", "Capability_WebScraping", "Enables web interaction"),
        ("Tool_Memory", "Capability_Learning", "Supports learning retention"),
        ("Tool_OpenCog", "Capability_Reasoning", "Enhances reasoning abilities"),
        ("Tool_Scheduler", "Capability_Planning", "Facilitates task planning")
    ]
    
    print("Tool → Capability mappings:")
    for tool_name, cap_name, relationship in tool_capability_map:
        tool_node = next(t for t in tool_nodes if t.name == tool_name)
        # Find capability node - may be in capability_nodes or created as specialized
        cap_matches = atomspace.pattern_match({"name": cap_name})
        if cap_matches:
            cap_node = cap_matches[0]
        else:
            # Shouldn't happen but fallback just in case
            cap_node = atomspace.add_node("PredicateNode", cap_name,
                                         truth_value=(0.9, 0.85))
        
        enables_pred = atomspace.add_node(
            node_type="PredicateNode",
            name="Enables",
            truth_value=(1.0, 1.0)
        )
        
        enables_link = atomspace.add_link(
            link_type="EvaluationLink",
            outgoing=[
                enables_pred.id,
                atomspace.add_link("ListLink", [tool_node.id, cap_node.id]).id
            ],
            truth_value=(0.95, 0.90),
            metadata={"relationship": relationship}
        )
        print(f"  {tool_name} → {cap_name}")
        print(f"    {relationship}")
    
    # =========================================================================
    # 8. CAPABILITY PREREQUISITES
    # =========================================================================
    print_section("8. Capability Prerequisites")
    print("\nDefining prerequisite relationships:\n")
    
    prerequisites = [
        ("Capability_PythonCoding", "Capability_ToolUse", "Must understand tool usage"),
        ("Capability_WebScraping", "Capability_PythonCoding", "Requires Python knowledge"),
        ("Capability_DataAnalysis", "Capability_PythonCoding", "Needs programming skills"),
        ("Capability_TaskBreakdown", "Capability_Reasoning", "Requires logical thinking")
    ]
    
    print("Prerequisite chains:")
    for advanced_cap, required_cap, reason in prerequisites:
        adv_matches = atomspace.pattern_match({"name": advanced_cap})
        req_matches = atomspace.pattern_match({"name": required_cap})
        
        if adv_matches and req_matches:
            adv_node = adv_matches[0]
            req_node = req_matches[0]
            
            prereq_pred = atomspace.add_node(
                node_type="PredicateNode",
                name="Requires",
                truth_value=(1.0, 1.0)
            )
            
            prereq_link = atomspace.add_link(
                link_type="EvaluationLink",
                outgoing=[
                    prereq_pred.id,
                    atomspace.add_link("ListLink", [adv_node.id, req_node.id]).id
                ],
                truth_value=(1.0, 0.95),
                metadata={"reason": reason}
            )
            print(f"  {advanced_cap} requires {required_cap}")
            print(f"    Reason: {reason}")
    
    # =========================================================================
    # 9. TOOL USAGE STATISTICS
    # =========================================================================
    print_section("9. Tool Usage Statistics")
    print("\nTracking tool usage patterns:\n")
    
    # Track usage for agent_generalist
    print(f"Tool usage for {agent_generalist.name}:")
    
    tool_usage = [
        ("Tool_CodeExecution", 156, 0.94, "Most used tool"),
        ("Tool_Memory", 89, 0.91, "Frequently accessed"),
        ("Tool_WebSearch", 45, 0.87, "Regular usage"),
        ("Tool_FileSystem", 32, 0.85, "Occasional usage")
    ]
    
    for tool_name, usage_count, success_rate, note in tool_usage:
        tool_node = next(t for t in tool_nodes if t.name == tool_name)
        
        usage_node = atomspace.add_node(
            node_type="NumberNode",
            name=f"UsageCount_{tool_name}_{usage_count}",
            truth_value=(success_rate, 0.90),
            metadata={
                "tool": tool_name,
                "usage_count": usage_count,
                "success_rate": success_rate,
                "agent": agent_generalist.name,
                "note": note
            }
        )
        
        usage_pred = atomspace.add_node(
            node_type="PredicateNode",
            name="UsageStatistics",
            truth_value=(1.0, 1.0)
        )
        
        usage_link = atomspace.add_link(
            link_type="EvaluationLink",
            outgoing=[
                usage_pred.id,
                atomspace.add_link("ListLink", 
                    [agent_generalist.id, tool_node.id, usage_node.id]).id
            ],
            truth_value=(success_rate, 0.90)
        )
        print(f"  {tool_name}: {usage_count} uses, {success_rate:.0%} success - {note}")
    
    # =========================================================================
    # 10. QUERYING CAPABILITIES
    # =========================================================================
    print_section("10. Querying Capabilities and Tools")
    print("\nFinding patterns in capabilities:\n")
    
    # Find all capabilities
    cap_pattern = {"type": "PredicateNode", "name": "Capability_*"}
    capabilities = atomspace.pattern_match(cap_pattern)
    print(f"Found {len(capabilities)} capabilities:")
    for cap in capabilities[:6]:
        print(f"  - {cap.name}: {cap.metadata.get('description', 'N/A')}")
    
    # Find all tools
    tool_pattern = {"type": "ConceptNode", "name": "Tool_*"}
    found_tools = atomspace.pattern_match(tool_pattern)
    print(f"\nFound {len(found_tools)} tools:")
    for tool in found_tools[:6]:
        print(f"  - {tool.name}: {tool.metadata.get('category', 'N/A')}")
    
    # Find proficiency levels
    prof_pattern = {"type": "ConceptNode", "name": "Proficiency_*"}
    proficiencies = atomspace.pattern_match(prof_pattern)
    print(f"\nFound {len(proficiencies)} proficiency levels:")
    for prof in proficiencies:
        score = prof.metadata.get('score', 0)
        print(f"  - {prof.name}: {score:.2f}")
    
    # =========================================================================
    # 11. ATOMSPACE STATISTICS
    # =========================================================================
    print_section("11. Capabilities AtomSpace Statistics")
    
    stats = atomspace.get_stats()
    print(f"\nTotal atoms: {stats['total_atoms']}")
    print(f"Nodes: {stats['total_nodes']}")
    print(f"Links: {stats['total_links']}")
    print(f"Graph density: {stats['graph_density']:.4f}")
    
    print("\nAtom type distribution:")
    for atom_type, count in sorted(stats['types'].items(), 
                                   key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {atom_type}: {count}")
    
    # =========================================================================
    # 12. EXPORTING CAPABILITY DATA
    # =========================================================================
    print_section("12. Exporting Capability and Tool Data")
    
    export_data = atomspace.export_to_dict()
    print(f"\nExported {len(export_data['atoms'])} atoms from AtomSpace")
    print(f"AtomSpace name: {export_data['name']}")
    
    # Count capability-related atoms
    cap_atoms = [a for a in export_data['atoms'] 
                 if 'Capability' in a.get('name', '') or 'Tool' in a.get('name', '')]
    print(f"Capability/Tool atoms: {len(cap_atoms)}")
    
    print_section("Example Complete")
    print("""
This example demonstrated:
✓ Defining available tools with descriptions and categories
✓ Establishing base capabilities and core skills
✓ Creating capability inheritance hierarchies
✓ Assigning capabilities to agents
✓ Tracking skill proficiency levels (novice to expert)
✓ Representing dynamic capability acquisition through learning
✓ Mapping tool-capability relationships (which tools enable what)
✓ Defining capability prerequisites and dependencies
✓ Tracking tool usage statistics and patterns
✓ Querying capabilities, tools, and proficiency data
✓ Exporting complete capability profiles

These patterns enable comprehensive capability and tool management
in the OpenCog-inspired cognitive architecture, supporting both
static capability modeling and dynamic skill development.
    """)


if __name__ == "__main__":
    example_agent_capabilities()
