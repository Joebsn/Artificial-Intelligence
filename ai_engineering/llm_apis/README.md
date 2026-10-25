# LLM APIs

Modern AI applications use LLM APIs from platforms like OpenAI to send prompts to language models and receive generated responses. AI engineers need to understand concepts such as:

## Function Calling

This allows the model to interact with external tools or services such as databases, calculators or APIs. Instead of only generating text, the model can trigger specific functions to perform tasks.

## Model Parameters

These are settings that control how the model generates responses.

- Temperature controls randomness in predictions
- Top-K limits choices to the most probable tokens
- Top-P selects tokens based on cumulative probability
- Used to tune output diversity and coherence

### Sampling

Sampling is the process of selecting a small group from a larger population to gather information and make conclusions about the whole group.
There are two types of Sampling Methods: Probability sampling methods and Non-probability sampling methods.

#### Probability Sampling Methods

Every element has a known, non-zero chance of selection. 4 types of probability sampling:

- Random Sampling Method: Every item or individual in a group has an equal chance of being selected. Example: Drawing names from a lottery to select participants.
- Cluster sampling: Split large population into small groups and pick few groups and study samples from chosen group. Example: Selecting some schools from clusters of schools.
- Systematic sampling: The population is arranged in order, and every nth item is selected to form the sample. Example: Selecting every 10th person from a list of 200 for a survey.
- Stratified random sampling or mixed sampling: The population is divided into subgroups (strata) based on distinct characteristics, and samples are selected proportionally from each subgroup. Example: Dividing students into Arts, Commerce, and Science groups to study academic performance.

### Non-Probability Sampling Methods

Selection not random; generalizability limited. 4 types in Non-probability Sampling:

- Quota Sampling: The population is divided into groups based on certain characteristics, and fixed numbers are selected from each group to ensure diversity in the sample. Example: Surveying a set percentage of people from different age groups.
- Convenience Sampling: The investigator selects items based on convenience, often using readily accessible individuals or items. Example: Interviewing people at a local mall for a survey about cooking habits.
- Purposive or Deliberate Sampling: The investigator deliberately selects a sample based on their judgment, focusing on items that are deemed most relevant to the study. Example: Selecting top FMCG companies like Nestle and Hindustan Unilever for a market study.
- Snowball Sampling: A research method where sample is increased when existing subjects recruit by referrals. Example: Study about Homelessness, where a person refer to two homeless and those people then refer to more homeless people.

### Temperature Sampling

Temperature controls how random the model’s output is and typically ranges from 0 to 2.

- Low temperature: Safer, more predictable text
- High temperature: More creative and varied text

### Top-K Sampling

Top-K limits the model to choosing the next word from only the K most likely options, ignoring all other possibilities. This helps control randomness by keeping the selection focused on higher-probability words.
How it works:

- The model ranks all possible next words by probability
- Keeps only the top K most likely words
- Randomly selects one word from this limited set

Example:

- Top K = 50: selects from the 50 most likely words
- Smaller K: safer output
- Larger K: more variety

### Top-P (Nucleus) Sampling

Top P selects the next word based on cumulative probability instead of a fixed number of options, allowing the set of possible choices to grow or shrink depending on how confident the model is. Example:
How it works:

- Words are ranked by their probability
- Starting from the most likely word, words are added one by one
- The model stops when the combined probability reaches or exceeds P
- One word is then randomly selected from this group

Example:

- Top P = 0.9: selects from words that together account for 90% of the total probability
- Lower P: fewer choices, safer output
- Higher P: more choices, more creative output

## Prompt Management

This involves designing, organizing and refining prompts to ensure the LLMs produces accurate, consistent and useful responses without hallucination.

## Structured Outputs

LLMs can return responses in structured formats such as JSON which makes it easier for applications to process and use the output programmatically.
