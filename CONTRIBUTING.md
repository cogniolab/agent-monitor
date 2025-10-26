# Contributing to agent-monitor

Thank you for your interest in contributing to agent-monitor! We're building the best observability platform for AI agents, and we need your help.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/agent-monitor.git`
3. Create a feature branch: `git checkout -b feature/your-feature`
4. Set up development environment: `pip install -e ".[dev]"`

## Development Guidelines

### Code Quality
- Follow PEP 8 style guide
- Use type hints for all functions
- Aim for >80% test coverage
- Run linting: `make lint`
- Format code: `make format`

### Commit Standards
Write clear, descriptive commits:
```
feat: add histogram metrics for token usage
fix: resolve race condition in trace aggregation
docs: update API documentation
test: add tests for cost calculator
```

### Pull Request Process
1. Update tests and documentation
2. Ensure all tests pass: `make test`
3. Add entry to CHANGELOG.md under Unreleased
4. Request review from maintainers
5. Address feedback promptly

## Areas We Need Help

- **Integrations**: LangChain, CrewAI, AutoGen connectors
- **Exporters**: New backend support (Datadog, NewRelic, etc.)
- **Documentation**: API guides, tutorials, deployment guides
- **Performance**: Optimization for high-volume traces
- **Instrumentation**: Framework-specific observability

## Testing Requirements

- Unit tests for all features
- Integration tests for agent frameworks
- Example: `tests/exporters/test_prometheus_exporter.py`
- Run: `pytest tests/ -v --cov=agent_monitor`

## Code Review Checklist

- [ ] Tests pass locally
- [ ] Code follows project style
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
- [ ] Performance impact considered

## Reporting Issues

Include:
- Python version and OS
- Reproduction steps
- Expected vs actual behavior
- Agent framework version
- Relevant logs/traces

## License

All contributions are under MIT License. By submitting PRs, you agree to these terms.

## Questions?

- Open a GitHub Discussion
- Join our community Slack
- Check existing issues first

Happy contributing!