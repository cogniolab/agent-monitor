# Contributing to agent-monitor

Thank you for your interest in contributing to agent-monitor! This document provides guidelines for contributing to our open-source observability platform.

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. All contributors must adhere to our Code of Conduct:
- Be respectful and professional
- Support fellow contributors
- Report violations to maintainers@agent-monitor.dev

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/agent-monitor.git`
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Set up development environment: `pip install -r requirements-dev.txt`
5. Run tests: `pytest tests/`

## Development Workflow

### Code Standards

- Follow PEP 8 style guidelines
- Use type hints for all functions
- Write docstrings for public APIs
- Maintain >85% test coverage

Example:
```python
def trace_agent_execution(agent_id: str, span_name: str) -> Span:
    """Create a trace span for agent execution.
    
    Args:
        agent_id: Unique agent identifier
        span_name: Name for the trace span
        
    Returns:
        Span object for tracking execution
    """
```

### Testing Requirements

- Write tests for new features in `tests/`
- Use pytest fixtures for common setup
- Test both success and failure scenarios
- Run: `pytest --cov=agent_monitor tests/`

### Commit Guidelines

- Use clear, descriptive commit messages
- Reference issues: "Fix issue #123"
- Format: `[type]: description` (feat, fix, docs, test, refactor)
- Example: `[feat]: add OpenTelemetry export support`

## Pull Request Process

1. Update CHANGELOG.md with your changes
2. Ensure all tests pass locally
3. Add tests covering new functionality
4. Update documentation as needed
5. Submit PR with detailed description
6. Address review feedback promptly

## Reporting Issues

- Search existing issues before creating new ones
- Provide reproducible examples
- Include: Python version, agent-monitor version, error logs
- Use issue templates provided

## Documentation

- Update docs/README.md for major features
- Add docstrings to all public methods
- Include usage examples in docstrings
- Update API documentation

## Areas for Contribution

- **Integrations**: New monitoring backends (Datadog, New Relic)
- **Features**: Cost tracking, custom metrics, performance optimization
- **Documentation**: Examples, tutorials, troubleshooting guides
- **Testing**: Edge cases, performance benchmarks
- **Bug fixes**: Issues labeled `good first issue`

## Build & Release

- Maintainers handle versioning (semver)
- Tag releases with `v*` prefix
- Update requirements.txt for dependencies
- Run linting: `black . && flake8 agent_monitor/`

## Questions?

- GitHub Discussions: For feature ideas and questions
- Issues: For bugs and technical problems
- Email: contributors@agent-monitor.dev

Thank you for making agent-monitor better! 🚀