"""
HUMMBL Decomposition Operator (DE)
Transforms complex problems into structured component trees

Design Principles:
- Explicit over implicit
- Traceable reasoning
- Measurable outputs
- Fail gracefully
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple, Set, Literal
import re
from datetime import datetime


@dataclass
class Component:
    """Represents a decomposed component of the problem"""
    id: str
    description: str
    type: Literal['action', 'entity', 'constraint', 'relationship']
    dependencies: List[str] = field(default_factory=list)
    coupling: Dict[str, float | str] = field(default_factory=lambda: {
        'score': 0.5,
        'reason': 'Initial estimate'
    })
    criticality: Dict[str, float | str] = field(default_factory=lambda: {
        'score': 0.5,
        'reason': 'Initial estimate'
    })
    metadata: Dict[str, float | str] = field(default_factory=lambda: {
        'extracted_from': '',
        'confidence': 0.7
    })


@dataclass
class DecompositionResult:
    """Result of decomposition operation"""
    components: List[Component]
    critical_path: List[str]
    parallelizable: List[List[str]]
    reasoning: Dict[str, List[str] | List[Dict[str, str]]]
    metadata: Dict[str, int | str | float | Optional[Dict[str, str]]]
    warnings: List[str]


class DecompositionOperator:
    """
    Decomposes complex problems into structured components
    Uses multi-pass analysis for extraction and graph building
    """
    
    def __init__(self):
        self.reasoning: List[str] = []
        self.decisions: List[Dict[str, str]] = []
        self.warnings: List[str] = []
        
    def decompose(self, problem_text: str, 
                  context: Optional[Dict] = None,
                  constraints: Optional[List[str]] = None) -> DecompositionResult:
        """
        Main decomposition algorithm
        
        Args:
            problem_text: Natural language description of problem
            context: Optional additional context
            constraints: Optional explicit constraints
            
        Returns:
            DecompositionResult with components and analysis
        """
        start_time = datetime.now()
        self.reasoning = []
        self.decisions = []
        self.warnings = []
        
        # Pass 1: Extract actions (verbs)
        actions = self._extract_actions(problem_text)
        self.reasoning.append(f"Pass 1: Identified {len(actions)} potential actions")
        
        # Pass 2: Extract entities (nouns)
        entities = self._extract_entities(problem_text)
        self.reasoning.append(f"Pass 2: Identified {len(entities)} entities")
        
        # Pass 3: Extract constraints
        all_constraints = self._extract_constraints(problem_text, constraints)
        self.reasoning.append(f"Pass 3: Identified {len(all_constraints)} constraints")
        
        # Pass 4: Build component graph
        components = self._build_components(actions, entities, all_constraints)
        self.reasoning.append(f"Pass 4: Generated {len(components)} components")
        
        # Pass 5: Detect dependencies
        self._detect_dependencies(components, problem_text)
        self.reasoning.append("Pass 5: Mapped dependencies")
        
        # Pass 6: Calculate coupling
        self._calculate_coupling(components)
        self.reasoning.append("Pass 6: Calculated coupling scores")
        
        # Pass 7: Determine criticality
        self._calculate_criticality(components)
        self.reasoning.append("Pass 7: Identified critical path")
        
        # Pass 8: Find parallelization opportunities
        parallelizable = self._find_parallelizable(components)
        critical_path = self._find_critical_path(components)
        
        duration = (datetime.now() - start_time).total_seconds() * 1000
        self.reasoning.append(f"Decomposition completed in {duration:.2f}ms")
        
        # Detect noise/ambiguity
        noise = self._detect_noise(problem_text, components)
        if noise:
            self.warnings.append(f"Detected {noise['type']} noise: {noise['description']}")
        
        return DecompositionResult(
            components=components,
            critical_path=critical_path,
            parallelizable=parallelizable,
            reasoning={
                'steps': self.reasoning,
                'decisions': self.decisions
            },
            metadata={
                'total_components': len(components),
                'max_depth': self._calculate_max_depth(components),
                'estimated_complexity': self._estimate_complexity(components),
                'confidence': self._calculate_overall_confidence(components),
                'noise_detected': noise
            },
            warnings=self.warnings
        )
    
    def _extract_actions(self, text: str) -> List[str]:
        """Extract action verbs indicating work to be done"""
        action_patterns = [
            r'\b(build|create|implement|develop|design|setup|configure|install|deploy|integrate|test|validate|optimize|refactor|migrate)\b',
            r'\b(add|remove|update|modify|fix|enhance|improve)\b',
            r'\b(analyze|evaluate|assess|review|audit|investigate)\b'
        ]
        
        actions = set()
        for pattern in action_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            actions.update(m.group().lower() for m in matches)
        
        return list(actions)
    
    def _extract_entities(self, text: str) -> List[str]:
        """Extract entities (technical terms and proper nouns)"""
        entities = set()
        
        # Technical entities
        tech_pattern = r'\b(API|MCP|server|database|worker|service|function|component|module|system|cache|storage|queue|D1|R2|KV|Cloudflare)\b'
        tech_matches = re.finditer(tech_pattern, text, re.IGNORECASE)
        entities.update(m.group().lower() for m in tech_matches)
        
        # Capitalized terms (likely proper nouns)
        cap_pattern = r'\b[A-Z][a-zA-Z]+\b'
        cap_matches = re.finditer(cap_pattern, text)
        
        skip_words = {'The', 'A', 'An', 'In', 'On', 'For', 'With', 'To', 'From', 'By'}
        entities.update(
            m.group().lower() for m in cap_matches 
            if m.group() not in skip_words
        )
        
        return list(entities)
    
    def _extract_constraints(self, text: str, explicit: Optional[List[str]] = None) -> List[str]:
        """Extract constraints (both explicit and implicit)"""
        constraints = set()
        
        # Add explicit constraints
        if explicit:
            constraints.update(explicit)
        
        # Detect implicit constraints
        patterns = {
            'time': r'\b(\d+\s+(day|week|month|hour|minute)s?)\b',
            'budget': r'\$\d+|\bzero budget\b|no budget',
            'team': r'\b(solo|alone|\d+\s+engineer(s)?|\d+\s+person)\b'
        }
        
        for pattern in patterns.values():
            matches = re.finditer(pattern, text, re.IGNORECASE)
            constraints.update(m.group().lower() for m in matches)
        
        return list(constraints)
    
    def _build_components(self, actions: List[str], 
                         entities: List[str],
                         constraints: List[str]) -> List[Component]:
        """Build components from extracted elements"""
        components = []
        id_counter = 0
        
        # Create action-based components
        for action in actions:
            related_entity = self._find_related_entity(action, entities)
            
            description = f"{action} {related_entity}" if related_entity else action
            
            components.append(Component(
                id=f"comp_{id_counter}",
                description=description,
                type='action',
                metadata={
                    'extracted_from': f"action: {action}",
                    'confidence': 0.7
                }
            ))
            id_counter += 1
        
        # Create entity components for unpaired entities
        paired_entities = [
            c.description.split(' ', 1)[1] 
            for c in components 
            if ' ' in c.description
        ]
        
        unpaired = [e for e in entities if e not in paired_entities]
        for entity in unpaired:
            components.append(Component(
                id=f"comp_{id_counter}",
                description=entity,
                type='entity',
                coupling={'score': 0.3, 'reason': 'Entity component'},
                criticality={'score': 0.3, 'reason': 'Supporting entity'},
                metadata={
                    'extracted_from': f"entity: {entity}",
                    'confidence': 0.6
                }
            ))
            id_counter += 1
        
        # Create constraint components
        for constraint in constraints:
            components.append(Component(
                id=f"comp_{id_counter}",
                description=f"respect constraint: {constraint}",
                type='constraint',
                coupling={'score': 0.8, 'reason': 'Constraint impacts all components'},
                criticality={'score': 0.9, 'reason': 'Constraint violation = failure'},
                metadata={
                    'extracted_from': f"constraint: {constraint}",
                    'confidence': 0.8
                }
            ))
            id_counter += 1
        
        self.decisions.append({
            'point': 'Component generation',
            'rationale': f"Generated {len(components)} components from {len(actions)} actions, {len(entities)} entities, {len(constraints)} constraints"
        })
        
        return components
    
    def _find_related_entity(self, action: str, entities: List[str]) -> Optional[str]:
        """Heuristic to find entity that commonly pairs with action"""
        common_pairs = {
            'build': ['server', 'api', 'system', 'component'],
            'deploy': ['worker', 'service', 'function'],
            'integrate': ['database', 'd1', 'api', 'service'],
            'configure': ['server', 'worker', 'cache'],
            'test': ['function', 'api', 'component']
        }
        
        preferred = common_pairs.get(action, [])
        
        for pref in preferred:
            match = next((e for e in entities if pref in e), None)
            if match:
                return match
        
        return entities[0] if entities else None
    
    def _detect_dependencies(self, components: List[Component], problem_text: str):
        """Detect dependencies between components"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', problem_text) if s.strip()]
        
        for comp in components:
            # Find sentences mentioning this component
            relevant = [
                s for s in sentences 
                if comp.description.lower() in s.lower()
            ]
            
            # Components mentioned together are likely related
            for other in components:
                if comp.id == other.id:
                    continue
                
                co_mentioned = any(
                    other.description.lower() in s.lower() 
                    for s in relevant
                )
                
                if co_mentioned:
                    # Action components depend on entity components
                    if comp.type == 'action' and other.type == 'entity':
                        comp.dependencies.append(other.id)
                    elif (comp.type == 'action' and other.type == 'action' and
                          self._is_sequential(comp.description, other.description)):
                        comp.dependencies.append(other.id)
            
            # All non-constraint components depend on constraints
            if comp.type != 'constraint':
                for other in components:
                    if other.type == 'constraint':
                        comp.dependencies.append(other.id)
    
    def _is_sequential(self, action1: str, action2: str) -> bool:
        """Determine if actions have natural ordering"""
        sequence = ['setup', 'build', 'configure', 'test', 'deploy', 'integrate']
        
        idx1 = next((i for i, s in enumerate(sequence) if s in action1), -1)
        idx2 = next((i for i, s in enumerate(sequence) if s in action2), -1)
        
        return idx1 != -1 and idx2 != -1 and idx2 < idx1
    
    def _calculate_coupling(self, components: List[Component]):
        """Calculate coupling scores based on connections"""
        for comp in components:
            dep_count = len(comp.dependencies)
            dependent_count = sum(
                1 for c in components 
                if comp.id in c.dependencies
            )
            
            total_connections = dep_count + dependent_count
            max_possible = (len(components) - 1) * 2
            
            score = min(total_connections / max(max_possible, 1), 1.0)
            comp.coupling = {
                'score': score,
                'reason': f"{dep_count} dependencies, {dependent_count} dependents"
            }
            
            if score > 0.7:
                self.warnings.append(
                    f"Component '{comp.description}' is highly coupled ({score:.2f})"
                )
    
    def _calculate_criticality(self, components: List[Component]):
        """Calculate criticality scores"""
        for comp in components:
            dependent_count = sum(
                1 for c in components 
                if comp.id in c.dependencies
            )
            
            if comp.type == 'constraint':
                comp.criticality = {
                    'score': 0.95,
                    'reason': 'Constraint affects all work'
                }
            else:
                score = min(0.3 + (dependent_count * 0.15), 1.0)
                comp.criticality = {
                    'score': score,
                    'reason': f"{dependent_count} components depend on this"
                }
    
    def _find_critical_path(self, components: List[Component]) -> List[str]:
        """Find critical path through component graph"""
        visited = set()
        path = []
        
        def dfs(comp_id: str) -> int:
            if comp_id in visited:
                return 0
            visited.add(comp_id)
            
            comp = next(c for c in components if c.id == comp_id)
            if not comp.dependencies:
                path.append(comp_id)
                return 1
            
            depths = [dfs(dep_id) for dep_id in comp.dependencies]
            max_depth = max(depths) if depths else 0
            path.append(comp_id)
            return max_depth + 1
        
        # Start from highest criticality component
        start = max(components, key=lambda c: c.criticality['score'])
        dfs(start.id)
        
        return list(reversed(path))
    
    def _find_parallelizable(self, components: List[Component]) -> List[List[str]]:
        """Find groups of components that can run in parallel"""
        groups = []
        processed = set()
        
        for comp in components:
            if comp.id in processed:
                continue
            
            group = [comp.id]
            processed.add(comp.id)
            
            for other in components:
                if other.id in processed:
                    continue
                
                # Can parallelize if no dependency relationship
                has_dep_relation = (
                    other.id in comp.dependencies or
                    comp.id in other.dependencies
                )
                
                if not has_dep_relation:
                    group.append(other.id)
                    processed.add(other.id)
            
            if len(group) > 1:
                groups.append(group)
        
        return groups
    
    def _calculate_max_depth(self, components: List[Component]) -> int:
        """Calculate maximum depth of dependency graph"""
        depths = {}
        
        def get_depth(comp_id: str) -> int:
            if comp_id in depths:
                return depths[comp_id]
            
            comp = next(c for c in components if c.id == comp_id)
            if not comp.dependencies:
                depths[comp_id] = 1
                return 1
            
            dep_depths = [get_depth(dep_id) for dep_id in comp.dependencies]
            depth = max(dep_depths) + 1 if dep_depths else 1
            depths[comp_id] = depth
            return depth
        
        all_depths = [get_depth(c.id) for c in components]
        return max(all_depths) if all_depths else 1
    
    def _estimate_complexity(self, components: List[Component]) -> str:
        """Estimate overall problem complexity"""
        count = len(components)
        avg_coupling = sum(c.coupling['score'] for c in components) / max(count, 1)
        depth = self._calculate_max_depth(components)
        
        if count <= 3 and avg_coupling < 0.4 and depth <= 2:
            return 'low'
        elif count <= 7 and avg_coupling < 0.6 and depth <= 4:
            return 'medium'
        elif count <= 12 and avg_coupling < 0.8 and depth <= 6:
            return 'high'
        else:
            return 'very high'
    
    def _calculate_overall_confidence(self, components: List[Component]) -> float:
        """Calculate average confidence across all components"""
        if not components:
            return 0.0
        return sum(c.metadata['confidence'] for c in components) / len(components)
    
    def _detect_noise(self, problem_text: str, 
                     components: List[Component]) -> Optional[Dict[str, str]]:
        """Detect different types of noise in the problem"""
        # Epistemic: Missing information
        if len(problem_text) < 50:
            return {
                'type': 'epistemic',
                'description': 'Problem description lacks detail and context'
            }
        
        # Aleatory: Vague/ambiguous language
        vague_terms = ['maybe', 'possibly', 'might', 'could', 'approximately']
        if any(term in problem_text.lower() for term in vague_terms):
            return {
                'type': 'aleatory',
                'description': 'Problem contains uncertain or probabilistic elements'
            }
        
        # Human: Low confidence components
        low_conf = [c for c in components if c.metadata['confidence'] < 0.5]
        if len(low_conf) > len(components) * 0.3:
            return {
                'type': 'human',
                'description': 'High uncertainty in component extraction'
            }
        
        return None


# Convenience function for direct use
def decompose(problem_text: str, 
              context: Optional[Dict] = None,
              constraints: Optional[List[str]] = None) -> DecompositionResult:
    """
    Decompose a problem into components
    
    Example:
        result = decompose(
            "Build HUMMBL Core MCP server with DE, IN, CO transformations",
            constraints=["2 weeks", "solo"]
        )
    """
    operator = DecompositionOperator()
    return operator.decompose(problem_text, context, constraints)
