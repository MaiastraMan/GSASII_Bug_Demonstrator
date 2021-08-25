#   #   # GSASII Scriptable Preferred Orientation Demonstrator
# Import libraries
import os,sys
sys.path.insert(0,'C:\GSASii2021\GSASII')
import GSASIIscriptable as G2sc

# Open existing project (needed because background must be specified manually for this dataset)
gpx = G2sc.G2Project('Bi2Se3_ElecScrape_LatestGSAS.gpx')

# Immediately save project so that starting file is not modified by autosave on refinement
gpx.save('Bi2Se3_ElecScrape_Diff_InitialSave.gpx')

# Assign histogram to a variable, for future use in this program
hist1 = gpx.histogram(0)

# Import phases and link them to the histogram
phase0 = gpx.add_phase(os.path.join("Bi2Se3_EntryWithCollCode165226.cif"),
                       phasename="Bi2Se3", histograms=[hist1])

# Refine preferred orientation
gpx.save('Bi2Se3_ElecScrape_Diff_PO.gpx')
phase0.setPhaseEntryValue(['Histograms', 'PWDR Bi2Se3_electrodeScraped.xrdml Scan 1', 'Pref.Ori.'],
                          ['MD', 1.0, True, [0, 0, 1], 0, {}, [''], 0.1])
gpx.do_refinements([{}])