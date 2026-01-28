
Vague Term Convergence Simulation

This project implements a simplified simulation algorithm inspired by my first Master’s thesis, which investigated the role of vague terms in human language. Natural languages remain functional and understandable despite vagueness, and this project explores how agents interacting in groups can converge on shared interpretations over time.

Overview

The simulation models agents communicating with each other and updating their beliefs iteratively. While the original thesis dealt with vague linguistic terms, this simplified version operates on degrees of belief in abstract terms, allowing experimentation with belief convergence in structured groups.

Algorithm Workflow

Create agents and assign initial beliefs:

Each agent is assigned a degree of belief, representing their initial understanding of a term or concept.

Beliefs are initialized randomly within a small margin around a starting probability.

Distribute agents into groups (villages):

Agents are evenly distributed across groups to simulate localized communities.

Construct group networks:

Each group is transformed into a small-world network.

Small-world networks are graphs that balance high local clustering with short average path lengths, which is suitable for modeling information transmission in real-world social networks.

Groups start as ring lattices (where each agent connects to k neighbors) and are rewired with a probability p to introduce randomness and simulate information diversity.

Belief updating via weighted averaging:

Agents update their beliefs based on the weighted beliefs of their neighbors (a simplified DeGroot model).

Weights allow some information to influence an agent more strongly than other information, simulating differential reliability in real-world communication.

Iterate over multiple runs:

Belief updates occur over multiple time steps, allowing observation of convergence patterns.

Observations

From running the model:

Convergence is influenced by group structure and rewiring probability:

Large groups with small subgroups and low rewiring probabilities create “echo chambers,” slowing the convergence of beliefs.

Higher rewiring probabilities increase information diversity and speed up convergence.

Regardless of structure, beliefs eventually converge over enough iterations.


Insights for natural language modeling:

The simulation demonstrates how local interactions and network structure influence the collective understanding of vague terms.

The simplified model captures the essential dynamics of belief propagation and convergence.

Potential Extensions

Future work could include:

Introducing rogue agents who propagate misinformation or hold fixed beliefs.

Modeling insular subgroups (like online echo chambers) to study belief divergence in extreme conditions.

Exploring optimal group structures and rewiring probabilities for faster convergence.

Usage

The simulation is implemented in Python and requires numpy and matplotlib. Users can:

Define the number of agents, groups, and initial belief probabilities.

Set network parameters such as the number of neighbors (k) and rewiring probability (p).

Run multiple iterations and visualize the evolution of average beliefs over time.

Example visualization:
<img width="909" height="688" alt="Screenshot 2026-01-28 at 14 34 22" src="https://github.com/user-attachments/assets/ac6d5dc5-6ce7-45f2-8d31-63cadcc654d4" />
<img width="1101" height="731" alt="Screenshot 2026-01-28 at 14 36 19" src="https://github.com/user-attachments/assets/39d6eb4f-4857-430f-9c04-6460bca84876" />
<img width="883" height="642" alt="Screenshot 2026-01-28 at 14 34 26" src="https://github.com/user-attachments/assets/0e77176f-b71e-432c-81e5-58a5ed3012af" />
<img width="1440" height="900" alt="Screenshot 2026-01-28 at 14 35 17" src="https://github.com/user-attachments/assets/f6579829-e974-4aa7-aaae-e6413b69d2bd" />
<img width="1082" height="583" alt="Screenshot 2026-01-28 at 14 37 44" src="https://github.com/user-attachments/assets/ab3d428b-1483-41d4-b210-c0e966e9f6d3" />
<img width="997" height="664" alt="Screenshot 2026-01-28 at 14 35 30" src="https://github.com/user-attachments/assets/49cfc6a3-e52c-438c-bb4e-69eef9367ec3" />

