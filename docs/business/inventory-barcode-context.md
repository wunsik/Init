# Inventory + Barcode Business Context
- Goal: reduce receiving errors in FBA prep and warehouse intake.
- Primary KPI: scan mismatch rate < 0.5% weekly.
- Actors: warehouse associate, ecommerce operator, FBA manager.

## Workflow Example
1. Associate scans item barcode.
2. System resolves SKU and checks inbound shipment manifest.
3. Mismatch triggers exception queue and supervisor review.
