# Enterprise SaaS Lifecycle Optimizer

An automated Software Asset Management (SAM) governance agent that ingests cross-platform telemetry from identity brokers and SaaS endpoints, isolates license waste, and identifies critical data gaps.

## 🚀 Business & Operational Impact
* **Reduces SaaS Spend:** Aggregates multi-vendor software metrics to programmatically flag over-licensed or stagnant software seats.
* **Hardens Security Compliance:** Proactively flags identity drift (such as terminated lifecycle profiles that failed downstream de-provisioning rules).
* **Minimizes Manual Toil:** Transforms multi-source operational metrics into actionable SecOps helpdesk tasks.

## ⚙️ Technical Architecture
The optimization pipeline decouples system architecture from local mock configurations. It reads complex JSON datasets containing contract renewal dates, cost metrics, and historical employee login telemetry. The Python runtime processes this metadata and orchestrates a `gemini-2.5-flash` workflow to generate localized, data-driven optimization blueprints.

## 🛠️ Step-by-Step Execution Guide

1. Clone the operational repository:
   ```bash
   git clone https://github.com/HexieB/sam-optimizer.git
   cd sam-optimizer
   ```

2. Establish your dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Export your enterprise Gemini API credential:
   ```bash
   export GOOGLE_API_KEY="your-api-key-here"
   ```

4. Execute the runtime budget optimization audit:
   ```bash
   python sam_optimizer.py
   ```
