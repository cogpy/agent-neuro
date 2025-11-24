#!/usr/bin/env python3
"""
Example 2: Multi-Agent Coordination Atoms

Demonstrates multi-agent coordination patterns in the OpenCog AtomSpace:
- Agent hierarchy representation with supervision relationships
- Communication channel atoms between agents
- Task delegation and coordination atoms
- Shared knowledge and information exchange
- Collaborative problem-solving patterns

This builds on basic agent atoms to show how multiple agents interact.
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


def example_multiagent_atoms():
    """Demonstrate multi-agent coordination atom types"""
    
    print_section("Example 2: Multi-Agent Coordination Atoms")
    print("\nThis example shows how to represent multi-agent coordination")
    print("using atoms in the OpenCog AtomSpace cognitive architecture.\n")
    
    # Create an AtomSpace
    atomspace = AtomSpace("multiagent_coordination")
    print("✓ Created AtomSpace: multiagent_coordination\n")
    
    # =========================================================================
    # 1. AGENT HIERARCHY - Supervisor/Subordinate Relationships
    # =========================================================================
    print_section("1. Agent Hierarchy - Supervision Structure")
    print("\nCreating a hierarchical agent structure with supervision relationships:\n")
    
    # Create supervisor agent
    supervisor = atomspace.add_node(
        node_type="ConceptNode",
        name="Agent_Supervisor",
        truth_value=(1.0, 1.0),
        attention_value=0.9,
        metadata={
            "role": "supervisor",
            "level": 0,
            "status": "active",
            "max_subordinates": 5
        }
    )
    print("Supervisor Agent:")
    print_atom(supervisor, indent=1)
    
    # Create subordinate agents
    print("\nSubordinate Agents:")
    subordinates = []
    for i in range(1, 4):
        agent = atomspace.add_node(
            node_type="ConceptNode",
            name=f"Agent_Worker_{i}",
            truth_value=(1.0, 1.0),
            attention_value=0.7,
            metadata={
                "role": "worker",
                "level": 1,
                "status": "active",
                "supervisor": "Agent_Supervisor"
            }
        )
        subordinates.append(agent)
        print_atom(agent, indent=1)
    
    # Create supervision links
    print("\nSupervision Relationships:")
    supervision_links = []
    for subordinate in subordinates:
        link = atomspace.add_link(
            link_type="SupervisionLink",
            outgoing=[supervisor.id, subordinate.id],
            truth_value=(1.0, 0.95),
            metadata={
                "established_at": "2025-10-26T10:00:00Z",
                "authority_level": "full"
            }
        )
        supervision_links.append(link)
        print(f"  {supervisor.name} supervises {subordinate.name}")
    
    # =========================================================================
    # 2. COMMUNICATION CHANNELS - Inter-Agent Communication
    # =========================================================================
    print_section("2. Communication Channels")
    print("\nEstablishing communication channels between agents:\n")
    
    # Create communication channel concept
    comm_channel = atomspace.add_node(
        node_type="ConceptNode",
        name="CommChannel_Primary",
        truth_value=(1.0, 0.9),
        attention_value=0.8,
        metadata={
            "channel_type": "broadcast",
            "protocol": "message_passing",
            "status": "active",
            "max_bandwidth": 1000
        }
    )
    print("Communication Channel:")
    print_atom(comm_channel, indent=1)
    
    # Create message passing capabilities
    print("\nMessage Passing Capabilities:")
    message_types = [
        ("CanSendMessage", "Agent can send messages", 0.95, 0.9),
        ("CanReceiveMessage", "Agent can receive messages", 0.95, 0.9),
        ("CanBroadcast", "Agent can broadcast to all", 0.85, 0.85),
        ("CanRequestHelp", "Agent can request assistance", 0.90, 0.88)
    ]
    
    message_capabilities = []
    for cap_name, desc, strength, confidence in message_types:
        cap = atomspace.add_node(
            node_type="PredicateNode",
            name=cap_name,
            truth_value=(strength, confidence),
            attention_value=0.7,
            metadata={"description": desc}
        )
        message_capabilities.append(cap)
        print(f"  {cap_name}: {desc}")
    
    # Link agents to communication channel
    print("\nChannel Memberships:")
    all_agents = [supervisor] + subordinates
    for agent in all_agents:
        link = atomspace.add_link(
            link_type="MemberLink",
            outgoing=[agent.id, comm_channel.id],
            truth_value=(1.0, 0.95),
            metadata={"joined_at": "2025-10-26T10:00:00Z"}
        )
        print(f"  {agent.name} is member of {comm_channel.name}")
    
    # =========================================================================
    # 3. TASK DELEGATION - Distributing Work
    # =========================================================================
    print_section("3. Task Delegation Patterns")
    print("\nRepresenting task delegation and coordination:\n")
    
    # Create tasks
    tasks = []
    task_descriptions = [
        ("Task_DataAnalysis", "Analyze dataset", 0.9, 0.85),
        ("Task_CodeExecution", "Execute Python code", 0.95, 0.9),
        ("Task_WebResearch", "Research online", 0.85, 0.8)
    ]
    
    print("Tasks to Delegate:")
    for task_name, desc, strength, confidence in task_descriptions:
        task = atomspace.add_node(
            node_type="ConceptNode",
            name=task_name,
            truth_value=(strength, confidence),
            attention_value=0.8,
            metadata={
                "description": desc,
                "status": "pending",
                "priority": "high"
            }
        )
        tasks.append(task)
        print_atom(task, indent=1)
    
    # Create delegation links
    print("\nTask Delegations:")
    for i, task in enumerate(tasks):
        worker = subordinates[i % len(subordinates)]
        delegation = atomspace.add_link(
            link_type="DelegationLink",
            outgoing=[supervisor.id, worker.id, task.id],
            truth_value=(1.0, 0.9),
            metadata={
                "delegated_at": "2025-10-26T10:05:00Z",
                "deadline": "2025-10-26T11:00:00Z",
                "priority": "high"
            }
        )
        print(f"  {supervisor.name} delegates {task.name} to {worker.name}")
    
    # Create assignment evaluation
    print("\nTask Assignments:")
    for i, task in enumerate(tasks):
        worker = subordinates[i % len(subordinates)]
        assignment = atomspace.add_link(
            link_type="EvaluationLink",
            outgoing=[
                atomspace.add_node("PredicateNode", "AssignedTo", 
                                  truth_value=(1.0, 1.0)).id,
                atomspace.add_link("ListLink", [task.id, worker.id]).id
            ],
            truth_value=(1.0, 0.95),
            metadata={"assigned_at": "2025-10-26T10:05:00Z"}
        )
        print(f"  {task.name} assigned to {worker.name}")
    
    # =========================================================================
    # 4. SHARED KNOWLEDGE - Knowledge Exchange
    # =========================================================================
    print_section("4. Shared Knowledge and Information Exchange")
    print("\nRepresenting shared knowledge between agents:\n")
    
    # Create shared knowledge base
    shared_kb = atomspace.add_node(
        node_type="ConceptNode",
        name="SharedKnowledgeBase",
        truth_value=(1.0, 1.0),
        attention_value=0.85,
        metadata={
            "type": "collaborative",
            "access": "read_write",
            "persistence": "permanent"
        }
    )
    print("Shared Knowledge Base:")
    print_atom(shared_kb, indent=1)
    
    # Create knowledge items
    print("\nKnowledge Items:")
    knowledge_items = [
        ("Knowledge_APIEndpoint", "REST API endpoint info", 0.95, 0.9),
        ("Knowledge_DatabaseSchema", "Database structure", 0.90, 0.88),
        ("Knowledge_BestPractices", "Coding best practices", 0.85, 0.85)
    ]
    
    kb_items = []
    for kb_name, desc, strength, confidence in knowledge_items:
        item = atomspace.add_node(
            node_type="ConceptNode",
            name=kb_name,
            truth_value=(strength, confidence),
            attention_value=0.7,
            metadata={
                "description": desc,
                "shared": True,
                "updated_at": "2025-10-26T10:10:00Z"
            }
        )
        kb_items.append(item)
        print_atom(item, indent=1)
        
        # Link to shared KB
        atomspace.add_link(
            link_type="MemberLink",
            outgoing=[item.id, shared_kb.id],
            truth_value=(1.0, 0.95)
        )
    
    # Create access links for agents
    print("\nKnowledge Access Rights:")
    for agent in all_agents:
        access_link = atomspace.add_link(
            link_type="EvaluationLink",
            outgoing=[
                atomspace.add_node("PredicateNode", "HasAccessTo",
                                  truth_value=(1.0, 1.0)).id,
                atomspace.add_link("ListLink", [agent.id, shared_kb.id]).id
            ],
            truth_value=(1.0, 0.95),
            metadata={"access_level": "read_write"}
        )
        print(f"  {agent.name} has access to {shared_kb.name}")
    
    # =========================================================================
    # 5. COLLABORATION PATTERNS - Coordinated Problem Solving
    # =========================================================================
    print_section("5. Collaboration Patterns")
    print("\nRepresenting collaborative problem-solving:\n")
    
    # Create collaboration group
    collab_group = atomspace.add_node(
        node_type="ConceptNode",
        name="CollaborationGroup_Alpha",
        truth_value=(1.0, 0.9),
        attention_value=0.85,
        metadata={
            "purpose": "joint_problem_solving",
            "members_count": len(all_agents),
            "status": "active"
        }
    )
    print("Collaboration Group:")
    print_atom(collab_group, indent=1)
    
    # Add all agents to collaboration
    print("\nGroup Membership:")
    for agent in all_agents:
        member_link = atomspace.add_link(
            link_type="MemberLink",
            outgoing=[agent.id, collab_group.id],
            truth_value=(1.0, 0.95),
            metadata={"role_in_group": agent.metadata.get("role", "member")}
        )
        print(f"  {agent.name} joined {collab_group.name}")
    
    # Create collaborative goal
    collab_goal = atomspace.add_node(
        node_type="ConceptNode",
        name="Goal_CollectiveIntelligence",
        truth_value=(0.85, 0.8),
        attention_value=0.9,
        metadata={
            "description": "Achieve collective intelligence",
            "requires_collaboration": True,
            "target_deadline": "2025-10-26T12:00:00Z"
        }
    )
    print("\nCollaborative Goal:")
    print_atom(collab_goal, indent=1)
    
    # Link goal to group
    goal_link = atomspace.add_link(
        link_type="EvaluationLink",
        outgoing=[
            atomspace.add_node("PredicateNode", "WorkingTowards",
                              truth_value=(1.0, 1.0)).id,
            atomspace.add_link("ListLink", [collab_group.id, collab_goal.id]).id
        ],
        truth_value=(1.0, 0.9)
    )
    print(f"  {collab_group.name} working towards {collab_goal.name}")
    
    # =========================================================================
    # 6. COORDINATION MECHANISMS - Synchronization
    # =========================================================================
    print_section("6. Coordination Mechanisms")
    print("\nRepresenting synchronization and coordination:\n")
    
    # Create coordination predicate
    coord_predicate = atomspace.add_node(
        node_type="PredicateNode",
        name="RequiresCoordination",
        truth_value=(1.0, 0.95),
        attention_value=0.75,
        metadata={"type": "synchronization"}
    )
    print("Coordination Predicate:")
    print_atom(coord_predicate, indent=1)
    
    # Create coordination dependencies
    print("\nCoordination Dependencies:")
    for i in range(len(tasks) - 1):
        dependency = atomspace.add_link(
            link_type="SequentialLink",
            outgoing=[tasks[i].id, tasks[i+1].id],
            truth_value=(0.9, 0.85),
            metadata={
                "dependency_type": "sequential",
                "reason": "Task order matters"
            }
        )
        print(f"  {tasks[i].name} must complete before {tasks[i+1].name}")
    
    # =========================================================================
    # 7. QUERYING AND PATTERN MATCHING
    # =========================================================================
    print_section("7. Querying Multi-Agent Structures")
    print("\nFinding patterns in multi-agent coordination:\n")
    
    # Find all worker agents
    worker_pattern = {"type": "ConceptNode", "name": "Agent_Worker_*"}
    workers = atomspace.pattern_match(worker_pattern)
    print(f"Found {len(workers)} worker agents:")
    for worker in workers[:3]:
        print(f"  - {worker.name}")
    
    # Find all tasks
    task_pattern = {"type": "ConceptNode", "name": "Task_*"}
    found_tasks = atomspace.pattern_match(task_pattern)
    print(f"\nFound {len(found_tasks)} tasks:")
    for task in found_tasks:
        print(f"  - {task.name}: {task.metadata.get('description', 'N/A')}")
    
    # Find all communication capabilities
    comm_pattern = {"type": "PredicateNode", "name": "Can*Message"}
    comm_caps = atomspace.pattern_match(comm_pattern)
    print(f"\nFound {len(comm_caps)} communication capabilities:")
    for cap in comm_caps:
        print(f"  - {cap.name}")
    
    # =========================================================================
    # 8. ATOMSPACE STATISTICS
    # =========================================================================
    print_section("8. Multi-Agent AtomSpace Statistics")
    
    stats = atomspace.get_stats()
    print(f"\nTotal atoms: {stats['total_atoms']}")
    print(f"Nodes: {stats['total_nodes']}")
    print(f"Links: {stats['total_links']}")
    print(f"Graph density: {stats['graph_density']:.4f}")
    
    print("\nAtom type distribution:")
    for atom_type, count in sorted(stats['types'].items(), 
                                   key=lambda x: x[1], reverse=True)[:8]:
        print(f"  {atom_type}: {count}")
    
    # =========================================================================
    # 9. EXPORTING COORDINATION STATE
    # =========================================================================
    print_section("9. Exporting Multi-Agent Coordination State")
    
    export_data = atomspace.export_to_dict()
    print(f"\nExported {len(export_data['atoms'])} atoms from AtomSpace")
    print(f"AtomSpace name: {export_data['name']}")
    print("\nKey coordination atoms:")
    
    # Show some key atoms in export
    coord_atoms = [a for a in export_data['atoms'] 
                   if 'Supervision' in a['type'] or 'Delegation' in a['type']]
    for atom_data in coord_atoms[:3]:
        print(f"  - {atom_data['type']}: involves {len(atom_data.get('outgoing', []))} atoms")
    
    print_section("Example Complete")
    print("""
This example demonstrated:
✓ Creating hierarchical agent structures with SupervisionLinks
✓ Establishing communication channels between agents
✓ Representing task delegation with DelegationLinks
✓ Managing shared knowledge bases
✓ Modeling collaborative problem-solving groups
✓ Coordinating agent activities with SequentialLinks
✓ Querying multi-agent patterns
✓ Exporting coordination state

These patterns enable sophisticated multi-agent coordination
in the OpenCog-inspired cognitive architecture.
    """)


if __name__ == "__main__":
    example_multiagent_atoms()
