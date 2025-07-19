# Project Overview

This repository contains three presentations covering key concepts in Large Language Models (LLMs) and their applications:
1. Multilayer Perceptron - Transformer Model - LLM Distillation
2. LLM Distillation - Fine Tuning, Deployment and Integration
3. Retrieval-Augmented Generation (RAG)

## Presentation 1: Multilayer Perceptron - Transformer Model - LLM Distillation

This presentation provides a theoretical perspective on neural networks, focusing on the Transformer model and LLM Distillation.

**Key Topics:**

* Multilayer Perceptron
* Transformer Model:
    * Input Embedding and Positional Encoding
    * Multi-Head Self-Attention
    * Add & Layer Norm
    * Position-wise Feedforward Network
    * Stacking Layers
    * Output Layer
    * Loss Function
    * LLM Distillation
    * Hugging Face
    * Vertex AI

## Presentation 2: LLM Distillation - Fine Tuning, Deployment and Integration

This presentation delves into the process of creating custom LLM models through fine-tuning. Also it focuses on deploying and integrating LLMs using Google Cloud Vertex AI

**Key Topics:**

* What is fine tuning (training-testing)
* Types of fine tuning:
    * Full Fine-Tuning
    * LoRA
    * QLoRA
* Dataset preparation:
    * Vectorization
    * K-Means (Pairwise distance)
* Hyperparameters:
    * Learning Rate
    * Batch Size
    * Gradient Accumulation
    * Grid Search
* Fine Tuning Use case
* Google Cloud Vertex AI's and its role in deployment
* Decoder Strategies (Generation Parameters) for LLMs
* Deployment & integration Use Case

## Presentation 3: Retrieval-Augmented Generation (RAG)

This presentation explains Retrieval-Augmented Generation (RAG) and its applications.

**Key Topics:**
* What is RAG?
* Why RAG?
* Grounding and Context
* Vectorization
* Distance Measurements
* Real-world use case

## Real-world use case

**RAG Functionalities:**

* Create requests
* Classification by priority
* Classification by department
* Summarization of requests
* Predict costs
* Predict fieldwork
* Geographic location

**Technologies used in RAG:**

* Google Gemini
* MongoDB - Vector Indexation
* Google Kubernetes Engine (GKE)
* Google Firebase Authentication
* Spring Boot