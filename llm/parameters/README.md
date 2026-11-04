# LLM parameters

LLM parameters are the internal weights learned during training that capture patterns in language such as grammar, context and relationships between words. These parameters often number in billions and determine the model’s capacity to understand and generate text.

## Decoding parameters (Generation Controls)

These parameters control how the model generates output during inference and are different from the internal model parameters learned during training.

### Temperature

It controls the randomness or creativity in the output generation

- High temperature means the model is more diverse and creative
- Low temperature means the model produces more focused and deterministic responses.

### Max Tokens

It limits the maximum number of tokens the model can generate in response.

### Top-p (Nucleus Sampling)

Top P selects the next word based on cumulative probability instead of a fixed number of options, allowing the set of possible choices to grow or shrink depending on how confident the model is.
How it works:

- Words are ranked by their probability
- Starting from the most likely word, words are added one by one
- The model stops when the combined probability reaches or exceeds P
- One word is then randomly selected from this group

Example:

- Top P = 0.9: selects from words that together account for 90% of the total probability
- Lower P: fewer choices, safer output
- Higher P: more choices, more creative output

### Presence Penalty

It discourages the model from reusing words or concepts that have already appeared in the generated text.
It encourages the introduction of new ideas and improves diversity in the output.

### Frequency Penalty

It reduces the likelihood of repeatedly using the same words based on how often they have already appeared.
It helps control excessive repetition of common words or phrases in the output and ensures the generated text remains balanced and less repetitive.

### Top-k

Top-K limits the model to choosing the next word from only the K most likely options, ignoring all other possibilities. This helps control randomness by keeping the selection focused on higher-probability words.
How it works:

- The model ranks all possible next words by probability
- Keeps only the top K most likely words
- Randomly selects one word from this limited set

Example:

- Top K = 50: selects from the 50 most likely words
- Smaller K: safer output
- Larger K: more variety

## Sampling

Sampling is the process of selecting a small group from a larger population to gather information and make conclusions about the whole group.
There are two types of Sampling Methods: Probability sampling methods and Non-probability sampling methods.

### Probability Sampling Methods

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

## Prompt Management

This involves designing, organizing and refining prompts to ensure the LLMs produces accurate, consistent and useful responses without hallucination.

## Structured Outputs

LLMs can return responses in structured formats such as JSON which makes it easier for applications to process and use the output programmatically.
