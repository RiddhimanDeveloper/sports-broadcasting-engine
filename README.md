# Live Sports Broadcasting & Localization System

This system automates live sports broadcasting by converting raw, structured match logs into high-fidelity audio commentary with synchronized stadium background noise in real time. 

---

## Project Overview & Business Case

Live sports broadcasting typically demands field commentary teams, dedicated studio production hardware, and regional voice talent for localized international streams. For niche or regional sports leagues, these logistical overheads make broadcasting financially unviable.

This project addresses the problem by substituting manual production workflows with programmatic script generation, speech synthesis, and automated audio mixing. The system allows smaller sports organizations to generate multi-language, localized game broadcasts immediately as match events occur, drastically lowering production costs.

---

## System Architecture

The application processes incoming match data through a sequential pipeline:

1. **Text Ingestion & Script Generation:** Receives structured play-by-play text logs and uses structured prompts to generate context-aware, concise commentary scripts utilizing authentic sports terminology.
2. **Speech Synthesis:** Processes the generated script through the ElevenLabs API to produce high-emotion vocal audio tracks.
3. **Audio Mixing:** Programmatically layers the vocal audio track over ambient background crowd noise using the `pydub` library, balancing decibel levels to ensure clear vocal delivery.
4. **Operator Interface:** Serves an interactive web dashboard built with Streamlit, enabling operators to input match events manually or trigger preset match scenarios.

---

## Core Features

* **Contextual Commentary:** Outputs tailored, sport-specific scripts containing relevant terminology based on raw event logs.
* **Low-Latency Processing:** Converts data points into complete mixed audio files within seconds of an event log entry.
* **Automated Audio Overlay:** Dynamically handles decibel adjustments to seamlessly mix voice narration over multi-layered background soundscapes.
* **Console Dashboard:** A web interface built for operators to submit events, adjust playback configurations, and test match conditions instantly.

---

## Tech Stack

* **Language:** Python 3.10+
* **Language Models:** OpenAI API (GPT-4o)
* **Voice Synthesis:** ElevenLabs API
* **Audio Processing:** Pydub, FFmpeg
* **Web Interface:** Streamlit

---

## Quickstart Guide

### 1. Prerequisites
You must have FFmpeg installed on your machine to handle audio processing.

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install ffmpeg
```
