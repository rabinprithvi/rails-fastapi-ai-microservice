# rails-fastapi-ai-microservice
Production-grade Python FastAPI AI microservice integrated with a Ruby on Rails backend, featuring enterprise RAG pipelines, multi-agent workflows, and LangSmith observability.


# 🚀 8-Week AI Engineer Shift: Ruby to Python/AI Stack
> **Developer:** [Your Name]  
> **Target:** 1 Hour/Day (20 Mins Theory | 40 Mins Active Coding)  
> **Objective:** Building a production-grade, hybrid Ruby-on-Rails + Python FastAPI AI Microservice to target South Indian GCCs & Product Startups.

---

## 🛠️ The Hybrid System Architecture
This repository tracks my daily progress as I build a scalable enterprise AI engine. The final architecture will connect a **Ruby on Rails** web app to a **Python FastAPI** microservice handling:
* Asynchronous Data Processing
* Enterprise RAG (Retrieval-Augmented Generation) with local Vector Storage
* Multi-Agent Collaborative Workflows via CrewAI / LangGraph
* Production-grade Telemetry via LangSmith

---

## 📅 The 8-Week Execution Dashboard

### 🔹 Phase 1: Python Bridge & Frameworks (Weeks 1–2)
*Goal: Master the environment, write asynchronous APIs, and orchestrate basic completions.*

#### Week 1: Environment & FastAPI
- [x] **Day 1:** Install Poetry. Run `poetry new ai-service`. Verify virtual environment works.
  - *Reinforcement:* What does `poetry shell` do that `pip install` alone cannot? What is the Rails equivalent of a Poetry virtual environment?
- [x] **Day 2:** Set up FastAPI and Pydantic. Build a dummy `/health` endpoint.
  - *Reinforcement:* What is the difference between `def` and `async def` in a FastAPI route? Name the Pydantic equivalent of Rails strong params + `ActiveModel::Serializer`.
- [ ] **Day 3:** Route an HTTP POST request from Rails console to the new FastAPI endpoint.
  - *Reinforcement:* Which Ruby HTTP library did you use and why? What HTTP status code should FastAPI return for a malformed request body?
- [ ] **Day 4:** Run `poetry add openai python-dotenv`. Make the first live API call via script.
  - *Reinforcement:* How does `python-dotenv` load your `.env` file, and what is its Rails equivalent (`dotenv` gem)? What happens if you exceed your OpenAI token quota?
- [ ] **Day 5:** Move the OpenAI call inside a FastAPI endpoint. Use Pydantic to validate input.
  - *Reinforcement:* Why should you never put a blocking `openai.chat.completions.create()` call inside an `async def` route without wrapping it? What Pydantic decorator enforces field types at runtime?
- [ ] **Weekend 1:** Handle API errors gracefully and refactor code into clean modules.
  - *Reinforcement:* What FastAPI class do you raise to return a structured HTTP error response (equivalent to `render json: {error:}, status: 422` in Rails)?

#### Week 2: DeepLearning.AI – LangChain Foundations
- [ ] **Day 8:** Watch Modules 1-2 of *LangChain for LLM Application Development* (Free).
  - *Reinforcement:* What problem does LangChain solve that raw `openai` SDK calls do not? Name one LangChain abstraction equivalent to a Rails concern/module.
- [ ] **Day 9:** Watch Modules 3-4 of the same course. Focus on Prompts and Parsers.
  - *Reinforcement:* What is a `PromptTemplate` and how is it different from a plain Python f-string? What does an output parser do to a raw LLM string response?
- [ ] **Day 10:** Replace raw OpenAI dictionary code with LangChain Expression Language (LCEL).
  - *Reinforcement:* Write the LCEL pipe syntax for: prompt → model → output parser. What operator does LCEL use to chain steps?
- [ ] **Day 11:** Watch the final modules of the course focusing on Memory chains.
  - *Reinforcement:* What does `ConversationBufferMemory` store and where? What is the risk of using it in a multi-user API without scoping by session ID?
- [ ] **Day 12:** Build a conversational endpoint in FastAPI that remembers past messages from Rails.
  - *Reinforcement:* How does Rails pass a `session_id` to FastAPI so each user gets isolated memory? Should memory live in-process or in Redis for a production system — and why?
- [ ] **Weekend 2:** Push framework orchestration code to production branch.
  - *Reinforcement:* What git branching strategy separates experimental LangChain work from a stable production endpoint?

---

### 🔹 Phase 2: Enterprise Data & Context (Weeks 3–4)
*Goal: Build a secure, local RAG pipeline to query private business documents.*

#### Week 3: DeepLearning.AI – Vector Databases & Chroma
- [ ] **Day 15:** Watch Modules 1-2 of *Vector Databases and RAG Fundamentals* (Free).
  - *Reinforcement:* What is an embedding vector and why can't a traditional SQL `LIKE` query replace semantic search?
- [ ] **Day 16:** Watch Modules 3-4 of the course. Focus on document chunking strategies.
  - *Reinforcement:* What happens to retrieval quality if your chunk size is too large? Too small? What is the overlap parameter for?
- [ ] **Day 17:** Run `poetry add chromadb`. Write a script to convert paragraphs into embeddings.
  - *Reinforcement:* Which OpenAI model generates embeddings (not completions)? What Python function call produces the embedding vector?
- [ ] **Day 18:** Initialize a local, disk-persistent Chroma database inside the workspace.
  - *Reinforcement:* What is the difference between an in-memory and a disk-persistent Chroma client? Which is safe to use across server restarts?
- [ ] **Day 19:** Write a script that saves sample text data and performs a simple semantic query.
  - *Reinforcement:* What does `collection.query(query_texts=["..."], n_results=3)` return? How do you use the returned `documents` in your LLM prompt?
- [ ] **Weekend 3:** Test how changing chunk sizes affects database query results.
  - *Reinforcement:* If semantic results are irrelevant, what is the first parameter you would tune — chunk size, overlap, or `n_results` — and why?

#### Week 4: The Automated Document Ingestion Pipeline
- [ ] **Day 22:** Complete the remaining modules of the RAG short course.
  - *Reinforcement:* What is the difference between a retriever and a vector store in LangChain's abstraction layer?
- [ ] **Day 23:** Build a `/api/v1/ingest` endpoint in FastAPI that accepts unstructured text or logs.
  - *Reinforcement:* Should the ingest endpoint return `200 OK` synchronously or `202 Accepted` and process in the background — and why?
- [ ] **Day 24:** Update Rails background job to automatically stream raw text files to this ingest API.
  - *Reinforcement:* Which Rails tool (Sidekiq, GoodJob, Solid Queue) did you use, and how did you pass the file payload to the HTTP client?
- [ ] **Day 25:** Build a `/api/v1/query` endpoint that executes a semantic look-up against ChromaDB.
  - *Reinforcement:* What is the correct HTTP verb for a query that reads data but needs a body payload — `GET` or `POST`? What does REST convention say vs. what is practical?
- [ ] **Day 26:** Feed retrieved Chroma context into the LLM prompt to answer context-aware questions.
  - *Reinforcement:* Write the prompt structure (system + user) that injects retrieved `{context}` and a `{question}`. What instruction prevents the LLM from hallucinating outside the context?
- [ ] **Weekend 4:** Refactor RAG pipeline to return an error if the answer isn't in the data.
  - *Reinforcement:* What string can you instruct the LLM to return when it cannot find an answer, so your code can detect and surface a structured error instead of a hallucination?

---

### 🔹 Phase 3: Premium Multi-Agent Workflows (Weeks 5–6)
*Goal: Build autonomous agents that can execute sequential, complex logical loops.*

#### Week 5: DeepLearning.AI – Agentic Architectures
- [ ] **Day 29:** Watch the first half of *Multi-AI Agent Systems with CrewAI* (Free).
  - *Reinforcement:* What is the key difference between a Chain (LangChain) and an Agent? Which one decides at runtime which tool to call next?
- [ ] **Day 30:** Complete the remaining video modules of the agent short course.
  - *Reinforcement:* In CrewAI, what are the three required properties of every `Agent`? What does the `goal` field influence at runtime?
- [ ] **Day 31:** Run `poetry add crewai` or `langgraph`. Initialize a single agent workspace.
  - *Reinforcement:* What is a LangGraph `StateGraph` node, and how does it differ from a CrewAI `Task`? Which framework gives you more control over conditional branching?
- [ ] **Day 32:** Write a custom Python tool (a basic function) that the agent can execute autonomously.
  - *Reinforcement:* What decorator or class wraps a plain Python function so CrewAI/LangGraph can discover and call it as a tool?
- [ ] **Day 33:** Build an endpoint where an agent chooses whether to use the tool based on user intent.
  - *Reinforcement:* What mechanism does the LLM use to decide whether to call a tool or respond directly? What field in the tool definition is most critical for that decision?
- [ ] **Weekend 5:** Debug agent loops and track how the system reacts to unexpected queries.
  - *Reinforcement:* How do you set a maximum iteration limit to prevent an agent from looping infinitely? What should your endpoint return if the limit is hit?

#### Week 6: The Autonomous Backend Worker
- [ ] **Day 36:** Define a two-agent system (Agent 1 processes complex logs, Agent 2 reviews errors).
  - *Reinforcement:* In CrewAI, what is a `Crew` and how does `Process.sequential` differ from `Process.hierarchical`?
- [ ] **Day 37:** Combine Week 4 RAG pipeline as a searchable tool for your new agents.
  - *Reinforcement:* Why must the RAG tool's description be highly specific? What happens if two tools have overlapping descriptions?
- [ ] **Day 38:** Wrap this entire multi-agent workflow inside a scalable FastAPI endpoint.
  - *Reinforcement:* Should the agent endpoint be `async def` with `await crew.kickoff_async()` or blocking `def`? What breaks if you block the event loop?
- [ ] **Day 39:** Set up an asynchronous Rails workflow (e.g., Sidekiq) to trigger this multi-agent endpoint.
  - *Reinforcement:* Why does Rails use a background job (Sidekiq) instead of a synchronous `Net::HTTP` call to trigger the agent endpoint?
- [ ] **Day 40:** Build a webhook mechanism where Python pings Rails back with the final data payload.
  - *Reinforcement:* Which FastAPI function (`httpx.AsyncClient` or `requests.post`) is correct inside an `async def` handler, and why?
- [ ] **Weekend 6:** Run 10 end-to-end tests to verify that data flows flawlessly across both systems.
  - *Reinforcement:* What test assertion proves the Rails → FastAPI → Agent → Rails webhook loop completed successfully end-to-end?

---

### 🔹 Phase 4: Productionization & Positioning (Weeks 7–8)
*Goal: Add enterprise telemetry, containerize your app, and launch your profile.*

#### Week 7: MLOps, Tracing, and Resilience
- [ ] **Day 43:** Create a free LangSmith account. Add tracking keys to the Python environment.
  - *Reinforcement:* Which two environment variables does LangSmith require? What does setting `LANGCHAIN_TRACING_V2=true` automatically instrument?
- [ ] **Day 44:** Run full systems tests. Inspect the LangSmith dashboard to review latency and model steps.
  - *Reinforcement:* In LangSmith, what is a "Run"? What does the flame graph view tell you that raw logs cannot?
- [ ] **Day 45:** Optimize prompt token counts using LangSmith metrics to lower potential production costs.
  - *Reinforcement:* If a LangSmith trace shows 80% of tokens are in the system prompt, what is one concrete technique to reduce that without losing context quality?
- [ ] **Day 46:** Write a `Dockerfile` to completely containerize your Python microservice repository.
  - *Reinforcement:* Why do you `COPY pyproject.toml poetry.lock` before `COPY . .` in the Dockerfile? What caching benefit does this layer ordering give?
- [ ] **Day 47:** Run the whole ecosystem locally using Docker to simulate a cloud production setup.
  - *Reinforcement:* In `docker-compose.yml`, how does the Rails container refer to the FastAPI container by hostname? What Docker network feature enables this?
- [ ] **Weekend 7:** Clean up the repository and prepare for public review.
  - *Reinforcement:* What should a `.dockerignore` file always exclude? Name three files/dirs critical to keep out of the production image.

#### Week 8: The Portfolio Launch
- [ ] **Day 50:** Write a comprehensive README user guide highlighting your system architectures.
  - *Reinforcement:* What is the one architecture diagram (draw.io / Mermaid) that would make a GCC hiring manager immediately understand your system in under 30 seconds?
- [ ] **Day 51:** Record a 3-minute Loom walkthrough showing your system executing an enterprise workflow.
  - *Reinforcement:* What is the single strongest "proof of production quality" you can demonstrate live — latency numbers, LangSmith trace, or the Docker compose boot?
- [ ] **Day 52:** Add technical stack to your resume: *Enterprise RAG, Multi-Agent Orchestration, FastAPI*.
  - *Reinforcement:* Write one resume bullet (XYZ format: accomplished X by doing Y, measured by Z) for this project.
- [ ] **Day 53:** Update LinkedIn profile. Position yourself as a *Senior Software & AI Systems Engineer*.
  - *Reinforcement:* What keyword does a GCC recruiter ATS system most likely filter for — "LangChain", "RAG", "FastAPI", or "LLM"? Add all four.
- [ ] **Day 54:** Apply directly to GCC and tech startup positions across Bengaluru, Chennai, and Hyderabad.
  - *Reinforcement:* What GitHub repository signal (stars, commit frequency, README quality) most influences a technical hiring manager's first impression?
- [ ] **Weekend 8:** Milestone complete! Market ready.
  - *Reinforcement:* Name the three biggest technical decisions you made across 8 weeks and what you would do differently with hindsight.

---

## 📈 Daily Engineering Logs

### Day 1
* **Date:** 2026-06-16
* **Time Invested:** 60 Mins
* **Tasks Done:** Successfully created public GitHub repository, initialized structured Poetry environment, and isolated runtime dependencies (`fastapi`, `uvicorn`, `pydantic`).
* **Blockers:** None.
* **Next Step:** Day 2 - Coding the asynchronous type-safe API server layer.

### Day 2
* **Date:** 2026-06-17
* **Time Invested:** 60 Mins
* **Tasks Done:** Built modular `app/` package with `app/main.py` (ASGI entry point + lifespan hooks), `app/schemas/health.py` (Pydantic v2 typed contract), and `app/routers/health.py` (scoped `APIRouter` at `/api/v1`). Verified `GET /api/v1/health` returns `200 OK` with a typed JSON payload. Explored auto-generated Swagger UI at `/docs`.
* **Reinforcement Answers:** `async def` suspends at `await` — no extra threads. `BaseModel` = serializer + strong params in one class. `APIRouter` = `namespace :api do namespace :v1`. `lifespan` = `config/initializers/` + `at_exit`.
* **Blockers:** None.
* **Next Step:** Day 3 - Fire an HTTP POST from Rails console into this FastAPI endpoint.


