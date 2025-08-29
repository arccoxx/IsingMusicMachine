# Ising Machine Simulator: Audio Annealing with Coupled Oscillators

Synthesize your own Ising sounds here... just run the script:) https://colab.research.google.com/drive/1xZ21S309-ecghKHOOkeCW06vhPB-BRMO?usp=sharing

## Overview
This project simulates an **Ising machine**—a specialized computer for solving optimization problems inspired by magnetic spins—using coupled oscillators in Python. By mapping Ising spins to audio oscillators, we turn the simulation into a **sound synthesizer**. As the system "anneals" (cools down from chaos to order), it generates evolving soundscapes, like a cinematic THX-inspired swell: starting as rumbling noise and building to harmonic drones. It's not just computation—it's audible art!

Run the code on Google Colab or locally to hear the machine "think" while solving Ising problems. Scale up oscillators for richer, cooler sounds.

## What is an Ising Machine?
The **Ising model** is a physics-inspired framework from statistical mechanics, modeling magnetism in materials. It consists of:

- **Spins**: Binary variables (e.g., +1 or -1, like magnetic poles "up" or "down") arranged on a lattice.
- **Couplings (J_ij)**: Interactions between spins. Positive J encourages alignment (ferromagnetic), negative J encourages opposition (antiferromagnetic).
- **Biases (h_i)**: External fields biasing individual spins.
- **Energy (Hamiltonian)**: The system's total energy is minimized when spins align to satisfy couplings:  
  \[ H = -\sum_{i<j} J_{ij} s_i s_j - \sum_i h_i s_i \]  
  The goal: Find the spin configuration with the lowest energy.

An **Ising machine** is hardware/software that solves this by physically or virtually evolving the system toward low-energy states. It's great for NP-hard optimization problems (e.g., graph partitioning, MAX-CUT) mapped to Ising form. Techniques like **simulated annealing** mimic cooling: Start "hot" (random flips) and cool to settle into optima.

## Simulating Ising Machines with a Synthesizer
We simulate the Ising model using the **Kuramoto model** of coupled oscillators (like synchronized fireflies or pendulums). This turns computation into sound generation:

- **Spins → Oscillators**: Each spin is an audio oscillator with phase θ_i. Phases cluster to represent spin states: Synced phases = same spin (+1/+1); anti-synced (π apart) = opposite (+1/-1).
- **Couplings (J_ij) → Coupling Strengths (K_ij)**: Positive K syncs oscillators (ferro), negative K anti-syncs (anti-ferro).
- **Lattice → Network**: Oscillators connect via a matrix, like a modular synth patchbay.
- **Annealing → Dynamics**: Add decreasing noise to mimic temperature drop. Oscillators evolve via:  
  \[ \dot{\theta_i} = \omega_i + \sum_j K_{ij} \sin(\theta_j - \theta_i) + \eta(t) \]  
  (ω_i: natural frequency; η: noise).
- **Sound Output**: Sum oscillator waveforms (e.g., sin(θ(t))). Chaos (high noise) sounds noisy/dissonant; order (low noise) sounds harmonic/stable.

This is like a virtual modular synthesizer (e.g., VCV Rack) where CV (control voltage) represents couplings, and noise injects "temperature." The result: An audible analog computer!

## How This Project Works
This Python script uses NumPy for simulation and SciPy for audio output. It:
1. Defines oscillators with initial frequencies and random phases.
2. Sets a coupling matrix for an Ising problem (e.g., random or custom graph).
3. Simulates dynamics with decreasing noise (annealing) and optional glissando (rising pitches) for THX-like effects.
4. Generates a WAV file of the summed waveforms, capturing the annealing process.
5. Infers final spins from phases and computes energy to "solve" the problem.

Key features:
- Scalable: Increase N (oscillators) for denser sounds (e.g., N=30 for THX depth).
- Customizable: Tweak frequencies, couplings, duration, or add crescendo for drama.
- No external deps beyond Colab defaults (NumPy, SciPy, IPython).

The audio isn't just a byproduct—it's the machine's "voice" during computation, turning math into music.

## How to Use Ising Machines to Solve Problems
Ising machines excel at combinatorial optimization. Map your problem to spins/couplings, then anneal:

1. **Formulate**: Encode variables as spins. E.g., for MAX-CUT (partition graph to maximize cut edges): Spins = partitions, J_ij = -edge weights (anti-ferro encourages cuts).
2. **Simulate/Anneal**: Run dynamics to find low-energy states.
3. **Read Solution**: Extract spins from final configuration.

Examples:
- **Traveling Salesman**: Map cities to spins, couplings to distances.
- **Protein Folding**: Spins as amino acid orientations.
- **Scheduling**: Assign tasks with conflict penalties.

In this project, we solve random or small custom Ising instances (e.g., frustrated triangles). For real hardware, see D-Wave or Fujitsu's digital annealers. Here, it's educational and sonic!

## The Really Cool Fun Sound: Recording the Annealing
The magic is the audio! As the machine anneals:
- **High "Temperature" (Start)**: High noise → Chaotic, rumbling dissonance (like static or alien whispers).
- **Critical Phase**: Noise drops → Emerging patterns, self-organizing clusters (swelling textures, metastable glitches).
- **Low "Temperature" (End)**: Stable alignment → Harmonic chords/drones (pure, resonant bliss).

For THX vibes:
- Start with clustered low frequencies (200-400 Hz rumble).
- Add glissando: Pitches rise and spread over octaves, building crescendo.
- Result: A cinematic swell, like engines revving to hyperspace—computation as symphony!

Hear it evolve in real-time: The sound *is* the solving process, not just the end. Scale to 30+ oscillators for epic density. Fun twist: Use as a sound design tool for music/FX!

## Installation and Requirements
- Python 3.8+ with NumPy, SciPy (pip install if needed).
- For Colab: No install—just paste and run.
- Optional: Matplotlib for visualizing phases/energy.

## Usage
1. Clone the repo: `git clone https://github.com/yourusername/ising-synth.git`
2. Run `ising_synth.py` (or paste into Colab).
3. Customize in code: Set N, couplings (K), frequencies, duration.
4. Output: `thx_ising_sound.wav` + console print of spins/energy.
5. Play the WAV: Hear the annealing!

Example snippet (full code in repo):
```python
# ... (simulation loop)
wavfile.write('thx_ising_sound.wav', fs, audio_data)
display(Audio('thx_ising_sound.wav'))  # In Colab
```

## Examples
- **Small Problem**: N=3, triangle graph → Solves frustration, sounds like evolving tones.
- **THX Mode**: N=30, random K, glissando → Epic build-up, low energy found audibly.
- **Custom**: Set K for your graph; add biases via frequency offsets.

## Contributing
Pull requests welcome! Ideas: Add MIDI output, real-time audio, or VCV Rack export.

## License
MIT License. Free to use, modify, and share. Credit appreciated!

Inspired by modular synth analogies and Kuramoto-Ising mappings. Questions? Open an issue! 🎶🧲
