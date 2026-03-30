


import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

# Spike generator (rate = spike per second(hz), duration = seconds)

class SpikeGenerator:
    def __init__(self, rate=10, duration=1.0, neurons = 3):
        self.rate = rate
        self.duration = duration
        self.neurons = neurons

    def generate_spikes(self):
        """
        Generates spike times using poisson process.
        Poisson process means that spikes are random and occur independently
        of each other.
        """
        num_points = int (self.duration  * 1000) # 1 ms resolution, neuronal spikes last ~1-2 ms
        time = np.linspace(0, self.duration, num_points)

        all_spikes = []

        for _ in range(self.neurons):
            spikes = np.random.rand(num_points) < (self.rate / 1000)
            spike_times = time[spikes]
            all_spikes.append(spike_times)

        return all_spikes

# Visualization class
# Raster plots are standard plot to visualize neuronal spike data.

class Visualizer:
    def plot_raster(self, all_spikes):
        plt.figure(figsize=(10,4))

        for i, neuron_spikes in enumerate(all_spikes):
            plt.vlines(neuron_spikes, i + 0.5, i + 1.5)

        plt.title("Multi-Neuron Raster Plot")
        plt.xlabel("Time (s)")
        plt.ylabel("Neuron Index")
        plt.ylim(0.5, len(all_spikes) + 0.5)
        plt.show()

class AppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Neuron Spike Visualizer")

        self.generator = SpikeGenerator()
        self.visualizer = Visualizer()

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid()

        # Firing rate inout
        ttk.Label(frame, text="Firing Rate (Hz)").grid(row=0, column=0)
        self.rate_entry = ttk.Entry(frame)
        self.rate_entry.insert(0, "1.0")
        self.rate_entry.grid(row=0, column=1)

        # Duration input
        ttk.Label(frame, text="Duration (s)").grid(row=1, column=0)
        self.duration_entry = ttk.Entry(frame)
        self.duration_entry.insert(0, "1.0")
        self.duration_entry.grid(row=1, column=1)

        # Number of neurons
        ttk.Label(frame, text="Number of Neurons").grid(row=2, column=0)
        self.neuron_entry = ttk.Entry(frame)
        self.neuron_entry.insert(0, "5")
        self.neuron_entry.grid(row=2, column=1)

        self.result_label = ttk.Label(frame, text="Total Spikes: 0")
        self.result_label.grid(row=4, column=0)

        # Button creation
        button_ctn = ttk.Button (frame, text="Generate & Plot", command=self.run_simulation)
        button_ctn.grid(row=2, column=2, pady=10)
        save_btn = ttk.Button(frame, text="Save Plot", command=self.save_plot)
        save_btn.grid(row=4, column=0, columnspan=2, pady=10)

    def run_simulation(self):
        try:
            rate = float(self.rate_entry.get())
            duration = float(self.duration_entry.get())
            neurons = int(self.neuron_entry.get())

            self.generator.rate = rate
            self.generator.duration = duration
            self.generator.neurons = neurons

            spikes = self.generator.generate_spikes()
            self.visualizer.plot_raster(spikes)

            total_spikes = sum(len(spike) for spike in spikes)
            self.result_label.config(text=f"Total Spikes: {total_spikes}")

        except ValueError:
            print("Invalid input")

    def save_plot(self):
        plt.savefig("Neuron_Spike_Raster.png")


if __name__ == "__main__":
    root = tk.Tk()
    app = AppGUI(root)
    root.mainloop()


