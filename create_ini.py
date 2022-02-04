import numpy as np
#program to write the configuration file for hazel2 inversion code
#
wavfile = '\'wavelength_2bin_trim.txt\''
#data = '\'/home/raya0718/hazel2/examples/grisinv/dataset/set00.h5\''
phrefmod = '\'f2binphotosphere.h5\''
chrefmod = '\'f2binchromosphere.h5\''
parefmod = '\'/home/raya0718/hazel2/examples/telluric/model_telluric.1d\''
strefmod = '\'/home/raya0718/hazel2/examples/straylight/model_stray.1d\''
for i in range(0,6):
	filin = 'conf/'+'conf_zmn_1c_'+'{:02d}'.format(i)+'.ini'
	outputfile = 'outputs/comp1/zmn_1c_'+'{:02d}'.format(i)+'.h5'
	data = '\'observations/spatially_binned_2pix.h5\''
	file = open(filin,'w') 
	 
	file.write('# Hazel configuration File\n \n') 
	file.write('[Working mode]\n') 
	file.write('Action = \'inversion\' \n')
	file.write('Output file = '+outputfile+'\n')
	file.write('Number of cycles = 3 \n')
	file.write('\n')

	#spectral region 
	file.write('[Spectral regions]\n')
	file.write('\t[[Region 1]]\n ')
	file.write('\tName = spec1\n')
	file.write('\t#Wavelength = 10826, 10833, 150\n')
	file.write('\tTopology = ph1 -> ch1 -> te1 #-> st1\n')
	file.write('\t#Stokes weights = 1.0, 1.0, 1.0, 1.0\n')

	file.write('\tWavelength file = '+wavfile+'\n')
	file.write('\t#Wavelength weight file = \'observations/gris_10830.weights\'\n')
	file.write('\tObservations file = '+data+'\n ')
	file.write('\tMask file = \'/scratch/rahul/grisinv/newtest/mask_zmn2.h5\'\n ')
	file.write('\tWeights Stokes I = 1.0, 0.1, 0.1, 0.0\n ')
	file.write('\tWeights Stokes Q = 10.0, 100.0, 100.0, 0.0\n ')
	file.write('\tWeights Stokes U = 10.0, 100.0, 100.0, 0.0\n ')
	file.write('\tWeights Stokes V = 10.0, 10.0, 10.0, 0.0\n ')
	file.write('\n')

	#Add atmospheres
	file.write('[Atmospheres]\n')
	file.write('\n')
	file.write('\t[[Photosphere 1]]\n')
	file.write('\tName = ph1\n')
	file.write('\tReference atmospheric model = '+phrefmod+'\n')
	file.write('\tSpectral region = spec1\n')
	file.write('\tWavelength = 10823, 10833\n')
	file.write('\tSpectral lines = 300,\n')
	file.write('\n')

	file.write('\t\t[[[Ranges]]]\n')
	file.write('\t\tT      = 0.0, 10000.0\n')
	file.write('\t\tvmic   = 0.0, 3.0\n')
	file.write('\t\tv      = -10.0, 10.0\n')
	file.write('\t\tBx     = -2000.0, 2000.0\n')
	file.write('\t\tBy     = -2000.0, 2000.0\n')
	file.write('\t\tBz     = -2000.0, 2000.0\n')
	file.write('\t\tff     = 0.0, 1.0001\n')
	file.write('\n')

	file.write('\t\t[[[Nodes]]]\n')
	file.write('\t\tT      = 2, 3, 5, 5\n')
	file.write('\t\tvmic   = 1, 2, 1, 1\n')
	file.write('\t\tv      = 1, 2, 1, 1\n')
	file.write('\t\tBx     = 1, 2, 1, 1\n')
	file.write('\t\tBy     = 1, 2, 1, 1\n')
	file.write('\t\tBz     = 1, 2, 1, 1\n')
	file.write('\t\tff     = 0, 0, 0, 0\n')
	file.write('\n')

	file.write('\t\t[[Regularization]]\n')
	file.write('\t\tT      = None\n')
	file.write('\t\tvmic   = None\n')
	file.write('\t\tv      = None\n')
	file.write('\t\tBx     = None\n')
	file.write('\t\tBy     = None\n')
	file.write('\t\tBz     = None\n')
	file.write('\n')

#chromosphere 1
	file.write('\t[[Chromosphere 1]]\n')
	file.write('\tName = ch1\n')
	file.write('\t Spectral region = spec1\n')
	file.write('\tHeight = 3.0\n')
	file.write('\tLine = 10830\n')
	file.write('\tWavelength = 10822, 10833\n')
	file.write('\tReference atmospheric model = '+chrefmod+'\n')
	file.write('\n')

	file.write('\t\t[[[Ranges]]]\n')
	cbx = 900+40*i
	vel = 40 + i*8
	file.write('\t\tBx     = -'+str(cbx)+','+str(cbx)+'\n')
	file.write('\t\tBy     = -'+str(cbx)+','+str(cbx)+'\n')
	file.write('\t\tBz     = -'+str(cbx)+','+str(cbx)+'\n')
	file.write('\t\ttau    = 0.1, 4.0\n')
	file.write('\t\tv      = -'+str(vel)+','+str(vel)+'\n')
	file.write('\t\tdeltav = 3.0, 15.0\n')
	file.write('\t\tbeta   = 1.0, 2.0\n')
	file.write('\t\ta      = 0, 0.1\n')
	file.write('\t\tff     = 0.0, 1.0\n')
	file.write('\n')

	file.write('\t\t[[[Nodes]]]\n')

	file.write('\t\tBx     = 1, 1, 1, 1\n')
	file.write('\t\tBy     = 1, 1, 1, 1\n')
	file.write('\t\tBz     = 1, 1, 1, 1\n')
	file.write('\t\ttau    = 1, 0, 0, 0\n')
	file.write('\t\tvmic   = 1, 0, 1, 1\n')
	file.write('\t\tv      = 1, 1, 0, 0\n')
	file.write('\t\tdeltav = 1, 0, 0, 0\n')
	file.write('\t\tbeta   = 0, 0, 0, 0\n')
	file.write('\t\ta      = 1, 0, 0, 0\n')
	file.write('\t\tff     = 0, 0, 0, 0\n')
	file.write('\n')

#chromosphere 2
	file.write('\t[[Chromosphere 2]]\n')
	file.write('\tName = ch2\n')
	file.write('\t Spectral region = spec1\n')
	file.write('\tHeight = 3.0\n')
	file.write('\tLine = 10830\n')
	file.write('\tWavelength = 10823, 10833\n')
	file.write('\tReference atmospheric model = '+chrefmod+'\n')
	file.write('\n')

	file.write('\t\t[[[Ranges]]]\n')

	file.write('\t\tBx     = -1000.0, 1000.0\n')
	file.write('\t\tBy     = -1000.0, 1000.0\n')
	file.write('\t\tBz     = -1000.0, 1000.0\n')
	file.write('\t\ttau    = 0.1, 4.0\n')
	file.write('\t\tv      = -10.0, 10.0\n')
	file.write('\t\tdeltav = 3.0, 15.0\n')
	file.write('\t\tbeta   = 1.0, 2.0\n')
	file.write('\t\ta      = 0, 0.1\n')
	file.write('\t\tff     = 0.0, 1.0\n')
	file.write('\n')

	file.write('\t\t[[[Nodes]]]\n')

	file.write('\t\tBx     = 1, 1, 1, 1\n')
	file.write('\t\tBy     = 1, 1, 1, 1\n')
	file.write('\t\tBz     = 1, 1, 1, 1\n')
	file.write('\t\ttau    = 1, 0, 0, 0\n')
	file.write('\t\tvmic   = 1, 0, 1, 1\n')
	file.write('\t\tv      = 1, 1, 0, 0\n')
	file.write('\t\tdeltav = 1, 0, 0, 0\n')
	file.write('\t\tbeta   = 0, 0, 0, 0\n')
	file.write('\t\ta      = 1, 0, 0, 0\n')
	file.write('\t\tff     = 0, 0, 0, 0\n')
	file.write('\n')

	file.write('\t[[Parametric 1]]\n')
	file.write('\tName = te1\n')
	file.write('\tSpectral region = spec1\n')
	file.write('\tWavelength = 10823, 10833\n')
	file.write('\tReference atmospheric model = '+parefmod+'\n')
	file.write('\tType = Gaussian\n')
	file.write('\n')

	file.write('\t\t[[[Ranges]]]\n')
	file.write('\t\tLambda0 = 10831, 10833\n')
	file.write('\t\tSigma = 0.1, 0.7\n')
	file.write('\t\tDepth = 0.2, 0.8\n')
	file.write('\t\ta = 0.0, 1.2\n')
	file.write('\t\tff = 0.0, 1.0\n') 
	file.write('\n')

	file.write('\t\t[[[Nodes]]]\n')
	file.write('\t\tLambda0 = 1, 1, 0, 0\n\t\tSigma = 1, 1, 0, 0\n\t\tDepth = 1, 1, 0, 0\n\t\ta = 1, 0, 0, 0\n\t\tff = 0, 0, 0, 0\n')
	file.write('\n')

	file.write('\t[[Straylight 1]]\n')
	file.write('\tName = st1\n\tSpectral region = spec1\n\tWavelength = 10824, 10833\n\tReference atmospheric model = '+strefmod+'\n')
	file.write('\n')

	file.write('\t\t[[[Ranges]]]\n\t\tv = -1.0, 1.0\n\t\tff = 0.0, 1.0\n')
	file.write('\n')
	file.write('\t\t[[[Nodes]]]\n\t\tv = 0, 0, 0, 0\n\t\tff = 0, 0, 0, 0\n')

	print(filin)
	file.close() 
