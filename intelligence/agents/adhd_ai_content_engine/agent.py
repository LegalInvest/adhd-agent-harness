"""Google ADK entrypoint for the ADHD × AI content engine.

Run with:
    adk run agents/adhd_ai_content_engine

This agent describes the local workflow. The operational scripts live under
`engines/` and `scripts/` so the project continues to work without a Google API
key or ADK server.
"""

from google.adk import Agent

root_agent = Agent(
    name="adhd_ai_content_engine",
    model="gemini-2.5-flash",
    instruction=(
        "You are the orchestration agent for a local ADHD × AI 400-pack content "
        "pool. Your rules: keep total packs at exactly 400; never silently replace "
        "a content pack; route new sources into research-inbox first; separate real "
        "publication feedback from templates; and explain every upgrade using the "
        "five scoring dimensions: pain intensity, ADHD×AI intersection, evidence "
        "strength, product-entry potential, and feedback potential. Use the local "
        "scripts self_growing_engine.py and build_llm_wiki_export.py as the source "
        "of operational truth."
    ),
)
