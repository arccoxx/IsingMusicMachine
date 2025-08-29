import numpy as np
from scipy.io import wavfile
from IPython.display import Audio, display

# Parameters
N = 30  # Scaled to 30 oscillators for THX-like depth
fs = 44100  # Sampling rate (Hz)
duration = 30.0  # Longer for THX-style build-up
num_steps = int(duration * fs)
dt = 1.0 / fs
t = np.linspace(0, duration, num_steps, endpoint=False)

# Initial frequencies: random in narrow 200-400 Hz range
f_min, f_max = 200, 400
freqs_init = np.random.uniform(f_min, f_max, N)
omega_init = 2 * np.pi * freqs_init

# Target frequencies: diverge to span ~3 octaves (up to ~3200 Hz)
freqs_target = freqs_init * 2**np.random.uniform(0, 3, N)  # Octave spread
omega_target = 2 * np.pi * freqs_target

# Linear interpolation for glissando: frequencies rise over time
omegas = omega_init[:, None] * (1 - t / duration) + omega_target[:, None] * (t / duration)

# Coupling matrix: random Ising-like couplings for complex "problem"
K = np.random.choice([-1, 1], size=(N, N)) * np.random.uniform(0.5, 2.0, (N, N))
np.fill_diagonal(K, 0)  # No self-coupling
K = (K + K.T) / 2  # Symmetric

# Initial phases (random)
theta = np.random.uniform(0, 2 * np.pi, N)
thetas = np.zeros((num_steps, N))
thetas[0] = theta

# Simulate dynamics with decreasing noise and crescendo
crescendo = np.linspace(0.1, 1.0, num_steps)  # Amplitude ramp for build-up
for i in range(1, num_steps):
    frac = t[i] / duration
    sigma = 5.0 * (1 - frac)  # Noise decreases
    sin_diff = np.sin(theta[None, :] - theta[:, None])
    dtheta = omegas[:, i] * dt + np.sum(K * sin_diff, axis=1) * dt / N + np.random.normal(0, sigma * dt, N)
    theta = (theta + dtheta) % (2 * np.pi)
    thetas[i] = theta

# Generate signal: sum of sin(phase) with time-varying omega and crescendo
signal = np.sum(np.sin(thetas.T) * crescendo, axis=0)  # Used sin for smoother tone

# Normalize to [-1, 1]
signal /= np.max(np.abs(signal)) + 1e-10

# Convert to 16-bit
audio_data = (signal * 32767).astype(np.int16)

# Save to WAV
wavfile.write('thx_ising_sound.wav', fs, audio_data)

# Display in Colab
display(Audio('thx_ising_sound.wav', autoplay=False))

# Infer final spins (binarize relative phases)
final_theta = thetas[-1]
phase_diffs = (final_theta - final_theta[0]) % (2 * np.pi)
spins = np.where(phase_diffs < np.pi, 1, -1)  # Threshold at π for sync/anti-sync

# Compute energy H = - sum J_ij s_i s_j / 2 (with J = K for simplicity)
energy = -0.5 * np.sum(K * np.outer(spins, spins))
print("Final inferred spins:", spins)
print("Computed energy:", energy)
