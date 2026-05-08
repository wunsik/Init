# Skill: deploy-to-aws
Purpose: Deploy service using container image and staged rollout.
Inputs: service name, environment, image tag.
Required context: CI pipeline + infra vars.
Execution steps: build/push image, apply env config, run migration checks, rollout.
Output expectations: deployment log and rollback command.
Validation checklist: health endpoint green, smoke tests pass.
