"""
Validation test for Decomposition operator on HUMMBL prototype project
"""

from transformations.decomposition import decompose

# Test on the actual HUMMBL project
problem = """
Build HUMMBL Python prototype with Decomposition, Inversion, 
and Composition operators. Validate each empirically on real 
problems. Only proceed to production if operators score ≥7/10.
Timeline: 2 weeks. Context: Research phase, rapid iteration,
no premature infrastructure.
"""

result = decompose(
    problem,
    context={'phase': 'research', 'timeline': '2 weeks'},
    constraints=['empirical validation', 'no premature infrastructure', 'rapid iteration']
)

print(f"\n{'='*70}")
print("DECOMPOSITION: HUMMBL Prototype Project")
print(f"{'='*70}\n")

print(f"Total Components: {result.metadata['total_components']}")
print(f"Complexity: {result.metadata['estimated_complexity']}")
print(f"Confidence: {result.metadata['confidence']:.2f}")
print(f"Max Depth: {result.metadata['max_depth']}\n")

print("COMPONENTS IDENTIFIED:")
print(f"{'='*70}")
for i, comp in enumerate(result.components, 1):
    print(f"\n{i}. {comp.description}")
    print(f"   Type: {comp.type}")
    print(f"   Criticality: {comp.criticality['score']:.2f} - {comp.criticality['reason']}")
    print(f"   Coupling: {comp.coupling['score']:.2f} - {comp.coupling['reason']}")
    if comp.dependencies:
        deps = ', '.join(comp.dependencies)
        print(f"   Dependencies: {deps}")

print(f"\n{'='*70}")
print("CRITICAL PATH (execution order):")
print(f"{'='*70}")
for i, comp_id in enumerate(result.critical_path, 1):
    comp = next(c for c in result.components if c.id == comp_id)
    print(f"{i}. {comp.description}")

if result.parallelizable:
    print(f"\n{'='*70}")
    print("PARALLELIZABLE WORK (can do simultaneously):")
    print(f"{'='*70}")
    for i, group in enumerate(result.parallelizable, 1):
        print(f"\nGroup {i}:")
        for comp_id in group:
            comp = next(c for c in result.components if c.id == comp_id)
            print(f"  - {comp.description}")

print(f"\n{'='*70}")
print("REASONING TRACE:")
print(f"{'='*70}")
for step in result.reasoning['steps']:
    print(f"  • {step}")

if result.warnings:
    print(f"\n{'='*70}")
    print("WARNINGS:")
    print(f"{'='*70}")
    for warning in result.warnings:
        print(f"  ⚠️  {warning}")

print(f"\n{'='*70}")
print("\nNOW SCORE THIS RESULT:")
print("1. Does this help you understand the project? (1-10): ___")
print("2. Would you use this to plan your work? (1-10): ___")
print("3. Did it catch things you'd miss manually? (1-10): ___")
print("4. Is it faster than thinking it through? (1-10): ___")
print("5. Would you recommend to others? (1-10): ___")
print("\nAVERAGE SCORE: ___/10")
print("\nThreshold: ≥7/10 = Success, continue to Inversion")
print("           <7/10 = Iterate on Decomposition first")
print(f"{'='*70}\n")
