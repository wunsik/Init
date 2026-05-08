# Skill: optimize-oracle-query
Purpose: Improve Oracle SQL latency and plan stability.
Inputs: SQL text, execution plan, table stats context.
Required context: data model docs, performance budget.
Execution steps: inspect predicates/indexes, rewrite joins, test explain plan.
Output expectations: optimized SQL + benchmark notes.
Validation checklist: lower cost, same row semantics, plan stability.
