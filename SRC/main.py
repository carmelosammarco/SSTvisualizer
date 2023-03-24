import lib.GenMaps
import lib.CreateGIFF

infile = "TEST-DATA/August2022_MedSST.nc"

dpi = 100

fps = 5

lib.GenMaps.timesteps(input=infile, Valuedpi=dpi)
lib.CreateGIFF.makeclip(frameps=fps)