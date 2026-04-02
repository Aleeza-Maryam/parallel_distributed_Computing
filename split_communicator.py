from mpi4py import MPI

rank=MPI.COMM_WORLD.rank
size=MPI.COMM_WORLD.size
color=rank%2
comm=MPI.COMM_WORLD.Split(color,rank)
print(f"Process {rank}:color={color},rank={comm.rank},size={comm.size}")