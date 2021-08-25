#   #   # GSASII Scriptable Phase Fraction Bug Demonstrator
# Import libraries
import os,sys
sys.path.insert(0,'C:\GSASii2021\GSASII')
import GSASIIscriptable as G2sc

# Open existing project (needed because background must be specified manually for this dataset)
gpx = G2sc.G2Project('EBTL31_Fresh_LatestGSAS.gpx')

# Immediately save project so that starting file is not modified by autosave on refinement
gpx.save('EBTL31_Fresh_InitialSave.gpx')

# Assign histogram to a variable, for future use in this program
hist1 = gpx.histogram(0)

# Import phases and link them to the histogram
phase0 = gpx.add_phase(os.path.join("Bi_EntryWithCollCode64703.cif"),
                      phasename="Bi",
                      histograms=[hist1])

phase1 = gpx.add_phase(os.path.join("BiLi_EntryWithCollCode58796.cif"),
                      phasename="LiBi",
                      histograms=[hist1])

phase2 = gpx.add_phase(os.path.join("Li2Te_EntryWithCollCode60434.cif"),
                      phasename="Li2Te",
                      histograms=[hist1])

# Do Initial Refinement (keep background refining off)
gpx.save('EBTL31_Programmatic_PFs.gpx')
refdict0 = {}
gpx.do_refinements([refdict0])

# Refine Phase fractions
phase0.setPhaseEntryValue(['Histograms', 'PWDR EBTL31.fxye Bank 1', 'Scale'], [1.0, True])
phase1.setPhaseEntryValue(['Histograms', 'PWDR EBTL31.fxye Bank 1', 'Scale'], [1.0, True])
phase2.setPhaseEntryValue(['Histograms', 'PWDR EBTL31.fxye Bank 1', 'Scale'], [1.0, True])
# Constrain Sum of Phase Fractions to Equal 1.0
gpx.add_EqnConstr(1.0, ('0:0:Scale', '1:0:Scale', '2:0:Scale'))
gpx.do_refinements([refdict0])
