# 🔴 ALERTsim ⚖️🔍🤖

Agent-driven Legal Eval for Red Teaming: A chat simulation tool focused on assessing legal requirements through agent-based interactive scenarios and adversarial dialogues. For Law x LLM NYC Hack 6/25-27

This project demonstrates a chatbot simulation based on pre-trained language models using Gradio, a library for creating web interfaces in Python. 

Run the notebook and interact in cell or on local URL:  http://127.0.0.1:7863

Final transcripts in [this google doc](https://docs.google.com/document/d/1MGOz5tw8rkABnmboQCw4BjzYtYGKT3xyHBTe3uwVvZU/edit#heading=h.ef9v4jpiavgm) TODO - put in more structured data format

<img width="1378" alt="image" src="https://github.com/andrewyu0/ALERTsim/assets/5696002/903fc05d-c657-460f-8003-96fb1adf15b4">


## Requirements

- Python 3.10
- Gradio
- Pydantic
- OpenAI / GPT-4 (example language model)
- AnyIO

## Components

1. **Player** class
   - Represents a participant in the conversation (responds and reflects).
2. **simulation_CoT** function
   - Runs the simulation, alternating between two Player instances.
3. **run_simulation** function
   - Wraps the simulation_CoT function for use with Gradio.
4. Gradio Interface
   - Accepts Human and Primary scenarios as well as initial message and number of turns, and outputs a transcript.

## Usage

- The Gradio interface will be used to execute the simulation with user-defined inputs.
- Users can input the scenarios in text or JSON format.
- The Gradio interface supports multiline text inputs for Human Scenario, Primary Scenario, and Initial Message.
- The simulation will output the conversation history as a transcript.

## Features

- The Gradio interface provides a user-friendly interface to input scenarios and messages for the simulation.
- The code handles both text and JSON-encoded inputs.
- The chatbot simulates the conversation based on the given scenarios and interacts accordingly.

## Limitations

- Real-time output updates are not supported in Gradio.
- The Gradio output has a length limit, and large outputs might break the interface.

## Notes

- Make sure to handle input formats correctly, especially when using JSON input.
- Check string format specifications in all PromptTemplate instances to avoid errors.
- Be cautious when reverting to the previous Git commit, as uncommitted changes might be lost.

## Key next steps (6/28 onwards)
1. Debug gradio error when longer inception prompts added - error indicates that there is an "Invalid format specifier" in one of the prompt templates being used, causing a Pydantic validation error. 
2. Usability - add gradio conditioning, user friendliness as transcripts are generated
3. "Cialdini" leveling - give both parties deep understanding of Cialdini's Persuasion principles to rigorously pressure test
4. Custom Knowlege Base (CKB) of case law that the primary can reference, to make more directed, distilled reccs - faster/rigorous persuasion
5. Dense Retrieval Methods: Implementing efficient dense retrieval techniques (e.g., DPR or REALM) can notably improve contextually relevant responses. Use existing libraries to speed up the process (particularly want to explore "gisting")
6. Emotion and Tone Modeling: Use pre-trained sentiment analysis models to quickly adapt the agent's responses based on the sentiment of the conversation, closely simulating human-like interaction
7. Synthetic data: capturing high quality convos for input data for other projects (e.g. training database of illegal activity convos)

# agent-sim

Law-making and legal interpretation convert opaque human goals and values into legible directives. At Stanford, we are working on [A Legal Informatics Approach to Aligning Artificial Intelligence with Humans](https://law.stanford.edu/projects/a-legal-informatics-approach-to-aligning-artificial-intelligence-with-humans/), a research agenda leveraging legal processes and concepts for AI alignment. Like how parties to a legal contract cannot foresee every potential “if-then” contingency of their future relationship, and legislators cannot predict all the circumstances under which their bills will be applied, we cannot ex ante specify “if-then” rules that provably direct good AI behavior. Legal theory and practice offer arrays of tools to address these problems. For instance, legal standards allow humans to develop shared understandings and adapt them to novel situations, i.e., to generalize expectations regarding actions taken to unspecified states of the world. We are leveraging the data generated by legal processes and the tools of law (methods of law-making, statutory interpretation, contract drafting, applications of standards, and legal reasoning) to facilitate the robust specification of inherently vague human goals to increase human-AI alignment.

To enable more deployments of LLMs in higher stakes use-cases, we are conducting in-depth LLM-powered multi-agent simulations demonstrating alignment of the actions of the LLM agents with legal standards through a variety of techniques. We have also received a research grant to pay human lawyers to review and rank outputs for legal human feedback on the outputs.

Our [initial focus is on fiduciary duties](https://law.stanford.edu/publications/large-language-models-as-fiduciaries-a-case-study-toward-robustly-communicating-with-artificial-intelligence-through-legal-standards/).

## How to run

### 1. Install dependencies

```bash
poetry install
```

### 2. Start the monitoring server

```bash
poetry run langchain plus start
```

### 3. Run the notebook

```bash
OPENAI_API_KEY="<your_api_key>" poetry run jupyter notebook
```

### Components

### 1. Agents

We have provided a simple implementation of an agent that supports conversation and memory as a starting point. Here are a couple of its features:

1. Model Instantiation: The agents could be generated with any model through langchain and will take in a role and an inception (role-definition) prompt
2. Memory: The agent has a selective and alterable conversation memory such that it could converse without remembering the conversation and additional/altered
   memory could be injected
3. Reflection: To support longer memory windows, a memory summarization function (called "reflection") is automatically triggered as the conversation gets longer.

Please feel free to modify this class or create your own as needed

### 2. Simulation Environment

We have provided some examples in Simulation Examples.ipynb but this is where you can get creative!
