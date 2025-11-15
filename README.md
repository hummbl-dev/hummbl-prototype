# HUMMBL Prototype

**Python research implementation of HUMMBL mental model transformations**

## Purpose

This repository validates the core HUMMBL transformation operators before building production infrastructure.

**Philosophy:**
- Research first, infrastructure later
- Python for rapid iteration
- Validate concepts before deploying
- Measure everything

## NOT in this repo

- ❌ Cloudflare Workers deployment
- ❌ TypeScript production code
- ❌ API infrastructure
- ❌ D1/R2/KV integration

## WHAT IS in this repo

- ✅ Pure Python transformation operators
- ✅ Comprehensive tests
- ✅ Fast iteration cycles (seconds, not minutes)
- ✅ Empirical validation
- ✅ Jupyter notebooks for exploration

## Quick Start
```bash
# Clone and setup
git clone https://github.com/hummbl-dev/hummbl-prototype.git
cd hummbl-prototype

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v

# Try validation example
python test_hummbl_project.py
```

## Project Structure
```
hummbl-prototype/
├── transformations/          # Core operators
│   ├── decomposition.py     # DE: Break problems into components
│   ├── inversion.py         # IN: Find failure modes (coming soon)
│   └── composition.py       # CO: Combine components (coming soon)
├── tests/                   # Pytest test suite
│   └── test_decomposition.py
├── notebooks/               # Jupyter exploration
├── examples/                # Real problem examples
├── data/                    # Test data and results
├── requirements.txt         # Python dependencies
└── README.md
```

## Current Status

### Implemented
- ✅ Decomposition (DE) operator - fully functional

### In Progress
- 🔄 Empirical validation on real problems
- 🔄 Documentation of findings

### Planned
- ⏳ Inversion (IN) operator
- ⏳ Composition (CO) operator
- ⏳ Perspective (P) operator
- ⏳ Recursion (RE) operator
- ⏳ Synthesis (SY) operator

## Usage Example
```python
from transformations.decomposition import decompose

# Decompose a problem
result = decompose(
    "Build HUMMBL Core with DE, IN, CO transformations",
    context={'timeline': '2 weeks', 'phase': 'research'},
    constraints=['rapid iteration', 'empirical validation']
)

# Examine results
print(f"Components: {len(result.components)}")
print(f"Complexity: {result.metadata['estimated_complexity']}")
print(f"Confidence: {result.metadata['confidence']:.2f}")

# Review reasoning
for step in result.reasoning['steps']:
    print(f"  - {step}")

# Check warnings
for warning in result.warnings:
    print(f"  ⚠ {warning}")
```

## Development Workflow

### Week 1: Core Operators
1. ✅ Build Decomposition (DE)
2. 🔄 Test on 5 real problems
3. 🔄 Measure utility (score ≥7/10 = success)
4. ⏳ Build Inversion (IN) if DE succeeds
5. ⏳ Build Composition (CO) if IN succeeds

### Week 2: Integration
1. Combine operators into pipelines
2. Test on complex problems
3. Build simple CLI for Triad use

### Week 3-4: Production (Only if validated)
1. Port to TypeScript
2. Deploy to Cloudflare Workers
3. Integrate via MCP

## Success Criteria

**Phase 0 (Research):** At least 2 of 3 operators (DE, IN, CO) score ≥7/10 utility

**Phase 1 (Integration):** Daily usage by development team

**Phase 2 (Production):** Only proceed if Phases 0-1 succeed

## Testing Philosophy

Every operator must:
1. Be testable with pytest
2. Have measurable outputs (scores 0-1)
3. Show traceable reasoning
4. Detect noise/ambiguity
5. Fail gracefully

## Running Tests
```bash
# All tests
pytest tests/ -v

# Specific test file
pytest tests/test_decomposition.py -v

# With coverage
pytest tests/ -v --cov=transformations

# Validation on real problems
python test_hummbl_project.py
```

## Validation Process

For each operator:

1. **Manual Baseline**
   - Solve problem yourself
   - Time how long it takes
   - Note quality of solution

2. **Operator Test**
   - Run operator on same problem
   - Compare time
   - Compare quality
   - Score utility 1-10

3. **Iteration**
   - If ≥7/10: Operator works, build next
   - If <7/10: Fix algorithm, test again

4. **Documentation**
   - Log all results
   - Document what worked/didn't
   - Extract lessons

## What Happens After Validation

**If operators are useful:**
- Port to TypeScript
- Build production infrastructure
- Deploy to Cloudflare
- Integrate with development workflow via MCP

**If operators are not useful:**
- Understand why
- Revise approach
- Don't waste time on premature infrastructure

## Related Repositories

**[hummbl-research](https://github.com/hummbl-dev/hummbl-research)** - Academic foundation, 120 mental models, validation studies, case studies

## Contributing

HUMMBL is currently in research phase. 

Internal development only during validation.

After validation, contributions welcome for:
- Additional test cases
- Algorithm improvements
- Documentation enhancements
- Performance optimizations

## License

MIT License - See [LICENSE](./LICENSE)

## Contact

**Reuben Bowlby**  
Chief Engineer, HUMMBL LLC

- Twitter: [@ReubenBowlby](https://twitter.com/ReubenBowlby)
- Email: reuben@hummbl.io
- GitHub: [@hummbl-dev](https://github.com/hummbl-dev)

---

**Status:** Research phase - validating Decomposition operator  
**Updated:** November 15, 2025  
**Next Milestone:** Complete DE validation, begin IN development
