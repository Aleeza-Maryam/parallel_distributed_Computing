from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

# Split the communicator into two groups (0 for even, 1 for odd)
color = rank % 2
new_comm = comm.Split(color, key=rank)

# Logic to match your desired output format
if color == 0:
    # Even processes represent 'comm1'
    print(f"I am process {new_comm.rank} of {new_comm.size} in comm1")
else:
    # Odd processes represent 'comm2'
    print(f"I am process {new_comm.rank} of {new_comm.size} in comm2")