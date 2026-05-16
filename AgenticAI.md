# Agentic AI Interview Questions

This document contains a comprehensive list of Agentic AI (Agentic Artificial Intelligence) interview questions, categorized by difficulty (20% Easy, 30% Medium, 50% Hard).

## Easy (20%)

### 1. What is Agentic AI?
**Answer:** Agentic AI refers to artificial intelligence systems that possess agency—the ability to act autonomously, make decisions, plan, and execute tasks to achieve a specific goal with minimal human intervention.
**Example:** An AI that books a flight, reserves a hotel, and adds it to your calendar based on the prompt "Plan my trip to Paris."
**Reference:** [What is Agentic AI?](https://www.ibm.com/topics/agentic-ai)

### 2. What is the difference between Generative AI and Agentic AI?
**Answer:** Generative AI is primarily reactive; it generates text, images, or code in response to a direct prompt. Agentic AI is proactive; it takes a high-level goal, breaks it down into steps, uses tools, and executes actions iteratively to achieve that goal.
**Example:** GenAI: "Write an email." Agentic AI: "Read my inbox, draft replies to urgent emails, and send them."
**Reference:** [Generative vs. Agentic AI](https://huggingface.co/blog/open-source-llms-as-agents)

### 3. What is an LLM Agent?
**Answer:** An LLM Agent is an agentic AI system where a Large Language Model acts as the central "brain." It uses the LLM to reason, plan, and decide which external tools or APIs to call to accomplish a task.
**Example:** AutoGPT or BabyAGI.
**Reference:** [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)

### 4. What are Tools in the context of AI Agents?
**Answer:** Tools are external functions, APIs, or scripts that an agent can invoke to interact with the outside world. This gives the agent capabilities beyond just text generation.
**Example:** A `search_web` tool, a `calculator` tool, or a `write_to_file` tool.
**Reference:** [LangChain - Tools](https://python.langchain.com/docs/modules/agents/tools/)

### 5. What is a Prompt in Agentic AI?
**Answer:** A prompt in agentic AI is not just a user query, but often a complex set of instructions (system prompt) that defines the agent's persona, its available tools, its constraints, and the format it must use to reason and act.
**Example:** "You are an assistant. You have access to the following tools: [Tool 1, Tool 2]. Use the Thought/Action/Observation format."
**Reference:** [Prompt Engineering Guide](https://www.promptingguide.ai/)


## Medium (30%)

### 6. Explain the ReAct (Reasoning and Acting) framework.
**Answer:** ReAct is a paradigm for LLM agents where the model generates both reasoning traces (Thoughts) and task-specific actions (Actions) in an interleaved manner. The Thought helps the agent plan, while the Action executes a tool and returns an Observation.
**Example:** Thought: I need to find the capital of France. Action: Search[Capital of France]. Observation: Paris.
**Reference:** [ReAct Paper](https://arxiv.org/abs/2210.03629)

### 7. What is the role of Memory in an AI Agent?
**Answer:** Memory allows an agent to retain information across steps or interactions. Short-term memory (in-context learning) stores the current conversational history and step-by-step reasoning. Long-term memory uses external vector databases to recall past experiences and information over long periods.
**Example:** Using a Vector DB to remember a user's preferences from a conversation last month.
**Reference:** [LangChain - Memory](https://python.langchain.com/docs/modules/memory/)

### 8. What is Chain of Thought (CoT) prompting?
**Answer:** CoT is a prompting technique that encourages the LLM to articulate its intermediate reasoning steps before arriving at a final answer. This significantly improves performance on complex reasoning tasks.
**Example:** "Let's think step by step. First... Second... Therefore..."
**Reference:** [Chain-of-Thought Prompting Paper](https://arxiv.org/abs/2201.11903)

### 9. What is LangChain?
**Answer:** LangChain is an open-source framework designed to simplify the creation of applications using large language models. It provides standard interfaces for components like LLMs, prompts, memory, tools, and agents.
**Example:** `agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)`
**Reference:** [LangChain Documentation](https://python.langchain.com/)

### 10. How do Multi-Agent Systems work?
**Answer:** In a multi-agent system, multiple distinct AI agents interact or collaborate to solve a problem. Each agent might have a specific role, persona, or set of tools. They communicate with each other, often via a simulated environment or chat interface.
**Example:** ChatDev, where one agent acts as a CEO, another as a Developer, and another as a Tester to build software.
**Reference:** [AutoGen - Multi-Agent Conversation Framework](https://microsoft.github.io/autogen/)


## Hard (50%)

### 11. Explain the Plan-and-Solve architecture.
**Answer:** Instead of reasoning step-by-step on the fly (like standard ReAct), a Plan-and-Solve agent first explicitly generates a comprehensive step-by-step plan to achieve the goal. Then, it executes the plan systematically, updating it if an execution step fails.
**Example:** Plan: 1. Search for stock price. 2. Calculate moving average. 3. Write report.
**Reference:** [Plan-and-Solve Prompting Paper](https://arxiv.org/abs/2305.04091)

### 12. What are the primary failure modes of Agentic AI?
**Answer:** 1. **Hallucination of tools:** Attempting to use tools that don't exist. 2. **Infinite Loops:** Getting stuck repeating the same Action/Observation cycle without making progress. 3. **Context Overflow:** Exceeding the LLM's token limit during a long task. 4. **Catastrophic forgetting:** Forgetting the original goal midway through execution.
**Example:** The agent keeps searching Google for the exact same query 50 times.
**Reference:** [LLM Agents Failure Modes](https://lilianweng.github.io/posts/2023-06-23-agent/#challenges)

### 13. How does Tool Calling (Function Calling) work at the API level in models like GPT-4?
**Answer:** Function calling is a feature where the model is fine-tuned to detect when a function should be called and to output a JSON object containing the arguments to call that function. The API halts, returns the JSON to the developer, the developer executes the local code, and returns the result back to the model as a "Tool/Function Message."
**Example:** OpenAI API `tools` array parameter and `tool_calls` response object.
**Reference:** [OpenAI - Function Calling](https://platform.openai.com/docs/guides/function-calling)

### 14. What is Self-Reflection in AI Agents?
**Answer:** Self-reflection allows an agent to evaluate its own past actions and outcomes, recognize mistakes, and refine its future strategies. Frameworks like Reflexion use heuristic feedback and self-evaluation to improve agent performance over multiple trials.
**Example:** "My last attempt to compile the code failed due to a syntax error on line 4. I need to fix the missing semicolon and try again."
**Reference:** [Reflexion Paper](https://arxiv.org/abs/2303.11366)

### 15. Describe the implementation of Vector Databases for Agent Long-Term Memory.
**Answer:** Text data is converted into high-dimensional numerical vectors using an embedding model (e.g., `text-embedding-ada-002`). These vectors are stored in a Vector DB (like Pinecone, Milvus, or Chroma). When the agent needs memory, it embeds the current context and performs a k-Nearest Neighbors (k-NN) or cosine similarity search to retrieve the most relevant past experiences.
**Example:** `db.similarity_search(query_embedding)`
**Reference:** [Pinecone - What is a Vector Database?](https://www.pinecone.io/learn/vector-database/)

### 16. What is Semantic Routing?
**Answer:** Semantic routing uses embedding models to quickly categorize user inputs and route them to specific agentic workflows or sub-agents, rather than relying on a massive, slow LLM to make the initial routing decision. It is much faster and cheaper.
**Example:** Using `semantic-router` to send math questions to a calculator agent and code questions to a coder agent based on vector similarity to predefined utterance sets.
**Reference:** [Semantic Router GitHub](https://github.com/aurelio-labs/semantic-router)

### 17. How do you evaluate the performance of an autonomous agent?
**Answer:** Agent evaluation is difficult because of the open-ended nature of tasks. Evaluators use frameworks like AgentBench, WebArena, or custom LLM-as-a-Judge pipelines. Metrics include Success Rate, Number of steps taken, Tool use efficiency, and adherence to constraints.
**Example:** Using GPT-4 as an automated evaluator to check if the agent correctly modified a simulated database.
**Reference:** [AgentBench Paper](https://arxiv.org/abs/2308.03688)

### 18. What is the Tree of Thoughts (ToT) prompting strategy?
**Answer:** ToT generalizes Chain of Thought by allowing an LM to explore multiple reasoning paths (branches) over decisions. It maintains a tree of intermediate steps, evaluating branches using heuristics (like "sure/maybe/impossible"), and using search algorithms (BFS/DFS) to navigate to the optimal solution.
**Example:** The agent generates 3 possible next steps, evaluates which one is most promising, and expands only that branch.
**Reference:** [Tree of Thoughts Paper](https://arxiv.org/abs/2305.10601)

### 19. What is Semantic Caching and why is it important for Agents?
**Answer:** Semantic caching stores the responses of previous LLM calls based on their vector embeddings. If an agent encounters a problem that is semantically similar to a previous one, it retrieves the cached response instead of making a slow, expensive API call to the LLM.
**Example:** Caching the generated plan for "Create a tic-tac-toe game in Python."
**Reference:** [GPTCache](https://github.com/zilliztech/GPTCache)

### 20. How do you handle Context Window exhaustion during long autonomous tasks?
**Answer:** Techniques include: 1. **Summarization:** Periodically summarizing the conversation history. 2. **Context Window Management:** Keeping only the last N messages and the system prompt. 3. **External Memory:** Offloading history to a Vector DB and retrieving only relevant snippets. 4. **Agent Handoff:** Passing a summarized state to a fresh agent instance.
**Example:** LangChain's `ConversationSummaryBufferMemory`.
**Reference:** [Managing Context Windows](https://www.promptingguide.ai/techniques/context)
