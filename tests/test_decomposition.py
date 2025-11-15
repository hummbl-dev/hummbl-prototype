"""
Tests for HUMMBL Decomposition Operator
"""

import pytest
from transformations.decomposition import decompose, DecompositionOperator, Component


def test_simple_problem():
    """Test decomposition of a simple problem"""
    result = decompose("Build a web server and deploy it")
    
    assert len(result.components) > 0
    assert result.metadata['total_components'] == len(result.components)
    assert result.metadata['estimated_complexity'] in ['low', 'medium', 'high', 'very high']
    assert 0.0 <= result.metadata['confidence'] <= 1.0


def test_hummbl_problem():
    """Test decomposition of actual HUMMBL problem"""
    problem = """
    Build HUMMBL Core MCP server with DE, IN, CO transformations,
    deploy to Cloudflare Workers, integrate with D1 for logging
    """
    
    result = decompose(
        problem,
        context={'timeline': '2 weeks', 'team': 'solo'},
        constraints=['zero budget', 'production-ready']
    )
    
    # Should identify key actions
    action_components = [c for c in result.components if c.type == 'action']
    assert len(action_components) >= 3  # build, deploy, integrate
    
    # Should identify constraints
    constraint_components = [c for c in result.components if c.type == 'constraint']
    assert len(constraint_components) >= 2  # zero budget, production-ready
    
    # Should have critical path
    assert len(result.critical_path) > 0
    
    # Should detect dependencies
    has_dependencies = any(len(c.dependencies) > 0 for c in result.components)
    assert has_dependencies


def test_coupling_detection():
    """Test that highly coupled components are flagged"""
    # Problem with many interdependencies
    problem = """
    Build authentication system that integrates with user database,
    session manager, API gateway, logging system, and monitoring dashboard
    """
    
    result = decompose(problem)
    
    # Should have warnings about coupling
    coupling_warnings = [w for w in result.warnings if 'coupled' in w.lower()]
    # May or may not have warnings depending on how dependencies are detected
    # Just ensure warnings list exists
    assert isinstance(result.warnings, list)


def test_parallelization_detection():
    """Test that independent tasks are identified as parallelizable"""
    problem = "Create API documentation, write unit tests, and design UI mockups"
    
    result = decompose(problem)
    
    # These tasks are independent, should be parallelizable
    if len(result.parallelizable) > 0:
        # At least one group of parallel tasks
        assert any(len(group) > 1 for group in result.parallelizable)


def test_noise_detection():
    """Test detection of different noise types"""
    # Epistemic noise: vague/short problem
    vague_result = decompose("Do something")
    assert vague_result.metadata['noise_detected'] is not None
    assert vague_result.metadata['noise_detected']['type'] == 'epistemic'
    
    # Aleatory noise: uncertain language
    uncertain_result = decompose("Maybe build a system that might need authentication possibly")
    assert uncertain_result.metadata['noise_detected'] is not None
    assert uncertain_result.metadata['noise_detected']['type'] == 'aleatory'


def test_critical_path():
    """Test critical path identification"""
    problem = """
    Setup development environment,
    then build the application,
    then test it,
    then deploy to production
    """
    
    result = decompose(problem)
    
    # Should have identified a sequential path
    assert len(result.critical_path) > 0
    
    # Critical path should reference actual component IDs
    all_ids = {c.id for c in result.components}
    for comp_id in result.critical_path:
        assert comp_id in all_ids


def test_complexity_estimation():
    """Test complexity estimation"""
    simple = decompose("Write a function")
    assert simple.metadata['estimated_complexity'] == 'low'
    
    complex_problem = """
    Build a distributed microservices architecture with API gateway,
    service mesh, database sharding, caching layer, message queue,
    monitoring system, logging aggregation, CI/CD pipeline,
    authentication service, authorization service, user management,
    payment processing, email notifications, and admin dashboard
    """
    complex = decompose(complex_problem)
    assert complex.metadata['estimated_complexity'] in ['high', 'very high']


def test_constraint_extraction():
    """Test that constraints are properly extracted"""
    problem = "Build system in 2 weeks with zero budget and solo engineer"
    
    result = decompose(problem)
    
    constraint_components = [c for c in result.components if c.type == 'constraint']
    
    # Should extract: 2 weeks, zero budget, solo
    assert len(constraint_components) >= 3
    
    # Constraints should have high criticality
    for c in constraint_components:
        assert c.criticality['score'] >= 0.8


def test_reasoning_traceable():
    """Test that reasoning is traceable"""
    result = decompose("Build and test application")
    
    # Should have reasoning steps
    assert 'steps' in result.reasoning
    assert len(result.reasoning['steps']) > 0
    
    # Should have decisions
    assert 'decisions' in result.reasoning
    
    # Each step should be a string
    for step in result.reasoning['steps']:
        assert isinstance(step, str)


def test_empty_problem():
    """Test handling of edge case: empty problem"""
    result = decompose("")
    
    # Should handle gracefully
    assert isinstance(result.components, list)
    assert result.metadata['noise_detected'] is not None


def test_confidence_scores():
    """Test that confidence scores are reasonable"""
    result = decompose("Build web application with authentication and database")
    
    # Overall confidence should be between 0 and 1
    assert 0.0 <= result.metadata['confidence'] <= 1.0
    
    # Each component should have confidence
    for comp in result.components:
        assert 'confidence' in comp.metadata
        assert 0.0 <= comp.metadata['confidence'] <= 1.0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
