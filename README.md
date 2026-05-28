# Granite Sandbox

Small local AI experiments with IBM Granite models through Ollama.

This repo focuses on a simple question:

Can a lightweight local pipeline extract useful information from a PDF without cloud APIs, and how much does runtime improve after a few practical iterations?

## What This Project Does

- reads a PDF resume with `PyPDF2`
- runs local inference with `granite3.3:2b` through Ollama
- extracts technical skills from the document
- tracks how runtime changes across prompt and pipeline changes

## Why I Built It

This is not meant to be a polished product demo.

It is a small student experiment for understanding how local LLM pipelines behave on normal hardware:

- cold start vs warm runs
- heavier prompts vs lean prompts
- simple extraction pipelines vs unnecessary complexity

## Benchmark

Baseline pipeline:

- total pipeline time: `133.69s`

Iterated version:

- total pipeline time: `10.65s`

README image used for the public comparison:

![Benchmark](benchmark_exp.png)

## What Changed Between Runs

- simplified prompting
- reduced overhead in the pipeline
- improved chunk handling in later experiments

## Example Run

```bash
python main.py
```

## Example Output

```text
- Python
- SQL
- PyTorch
- Git
- REST APIs

took 13.96s
```

## Requirements

```text
PyPDF2
ollama
```

## Install

```bash
pip install -r requirements.txt
ollama pull granite3.3:2b
```

## Notes

- the repo is intentionally small
- the goal is experimentation, not fake production scope
- future work is mostly around better benchmarking and broader document tests
