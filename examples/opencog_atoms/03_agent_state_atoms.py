#!/usr/bin/env python3
"""
Example 3: Agent State and Lifecycle Atoms

Demonstrates agent state and lifecycle management in the OpenCog AtomSpace:
- Agent lifecycle states (initialized, active, idle, paused, terminated)
- State transitions and history tracking
- Resource usage monitoring and tracking
- Performance metrics and evaluation
- Health status and diagnostics
- Temporal state evolution

This shows how to track agent status and evolution over time.
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


def example_agent_state_atoms():
    """Demonstrate agent state and lifecycle atom types"""
    
    print_section("Example 3: Agent State and Lifecycle Atoms")
    print("\nThis example shows how to represent agent states and lifecycle")
    print("using atoms in the OpenCog AtomSpace cognitive architecture.\n")
    
    # Create an AtomSpace
    atomspace = AtomSpace("agent_state_lifecycle")
    print("✓ Created AtomSpace: agent_state_lifecycle\n")
    
    # =========================================================================
    # 1. LIFECYCLE STATE NODES - Agent States
    # =========================================================================
    print_section("1. Lifecycle State Nodes")
    print("\nDefining possible lifecycle states for agents:\n")
    
    lifecycle_states = [
        ("State_Initialized", "Agent created but not started", 1.0, 1.0),
        ("State_Active", "Agent actively processing tasks", 1.0, 1.0),
        ("State_Idle", "Agent waiting for tasks", 1.0, 1.0),
        ("State_Paused", "Agent temporarily suspended", 1.0, 1.0),
        ("State_Error", "Agent encountered error", 1.0, 1.0),
        ("State_Terminated", "Agent shutdown completed", 1.0, 1.0)
    ]
    
    state_nodes = []
    for state_name, desc, strength, confidence in lifecycle_states:
        state = atomspace.add_node(
            node_type="ConceptNode",
            name=state_name,
            truth_value=(strength, confidence),
            attention_value=0.7,
            metadata={
                "description": desc,
                "category": "lifecycle_state"
            }
        )
        state_nodes.append(state)
        print(f"  {state_name}: {desc}")
    
    # =========================================================================
    # 2. AGENT WITH STATE TRACKING
    # =========================================================================
    print_section("2. Agent with State Tracking")
    print("\nCreating agents with current state tracking:\n")
    
    # Create agents
    agents = []
    agent_configs = [
        ("Agent_Alpha", "State_Active", 0.9),
        ("Agent_Beta", "State_Idle", 0.6),
        ("Agent_Gamma", "State_Paused", 0.3)
    ]
    
    for agent_name, initial_state, attention in agent_configs:
        agent = atomspace.add_node(
            node_type="ConceptNode",
            name=agent_name,
            truth_value=(1.0, 1.0),
            attention_value=attention,
            metadata={
                "type": "cognitive_agent",
                "created_at": "2025-10-26T10:00:00Z",
                "version": "1.0"
            }
        )
        agents.append(agent)
        print_atom(agent, indent=1)
        
        # Create current state link
        current_state_pred = atomspace.add_node(
            node_type="PredicateNode",
            name="CurrentState",
            truth_value=(1.0, 1.0)
        )
        
        state_node = next(s for s in state_nodes if s.name == initial_state)
        state_link = atomspace.add_link(
            link_type="StateLink",
            outgoing=[agent.id, state_node.id],
            truth_value=(1.0, 0.95),
            metadata={
                "timestamp": "2025-10-26T10:00:00Z",
                "reason": "initial_state"
            }
        )
        print(f"    → Current state: {initial_state}")
    
    # =========================================================================
    # 3. STATE TRANSITIONS - Lifecycle Evolution
    # =========================================================================
    print_section("3. State Transitions")
    print("\nRepresenting state transitions for Agent_Alpha:\n")
    
    agent_alpha = agents[0]
    
    # Define transition sequence
    transitions = [
        ("State_Initialized", "State_Active", "Agent startup completed"),
        ("State_Active", "State_Idle", "No tasks in queue"),
        ("State_Idle", "State_Active", "New task received"),
        ("State_Active", "State_Paused", "Manual pause requested"),
        ("State_Paused", "State_Active", "Resume requested")
    ]
    
    print(f"Transition history for {agent_alpha.name}:")
    for from_state, to_state, reason in transitions:
        from_node = next(s for s in state_nodes if s.name == from_state)
        to_node = next(s for s in state_nodes if s.name == to_state)
        
        transition = atomspace.add_link(
            link_type="TransitionLink",
            outgoing=[from_node.id, to_node.id],
            truth_value=(0.95, 0.9),
            metadata={
                "agent": agent_alpha.name,
                "reason": reason,
                "timestamp": "2025-10-26T10:15:00Z"
            }
        )
        print(f"  {from_state} → {to_state}")
        print(f"    Reason: {reason}")
    
    # =========================================================================
    # 4. RESOURCE USAGE TRACKING
    # =========================================================================
    print_section("4. Resource Usage Tracking")
    print("\nTracking resource consumption for agents:\n")
    
    # Create resource metric nodes
    resource_metrics = [
        ("CPU_Usage", "Percentage of CPU used", "percent"),
        ("Memory_Usage", "Memory consumption", "megabytes"),
        ("Token_Count", "Tokens processed", "count"),
        ("API_Calls", "API calls made", "count"),
        ("Execution_Time", "Total execution time", "seconds")
    ]
    
    print("Resource Metrics:")
    for metric_name, desc, unit in resource_metrics:
        metric = atomspace.add_node(
            node_type="PredicateNode",
            name=metric_name,
            truth_value=(1.0, 1.0),
            attention_value=0.6,
            metadata={
                "description": desc,
                "unit": unit,
                "category": "resource_metric"
            }
        )
        print(f"  {metric_name} ({unit}): {desc}")
    
    # Track resource values for each agent
    print(f"\nResource usage for {agent_alpha.name}:")
    resource_values = [
        ("CPU_Usage", 45.5),
        ("Memory_Usage", 512.0),
        ("Token_Count", 15000),
        ("API_Calls", 127),
        ("Execution_Time", 3600.5)
    ]
    
    for metric_name, value in resource_values:
        value_node = atomspace.add_node(
            node_type="NumberNode",
            name=f"{metric_name}_Value_{value}",
            truth_value=(1.0, 0.95),
            metadata={
                "value": value,
                "agent": agent_alpha.name,
                "measured_at": "2025-10-26T10:30:00Z"
            }
        )
        
        metric_pred = atomspace.add_node(
            node_type="PredicateNode",
            name=metric_name,
            truth_value=(1.0, 1.0)
        )
        
        usage_link = atomspace.add_link(
            link_type="EvaluationLink",
            outgoing=[
                metric_pred.id,
                atomspace.add_link("ListLink", [agent_alpha.id, value_node.id]).id
            ],
            truth_value=(1.0, 0.95),
            metadata={"timestamp": "2025-10-26T10:30:00Z"}
        )
        print(f"  {metric_name}: {value}")
    
    # =========================================================================
    # 5. PERFORMANCE METRICS
    # =========================================================================
    print_section("5. Performance Metrics")
    print("\nTracking performance indicators:\n")
    
    performance_metrics = [
        ("TaskCompletionRate", 0.92, "Percentage of tasks completed successfully"),
        ("AverageResponseTime", 2.5, "Average time to respond (seconds)"),
        ("ErrorRate", 0.05, "Percentage of tasks with errors"),
        ("EfficiencyScore", 0.88, "Overall efficiency rating"),
        ("QualityScore", 0.91, "Output quality rating")
    ]
    
    print(f"Performance metrics for {agent_alpha.name}:")
    for metric_name, value, desc in performance_metrics:
        perf_metric = atomspace.add_node(
            node_type="PredicateNode",
            name=metric_name,
            truth_value=(1.0, 1.0),
            metadata={
                "description": desc,
                "category": "performance_metric"
            }
        )
        
        value_node = atomspace.add_node(
            node_type="NumberNode",
            name=f"{metric_name}_{value}",
            truth_value=(1.0, 0.9),
            metadata={
                "value": value,
                "agent": agent_alpha.name,
                "computed_at": "2025-10-26T10:30:00Z"
            }
        )
        
        perf_link = atomspace.add_link(
            link_type="EvaluationLink",
            outgoing=[
                perf_metric.id,
                atomspace.add_link("ListLink", [agent_alpha.id, value_node.id]).id
            ],
            truth_value=(1.0, 0.9)
        )
        print(f"  {metric_name}: {value} - {desc}")
    
    # =========================================================================
    # 6. HEALTH STATUS AND DIAGNOSTICS
    # =========================================================================
    print_section("6. Health Status and Diagnostics")
    print("\nMonitoring agent health and diagnostics:\n")
    
    # Create health status nodes
    health_statuses = [
        ("Health_Excellent", "All systems optimal", 1.0),
        ("Health_Good", "Minor issues detected", 0.9),
        ("Health_Warning", "Attention needed", 0.7),
        ("Health_Critical", "Immediate action required", 0.4),
        ("Health_Failed", "System failure", 0.1)
    ]
    
    print("Health Status Levels:")
    for status_name, desc, strength in health_statuses:
        health = atomspace.add_node(
            node_type="ConceptNode",
            name=status_name,
            truth_value=(strength, 0.95),
            attention_value=strength,
            metadata={
                "description": desc,
                "severity_level": strength
            }
        )
        print(f"  {status_name}: {desc} (severity: {strength})")
    
    # Assign health to agents
    print(f"\nHealth status assignments:")
    agent_health = [
        (agents[0], "Health_Excellent"),
        (agents[1], "Health_Good"),
        (agents[2], "Health_Warning")
    ]
    
    for agent, health_name in agent_health:
        health_node = next(h for h in atomspace.pattern_match(
            {"type": "ConceptNode", "name": health_name}))
        
        health_link = atomspace.add_link(
            link_type="EvaluationLink",
            outgoing=[
                atomspace.add_node("PredicateNode", "HasHealthStatus",
                                  truth_value=(1.0, 1.0)).id,
                atomspace.add_link("ListLink", [agent.id, health_node.id]).id
            ],
            truth_value=(1.0, 0.95)
        )
        print(f"  {agent.name}: {health_name}")
    
    # Create diagnostic findings
    print(f"\nDiagnostic findings for {agents[2].name}:")
    diagnostic_issues = [
        "High memory usage detected",
        "Response time degradation",
        "Connection timeout warnings"
    ]
    
    for issue in diagnostic_issues:
        diagnostic = atomspace.add_node(
            node_type="ConceptNode",
            name=f"Issue_{issue.replace(' ', '_')}",
            truth_value=(0.8, 0.85),
            metadata={
                "description": issue,
                "severity": "warning",
                "agent": agents[2].name,
                "detected_at": "2025-10-26T10:35:00Z"
            }
        )
        print(f"  ⚠ {issue}")
    
    # =========================================================================
    # 7. TEMPORAL STATE EVOLUTION
    # =========================================================================
    print_section("7. Temporal State Evolution")
    print("\nTracking state changes over time:\n")
    
    # Create time snapshots
    time_snapshots = [
        ("10:00:00", "State_Initialized", 0.0, 0.0, "System startup"),
        ("10:05:00", "State_Active", 15.5, 128.0, "First task started"),
        ("10:15:00", "State_Active", 45.2, 256.0, "Processing tasks"),
        ("10:30:00", "State_Active", 55.8, 512.0, "Peak load"),
        ("10:45:00", "State_Idle", 12.3, 256.0, "Tasks completed")
    ]
    
    print(f"Temporal evolution for {agent_alpha.name}:")
    print(f"  {'Time':<10} {'State':<20} {'CPU%':<8} {'Mem(MB)':<10} {'Event'}")
    print(f"  {'-'*70}")
    
    for timestamp, state_name, cpu, mem, event in time_snapshots:
        snapshot = atomspace.add_node(
            node_type="ConceptNode",
            name=f"Snapshot_{agent_alpha.name}_{timestamp.replace(':', '')}",
            truth_value=(1.0, 0.95),
            metadata={
                "agent": agent_alpha.name,
                "timestamp": f"2025-10-26T{timestamp}Z",
                "state": state_name,
                "cpu_usage": cpu,
                "memory_usage": mem,
                "event": event
            }
        )
        print(f"  {timestamp:<10} {state_name:<20} {cpu:<8.1f} {mem:<10.1f} {event}")
    
    # =========================================================================
    # 8. STATE PREDICATES - Current Conditions
    # =========================================================================
    print_section("8. State Predicates - Agent Conditions")
    print("\nRepresenting current agent conditions:\n")
    
    conditions = [
        ("IsProcessing", agent_alpha, True, "Agent is processing tasks"),
        ("IsIdle", agent_alpha, False, "Agent is idle"),
        ("HasErrors", agent_alpha, False, "Agent has errors"),
        ("NeedsAttention", agents[2], True, "Agent needs attention"),
        ("IsHealthy", agent_alpha, True, "Agent is healthy"),
        ("IsOverloaded", agent_alpha, False, "Agent is overloaded")
    ]
    
    for pred_name, agent, value, desc in conditions:
        predicate = atomspace.add_node(
            node_type="PredicateNode",
            name=pred_name,
            truth_value=(1.0 if value else 0.0, 0.95),
            metadata={"description": desc}
        )
        
        condition_link = atomspace.add_link(
            link_type="EvaluationLink",
            outgoing=[
                predicate.id,
                atomspace.add_link("ListLink", [agent.id]).id
            ],
            truth_value=(1.0 if value else 0.0, 0.95)
        )
        status = "✓" if value else "✗"
        print(f"  {status} {pred_name}({agent.name}): {desc}")
    
    # =========================================================================
    # 9. QUERYING STATE AND METRICS
    # =========================================================================
    print_section("9. Querying State and Metrics")
    print("\nFinding patterns in agent states:\n")
    
    # Find all state nodes
    state_pattern = {"type": "ConceptNode", "name": "State_*"}
    states = atomspace.pattern_match(state_pattern)
    print(f"Found {len(states)} lifecycle states:")
    for state in states[:6]:
        print(f"  - {state.name}")
    
    # Find all health status nodes
    health_pattern = {"type": "ConceptNode", "name": "Health_*"}
    health_nodes = atomspace.pattern_match(health_pattern)
    print(f"\nFound {len(health_nodes)} health status levels:")
    for health in health_nodes[:5]:
        print(f"  - {health.name}: severity {health.truth_value[0]:.2f}")
    
    # Find all resource metrics
    resource_pattern = {"type": "PredicateNode", "name": "*_Usage"}
    resources = atomspace.pattern_match(resource_pattern)
    print(f"\nFound {len(resources)} resource metrics:")
    for resource in resources[:5]:
        print(f"  - {resource.name}")
    
    # =========================================================================
    # 10. ATOMSPACE STATISTICS
    # =========================================================================
    print_section("10. State Lifecycle AtomSpace Statistics")
    
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
    # 11. EXPORTING STATE DATA
    # =========================================================================
    print_section("11. Exporting State and Lifecycle Data")
    
    export_data = atomspace.export_to_dict()
    print(f"\nExported {len(export_data['atoms'])} atoms from AtomSpace")
    print(f"AtomSpace name: {export_data['name']}")
    
    # Count state-related atoms
    state_atoms = [a for a in export_data['atoms'] 
                   if 'State' in a.get('name', '') or 'Health' in a.get('name', '')]
    print(f"State-related atoms: {len(state_atoms)}")
    
    print_section("Example Complete")
    print("""
This example demonstrated:
✓ Defining lifecycle state nodes (initialized, active, idle, paused, etc.)
✓ Tracking agent current state with StateLinks
✓ Representing state transitions with TransitionLinks
✓ Monitoring resource usage (CPU, memory, tokens, API calls)
✓ Evaluating performance metrics (completion rate, efficiency, quality)
✓ Tracking health status and diagnostics
✓ Recording temporal state evolution
✓ Representing current agent conditions with predicates
✓ Querying state and metrics patterns
✓ Exporting complete state data

These patterns enable comprehensive agent state and lifecycle
management in the OpenCog-inspired cognitive architecture.
    """)


if __name__ == "__main__":
    example_agent_state_atoms()
