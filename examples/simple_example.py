```python
#!/usr/bin/env python3
"""
Agent Monitor Example - Production-ready observability for AI agents
Demonstrates real-time tracing, metrics, cost tracking, and debugging
"""

import anthropic
import json
import time
from datetime import datetime
from typing import Any


class AgentMonitor:
    """Production-grade monitoring system for AI agents"""
    
    def __init__(self):
        self.client = anthropic.Anthropic()
        self.traces: list[dict[str, Any]] = []
        self.metrics = {
            "total_requests": 0,
            "total_tokens": 0,
            "total_cost": 0.0,
            "errors": 0,
            "avg_latency": 0.0
        }
        self.latencies: list[float] = []
    
    def trace_agent_call(
        self,
        agent_name: str,
        task: str,
        model: str = "claude-3-5-sonnet-20241022"
    ) -> dict[str, Any]:
        """
        Execute and monitor an agent call with full observability
        Returns monitoring data with metrics and traces
        """
        start_time = time.time()
        trace_id = f"{agent_name}_{int(start_time * 1000)}"
        
        trace_event = {
            "trace_id": trace_id,
            "agent_name": agent_name,
            "timestamp": datetime.now().isoformat(),
            "status": "started",
            "task": task
        }
        
        try:
            # Execute the agent task
            message = self.client.messages.create(
                model=model,
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": task
                    }
                ]
            )
            
            # Calculate metrics
            latency = time.time() - start_time
            self.latencies.append(latency)
            
            # Update trace with results
            trace_event.update({
                "status": "completed",
                "latency_ms": latency * 1000,
                "input_tokens": message.usage.input_tokens,
                "output_tokens": message.usage.output_tokens,
                "response": message.content[0].text[:200] + "..." if len(message.content[0].text) > 200 else message.content[0].text
            })
            
            # Update metrics
            self._update_metrics(message, latency)
            
        except Exception as e:
            trace_event.update({
                "status": "failed",
                "error": str(e),
                "latency_ms": (time.time() - start_time) * 1000
            })
            self.metrics["errors"] += 1
        
        self.traces.append(trace_event)
        return trace_event
    
    def _update_metrics(self, message: Any, latency: float) -> None:
        """Update monitoring metrics from API response"""
        self.metrics["total_requests"] += 1
        input_tokens = message.usage.input_tokens
        output_tokens = message.usage.output_tokens
        total_tokens = input_tokens + output_tokens
        
        self.metrics["total_tokens"] += total_tokens
        
        # Claude 3.5 Sonnet pricing (per million tokens)
        input_cost = (input_tokens / 1_000_000) * 3.0
        output_cost = (output_tokens / 1_000_000) * 15.0
        cost = input_cost + output_cost
        
        self.metrics["total_cost"] += cost
        
        # Calculate average latency
        avg_latency = sum(self.latencies) / len(self.latencies)
        self.metrics["avg_latency"] = avg_latency
    
    def get_monitoring_dashboard(self) -> dict[str, Any]:
        """Generate comprehensive monitoring dashboard"""
        return {
            "timestamp": datetime.now().isoformat(),
            "metrics": self.metrics,
            "recent_traces": self.traces[-5:],  # Last 5 traces
            "health_status": "healthy" if self.metrics["errors"] == 0 else "degraded",
            "total_traces": len(self.traces)
        }
    
    def debug_agent_performance(self) -> str:
        """Generate debugging report for agent performance"""
        if not self.traces:
            return "No traces recorded yet"
        
        failed_traces = [t for t in self.traces if t.get("status") == "failed"]
        successful_traces = [t for t in self.traces if t.get("status") == "completed"]
        
        report = f"""
=== Agent Performance Debug Report ===
Total Requests: {len(self.traces)}
Successful: {len(successful_traces)}
Failed: {len(failed_traces)}
Success Rate: {(len(successful_traces) / len(self.traces) * 100):.1f}%

Cost Analysis:
- Total Cost: ${self.metrics['total_cost']:.4f}
- Total Tokens: {self.metrics['total_tokens']}
- Cost per Request: ${self.metrics['total_cost'] / max(self.metrics['total_requests'], 1):.4f}

Performance:
- Average Latency: {self.metrics['avg_latency']*1000:.1f}ms
- Min Latency: {min(self.latencies)*1000:.1f}ms
- Max Latency: {max(self.latencies)*1000:.1f}ms
"""
        
        if failed_traces:
            report += f"\nRecent Errors:\n"
            for trace in failed_traces[-3:]:
                report += f"- {trace['trace_id']}: {trace.get('error', 'Unknown error')}\n"
        
        return report


def main():
    """Demonstrate the agent monitor with multiple tasks"""
    monitor = AgentMonitor()
    
    # Example tasks for the AI agent
    tasks = [
        "What are the top 3 best practices for monitoring AI systems?",
        "Explain the importance of cost tracking in production AI deployments.",
        "How can distributed tracing improve AI agent debugging?"
    ]
    
    print("Starting Agent Monitor Demo...\n")
    
    # Run agent tasks with monitoring
    for i, task in enumerate(tasks, 1):
        print(f"Running Task {i}: {task[:50]}...")
        trace = monitor.trace_agent_call(
            agent_name=f"ai-assistant",
            task=task
        )
        print(f"Status: {trace['status']} | Latency: {trace.get('latency_ms', 0):.1f}ms\n")
    
    # Display monitoring dashboard
    print("\n" + "="*50)
    print("MONITORING DASHBOARD")
    print("="*50)
    dashboard = monitor.get_monitoring_dashboard()
    print(json.dumps(dashboard, indent=2))
    
    # Display performance debug report
    print("\n" + monitor.debug_agent_performance())


if __name__ == "__main__":
    main()
```