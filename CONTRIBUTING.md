# Contributing to Agent-Monitor

Thank you for your interest in contributing to Agent-Monitor! We're excited to have community members help improve observability for AI agents.

## Code of Conduct

We are committed to providing a welcoming and inspiring community for all. Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/agent-monitor.git`
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Set up development environment: `make setup`
5. Run tests: `make test`

## Development Guidelines

### Code Style
- Follow PEP 8 for Python code
- Use type hints for all functions
- Format code with `black` and `isort`
- Run linters: `make lint`

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb: "Add", "Fix", "Update", "Refactor"
- Example: `Add trace sampling configuration for cost optimization`

### Testing Requirements
- Write tests for all new features
- Maintain minimum 80% code coverage
- Test both happy path and error cases
- Example:
  ```python
  def test_trace_creation_with_invalid_span():
      agent = Agent("test")
      with pytest.raises(ValueError):
          agent.create_span(span_name="")
  ```

## Submitting Changes

### Pull Request Process
1. Ensure all tests pass: `make test`
2. Update documentation for API changes
3. Add entry to CHANGELOG.md
4. Create PR with clear description of changes
5. Respond to review feedback promptly

### PR Template
```
## Description
Brief summary of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] Performance improvement

## Testing
Describe testing performed

## Checklist
- [ ] Tests pass
- [ ] Documentation updated
- [ ] No breaking changes
```

## Documentation

- Update README.md for user-facing changes
- Add docstrings to all public APIs
- Include code examples for new features
- Update docs/features/ for major functionality

## Reporting Issues

- Search existing issues first
- Include clear reproduction steps
- Provide environment details (OS, Python version, agent framework)
- Attach relevant logs or traces

## Areas for Contribution

- **Core Features**: Tracing, metrics collection, cost tracking
- **Integrations**: New AI agent framework support
- **Performance**: Optimization of trace processing
- **Documentation**: Guides and examples
- **Tests**: Improved coverage and edge cases

## Review Process

- Maintainers review all PRs
- 2+ approvals required for merge
- CI/CD checks must pass
- We aim to respond within 48 hours

## Questions?

- Open a discussion in GitHub Discussions
- Check existing documentation: docs/
- Join our community Slack (link in README.md)

Thank you for contributing to Agent-Monitor! 🚀