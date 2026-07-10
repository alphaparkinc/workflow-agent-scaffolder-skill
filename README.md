# genpark-workflow-agent-scaffolder-skill

> **GenPark AI Agent Skill** -- Automatic workflow task deconstructor and agent template architect.

## Quick Start

```python
from client import WorkflowAgentScaffolderClient
client = WorkflowAgentScaffolderClient()
res = client.deconstruct_workflow("analyze logs and email alerts")
print(res["scaffolded_agents"])
```
