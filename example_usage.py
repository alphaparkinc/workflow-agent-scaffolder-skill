"""
example_usage.py -- Demonstrates WorkflowAgentScaffolderClient
"""
from client import WorkflowAgentScaffolderClient

def main():
    client = WorkflowAgentScaffolderClient()
    result = client.deconstruct_workflow(
        "Every Monday we check stock levels and if empty, we order more from the supplier and email shipping labels."
    )
    print("[Workflow Deconstruction Result]")
    print(f"Phases: {result['steps_detected']}")
    for a in result['scaffolded_agents']:
        print(f"\nAgent: {a['role']}\nSystem: {a['system_prompt']}")

if __name__ == "__main__":
    main()
