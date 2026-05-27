# Granite Sandbox

Started as a small experiment with local Document AI using IBM Granite 3.3 + Ollama.

At first the goal was simple:
extract useful information from PDFs locally without relying on cloud APIs.

But after multiple experiments, the interesting part became the system behavior itself.

Things like:
- why cold-start latency becomes huge
- how prompt structure changes runtime
- why semantic chunking works better than blind slicing
- how lightweight pipelines behave on consumer hardware

This sandbox is now focused more on understanding lightweight local AI systems than just PDF extraction.

---

# Current Experiments

## Experiment #1 — Cold Start Pipeline

Initial whole-document inference pipeline.

Observed:
- very high latency
- unstable runtime behavior
- unnecessary prompt overhead

Result:
~133s local CPU runtime.

---

## Experiment #2 — Lean Prompt + Warmup

Reduced prompt complexity and added warm-cache execution.

Observed:
- major latency reduction
- more stable inference
- cleaner outputs

Result:
~14s runtime.

---

## Experiment #3 — Semantic Chunking + Hot Cache

Moved from aggressive filtering to sentence-aware chunking.

Observed:
- better context preservation
- cleaner aggregation
- faster runtime behavior

Result:
~10.65s runtime across repeated runs.

---

# Pipeline

PDF
↓
PyPDF2 extraction
↓
cleaning + chunking
↓
local Granite inference
↓
Python-side cleanup
↓
final structured summary

---

# Benchmark Results

| Experiment | Runtime |
|---|---|
| Cold Start | 133.69s |
| Warmup + Lean Prompt | 14.37s |
| Hot Cache + Semantic Chunking | 10.65s |

---

# Example Output

## Technical Skills
- Python
- PyTorch
- CNN
- SQL

## Projects
- Chest X-ray Segmentation
- Chessboard State Recognition

---

# Tool Decisions

## Why PyPDF2?
Simple and lightweight for current text extraction experiments.

More complex frameworks added unnecessary overhead for this stage.

---

## Why Not Strict JSON?
Strict JSON formatting increased reasoning overhead on small local models.

Lightweight structured text was faster and easier to clean using Python.

---

## Why Python-side Cleanup?
Simple deterministic operations like:
- regex
- ordered deduplication
- filtering

are cheaper and faster than forcing the model to handle everything itself.

---

# What Was Observed

- warm-cache inference drastically reduced latency
- prompt complexity heavily affected runtime
- semantic chunking preserved context better than blind slicing
- Python memory usage stayed tiny
- runtime engine behavior mattered more than Python-side orchestration

---

# How To Run

## Install Requirements

```bash
pip install -r requirements.txt
