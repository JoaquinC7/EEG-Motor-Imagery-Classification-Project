import numpy as np
import mne
import matplotlib.pyplot as plt


data = np.load("A01T.npz", allow_pickle=True) #Allows loading of object arrays (common in EEG data)
print(data.files)

    #What's inside the EEG Files:
#s = EEG Signals (the raw continuous data)
#etyp = Event Types
#epos = Event Positions (sample indices when something occurs) it is a 1D array of integers marking the start time of an event
#edur =Event Durations
#y = Class Labels

print( "s.shapes: ", data['s'].shape)  # Shape of EEG signals
print("First 10 event positions: ", data['epos'][:10])  # First 10 event positions
#print("first 10 labels:", data['y'][:10])

for k in data.files:
    print(k, type(data[k]), np.shape(data[k]))
# prints out every file in the npz, its data type, and the shape of its data






