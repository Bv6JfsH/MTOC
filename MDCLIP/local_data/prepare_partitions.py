
import os
import pandas as pd
import numpy as np
from MDCLIP.local_data.constants import *

def process_rfmid_other():
    template_diseases = {'DR': 'diabetic retinopathy', 'ARMD': 'age-related macular degeneration',
                         'MH': 'media haze', 'DN': 'drusens', 'MYA': 'myopia', 'BRVO': 'branch retinal vein occlusion',
                         'TSLN': 'tessellation', 'ERM': 'epiretinal membrane', 'LS': 'laser scar',
                         'MS': 'macular scar', 'CSR': 'central serous retinopathy', 'ODC': 'optic disc cupping',
                         'CRVO': 'central retinal vein occlusion', 'TV': 'tortuous vessels', 'AH': 'asteroid hyalosis',
                         'ODP': 'optic disc pallor', 'ODE': 'optic disc edema', 'ST': 'optociliary shunt vessels',
                         'AION': 'anterior ischemic optic neuropathy', 'PT': 'parafoveal telangiectasia',
                         'RT': 'retinal traction', 'RS': 'retinitis', 'CRS': 'chorioretinitis', 'EDN': 'exudation',
                         'RPEC': 'retinal pigment epithelium changes', 'MHL': 'macular hole',
                         'RP': 'retinitis pigmentosa', 'CWS': 'cotton wool spots', 'CB': 'colobomas',
                         'ODPM': 'optic disc pit maculopathy', 'PRH': 'preretinal haemorrhage',
                         'MNF': 'myelinated nerve fibers', 'HR': 'haemorrhagic retinopathy',
                         'CRAO': 'central retinal artery occlusion', 'TD': 'tilted disc',
                         'CME': 'cystoid macular edema', 'PTCR': 'post traumatic choroidal rupture',
                         'CF': 'choroidal folds', 'VH': 'vitreous haemorrhage', 'MCA': 'macroaneurysm',
                         'VS': 'vasculitis', 'BRAO': 'branch retinal artery occlusion', 'PLQ': 'plaque',
                         'HPED': 'haemorrhagic pigment epithelial detachment', 'CL': 'collaterals'}

    partitions = ["Training", "Validation", "Testing"]
    for iPartition in partitions:

        data = []
        dataframe = pd.read_csv(PATH_DATASETS+'RFMID/'+iPartition+'_Set/RFMiD_'+iPartition+'_Labels.csv')
        for iFile in range(dataframe.shape[0]):
            image_path = 'RFMID/'+iPartition+'_Set/'+iPartition+'/' + str(dataframe["ID"][iFile]) + ".png"
            categories, atributes = [], []
            if dataframe["Disease_Risk"][iFile] == 1:
                categories.append("a disease")
                ids = np.argwhere(np.array(dataframe)[iFile, 2:])

                for i in list(ids):
                    if(i < 27):
                        dis_abreviation = dataframe.columns.to_list()[i[0] + 2]
                        categories.append(template_diseases[dis_abreviation])
                    if (i >= 27):
                        if("other" not in categories):
                            categories.append("other")

            else:
                categories.append("normal")


            if os.path.isfile(PATH_DATASETS + image_path):
                data.append({"image": image_path,
                             "atributes": atributes,
                             "categories": categories})
        df_out = pd.DataFrame(data)
        df_out.to_csv(PATH_DATAFRAME_PRETRAIN + "RFMid_" + iPartition+"_other" + ".csv")

if __name__ == "__main__":
    process_rfmid_other()