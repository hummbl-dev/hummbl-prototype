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

### Phase 0: COMPLETE ✅ (November 2025)

All 6 transformation operators implemented and validated:

| Operator | Code | Status | Utility Score | Notes |
|----------|------|--------|---------------|-------|
| **Decomposition** | DE | ✅ VALIDATED | 9.2/10 | Production-ready, exemplar operator |
| **Meta-Systems** | SY | ⚠️ BASELINE | 8.0/10 | Strong meta-systems baseline, minor refinements needed |
| **Recursion** | RE | ⚠️ BASELINE | 8.0/10 | Strong iterative refinement baseline, minor refinements needed |
| **Perspective** | P | ⚠️ BASELINE | 7.8/10 | Strong multi-perspective baseline, minor refinements needed |
| **Composition** | CO | ⚠️ BASELINE | 6.0/10 | Functional integration patterns, needs refinement |
| **Inversion** | IN | ⚠️ BASELINE | 3.6/10 | Structurally sound, needs extraction refinements |

**Validation Criteria:** Operators scoring ≥7.0/10 are marked VALIDATED for production use.

### Phase 1: Case Studies & Intelligence (In Progress)

- [ ] Case Study 1: Multi-service AI system (Target: Jan 2026)
- [ ] Case Study 2: Fitness transformation (Target: Dec 2025)
- [ ] Case Study 3: Ozzy health protocol (Target: Dec 2025)
- [ ] SY19 `recommend_models()` prototype

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

## Development History

### Phase 0: Baseline Implementations (Oct-Nov 2025) ✅ COMPLETE
1. ✅ Decomposition (DE) - Validated at 9.2/10
2. ✅ Inversion (IN) - Baseline at 3.6/10
3. ✅ Composition (CO) - Baseline at 6.0/10
4. ✅ Perspective (P) - Baseline at 7.8/10
5. ✅ Recursion (RE) - Baseline at 8.0/10
6. ✅ Meta-Systems (SY) - Baseline at 8.0/10
7. ✅ 333 relationship classifications complete
8. ✅ Production infrastructure deployed

### Phase 1: Case Studies & Intelligence (Current)
1. Real-world case study implementations
2. Operator refinements (IN, CO improvements)
3. Intelligence layer prototyping (SY19)
4. Enhanced UX development

### Phase 2: Production & Scale (Q1-Q2 2026)
1. Commercial deployment preparation
2. Public beta launch
3. Community contributions
4. Partnership development

## Success Criteria

**Phase 0 (Research):** ✅ ACHIEVED - 4 of 6 operators scored ≥7/10 utility
- DE: 9.2/10 ✅
- SY: 8.0/10 ✅
- RE: 8.0/10 ✅
- P: 7.8/10 ✅
- CO: 6.0/10 (baseline, refinement planned)
- IN: 3.6/10 (baseline, refinement planned)

**Phase 1 (Case Studies):** In Progress - Target completion Jan 2026

**Phase 2 (Production):** Proceeding based on Phase 0 success

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

**[hummbl-research](https://github.com/hummbl-dev/hummbl-research)** - Main research repository with:
- All 6 operator implementations (DE, IN, CO, P, RE, SY)
- 120 mental models across 6 transformations
- Complete validation studies and case studies
- Comprehensive documentation
- v0.1.0 released November 2025

**Note:** This prototype repository contains the initial DE operator development. For the latest implementations of all operators, see [hummbl-research](https://github.com/hummbl-dev/hummbl-research).

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

**Status:** Phase 0 Complete - All 6 operators at baseline or validated  
**Updated:** November 16, 2025  
**Current Phase:** Phase 1 - Case Studies & Intelligence  
**Next Milestone:** Case study implementations (Q4 2025 - Q1 2026)

**Latest Success:** Meta-Systems operator baseline validated at 8.0/10 utility score ⚠️
