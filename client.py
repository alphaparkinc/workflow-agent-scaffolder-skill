"""
workflow-agent-scaffolder-skill: Client SDK
Parses workflow processes to automatically create specific sub-agent instructions.
"""
from __future__ import annotations
from typing import Optional


class WorkflowAgentScaffolderClient:
    """
    SDK for agent role planning and scaffolding.
    """

    def deconstruct_workflow(self, workflow_description: str) -> dict:
        desc = workflow_description.lower()
        steps = []
        agents = []

        # Parse task phases
        if "analyze" in desc or "check" in desc:
            steps.append("Analysis Phase: Scan resources to evaluate state.")
            agents.append({
                "role": "Data Analyst Agent",
                "system_prompt": "You are a metrics scanning bot. Parse input data files to detect anomalies, threshold breaches, and trends.",
                "input_spec": "Data log files or parameters"
            })
        if "email" in desc or "send" in desc or "notify" in desc:
            steps.append("Notification Phase: Send targeted communication.")
            agents.append({
                "role": "Communication Agent",
                "system_prompt": "You are an automated copywriter. Draft and transmit updates based on data triggers.",
                "input_spec": "Recipient details and trigger context"
            })
        if "order" in desc or "buy" in desc or "purchase" in desc:
            steps.append("Fulfillment Phase: Execute procurement or transaction.")
            agents.append({
                "role": "Fulfillment Coordinator",
                "system_prompt": "You verify catalog pricing and checkout logic parameters to confirm vendor ordering execution.",
                "input_spec": "Procurement quantities and SKU configurations"
            })

        if not steps:
            steps.append("General Phase: Standard business pipeline task.")
            agents.append({
                "role": "General Task Helper",
                "system_prompt": "You complete requested custom actions within instructions.",
                "input_spec": "Action prompt details"
            })

        return {
            "steps_detected": steps,
            "scaffolded_agents": agents,
            "scaffold_count": len(agents)
        }
