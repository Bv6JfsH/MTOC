

labels = {"normal": ["normal"],
          "epiretinal membrane": ["epiretinal membrane"],
          "macular edema": ["macular edema"],
          "diabetic retinopathy": ["diabetic retinopathy"],
          "non-exudative age related macular degeneration": ["non-exudative age related macular degeneration"],
          "exudative age related macular degeneration": ["exudative age related macular degeneration"],
          "degenerative myopia": ["degenerative myopia with degenerative myopia"]
          }

description1 = {"normal": ["healthy", "no findings", "no lesion signs", "no glaucoma", "no retinopathy"],
                "epiretinal membrane": ["epiretinal membrane with greyish semi-translucent avascular membrane",
                                        "epiretinal membrane with a sheen or abnormal reflectivity of the macular surface",
                                        "epiretinal membrane with small translucent wrinkles or folds on the surface of the retina",
                                        "epiretinal membrane with retinal thickening in the macular area",
                                        "epiretinal membrane with macular gold foil-like reflection",
                                        "epiretinal membrane with blunting of the foveal contour or wrinkling on the retinal surface from membrane contracture"],
                "macular edema": ["macular edema with cystoid spaces",
                                  "macular edema with distortion of the retinal architecture",
                                  "macular edema with yellowish deposits in the macula",
                                  "macular edema with a blurring of the foveal reflex",
                                  "macular edema with disappearance of reflection in the macular",
                                  "macular edema with swelling and thickening of the macula"],
                "diabetic retinopathy": ["diabetic retinopathy with retinal hemorrhages",
                                         "diabetic retinopathy with cotton wool spots",
                                         "diabetic retinopathy with hard exudates",
                                         "diabetic retinopathy with microaneurysms",
                                         "diabetic retinopathy with venous beading"],
                "non-exudative age related macular degeneration": [
                    "non-exudative age related macular degeneration with hard and soft drusen",
                    "non-exudative age related macular degeneration with pigment epithelial atrophy and proliferation",
                    "non-exudative age related macular degeneration with pigmentary disturbances",
                    "non-exudative age related macular degeneration with map-like atrophy of the retina and choroid"],
                "exudative age related macular degeneration": [
                    "exudative age related macular degeneration with subretinal fluid",
                    "exudative age related macular degeneration with serous or hemorrhagic pigment epithelial detachment",
                    "exudative age related macular degeneration with choroidal neovascularization",
                    "exudative age related macular degeneration with retinal edema",
                    "exudative age related macular degeneration with hemorrhage",
                    "exudative age related macular degeneration with exudation",
                    "exudative age related macular degeneration with fibrotic scarring",
                    "exudative age related macular degeneration with disciform degeneration"],
                "degenerative myopia": ["degenerative myopia with pathological myopia",
                                        "degenerative myopia with pathologic myopia",
                                        "degenerative myopia with atrophy of the retina and choroid",
                                        "degenerative myopia with retinal fissures",
                                        "degenerative myopia with vitreomacular traction",
                                        "degenerative myopia with detachment of the retinal neurosensory layer",
                                        "degenerative myopia with macular hole",
                                        "degenerative myopia with macular hemorrhage"],
                }

description0 = {"normal": ["healthy", "no findings", "no lesion signs", "no glaucoma", "no retinopathy"],
                "epiretinal membrane": ["greyish semi-translucent avascular membrane",
                                        "a sheen or abnormal reflectivity of the macular surface",
                                        "small translucent wrinkles or folds on the surface of the retina",
                                        "retinal thickening in the macular area", "macular gold foil-like reflection",
                                        "blunting of the foveal contour or wrinkling on the retinal surface from membrane contracture"],
                "macular edema": ["cystoid spaces", "distortion of the retinal architecture",
                                  "yellowish deposits in the macula", "a blurring of the foveal reflex",
                                  "disappearance of reflection in the macular",
                                  "swelling and thickening of the macula"],
                "diabetic retinopathy": ["retinal hemorrhages", "cotton wool spots", "hard exudates", "microaneurysms",
                                         "venous beading"],
                "non-exudative age related macular degeneration": ["hard and soft drusen",
                                                                   "pigment epithelial atrophy and proliferation",
                                                                   "pigmentary disturbances",
                                                                   "map-like atrophy of the retina and choroid"],
                "exudative age related macular degeneration": ["subretinal fluid",
                                                               "serous or hemorrhagic pigment epithelial detachment",
                                                               "choroidal neovascularization", "retinal edema",
                                                               "hemorrhage", "exudation", "fibrotic scarring",
                                                               "disciform degeneration"],
                "degenerative myopia": ["pathological myopia", "pathologic myopia", "atrophy of the retina and choroid",
                                        "retinal fissures", "vitreomacular traction",
                                        "detachment of the retinal neurosensory layer", "macular hole",
                                        "macular hemorrhage"],
                }

description_focus = {
"a disease": ["a disease with no healthy", "a disease with lesions", "a disease with abnormal","a disease with blurring sings"],
    "health": ["health with normal",
               "health with no findings ",
               "health with normal appearance ",
               "health with normal with",
               "health with clear macula"],


    "normal": ["normal with healthy",
               "normal with no findings",
               "normal with no glaucoma",
               "normal with no retinopathys",
               "normal with no lesion signs",
               "normal with clear macula"],

    "epiretinal membrane": ["epiretinal membrane with surface membrane",
                            "epiretinal membrane with color changes",
                            "epiretinal membrane with light reflection changes",
                            "epiretinal membrane with vascular distortion",
                            "epiretinal membrane with changes in the macular area"],

    "macular edema": ["macular edema with macular thickening ",
                      "macular edema with vascular changes",
                      "macular edema with fluid accumulation",
                      "macular edema with color changes",
                      ],

    "diabetic retinopathy": ["diabetic retinopathy with retinal hemorrhages",
                             "diabetic retinopathy with cotton wool spots",
                             "diabetic retinopathy with hard exudates",
                             "diabetic retinopathy with microaneurysms",
                             "diabetic retinopathy with venous beading",
                             "diabetic retinopathy with ischemic areas",
                             "diabetic retinopathy with neovascularization",

                             ],

    "non-exudative age related macular degeneration": [
        "non-exudative age related macular degeneration with hard and soft drusen",
        "non-exudative age related macular degeneration with pigment epithelial atrophy and proliferation",
        "non-exudative age related macular degeneration with pigmentary disturbances",
        "non-exudative age related macular degeneration with geographic atrophy",
        "non-exudative age related macular degeneration with reticular pseudodrusen",
        "non-exudative age related macular degeneration with map-like atrophy of the retina and choroid"],

    "exudative age related macular degeneration": [
        "exudative age related macular degeneration with subretinal fluid",
        "exudative age related macular degeneration with serous or hemorrhagic pigment epithelial detachment",
        "exudative age related macular degeneration with choroidal neovascularization",
        "exudative age related macular degeneration with retinal edema",
        "exudative age related macular degeneration with hemorrhage",
        "exudative age related macular degeneration with exudation",
        "exudative age related macular degeneration with fibrotic scarring",
        "exudative age related macular degeneration with disciform degeneration"],

    "degenerative myopia": ["degenerative myopia with myopic maculopathy",
                            "degenerative myopia with choroidal thinning",
                            "degenerative myopia with staphyloma formation",
                            "degenerative myopia with optic disc changes",
                            "degenerative myopia with foveal Changes",
                            "degenerative myopia with macular holes and tears",
                            "degenerative myopia with macular hemorrhage"],










    "age-related macular degeneration": ["age-related macular degeneration with drusen formation",
                                         "age-related macular degeneration with macular changes",
                                         "age-related macular degeneration with geographic atrophy",
                                         "age-related macular degeneration with choroidal neovascularization",
                                         "age-related macular degeneration with pigmentary changes",
                                         "age-related macular degeneration with macular edema",
                                         "age-related macular degeneration with retinal pigment epithelium",
                                         "age-related macular degeneration with loss of central vision"],

    'media haze': ["media haze with blurred appearance",
                   "media haze with retinal structure examination",
                   "media haze with transparency assessment",
                   "media haze with iris examination",
                   "media haze with observation of light scattering effects",
                   "media haze with image quality assessment",
                   "media haze with difficulty in identifying fundus details",
                   "media haze with assessment of decreased visibility",
                   "media haze with understanding potential causes",
                   "media haze with vision impairment"],

    "drusens" :["drusens with identification",
                "drusens with size assessment",
                "drusens with distribution examination",
                "drusens with border characteristics",
                "drusens with color analysis",
                "drusens with proximity to macula or optic nerve",
                "drusens with fundus autofluorescence examination",
                "drusens with optical coherence tomography confirmation",
                "drusens with patient medical history",
                "drusens with comprehensive eye examination"],















    "myopia": [
"myopia with optic disc characteristics with a tilted or elongated appearance indicating axial elongation",
"myopia with retinal blood vessel features with increased tortuosity or abnormal courses",
"myopia with macular observations with myopic macular degeneration or presence of a posterior staphyloma",
"myopia with peripapillary atrophy with crescent-shaped chorioretinal atrophy around the optic disc",
"myopia with fundus tessellation with a mottled appearance in the periphery",
"myopia with choroidal thinning signs with thinning of the choroid, especially in the posterior pole",
"myopia with foveal changes manifestation with myopic changes like lacquer cracks or myopic foveoschisis",
"myopia with axial length estimation with indirect estimation of increased axial length by assessing the distance between the optic disc and fovea"],

"branch retinal vein occlusion": ["branch retinal vein occlusion with retinal hemorrhages with presence of flame-shaped or dot/blot hemorrhages in the affected quadrant of the retina",
"branch retinal vein occlusion with cotton-wool spots with identification of soft, fluffy, white lesions indicating ischemic areas",
"branch retinal vein occlusion with dilated and tortuous veins with observation of enlarged and twisted retinal veins in the affected region",
"branch retinal vein occlusion with macular edema with detection of fluid accumulation in the macular area, leading to swelling",
"branch retinal vein occlusion with hard exudates with visualization of yellowish deposits around the macula, suggesting lipid leakage",
"branch retinal vein occlusion with capillary non-perfusion, recognition of areas with reduced or absent blood flow, indicative of ischemia",
"branch retinal vein occlusion with optic disc swelling, presence of disc edema, often associated with severe cases or ischemic complications",
"branch retinal vein occlusion with venous sheathing, noting the thickening and sclerosis of retinal veins in the affected quadrant",
"branch retinal vein occlusion with collateral vessel formation, identification of new vessels as a response to the occluded vein, especially at the periphery",
"branch retinal vein occlusion with macular ischemia, assessment of decreased perfusion in the macular area, contributing to visual impairment"],



"tessellation": [
"tessellation with geographic atrophy: identification of well-defined areas of retinal pigment epithelium (RPE) loss, leading to a map-like appearance on the fundus",
"tessellation with drusen: presence of small, yellowish deposits between the RPE and Bruchs membrane, indicating early stages of age-related macular degeneration",
"tessellation with pigmentary changes: observation of alterations in retinal pigmentation, including hypo- or hyperpigmented areas, contributing to the tessellated pattern",
"tessellation with choroidal neovascularization (CNV): detection of abnormal blood vessel growth beneath the retina, often associated with exudative or wet macular degeneration",
"tessellation with reticular pseudodrusen: recognition of yellowish subretinal deposits forming a network pattern, distinct from conventional drusen",
"tessellation with outer retinal tubulations: visualization of tubular structures in the outer retina, indicative of degenerative changes in photoreceptor cells",
"tessellation with retinal thinning: measurement of reduced retinal thickness, especially in the macular area, contributing to the tessellated appearance",
"tessellation with ellipsoid zone disruption: identification of disruptions in the ellipsoid zone on optical coherence tomography, reflecting structural damage in the retina",
"tessellation with subretinal fluid: presence of fluid accumulation beneath the retina, often associated with macular diseases and contributing to the tessellation pattern",
"tessellation with visual field defects: correlation of the tessellated fundus pattern with specific visual field abnormalities, aiding in the overall diagnostic assessment"],

"laser scar": [
"laser scar with round or oval, yellowish-white with variable black pigment centrally",
"laser scar with 50 to 200 micron diameter lesions"
],







# "laser scar with hyperpigmentation: observation of darker pigmentation within the scarred region, indicative of altered melanin content",
# "laser scar with tissue atrophy: recognition of thinning and loss of retinal tissue in the scarred area, contributing to the overall structural changes",
# "laser scar with vascular changes: noting alterations in blood vessel patterns or disruption within the scar, reflecting the impact on retinal vasculature",
# "laser scar with loss of retinal architecture: visualization of disruptions in the normal retinal layers and structures, especially in the scarred region",
# "laser scar with choroidal changes: detection of modifications in the choroid beneath the scar, potentially affecting blood supply and tissue support",
# "laser scar with scarring-related distortion: observation of distortion in the surrounding retinal anatomy due to the presence of the laser scar",
# "laser scar with absence of normal fluorescence: using fundus autofluorescence imaging to identify areas where the laser scar shows reduced or altered autofluorescence",
# "laser scar with visual field defects: correlation of the laser scar location with specific visual field abnormalities, contributing to the diagnostic evaluation"



"macular scar" :["macular scar with central atrophy: identification of a region in the macula exhibiting significant tissue loss and retinal thinning",
"macular scar with pigment alterations: observation of changes in pigmentation, such as hypo- or hyperpigmented areas within the scarred macula",
"macular scar with disrupted retinal layers: visualization of irregularities or interruptions in the normal layering of the retina, indicating structural damage",
"macular scar with surrounding fibrosis: noting the presence of fibrotic tissue around the macular scar, contributing to the overall pathology",
"macular scar with photoreceptor loss: detection of a decrease in the number of photoreceptor cells in the scarred macular region",
"macular scar with distortion of foveal architecture: recognizing alterations in the central foveal structure due to the presence of the scar",
"macular scar with scarring-related vascular changes: identification of modifications in retinal blood vessels associated with the scarred macula",
"macular scar with fluorescein angiography abnormalities: using angiography to reveal any abnormal blood flow patterns or leakage around the macular scar",
"macular scar with disrupted ellipsoid zone on OCT: visualization of interruptions in the ellipsoid zone on optical coherence tomography, indicative of structural damage",
"macular scar with visual acuity changes: correlation of the macular scar location and size with documented changes in visual acuity, providing crucial diagnostic insights"],



"central serous retinopathy":["central serous retinopathy with serous retinal detachment: identification of localized detachment of the neurosensory retina, typically in the macular region",
"central serous retinopathy with macular edema: detection of fluid accumulation in the macula, leading to swelling and potential distortion of the central vision",
"central serous retinopathy with pigment epithelial changes: observation of alterations in the retinal pigment epithelium (RPE) layer, often manifesting as RPE detachments or irregularities",
"central serous retinopathy with choroidal hyperpermeability: noting increased permeability of choroidal vessels, leading to subretinal fluid accumulation",
"central serous retinopathy with focal leakage on fluorescein angiography: visualization of dye leakage from choroidal vessels into the subretinal space, indicating active disease",
"central serous retinopathy with bullous retinal elevation: recognition of large, blister-like elevations in the retina due to accumulated subretinal fluid",
"central serous retinopathy with RPE window defects: identification of areas where the RPE appears window-like or atrophic, allowing visualization of choroidal vasculature",
"central serous retinopathy with mottled hyperautofluorescence: using fundus autofluorescence to reveal irregular areas of increased and decreased autofluorescence within the affected region",
"central serous retinopathy with decreased central macular thickness on OCT: measurement of reduced thickness in the central macula due to subretinal fluid accumulation",
"central serous retinopathy with symptoms of metamorphopsia or micropsia: consideration of patient-reported visual distortions, such as straight lines appearing wavy or objects seeming smaller than they are"],

"optic disc cupping":["optic disc cupping with increased cup-to-disc ratio: assessment of the ratio between the size of the cup (central depression) and the overall optic disc diameter, with an enlarged cup",
"optic disc cupping with thinning of neuroretinal rim: observation of a decrease in the thickness of the neuroretinal rim, the tissue surrounding the optic cup",
"optic disc cupping with notching: identification of a distinct notch or depression in the rim of the optic disc, often associated with glaucomatous damage",
"optic disc cupping with asymmetry between the two eyes: noting a significant difference in cupping appearance between the optic discs of the two eyes",
"optic disc cupping with pallor of the neuroretinal rim: visualization of a pale or whitened appearance in the neuroretinal rim due to reduced nerve fiber layer thickness",
"optic disc cupping with vascular changes: recognition of alterations in the pattern and appearance of blood vessels on the optic disc surface",
"optic disc cupping with peripapillary atrophy: presence of atrophic changes in the tissue surrounding the optic disc, often accompanied by pigmentary changes",
"optic disc cupping with glaucomatous visual field defects: correlation of the cupping findings with specific visual field abnormalities characteristic of glaucoma",
"optic disc cupping with disc hemorrhages: identification of small hemorrhages on or around the optic disc, which may indicate glaucomatous damage",
"optic disc cupping with progressive changes over time: comparison of current fundus findings with previous images to assess the progression of optic disc cupping and potential glaucomatous damage"],


"central retinal vein occlusion": ["central retinal vein occlusion with retinal hemorrhages: presence of flame-shaped or dot/blot hemorrhages scattered throughout the retina, especially in the posterior pole",
"central retinal vein occlusion with cotton-wool spots: identification of soft, fluffy, white lesions indicating areas of retinal ischemia",
"central retinal vein occlusion with macular edema: detection of fluid accumulation in the macular region, leading to central vision impairment",
"central retinal vein occlusion with dilated and tortuous veins: observation of enlarged and twisted retinal veins, particularly in the posterior pole",
"central retinal vein occlusion with optic disc edema: presence of swelling at the optic disc, often referred to as disc edema or papilledema",
"central retinal vein occlusion with widespread retinal ischemia: recognition of extensive areas of reduced blood flow and perfusion in the retina",
"central retinal vein occlusion with venous congestion: noting congestion and engorgement of retinal veins due to impaired blood outflow",
"central retinal vein occlusion with cherry-red spot on macula: identification of a cherry-red spot at the fovea, contrasting against the ischemic, pale retina",
"central retinal vein occlusion with collateral vessel formation: visualization of new vessels as a compensatory response to the occluded vein, especially in the periphery",
"central retinal vein occlusion with visual field defects: correlation of fundus findings with specific visual field abnormalities, contributing to the overall diagnostic assessment"],


"tortuous vessels":["tortuous vessels with identification of abnormality: examine the fundus image for the presence of blood vessels displaying abnormal winding or twisting, indicating tortuosity",
"tortuous vessels with distribution pattern: assess the distribution pattern of the tortuous vessels, considering whether they are localized to a specific area or involve a more widespread portion of the retina",
"tortuous vessels with comparison to normal vessels: compare the suspected tortuous vessels with adjacent normal vessels to highlight the extent of deviation from the typical vascular architecture",
"tortuous vessels with vessel caliber changes: look for changes in the caliber of the tortuous vessels, as abnormal dilations or constrictions may provide additional diagnostic information",
"tortuous vessels with impact on surrounding structures: evaluate whether the tortuous vessels exert any pressure or have an impact on neighboring structures, such as the optic nerve or macula"],


"asteroid hyalosis":["asteroid hyalosis with numerous small, reflective, yellow-white opacities in the vitreous humor: presence of multiple tiny, reflective opacities distributed throughout the vitreous humor",
"asteroid hyalosis with dense, spherical bodies resembling stellate or star-like patterns: observation of compact, spherical opacities with a characteristic star-like appearance",
"asteroid hyalosis with opacities casting shadows on the retina: identification of shadows cast by the opacities on the underlying retina, often visible during fundus examination",
"asteroid hyalosis with opacities exhibiting minimal impact on visual acuity: typically, these opacities have a limited effect on visual function, as they are situated in the vitreous rather than directly on the retina"],


# "optic disc pallor":["optic disc pallor with thinning and paleness of the optic disc rim: thinning and a pale appearance of the rim surrounding the optic disc",
# "optic disc pallor with loss of normal pink coloration: absence of the usual pink hue typically seen in a healthy optic disc",
# "optic disc pallor with sharp demarcation between the pale optic disc and surrounding retina: clear distinction between the pale optic disc and the adjacent retinal tissue",
# "optic disc pallor with decreased visibility of blood vessels on the optic disc: reduced prominence and visibility of blood vessels within the optic disc due to the pallor",
# "optic disc pallor with associated optic nerve atrophy: often indicative of optic nerve atrophy, where the nerve fibers become damaged, leading to a reduction in disc color",
# "optic disc pallor with involvement of one or both optic discs: the condition can affect either one or both optic discs, and the extent of pallor may vary"],


"optic disc pallor":["optic disc pallor with pale yellow discoloration that can be segmental or generalized on optic disc"],

"optic disc edema":["optic disc edema with blurring of the optic disc margins: presence of indistinct or blurred margins of the optic disc due to swelling",
"optic disc edema with hyperemia or engorgement of blood vessels on the optic disc: increased visibility and dilation of blood vessels on the surface of the optic disc",
"optic disc edema with elevation of the optic disc surface: a raised appearance of the optic disc, indicating fluid accumulation and swelling",
"optic disc edema with loss of physiological cupping: diminished or absent cupping, the normal depression at the center of the optic disc, due to increased intrapapillary pressure",
"optic disc edema with peripapillary hemorrhages: presence of hemorrhages in the surrounding region of the optic disc, often a sign of increased pressure within the optic nerve head",
"optic disc edema with associated cotton-wool spots: presence of cotton-wool spots in the vicinity of the optic disc, indicating localized retinal ischemia associated with the edema"],



"optociliary shunt vessels": [
"optociliary shunt vessels with collateral vessels connecting the choroidal and the retinal vasculature",
"optociliary shunt vessels with collateral vessels of large caliber and lack of leakage",
"optociliary shunt vessels with tortuous vascular loops that start and end on the disc",
"optociliary shunt vessels with tortuous red small lines that start and end on the disc","collateral vessels connecting the choroidal and the retinal vasculature",
                         "collateral vessels of large caliber and lack of leakage"

                              ],



"anterior ischemic optic neuropathy":[
"anterior ischemic optic neuropathy with swelling optic disc with the edema can be either segmental or diffuse",
"anterior ischemic optic neuropathy with pale or edematous appearance of the optic nerve head with the optic disc may appear pale or edematous due to compromised blood supply",
"anterior ischemic optic neuropathy with optic disc hyperemia with increased redness or hyperemia of the optic disc, indicating possible inflammation or ischemia",
"anterior ischemic optic neuropathy with accompanying hemorrhages with linear or flame-shaped red bleeding around the optic disc",
"anterior ischemic optic neuropathy with swollen, pale or anamolous optic discc with blurring yellow optic discc"],


# "parafoveal telangiectasia":["parafoveal telangiectasia with telangiectatic vessels: identification of abnormal, dilated blood vessels near the fovea, often appearing as small, tortuous vessels",
# "parafoveal telangiectasia with right-angled venules: presence of venules that exhibit a right-angled turn, a characteristic feature of parafoveal telangiectasia",
# "parafoveal telangiectasia with retinal crystalline deposits: observation of crystalline-like deposits within the retina, a distinctive finding associated with this condition",
# "parafoveal telangiectasia with absence of macular edema: unlike some other retinal conditions, parafoveal telangiectasia typically presents without significant macular edema",
# "parafoveal telangiectasia with mild-to-moderate retinal atrophy: progressive thinning of the retina, particularly in the parafoveal region, indicating the stage of the disease",
# "parafoveal telangiectasia with reduced capillary density: a decrease in the density of capillaries in the affected area, contributing to altered blood flow patterns",
# "parafoveal telangiectasia with pigmentary changes: alterations in retinal pigmentation, including pigment clumping or migration, as the disease progresses",
# "parafoveal telangiectasia with subtle fluorescein angiography findings: the use of fluorescein angiography may reveal subtle abnormalities in the parafoveal region, aiding in the diagnosis of parafoveal telangiectasia"],


"parafoveal telangiectasia":[
"parafoveal telangiectasia with yellow, lipid-rich exudation or parafoveal graying or abnormalities from fovea",
"parafoveal telangiectasia with gray or yellow abnormalities in fovea",
"parafoveal telangiectasia with gray or yellow abnormalities in macula"
],



"retinal traction":[
"retinal traction with yellow line around",
"retinal traction with blurring yellow line",
"retinal traction with with retinal folds with the appearance of folds, manifesting as wrinkled or undulating patterns on the retina, observable on the fundus image",
"retinal traction with with disapperance of retinal vessels with distort the surrounding retinal blood vessels",
"retinal traction with retinal traction may result in the rupture of blood vessels within the vitreous, leading to vitreous hemorrhage with hemorrhages within the red spot",
"retinal traction with retinal tears with irregular defects and signs of retinal detachment",
"retinal traction with retinal detachment with signs of retinal separation, characterized by wrinkling, undulating changes, and possible holes and vitreous hemorrhage"],




# "retinitis":["retinitis with white, fluffy exudates: presence of white, fluffy exudates on the retina, indicative of inflammatory changes associated with retinitis",
# "retinitis with retinal hemorrhages: identification of hemorrhages on the retina, suggesting vascular involvement and inflammation",
# "retinitis with focal areas of retinal whitening: localized areas of whitening on the retina, corresponding to regions of active inflammation",
# "retinitis with blurred or indistinct retinal vessels: vessels appearing hazy or less distinct due to inflammatory changes in the surrounding tissue",
# "retinitis with perivascular sheathing: presence of inflammation around retinal blood vessels, often visible as a sheathing effect",
# "retinitis with optic disc swelling: swelling of the optic disc, indicating involvement of the optic nerve head in the inflammatory process",
# "retinitis with macular involvement: inflammation affecting the macular region, leading to potential visual impairment",
# "retinitis with the presence of inflammatory cells in the vitreous: identification of inflammatory cells, such as cells or debris, within the vitreous humor, further supporting the diagnosis of retinitis"],
#

"retinitis":["retinitis with vitreous inflammation",
             "retinitis with intraretinal hemorrhage ",
"retinitis with macular star",
"retinitis with phlebitis",
"retinitis with arteritis",
"retinitis withhyperemic disc",
"retinitis with white, fluffy exudates: presence of white, fluffy exudates on the retina",
             ],





# "chorioretinitis":["chorioretinitis with focal areas of retinal whitening: localized areas of whitening on the retina, indicating inflammation and damage to the choroid and retina",
# "chorioretinitis with irregular borders and fuzzy margins: presence of lesions with indistinct edges, often characterized by fuzzy margins due to inflammatory changes",
# "chorioretinitis with hyperpigmented and hypopigmented patches: variations in pigmentation, with some areas appearing darker (hyperpigmented) and others lighter (hypopigmented) than the surrounding tissue",
# "chorioretinitis with presence of exudates or infiltrates: identification of exudates or infiltrates, indicative of the accumulation of inflammatory cells or debris in the choroid and retina",
# "chorioretinitis with retinal hemorrhages: occurrence of hemorrhages on the retina, suggesting vascular involvement and inflammation in the affected areas",
# "chorioretinitis with optic disc swelling: swelling of the optic disc, often associated with inflammation spreading from the choroid to the optic nerve head",
# "chorioretinitis with variable involvement of the macular region: inflammation affecting the macular area to different degrees, potentially impacting visual function",
# "chorioretinitis with presence of vitreous cells or opacities: identification of inflammatory cells or opacities within the vitreous humor, supporting the diagnosis of chorioretinitis"],

"chorioretinitis":["chorioretinitis with focal areas of retinal whitening: localized areas of whitening on the retina, indicating inflammation and damage to the choroid and retina",
"chorioretinitis with irregular borders and fuzzy margins: presence of lesions with indistinct edges, often characterized by fuzzy margins due to inflammatory changes",
"chorioretinitis with inflammation of choroid and retina"

],



"exudation":["exudation with localized or diffuse retinal thickening with identification of areas where the retina appears thicker than normal, indicating fluid accumulation",
"exudation with white or yellowish lipid deposits with presence of fluffy, white lesions on the retina, often associated with microinfarctions and white or yellow spots",
"exudation with exudates with accumulation of lipid or protein deposits on the retina, often appearing as yellowish lesions",
"exudation with macular involvement with swelling and fluid accumulation in the macular region, potentially leading to decreased visual acuity",
"exudation with hard exudates with deposition of lipid-rich material on the retina, often presenting as yellowish, well-defined lesions",
"exudation with optic disc swelling with swelling of the optic disc, indicating increased pressure within the eye and potential involvement of the optic nerve head",
"exudation with serous retinal detachment with separation of the neurosensory retina from the underlying retinal pigment epithelium due to the accumulation of serous fluid"],


# "retinal pigment epithelium changes":["retinal pigment epithelium changes with mottled or granular appearance: observation of irregular or grainy alterations in the retinal pigment epithelium (RPE), often indicative of degenerative changes",
# "retinal pigment epithelium changes with hypo- or hyperpigmented patches: areas of the RPE displaying either lighter (hypopigmented) or darker (hyperpigmented) pigmentation compared to the surrounding tissue",
# "retinal pigment epithelium changes with presence of drusen: identification of small, yellowish deposits beneath the RPE, a common sign of age-related macular degeneration",
# "retinal pigment epithelium changes with geographic atrophy: development of well-defined areas of RPE loss, often leading to corresponding retinal thinning",
# "retinal pigment epithelium changes with pigment clumping: aggregation of pigmented material within the RPE layer, contributing to alterations in pigmentation",
# "retinal pigment epithelium changes with window defects: areas where the underlying choroidal vessels become visible due to RPE thinning or atrophy",
# "retinal pigment epithelium changes with alterations in autofluorescence patterns: variations in the natural fluorescence emitted by the RPE, detectable through imaging techniques like fundus autofluorescence",
# "retinal pigment epithelium changes with irregularities in the RPE layer: disruptions or irregularities in the normally smooth RPE layer, often associated with degenerative processes or diseases affecting the retina"],


"retinal pigment epithelium changes":["retinal pigment epithelium changes with increased thickness of Bruch’s membrane",
                                      "retinal pigment epithelium changes with loss of melanin granules",
                                      "retinal pigment epithelium changes with accumulation of lipofuscin",
                                      "retinal pigment epithelium changes with formation of drusen",
                                      "retinal pigment epithelium changes with increase in the density of residual bodies",
                                      "retinal pigment epithelium changes with accumulation of basal deposits on r within Bruch’s membrane",
                                      "retinal pigment epithelium changes with disorganization of the basal infoldings",
                                      "retinal pigment epithelium changes with microvilli atrophy"],


# "macular hole":["macular hole with central foveal dehiscence: presence of a gap or opening in the central fovea, often observed as a well-defined break in the retinal tissue",
# "macular hole with loss of foveal contour: flattening or distortion of the normal foveal shape, indicating structural changes associated with the macular hole",
# "macular hole with surrounding cystic changes: fluid-filled spaces around the macular hole, contributing to alterations in retinal thickness",
# "macular hole with absence of a foveal reflex: the normal light reflex at the fovea may be absent or altered due to the structural changes caused by the macular hole",
# "macular hole with disruption of the inner retinal layers: identification of breaks or discontinuities in the inner retinal layers, often visible on optical coherence tomography (OCT) imaging",
# "macular hole with adjacent retinal tissue bridging: formation of tissue bridges across the macular hole, creating a characteristic appearance often described as a bridge or flap",
# "macular hole with absence of epiretinal membrane: differentiation from other macular conditions, as a macular hole typically lacks the presence of an epiretinal membrane",
# "macular hole with decreased visual acuity: associated vision impairment, often disproportionate to the size of the hole, as the central fovea is affected"],

"macular hole":["macular hole with central foveal dehiscence with presence of a gap or opening in the central fovea, often observed as a well-defined break in the retinal tissue",
"macular hole with loss of foveal contour with flattening or distortion of the normal foveal shape, indicating structural changes associated with the macular hole",
"macular hole with small retinal break located in the center of the fovea",
                "macular hole with lesion in the macula",
                "macular hole with grayish fovea"],



"retinitis pigmentosa":["retinitis pigmentosa with bone spicule-like pigmentation with presence of characteristic pigmentary changes resembling bone spicules, often distributed in the mid-peripheral and peripheral retina",
"retinitis pigmentosa with bone-spicule deposits with black lines around the retina ",
"retinitis pigmentosa with arterial narrowing with light red blood vessels narrowing"],


"cotton wool spots":["cotton wool spots with soft, fluffy edges: identification of soft-edged, white or off-white lesions on the retina, often associated with nerve fiber layer infarctions",
"cotton wool spots with nerve fiber layer thickening: thickening of the nerve fiber layer in areas surrounding the cotton wool spots, contributing to their characteristic appearance",
"cotton wool spots with blurred or indistinct retinal vessels: vessels appearing hazy or less distinct due to the presence of cotton wool spots along the course of the vessels",
"cotton wool spots with superficial retinal hemorrhages: associated hemorrhages on the retinal surface near the cotton wool spots, indicating localized ischemia",
"cotton wool spots with microinfarctions: small areas of tissue infarction, often seen as discrete patches adjacent to the cotton wool spots",
"cotton wool spots with asymmetrical distribution: uneven distribution of cotton wool spots throughout the retina, often more concentrated in specific areas",
"cotton wool spots with associated systemic conditions: consideration of underlying systemic conditions such as hypertension or diabetes, as cotton wool spots can be associated with these diseases",
"cotton wool spots with absence of hard exudates: differentiation from other retinal conditions, as cotton wool spots typically lack the presence of lipid-rich hard exudates"],


"colobomas":["colobomas with well-defined, excavated optic disc: identification of a well-defined, cup-shaped excavation of the optic disc, often larger than the physiological cup",
"colobomas with extension into the adjacent retina: presence of a gap or defect in the retinal tissue, extending from the optic disc towards the peripheral retina",
"colobomas with pigmentary changes: alterations in pigmentation within and around the colobomatous area, contributing to a distinctive appearance",
"colobomas with associated vascular changes: variations in retinal blood vessels, including tortuosity or anomalous branching patterns near the coloboma",
"colobomas with posterior staphyloma: a localized, outward bulging of the posterior eye wall often associated with colobomas, especially in the setting of high myopia",
"colobomas with adjacent choroidal thinning: thinning of the choroid in the region of the coloboma, visible as a darker area in fundus imaging",
"colobomas with peripapillary atrophy: the presence of atrophic changes surrounding the optic disc, often seen in conjunction with colobomas",
"colobomas with absence of retinal tissue at the colobomatous site: a clear void or absence of retinal tissue at the location of the coloboma, often visible on fundus examination"],


"optic disc pit":["optic disc pit maculopathy with peripapillary atrophy: observation of atrophic changes surrounding the optic disc, often extending into the adjacent retina",
"optic disc pit maculopathy with macular serous detachment: detection of serous retinal detachment in the macular region, commonly associated with fluid accumulation",
"optic disc pit maculopathy with schisis-like changes: identification of split-like changes or cavities in the layers of the macula, often visible on optical coherence tomography (OCT) imaging",
"optic disc pit maculopathy with pigmentary changes: alterations in retinal pigmentation within the macula, contributing to a mottled or speckled appearance",
"optic disc pit maculopathy with optic disc excavation: recognition of an excavated or depressed appearance of the optic disc, often associated with the optic disc pit",
"optic disc pit maculopathy with disrupted photoreceptor layer: visualizing interruptions or irregularities in the photoreceptor layer of the macula, indicative of structural changes",
"optic disc pit maculopathy with macular edema: presence of fluid accumulation leading to macular edema, often contributing to visual impairment",
"optic disc pit maculopathy with absence of exudates in the macular region: differentiation from other macular pathologies, as optic disc pit maculopathy typically lacks the presence of lipid-rich exudates in the macular area"],


"preretinal haemorrhage":["preretinal haemorrhage with layered appearance: identification of blood accumulation between the retina and the vitreous, often forming a distinct layered appearance",
"preretinal haemorrhage with sharp demarcation: clear boundaries between the preretinal hemorrhage and surrounding retinal tissue, visible on fundus examination",
"preretinal haemorrhage with obscured retinal vessels: partial or complete covering of retinal vessels by the hemorrhagic layer, contributing to vessel obscurity",
"preretinal haemorrhage with a localized distribution: concentration of blood in a specific area of the retina, often related to the site of vascular rupture",
"preretinal haemorrhage with associated with detection of tractional forces on the retina caused by the hemorrhage, visible as distortion or pulling of retinal tissue",
"preretinal haemorrhage with variable coloration: ranging from bright red to darker hues as the hemorrhage undergoes changes in age",
"preretinal haemorrhage with absence of underlying retinal pathology: differentiation from retinal hemorrhages associated with other conditions, as preretinal hemorrhages are typically not directly related to retinal diseases",
"preretinal haemorrhage with gradual resolution over time: monitoring the fundus for signs of resolution as the hemorrhage is reabsorbed, indicating healing and improvement"],

"myelinated nerve fibers":["myelinated nerve fibers with feathered edges: identification of nerve fibers with distinct, feathered borders, often giving them a wispy or brush-like appearance",
"myelinated nerve fibers with a striated pattern: observation of a striped or streaked pattern along the course of the nerve fibers, enhancing their visibility",
"myelinated nerve fibers with variable coloration: ranging from a lighter, more translucent appearance to a more opaque, white or yellowish hue compared to the surrounding retina",
"myelinated nerve fibers with respect to retinal vessels: noting the relationship of myelinated nerve fibers in proximity to retinal vessels, as they often follow the course of blood vessels",
"myelinated nerve fibers with preservation of retinal layers: absence of retinal thinning or disruption in the areas occupied by myelinated nerve fibers, differentiating them from other pathological changes",
"myelinated nerve fibers with sharp demarcation: clear boundaries between the myelinated nerve fibers and adjacent retinal tissue, facilitating their recognition",
"myelinated nerve fibers with nerve fiber layer transparency: the transparency of the nerve fiber layer in the affected areas, allowing visibility of the underlying choroidal vessels",
"myelinated nerve fibers with absence of associated visual field defects: typically, myelinated nerve fibers do not cause visual field deficits, aiding in differentiation from other conditions affecting the visual field"],

"haemorrhagic retinopathy":["haemorrhagic retinopathy with flame-shaped hemorrhages: identification of flame-shaped, linear hemorrhages along the retinal nerve fiber layer, often associated with hypertensive retinopathy",
"haemorrhagic retinopathy with dot and blot hemorrhages: presence of small dot-like and larger blot-shaped hemorrhages scattered throughout the retina, indicating vascular damage",
"haemorrhagic retinopathy with cotton wool spots: detection of fluffy, white lesions on the retina, resulting from microinfarctions and ischemic changes",
"haemorrhagic retinopathy with macular edema: observation of fluid accumulation in the macular region, often contributing to visual impairment",
"haemorrhagic retinopathy with vascular changes: alterations in retinal blood vessels, including arteriolar narrowing, arteriovenous nicking, or vascular sheathing",
"haemorrhagic retinopathy with optic disc swelling: swelling of the optic disc, indicating involvement of the optic nerve head in the hemorrhagic process",
"haemorrhagic retinopathy with hemorrhagic choroidal detachment: presence of blood accumulation between the choroid and the sclera, visible as a dark, dome-shaped area on fundus examination",
"haemorrhagic retinopathy with associated systemic conditions: consideration of underlying systemic diseases such as hypertension or diabetes, as these conditions can contribute to the development of haemorrhagic retinopathy"],

"central retinal artery occlusion":["central retinal artery occlusion with pale retina: observation of a pale or whitened appearance of the retina due to the lack of blood supply, especially in the macular region",
"central retinal artery occlusion with cherry-red spot: identification of a cherry-red spot at the fovea, contrasting with the pale retina, caused by the transparency of the foveal area and the absence of blood flow",
"central retinal artery occlusion with attenuated retinal arteries: narrowing of retinal arteries, often visible as thin, thread-like vessels throughout the retina",
"central retinal artery occlusion with boxcarring of retinal arterioles: segmented appearance of retinal arterioles, resembling a series of boxes due to decreased blood flow",
"central retinal artery occlusion with retinal edema: presence of retinal edema, particularly in the posterior pole, contributing to the overall whitening of the retina",
"central retinal artery occlusion with emboli: detection of emboli, often visible as bright or refractile particles within the retinal vessels, contributing to the arterial occlusion",
"central retinal artery occlusion with cilioretinal artery sparing: in some cases, sparing of the cilioretinal artery may lead to a localized area of preserved retinal perfusion within the macula",
"central retinal artery occlusion with absence of venous pulsations: absence of venous pulsations due to compromised blood flow, especially in the larger retinal veins"],


"tilted disc":["tilted disc with oblique optic disc appearance: recognition of an oval or obliquely shaped optic disc, deviating from the typical round configuration",
"tilted disc with inferotemporal tilting: observation of the optic disc tilted in the inferotemporal direction, potentially resulting in a crescent-shaped or tilted appearance",
"tilted disc with associated peripapillary atrophy: presence of atrophic changes in the peripapillary region, often more noticeable on the side opposite to the tilt",
"tilted disc with asymmetric cup-to-disc ratio: uneven cupping of the optic disc, with one side appearing more excavated than the other due to the tilt",
"tilted disc with abnormal vascular branching patterns: alterations in the branching pattern of retinal vessels near the optic disc, reflecting the tilted nature of the optic disc",
"tilted disc with torsional changes in retinal vessels: twisting or torsion of retinal vessels as they approach the optic disc, indicative of the tilted disc configuration",
"tilted disc with absence of true optic disc swelling: differentiation from true optic disc swelling, as the tilting may create a pseudopapilledema appearance",
"tilted disc with compensatory head tilt: in some cases, patients may adopt a compensatory head tilt to align their visual axis with the tilted optic disc, potentially revealing a head posture abnormality"],


"cystoid macular edema":["cystoid macular edema with retinal cystoid spaces: identification of multiple cyst-like spaces within the macula, often visible as fluid-filled lacunae on fundus imaging",
"cystoid macular edema with petalloid pattern: recognition of a characteristic petal-shaped pattern of fluid accumulation in the macula, radiating from the fovea",
"cystoid macular edema with macular thickening: measurement of increased macular thickness, often seen on optical coherence tomography (OCT) imaging",
"cystoid macular edema with blurred or indistinct foveal reflex: haziness or loss of the normal foveal light reflex due to the presence of cystoid spaces and fluid",
"cystoid macular edema with fluorescein angiography leakage: visualization of leakage on fluorescein angiography, indicating abnormal fluid dynamics within the macula",
"cystoid macular edema with disruption of inner retinal layers: identification of irregularities or disorganization in the inner retinal layers, visible on OCT scans",
"cystoid macular edema with decreased visual acuity: associated vision impairment due to the accumulation of fluid in the macular region",
"cystoid macular edema with absence of other macular pathologies: differentiation from other macular conditions, as cystoid macular edema has specific characteristics on imaging that distinguish it from other macular abnormalities"],


"post traumatic choroidal rupture":["post traumatic choroidal rupture with linear configuration: identification of a linear, often jagged or irregular-shaped lesion on the fundus, corresponding to the choroidal rupture",
"post traumatic choroidal rupture with extension from the optic disc or peripapillary region: noting the origin of the choroidal rupture, often arising from the optic disc or extending radially from the peripapillary area",
"post traumatic choroidal rupture with associated overlying retinal pigment epithelium changes: observation of alterations in pigmentation overlying the choroidal rupture site, indicating disruption to the retinal pigment epithelium",
"post traumatic choroidal rupture with overlying subretinal hemorrhage: presence of hemorrhage between the neurosensory retina and the retinal pigment epithelium, directly overlying the choroidal rupture",
"post traumatic choroidal rupture with choroidal vessel visibility: visualization of choroidal vessels within the rupture site, contrasting with the surrounding normal choroid",
"post traumatic choroidal rupture with adjacent retinal folds: detection of retinal folds near the site of choroidal rupture, resulting from the mechanical forces involved in the traumatic event",
"post traumatic choroidal rupture with associated vitreous hemorrhage: in some cases, concurrent vitreous hemorrhage may be present, complicating the clinical picture",
"post traumatic choroidal rupture with corresponding visual field defects: consideration of visual field testing to identify any scotomas or defects corresponding to the location of the choroidal rupture"],

"choroidal folds":["choroidal folds with undulating appearance: recognition of wave-like or undulating folds in the choroid, often extending across the fundus",
"choroidal folds with parallel orientation: observation of folds running parallel to each other, typically separated by normal choroidal tissue",
"choroidal folds with associated retinal pigment epithelium changes: detection of alterations in pigmentation overlying the choroidal folds, reflecting the influence of the folds on the overlying retina",
"choroidal folds with preserved retinal layers: absence of significant disruption or damage to the neurosensory retina, as choroidal folds primarily affect the choroid",
"choroidal folds with displacement of choroidal vessels: visualization of choroidal vessels appearing displaced or distorted within the folds",
"choroidal folds with localized choroidal thickening: measurement of increased choroidal thickness in the areas corresponding to the folds, visible on optical coherence tomography (OCT) imaging",
"choroidal folds with absence of hemorrhage or exudates: differentiation from other fundus abnormalities, as choroidal folds typically do not present with associated hemorrhage or exudative changes",
"choroidal folds with correlation to patient symptoms: consideration of patient symptoms such as metamorphopsia or visual distortion, as choroidal folds may affect visual perception",],

"vitreous haemorrhage":["vitreous haemorrhage with obscured fundus details: presence of blood in the vitreous cavity leading to reduced visibility of retinal structures, making fundus details indistinct",
"vitreous haemorrhage with floating blood cells: observation of floating red blood cells within the vitreous humor, contributing to the hazy appearance",
"vitreous haemorrhage with blotchy or speckled fundus: fundus exhibiting irregular blotches or speckles due to the dispersed blood within the vitreous",
"vitreous haemorrhage with dense, layered blood accumulation: detection of dense, layered blood accumulation, potentially forming a horizontal level in the vitreous cavity",
"vitreous haemorrhage with obscuration of retinal vessels: obscuring or masking of retinal vessels as a result of the hemorrhage, leading to diminished vessel visibility",
"vitreous haemorrhage with dynamic movement of blood particles: potential movement or settling of blood particles within the vitreous, observable during eye movements",
"vitreous haemorrhage with associated retinal pathology: determination of any underlying retinal pathologies, such as diabetic retinopathy or retinal tears, that may have contributed to the vitreous hemorrhage",
"vitreous haemorrhage with potential clearing over time: consideration of the possibility of spontaneous clearing of the vitreous hemorrhage over time, allowing for improved visualization of the fundus"],

"macroaneurysm":["macroaneurysm with round or oval-shaped lesion: identification of a well-defined, round or oval-shaped lesion on the fundus, often distinguishable from surrounding vessels",
"macroaneurysm with dilated and tortuous appearance: recognition of a dilated and tortuous vessel segment, forming the macroaneurysm, often exceeding the normal caliber of surrounding vessels",
"macroaneurysm with associated hemorrhage: detection of adjacent retinal hemorrhage, either intraretinal or subretinal, indicating rupture or leakage from the macroaneurysm",
"macroaneurysm with exudates or lipid deposition: presence of lipid-rich exudates or deposits around the macroaneurysm, reflecting chronic leakage and tissue damage",
"macroaneurysm with hard exudates: observation of lipid-rich deposits at a distance from the macroaneurysm, suggestive of chronic leakage and lipid accumulation",
"macroaneurysm with fluorescein angiography findings: abnormal dye leakage or pooling during fluorescein angiography, highlighting the site of the macroaneurysm and associated vascular abnormalities",
"macroaneurysm with surrounding edema: presence of macular edema or localized retinal thickening in proximity to the macroaneurysm",
"macroaneurysm with absence of neovascularization: differentiation from other retinal pathologies, as macroaneurysms typically do not lead to the development of neovascularization"],


"vasculitis":["vasculitis with vessel wall inflammation: identification of signs indicating inflammation of retinal vessels, such as vessel wall thickening or hyperemia",
"vasculitis with perivascular sheathing: presence of white or yellowish sheathing around retinal vessels, indicative of inflammatory infiltration in the perivascular spaces",
"vasculitis with cuffing of retinal vessels: detection of localized or diffuse thickening or cuffing of retinal vessels due to inflammatory changes",
"vasculitis with retinal hemorrhages: observation of dot and blot retinal hemorrhages scattered along the course of affected vessels, reflecting vascular damage",
"vasculitis with cotton wool spots: presence of fluffy, white lesions on the retina, resulting from microinfarctions and ischemic changes associated with vasculitis",
"vasculitis with arterial narrowing: identification of narrowed or constricted retinal arteries, reflecting reduced blood flow due to inflammatory changes",
"vasculitis with neovascularization: potential development of abnormal, new blood vessels as a response to ischemia, visible on the disc or elsewhere in the retina",
"vasculitis with associated retinal edema: detection of fluid accumulation in the retinal layers, leading to retinal thickening and potential macular involvement"],






"branch retinal artery occlusion":["branch retinal artery occlusion with retinal whitening: identification of localized whitening of the retina in the distribution of the affected branch retinal artery, reflecting ischemia",
"branch retinal artery occlusion with emboli: visualization of emboli or plaque-like material within the affected branch retinal artery, indicating the source of the occlusion",
"branch retinal artery occlusion with abrupt vessel cutoff: observation of a sudden termination or sharp demarcation of the affected branch retinal artery, often visible as a straight edge on fundus examination",
"branch retinal artery occlusion with cherry-red spot at the fovea: recognition of a cherry-red spot at the fovea, surrounded by the whitened ischemic retina, due to transparency of the foveal area",
"branch retinal artery occlusion with narrowed and attenuated retinal arteries: identification of reduced caliber and attenuated appearance of the affected branch retinal artery and its tributaries",
"branch retinal artery occlusion with segmentation of retinal blood flow: appearance of segmented or fragmented blood flow within the occluded branch retinal artery, visible as a series of disconnected segments",
"branch retinal artery occlusion with associated cotton wool spots: presence of cotton wool spots in the affected area, indicating ischemic damage and nerve fiber layer infarction",
"branch retinal artery occlusion with delayed or absent arteriovenous transit: abnormal or delayed passage of dye through retinal vessels during fluorescein angiography, revealing impaired blood flow in the affected area"],

"plaque":["plaque with yellowish or white appearance: identification of a localized yellowish or white lesion on the fundus, often contrasting with the surrounding retinal tissue",
"plaque with well-defined borders: recognition of clear and demarcated borders outlining the plaque, facilitating differentiation from adjacent retinal structures",
"plaque with surface irregularities: observation of irregularities or undulations on the surface of the plaque, indicating variations in thickness or composition",
"plaque with associated retinal pigment epithelium changes: detection of alterations in pigmentation overlying the plaque, suggestive of chronic changes or interactions with the retinal pigment epithelium",
"plaque with subretinal fluid accumulation: presence of fluid between the plaque and the neurosensory retina, contributing to localized retinal detachment or elevation",
"plaque with overlying exudates or lipid deposition: identification of lipid-rich exudates or deposits around the plaque, reflecting chronic leakage and tissue damage",
"plaque with fluorescence characteristics on angiography: abnormal dye patterns during fluorescein angiography, revealing the plaque vascular or perfusion characteristics",
"plaque with absence of neovascularization: differentiation from other retinal pathologies, as plaques typically do not lead to the development of neovascularization",],


"haemorrhagic pigment epithelial detachment":["haemorrhagic pigment epithelial detachment with subretinal bleeding: identification of blood accumulation between the retinal pigment epithelium (RPE) and the neurosensory retina, leading to a noticeable detachment",
"haemorrhagic pigment epithelial detachment with irregular borders: recognition of the irregular or jagged borders outlining the area of pigment epithelial detachment",
"haemorrhagic pigment epithelial detachment with hemorrhagic or reddish appearance: observation of a reddish or hemorrhagic component within the pigment epithelial detachment, indicating the presence of blood",
"haemorrhagic pigment epithelial detachment with associated subretinal fluid: detection of fluid accumulation between the RPE and the retina, contributing to the detachment and potentially obscuring underlying details",
"haemorrhagic pigment epithelial detachment with overlying retinal changes: identification of changes in the overlying retina, such as exudates or lipid deposition, due to the presence of blood and altered RPE function",
"haemorrhagic pigment epithelial detachment with fluorescein angiography findings: abnormal dye patterns during fluorescein angiography, reflecting the vascular characteristics and leakage associated with the haemorrhagic pigment epithelial detachment",
"haemorrhagic pigment epithelial detachment with decreased visual acuity: consideration of associated vision impairment due to the presence of blood and fluid affecting the macula",
"haemorrhagic pigment epithelial detachment with absence of neovascularization: differentiation from other retinal pathologies, as haemorrhagic pigment epithelial detachments typically do not lead to the development of neovascularization"],


"collaterals":["collaterals with vessel dilation: identification of dilated retinal vessels, often forming collateral pathways that deviate from the normal vascular pattern",
"collaterals with tortuous appearance: recognition of tortuosity or twisting in the course of collateral vessels, reflecting the compensatory changes in blood flow",
"collaterals with anastomoses: observation of connections or anastomoses between retinal vessels, creating alternative pathways for blood circulation",
"collaterals with abnormal branching patterns: detection of irregularities or aberrant branching in retinal vessels, indicative of collateral formation",
"collaterals with visible pulsations: observation of pulsatile movements in collateral vessels, potentially visible with careful examination or dynamic imaging",
"collaterals with fluorescein angiography findings: abnormal dye patterns during fluorescein angiography, highlighting the presence and characteristics of collateral vessels",
"collaterals with associated retinal changes: identification of changes in the overlying retina, such as exudates or hemorrhages, due to altered blood flow and collateral circulation",
"collaterals with correlation to underlying vascular pathology: consideration of the underlying vascular pathology leading to collateral formation, such as occlusive diseases or venous abnormalities"],


"other": [
              "other with cotton wool spots",
                "other with colobomas",
        "other with optic disc pit maculopathy",
        "other with preretinal haemorrhage",
        "other with myelinated nerve fibers",
        "other with haemorrhagic retinopathy",
        "other with central retinal artery occlusion",
        "other with tilted disc",
        "other with cystoid macular edema",
        "other with post traumatic choroidal rupture",
        "other with choroidal folds",
        "other with vitreous haemorrhage",
        "other with macroaneurysm",
        "other with vasculitis",
        "other with branch retinal artery occlusion",
        "other with plaque",
        "other with haemorrhagic pigment epithelial detachment",
        "other with collaterals with vessel dilation"],

















"glaucoma":[
"glaucoma with optic disc atrophy with glaucoma can lead to atrophy of the optic disc, the initial part of the optic nerve. This may be characterized by a change in color of the optic disc, often appearing pale yellow or white",
"glaucoma with defects in the retinal nerve fiber layer with glaucoma may cause damage to the retinal nerve fiber layer, resulting in specific areas of the fundus lacking nerve fibers, forming so-called nerve fiber layer defects",
"glaucoma with blurry optic disc margins with glaucoma may render the margins of the optic disc blurry or irregular, presenting an appearance distinct from the normal clear edges",
"glaucoma with cupping of the optic disc with atrophy of the optic disc caused by glaucoma may lead to cupping, a phenomenon where the optic disc becomes inwardly concave",
"glaucoma with optic disc hemorrhage with glaucoma may result in hemorrhage around the optic disc or within the optic disc itself"
],


"cataract":[
"cataract with opacification of the lens with the primary manifestation of cataracts is the opacification of the lens, possibly appearing as a blurry or hazy region in the lens area on fundus images",
"cataract with uneven pupil coloring with when the lens becomes cloudy due to cataracts, the pupil on fundus images may exhibit uneven coloring, as reduced transparency causes light scattering",
"cataract with reflection from the retina with opacification of the lens may lead to a reflection from the retina, manifesting as a reflective light within the pupil on fundus images",
"cataract with loss of clear lens edges with normally, the lens in fundus images should have clear edges, but cataracts can cause these edges to become blurred or indistinct"],


"hypertensive retinopathy": ["hypertensive retinopathy with possible signs of haemorraghe with blot, dot, or flame-shaped",
                                 "hypertensive retinopathy with possible presence of microaneurysm, cotton-wool spot, or hard exudate",
                                 "hypertensive retinopathy with arteriolar narrowing", "hypertensive retinopathy with vascular wall changes", "hypertensive retinopathy with optic disk edema"],

    "other disease": ["other disease with a disease",

                      "other disease with may laser spot with bright or white small dots on the fundus image, contrasting sharply with the surrounding tissue",

                      "other disease with retinal Detachment with irregular, wavy, or separated features in the fundus image",

                      "other disease with macular hole with signs of central depression or absence in the macular region, potentially leading to decreased central vision",

                      "other disease with retinal artery occlusion with  ischemia in the corresponding area of the retina, presenting as a lightening or whitening of the affected region",

                      "other disease with retinal vein occlusion with hemorrhages and swelling in the affected retinal area, visible as spots and edema",

                      "other disease with optic neuropathy with color changes, swelling, or irregular edges in the optic nerve head, potentially affecting the surrounding retinal tissue",

                      "other disease with choroidal neovascularization with bleeding, leakage, and discoloration in the macular region",

                      "other disease with drusen with yellow or white deposits in the retina, often located on the surface of the retina",

                      "other disease with epiretinal membrane with folds or membranous structures on the surface of the retina",

                      "other disease with post laser photocoagulation with alterations around the laser spots, such as scar tissue formation",

                      "other disease with vitreous degeneration opacities or irregular shapes in the vitreous observed in the fundus image",

                      "other disease with pigment epithelium proliferation with pigment deposition and cellular proliferation in the fundus image"
                      ]



}

               # "moderate diabetic retinopathy": ["many exudates near the macula",
               #                                   "many haemorrhages near the macula",
               #                                   "retinal thickening near the macula",
               #                                   "hard exudates",
               #                                   "cotton wool spots",
               #                                   "few severe haemorrhages"],
description_performance = {
    "a disease": ["a disease with no healthy", "a disease with lesions", "a disease with abnormal","a disease with blurring sings"],



#LLAMA2
# "normal":[
# "normal with optic disc with The optic disc, also known as the optic nerve head, appears as a round or oval-shaped area at the center of the retina, where the retinal vessels converge. It can appear as a slightly elevated area with a pale yellowish color",
# "normal with macula with the macula, located at the center of the retina, appears as a small, round or oval-shaped area with a slightly darker color than the surrounding retina. It is responsible for central vision",
# "normal with fovea with the fovea, located within the macula, appears as a small, round or oval-shaped depression in the retina. It is responsible for sharp central vision",
# "normal with retinal nerve fiber layer with the retinal nerve fiber layer appears as a thin, translucent layer that covers the surface of the retina. It can be seen as a subtle, wavy line or a series of lines that parallel the vessels and nerve fibers of the retina",
# "normal with retinal ganglion cells with the retinal ganglion cells, located at the inner layer of the retina, appear as small, dark spots. They are responsible for transmitting visual information to the brain",
# "normal with photoreceptors with the photoreceptors, located at the outer layer of the retina, appear as small, dark spots. They are responsible for converting light into electrical signals that are transmitted to the brain",
# "normal with retinal pigment epithelium with the retinal pigment epithelium, located at the outer layer of the retina, appears as a thin, dark layer. It is responsible for maintaining the health and function of the photoreceptors",
# "normal with choroid with the choroid, located between the retina and the sclera, appears as a dark, irregular area. It is responsible for providing blood supply to the retina"
# ],


#Gemini
"normal":[
"normal with optic Disc with Round or slightly oval",
"normal with optic Disc with Pink-orange in color",
"normal with optic Disc with Sharp margins",
"normal with optic Disc with Central cup with a cup-to-disc ratio of less than 0.5",
"normal with optic Disc with No hemorrhage or exudates",
"normal with retinal Vessels with Arteries: Narrower, lighter in color, and less tortuous",
"normal with retinal Vessels with Veins: Wider, darker in color, and more tortuous",
"normal with retinal Vessels with No significant arteriovenous nicking or crossing defects",
"normal with macula with Yellowish-orange in color",
"normal with macula with Fovea centralis appears as a small, dark spot",
"normal with macula with No hemorrhage, exudates, or drusen",
"normal with periphery with Uniform red-orange color",
"normal with periphery with No retinal tears, holes, or detachments",
"normal with periphery with No lattice degeneration or other peripheral abnormalities",
"normal with blood Vessels with No significant hemorrhages, exudates, or microaneurysms",
"normal with blood Vessels with No cotton-wool spots or hard exudates",
"normal with pigmentation with Uniform distribution of melanin pigment",
"normal with pigmentation with No abnormal hyperpigmentation or hypopigmentation",
"normal with overall with Clear and well-defined image",
"normal with overall with No signs of inflammation, infection, or other pathology"],


#Claude3

# "normal":
# [
# "normal with optic disc with well-defined circular or slightly oval shape ",
# "normal with optic disc with Distinct neuroretinal rim surrounding the optic cup",
# "normal with optic disc with physiological cupping",
# "normal with optic disc with crisp and regular margins",
# "normal with retinal vasculature with arteries appear brighter red and narrower than veins",
# "normal with retinal vasculature with veins appear darker red and wider than arteries",
# "normal with retinal vasculature with vessel caliber tapering towards the periphery",
# "normal with retinal vasculature with vessels following a typical branching pattern",
# "normal with retinal vasculature with no abnormal vascular tortuosity, caliber changes, or arteriovenous nicking",
# "normal with macula with well-defined foveal avascular zone (FAZ) with a darker central foveal reflex",
# "normal with macula with surrounding macular area appearing slightly darker than the surrounding retina",
# "normal with macula with no abnormal pigmentary changes, edema, or distortion",
# "normal with retinal background with uniform, smooth, and orange-red color",
# "normal with retinal background with no areas of pigmentary disturbance or exudation",
# "normal with retinal background with no evidence of hemorrhages, cotton-wool spots, or other abnormal lesions",
# "normal with retinal periphery with intact and clearly visible peripheral retinal vasculature",
# "normal with retinal periphery with no visible tears, holes, or detachments",
# "normal with vitreous with clear and transparent, allowing an unobstructed view of the fundus"],


#GPT
    # "normal": ["normal with healthy with optic disc appears well-defined and within normal limits",
    #            "normal with no findings with clear circular shape with distinct margins",
    #            "normal with healthy appearance of retina wia uniform color and texture",
    #            "normal with health with well-defined blood vessels, arteries and veins",
    #            "normal with clear macula with clear retinal background",
    #            "normal with health with no hemorrhages",
    #            "normal with no findings and no exudates",
    #            "normal with no findings",
    #            "normal with no exudates",
    #            "normal with clear photo"],






#LLAMA2
# "epiretinal membrane":[
# "epiretinal membrane with thin, translucent membrane an epiretinal membrane with appears as a thin, translucent membrane that covers part or all of the retina",
# "epiretinal membrane with epiretinal membrane wavy lines with the membrane can be seen as a subtle, wavy line or a series of lines that parallel the vessels and nerve fibers of the retina",
# "epiretinal membrane with faint glistening line with The membrane can appear as a faint, glistening line, depending on its thickness and the angle of the light used to image the retina",
# "epiretinal membrane with opaque membrane with In some cases, the membrane may appear as a more prominent, opaque membrane, depending on its thickness and the angle of the light used to image the retina",
# "epiretinal membrane with elevated retina with The membrane may also cause the retina to appear elevated or puckered",
# "epiretinal membrane with retinal edema with The presence of an epiretinal membrane can cause retinal edema, which can appear as small, round or oval-shaped fluid accumulations in the retina",
# "epiretinal membrane with hemorrhages with the presence of an epiretinal membrane can also cause hemorrhages, which appear as small, round or oval-shaped red lesions in the retina",
# "epiretinal membrane with exudates with The presence of an epiretinal membrane can also cause exudates, which appear as small, round or oval-shaped yellow or white lesions in the retina"],


#Gemini-pro

"epiretinal membrane":[
"epiretinal membrane with appearance with thin, transparent or translucent membrane",
"epiretinal membrane with appearance with wrinkled or folded surface",
"epiretinal membrane with appearance with may have a glistening or shimmering appearance",
"epiretinal membrane with location on the surface of the retina, overlying the macula",
"epiretinal membrane with size and shape with Variable in size, from small to large",
"epiretinal membrane with size and shape with may be round, oval, or irregular",
"epiretinal membrane with effect on retinal vessels with retinal vessels may be tortuous or displaced",
"epiretinal membrane with effect on retinal vessels with may cause retinal folds or traction",
"epiretinal membrane with macular involvement with can cause macular distortion or edema",
"epiretinal membrane with macular involvement with may lead to decreased visual acuity",
"epiretinal membrane with other associated findings with posterior vitreous detachment",
"epiretinal membrane with other associated findings with vitreomacular traction",
"epiretinal membrane with other associated findingswith macular hole",
"epiretinal membrane with differential diagnosis with cellophane maculopathy",
"epiretinal membrane with differential diagnosis with internal limiting membrane wrinkling",
"epiretinal membrane with differential diagnosis with retinal detachment"],




    # Claude-3-Sonnet
# "epiretinal membrane" :["epiretinal membrane with graying or distortion of the retinal vessels with the presence of the ERM can cause the underlying retinal vessels to appear slightly gray or distorted in appearance",
# "epiretinal membrane with crinkled or wrinkled appearance of the retina with the ERM can exert traction on the retinal surface, causing it to appear crinkled or wrinkled, especially around the macula",
# "epiretinal membrane with thickening or elevation of the retina with the ERM can cause the retina to appear thickened or elevated, particularly in the macular region",
# "epiretinal membrane with striae or folds with striae or folds may be visible on the retinal surface, radiating outward from the macula, due to the contraction of the ERM",
# "epiretinal membrane with opacification or grayish discoloration with the ERM itself may appear as a grayish or semi-translucent membrane obscuring the underlying retinal details",
# "epiretinal membrane with distortion of retinal features with the ERM can distort the appearance of the macula, foveal avascular zone, and other retinal landmarks"],



    #GPT
    # "epiretinal membrane": ["epiretinal membrane with surface membrane with small translucent wrinkles or folds on the surface of the retina",
    #                         "epiretinal membrane with color changes with greyish semi-translucent avascular membrane",
    #                         "epiretinal membrane with color changes with different from the surrounding normal tissue",
    #                         "epiretinal membrane with light reflection changes with a sheen or abnormal reflectivity of the macular surface",
    #                         "epiretinal membrane with light reflection changes with macular gold foil-like reflection",
    #                         "epiretinal membrane with vascular distortion with blood vessels underlying show irregular or distorted shapes",
    #                         "epiretinal membrane with changes in the macular area with changing the morphology of the macula",
    #                         "epiretinal membrane with changes in the macular area with blunting of the foveal contour or wrinkling on the retinal surface from membrane contracture",
    #                         "epiretinal membrane with changes in the macular area with retinal thickening in the macular area"],






#LLAMA2


# "macular edema":[
# "macular edema with Retinal thickening with Macular edema can cause the retina to appear thicker than normal, especially in the macular area"
# "macular edema with Fluid accumulation with Macular edema can cause fluid to accumulate in the retina, resulting in a saucer-like appearance or cobblestone appearance"
# "macular edema with Exudates with Macular edema can cause exudates, which appear as small, round or oval-shaped yellow or white lesions in the retina"
# "macular edema with Hemorrhages with Macular edema can cause hemorrhages, which appear as small, round or oval-shaped red lesions in the retina"
# "macular edema with Microaneurysms with Macular edema can cause microaneurysms, which appear as small, round or oval-shaped dark spots in the retina"
# "macular edema with Retinal pigment epithelial abnormalities with Macular edema can cause abnormalities in the retinal pigment epithelium, such as a bull eye appearance or a sunburst pattern"
# "macular edema with Vitreomacular traction with Macular edema can cause vitreomacular traction, which can cause the retina to appear pulled or distorted"
# "macular edema with Foveal thickening with Macular edema can cause the fovea to appear thicker than normal"
# "macular edema with Foveal pit with Macular edema can cause a foveal pit, which appears as a small, round or oval-shaped depression in the fovea"],
#






#Gemini-pro

"macular edema":[
"macular edema with appearance with thickening of the retina in the macular area",
"macular edema with appearance with loss of normal retinal transparency",
"macular edema with appearance with may have a hazy or cloudy appearance"
"macular edema with location with central macula, involving the fovea",
"macular edema with size and shape with Variable in size, from small to large",
"macular edema with size and shape with May be focal or diffuse",
"macular edema with retinal layers with Thickening of the inner retinal layers (ganglion cell layer and nerve fiber layer)",
"macular edema with retinal layers with May also involve the outer retinal layers (photoreceptor layer)",
"macular edema with macular vessels with Retinal vessels may be obscured or distorted",
"macular edema with macular vessels with May have peripapillary telangiectasia (dilated retinal vessels around the optic disc)",
"macular edema with other associated findings with Hard exudates (yellowish-white deposits)",
"macular edema with other associated findings with Retinal hemorrhages",
"macular edema with other associated findings with Drusen (small, yellow deposits)",
"macular edema with differential diagnosis with Epiretinal membrane",
"macular edema with differential diagnosis with Central serous chorioretinopathy",
"macular edema with differential diagnosis with Diabetic retinopathy",
"macular edema with differential diagnosis with Retinal vein occlusion"
],






#Claude3

# "macular edema":[
# "macular edema with macular thickening with loss of the normal foveal depression or foveal light reflex",
# "macular edema with macular thickening with elevation or swelling of the macula, giving a blurred or hazy appearance",
# "macular edema with exudates with hard exudates (lipid deposits) appearing as bright yellow or white spots within the macular area",
# "macular edema with exudates with Soft or cotton wool exudates appearing as fluffy white lesions",
# "macular edema with retinal hemorrhages with presence of intraretinal hemorrhages, typically flame-shaped or dot-blot hemorrhages, within or around the macular area",
# "macular edema with retinal edema with generalized retinal thickening or edema, not limited to the macular area",
# "macular edema with retinal edema with retinal vasculature appearing less distinct or blurred due to edema",
# "macular edema with vascular changes with dilation and tortuosity of retinal vessels, particularly the venous system",
# "macular edema with vascular changes with Obscuration or blurring of the retinal vasculature due to edema",
# "macular edema with cystoid changes with cystoid macular edema (CME) appearing as cystic spaces or lucent areas within the macula",
# "macular edema with macular ischemia with in chronic or severe cases, the macular area may appear pale or ischemic due to capillary non-perfusion"],




#GPT
    # "macular edema": ["macular edema with macular thickening with swelling and thickening of the macula",
    #                   "macular edema with color changes with disappearance of reflection in the macular",
    #                   "macular edema with fluid accumulation with formation of cyst-like or blister-like structures, visible on fundus imaging",
    #                   "macular edema with color changes with opaque compared to the surrounding healthy tissue",
    #                   "macular edema with color changes with yellowish deposits in the macula",
    #                   "macular edema with vascular changes with irregular blood vessels",
    #                   ],





#LLAMA2 DR
# "diabetic retinopathy":[
# "diabetic retinopathy with microaneurysms with Diabetic retinopathy can cause microaneurysms, which appear as small, round or oval-shaped dark spots in the retina"
# "diabetic retinopathy with Hemorrhages with Diabetic retinopathy can cause hemorrhages, which appear as small, round or oval-shaped red lesions in the retina"
# "diabetic retinopathy with Exudates with Diabetic retinopathy can cause exudates, which appear as small, round or oval-shaped yellow or white lesions in the retina"
# "diabetic retinopathy with Retinal vasculature abnormalities with Diabetic retinopathy can cause abnormalities in the retinal vasculature, such as tortuosity, dilatation, and irregularity of the vessels"
# "diabetic retinopathy with Retinal edema with Diabetic retinopathy can cause retinal edema, which appears as a saucer-like appearance or cobblestone appearance"
# "diabetic retinopathy with Foveal thickening with Diabetic retinopathy can cause the fovea to appear thicker than normal"
# "diabetic retinopathy with Foveal pit with Diabetic retinopathy can cause a foveal pit, which appears as a small, round or oval-shaped depression in the fovea"
# "diabetic retinopathy with Vitreomacular traction with Diabetic retinopathy can cause vitreomacular traction, which can cause the retina to appear pulled or distorted"
# "diabetic retinopathy with Retinal detachment with Diabetic retinopathy can cause retinal detachment, which appears as a dark, irregular area in the retina"
# "diabetic retinopathy with Optic disc edema with Diabetic retinopathy can cause optic disc edema, which appears as a swelling of the optic disc"],






# #Gemini-pro DR
"diabetic retinopathy":[

"diabetic retinopathy with Early Signs with Microaneurysms (small, round red dots)",
"diabetic retinopathy with Early Signs with Hemorrhages (dot or blot hemorrhages)",
"diabetic retinopathy with Early Signs with Hard exudates (yellowish-white deposits)",


"diabetic retinopathy with Moderate Signs with Venous beading (dilation and tortuosity of retinal veins)",
"diabetic retinopathy with Moderate Signs with Intraretinal microvascular abnormalities (IRMA)",
"diabetic retinopathy with Moderate Signs with Cotton-wool spots (fluffy white patches)",


"diabetic retinopathy with Severe Signs with Proliferative diabetic retinopathy (PDR):",
"diabetic retinopathy with Severe Signs with New vessels (neovascularization) on the optic disc or retina",
"diabetic retinopathy with Severe Signs with Vitreous hemorrhage",
"diabetic retinopathy with Severe Signs with Tractional retinal detachment",
"diabetic retinopathy with Severe Signs with Diabetic macular edema (DME)",
"diabetic retinopathy with Severe Signs with Thickening of the retina in the macular area",
"diabetic retinopathy with Severe Signs with Hard exudates in the macula",
"diabetic retinopathy with Other Associated Findings with Drusen (small, yellow deposits)",
"diabetic retinopathy with Other Associated Findings with Retinal pigment epithelium (RPE) changes",
"diabetic retinopathy with Other Associated Findings with Optic disc edema",
"diabetic retinopathy with Differential Diagnosis with Hypertensive retinopathy",
"diabetic retinopathy with Differential Diagnosis with Central serous chorioretinopathy",
"diabetic retinopathy with Differential Diagnosis with Retinal vein occlusion"],






#Claude3-sonnet
# "diabetic retinopathy":[
#     "diabetic retinopathy with microaneurysms with small, red, dot-like lesions representing outpouchings of the retinal capillaries, typically scattered throughout the posterior pole",
# "diabetic retinopathy with retinal hemorrhages with intraretinal hemorrhages, typically flame-shaped or dot-blot hemorrhages, scattered throughout the retina",
# "diabetic retinopathy with hard exudates with bright yellow or white lipid deposits, often arranged in a circular or ring-like pattern, particularly in the macular area","cotton-wool spots with fluffy white lesions representing areas of retinal ischemia or nerve fiber layer infarcts",
# "diabetic retinopathy with Venous beading with focal dilations or irregularities in the caliber of the retinal venules",
# "diabetic retinopathy with intraretinal microvascular abnormalities with abnormal dilation and shunting of retinal capillaries, appearing as irregular, dilated, and convoluted vessels",
# "diabetic retinopathy with neovascularization with proliferation of new, abnormal blood vessels on the optic disc (neovascularization of the disc, NVD) or elsewhere on the retina (neovascularization elsewhere, NVE)",
# "diabetic retinopathy with vitreous hemorrhage with presence of blood within the vitreous cavity, obscuring the fundus view",
# "diabetic retinopathy with tractional retinal detachment with detachment of the neurosensory retina due to fibrovascular proliferation and contraction",
# "diabetic retinopathy with macular edema with thickening or swelling of the macula, often accompanied by hard exudates, hemorrhages, and cystoid spaces"],



#GPT
    # "diabetic retinopathy": ["diabetic retinopathy with retinal hemorrhages with red spots in retina of damaged blood vessels",
    #                          "diabetic retinopathy with cotton wool spots with fluffy white lesions",
    #                          "diabetic retinopathy with hard exudates with yellowish or white lipid deposits",
    #                          "diabetic retinopathy with microaneurysms with round, red dots representing dilated capillaries and microaneurysms in retina",
    #                          "diabetic retinopathy with venous beading with beading veins",
    #                          "diabetic retinopathy with neovascularization with small, irregular red lines on the retina",
    #                          "diabetic retinopathy with ischemic areas with dark areas or black areas"],






#LLAMA2
# "non-exudative age related macular degeneration":[
#
# "non-exudative age related macular degeneration with Yellow deposits with Non-exudative age-related macular degeneration can cause yellow deposits, also known as drusen, which appear as small, round or oval-shaped yellow spots in the retina.",
#
# "non-exudative age related macular degeneration with Retinal pigment epithelial abnormalities with Non-exudative age-related macular degeneration can cause abnormalities in the retinal pigment epithelium, such as a bull eye appearance or a sunburst pattern.",
#
# "non-exudative age related macular degeneration with RPE atrophy with Non-exudative age-related macular degeneration can cause atrophy of the retinal pigment epithelium, which can appear as a loss of the normal dark pigmentation in the retina.",
#
# "non-exudative age related macular degeneration with Foveal thinning with Non-exudative age-related macular degeneration can cause the fovea to appear thinner than normal.",
#
# "non-exudative age related macular degeneration with Foveal pit with Non-exudative age-related macular degeneration can cause a foveal pit, which appears as a small, round or oval-shaped depression in the fovea.",
#
# "non-exudative age related macular degeneration with Vitreomacular traction with Non-exudative age-related macular degeneration can cause vitreomacular traction, which can cause the retina to appear pulled or distorted.",
#
# "non-exudative age related macular degeneration with Retinal thinning with Non-exudative age-related macular degeneration can cause the retina to appear thinner than normal.",
#
# "non-exudative age related macular degeneration with Retinal folds with Non-exudative age-related macular degeneration can cause retinal folds, which appear as small, wavy lines or folds in the retina.",
#
# "non-exudative age related macular degeneration with Retinal pigment epithelial hyperplasia with Non-exudative age-related macular degeneration can cause hyperplasia of the retinal pigment epithelium, which can appear as a dark, irregular area in the retina."
# ],

#Gemini-pro
"non-exudative age related macular degeneration":[

"non-exudative age related macular degeneration with Early Signs with Drusen (small, yellow deposits)",
"non-exudative age related macular degeneration with Early Signs with Pigmentary changes in the retinal pigment epithelium (RPE)",
"non-exudative age related macular degeneration with Early Signs with Geographic atrophy (GA)",
"non-exudative age related macular degeneration with Early Signs with Well-demarcated areas of RPE and photoreceptor loss",
"non-exudative age related macular degeneration with Early Signs with May have a grayish or yellowish appearance",


"non-exudative age related macular degeneration with Intermediate Signs with Increased number and size of drusen",
"non-exudative age related macular degeneration with Intermediate Signs with RPE changes become more prominent",
"non-exudative age related macular degeneration with Intermediate Signs with GA may enlarge",


"non-exudative age related macular degeneration with Advanced Signs with Extensive GA involving the central macula",
"non-exudative age related macular degeneration with Advanced Signs with Loss of central vision",


"non-exudative age related macular degeneration with Other Associated Findings with Hyperpigmentation of the RPE",
"non-exudative age related macular degeneration with Other Associated Findings with Hypopigmentation of the RPE",
"non-exudative age related macular degeneration with Other Associated Findings with Choroidal thinning",


"non-exudative age related macular degeneration with Differential Diagnosis with Exudative AMD",
"non-exudative age related macular degeneration with Differential Diagnosis with Stargardt disease",
"non-exudative age related macular degeneration with Differential Diagnosis with Cone-rod dystrophy"],




#Claude3
# "non-exudative age related macular degeneration":
# ["non-exudative age related macular degeneration with drusen with accumulation of yellowish or pale deposits beneath the retinal pigment epithelium (RPE) in the macular area",
# "non-exudative age related macular degeneration with drusen with drusen can appear as discrete dots, confluent patches, or diffuse deposits",
# "non-exudative age related macular degeneration with drusen with larger drusen and confluent drusen are associated with an increased risk of progression to advanced AMD",
# "non-exudative age related macular degeneration with Geographic atrophy (GA) with well-demarcated areas of RPE and choriocapillaris atrophy, typically appearing as sharply delineated areas of depigmentation or hypopigmentation",
# "non-exudative age related macular degeneration with retinal pigment epithelium (RPE) changes with hyperpigmentation or hypopigmentation of the RPE in the macular area",
# "non-exudative age related macular degeneration with retinal pigment epithelium (RPE) changes with RPE disturbance or clumping",
# "non-exudative age related macular degeneration with choroidal vessels with increased visibility or prominence of the underlying choroidal vasculature due to RPE atrophy or thinning",
# "non-exudative age related macular degeneration with foveal involvement with involvement of the foveal avascular zone (FAZ) or foveal center by drusen, atrophy, or pigmentary changes",
# "non-exudative age related macular degeneration with retinal thinning with thinning or atrophy of the neurosensory retina in areas of geographic atrophy",
# "non-exudative age related macular degeneration with pseudodrusen with yellowish or pale deposits that may be visible underneath the RPE, often arranged in a reticular or ribbon-like pattern"],



#GPT
    # "non-exudative age related macular degeneration": [
    #     "non-exudative age related macular degeneration with hard and soft drusen with small yellow or white deposits beneath the retina",
    #     "non-exudative age related macular degeneration with pigment epithelial with changes in the pigmentation of the retinal pigment epithelium",
    #     "non-exudative age related macular degeneration with pigmentary disturbances with changes in the pigmentation of the retinal pigment epithelium",
    #     "non-exudative age related macular degeneration with geographic atrophy with atrophy and thinning of the retinal layers",
    #     "non-exudative age related macular degeneration with drusen with yellowish-white spots",
    #     "non-exudative age related macular degeneration with map-like atrophy of the retina and choroid"],





#LLAMA2
#
# "exudative age related macular degeneration":[
# "exudative age related macular degeneration Exudates with Exudative age-related macular degeneration can cause exudates, which appear as small, round or oval-shaped yellow or white lesions in the retina."
#
# "exudative age related macular degeneration Exudates with Retinal pigment epithelial abnormalities with Exudative age-related macular degeneration can cause abnormalities in the retinal pigment epithelium, such as a bull eye appearance or a sunburst pattern."
#
# "exudative age related macular degeneration Exudates with RPE atrophy with Exudative age-related macular degeneration can cause atrophy of the retinal pigment epithelium, which can appear as a loss of the normal dark pigmentation in the retina."
#
# "exudative age related macular degeneration Exudates with Foveal thickening with Exudative age-related macular degeneration can cause the fovea to appear thicker than normal."
#
# "exudative age related macular degeneration Exudates with Foveal pit with Exudative age-related macular degeneration can cause a foveal pit, which appears as a small, round or oval-shaped depression in the fovea."
#
# "exudative age related macular degeneration Exudates with Vitreomacular traction with Exudative age-related macular degeneration can cause vitreomacular traction, which can cause the retina to appear pulled or distorted."
#
# "exudative age related macular degeneration Exudates with Retinal hemorrhages with Exudative age-related macular degeneration can cause retinal hemorrhages, which appear as small, round or oval-shaped red lesions in the retina."
#
# "exudative age related macular degeneration Exudates with Retinal edema with Exudative age-related macular degeneration can cause retinal edema, which appears as a saucer-like appearance or cobblestone appearance."
#
# "exudative age related macular degeneration Exudates with Retinal pigment epithelial hyperplasia with Exudative age-related macular degeneration can cause hyperplasia of the retinal pigment epithelium, which can appear as a dark, irregular area in the retina."
# ],



#Gemini3
"exudative age related macular degeneration":[


"exudative age related macular degeneration with Early Signs with Drusen (small, yellow deposits)",
"exudative age related macular degeneration with Early Signs with Pigmentary changes in the retinal pigment epithelium (RPE)",
"exudative age related macular degeneration with Early Signs with Subretinal fluid (SRF)",
"exudative age related macular degeneration with Early Signs with Clear or yellowish fluid beneath the retina",
"exudative age related macular degeneration with Early Signs with May be localized or diffuse",


"exudative age related macular degeneration with Intermediate Signs with Increased amount of SRF",
"exudative age related macular degeneration with Intermediate Signs with Hard exudates (yellowish-white deposits)",
"exudative age related macular degeneration with Intermediate Signs with Retinal hemorrhages",
"exudative age related macular degeneration with Intermediate Signs with RPE detachment",
"exudative age related macular degeneration with Advanced Signs with Extensive SRF involving the central macula",
"exudative age related macular degeneration with Advanced Signs with Geographic atrophy (GA)",
"exudative age related macular degeneration with Advanced Signs with Well-demarcated areas of RPE and photoreceptor loss",
"exudative age related macular degeneration with Advanced Signs with May develop in areas of previous SRF",


"exudative age related macular degeneration with Other Associated Findings with Choroidal neovascularization (CNV):",
"exudative age related macular degeneration with Other Associated Findings with New blood vessels beneath the retina",
"exudative age related macular degeneration with Other Associated Findings with May be visible as a dark red or brown lesion",
"exudative age related macular degeneration with Other Associated Findings with Epiretinal membrane",
"exudative age related macular degeneration with Other Associated Findings with Vitreous hemorrhage",


"exudative age related macular degeneration with Differential Diagnosis with Non-exudative AMD",
"exudative age related macular degeneration with Differential Diagnosis with Central serous chorioretinopathy",
"exudative age related macular degeneration with Differential Diagnosis with Retinal vein occlusion"],



#Claude3
# "exudative age related macular degeneration":[
# "exudative age related macular degeneration with subretinal fluid with accumulation of fluid between the neurosensory retina and the retinal pigment epithelium, causing elevation or detachment of the retina",
# "exudative age related macular degeneration with subretinal fluid with appears as a gray-green or yellow-green area of elevation or blurring of the retinal details",
# "exudative age related macular degeneration with intraretinal fluid with fluid accumulation within the neurosensory retina, causing retinal thickening and cystic spaces",
# "exudative age related macular degeneration with hemorrhages with subretinal or intraretinal hemorrhages, often appearing as irregular or splinter-shaped lesions in the macular area",
# "exudative age related macular degeneration with lipid exudates with Bright yellow or white lipid deposits, often arranged in a ring or circular pattern around the macular area",
# "exudative age related macular degeneration with retinal pigment epithelial detachment with Elevation or detachment of the RPE, often appearing as a well-defined, dome-shaped elevation with a smooth or irregular surface",
# "exudative age related macular degeneration with choroidal neovascularization with abnormal growth of new blood vessels originating from the choroid, which can appear as a gray-green or reddish-brown lesion beneath the retina",
# "exudative age related macular degeneration with choroidal neovascularization with may be associated with subretinal hemorrhage or fluid"
# "exudative age related macular degeneration with fibrovascular pigment epithelial detachment (PED) with elevation or detachment of the RPE, with a fibrovascular component and possible subretinal hemorrhage or fluid accumulation",
# "exudative age related macular degeneration with macular scar or disciform scar with in long-standing or advanced cases, a well-defined area of fibrosis or scarring in the macular area, often associated with retinal pigment epithelial atrophy or geographic atrophy"],


#GPT
    # "exudative age related macular degeneration": [
    #     "exudative age related macular degeneration with subretinal fluid with accumulation of fluid beneath the retina",
    #     "exudative age related macular degeneration with serous or hemorrhagic pigment epithelial detachment",
    #     "exudative age related macular degeneration with choroidal neovascularization with the formation of abnormal blood vessels beneath the retina",
    #     "exudative age related macular degeneration with retinal edema with swelling and morphological changes in the macular regio",
    #     "exudative age related macular degeneration with hemorrhage with red or dark red spots beneath the retina",
    #     "exudative age related macular degeneration with exudation with yellow or white fluid deposits beath the retina",
    #     "exudative age related macular degeneration with fibrotic scarring with prolonged presence of exudates and hemorrhages ",
    #     "exudative age related macular degeneration with disciform degeneration with the presence of a well-defined scar or fibrous tissue in the macular region."],





# LLAMA2-PM
"degenerative myopia":[

"degenerative myopia with Retinal pigment epithelial abnormalities with Degenerative myopia can cause abnormalities in the retinal pigment epithelium, such as a bull eye appearance or a sunburst pattern",

"degenerative myopia with Foveal thinning with Degenerative myopia can cause the fovea to appear thinner than normal.",

"degenerative myopia with Foveal pit with Degenerative myopia can cause a foveal pit, which appears as a small, round or oval-shaped depression in the fovea.",

"degenerative myopia with Vitreomacular traction with Degenerative myopia can cause vitreomacular traction, which can cause the retina to appear pulled or distorted.",
"degenerative myopia with Retinal hemorrhages with Degenerative myopia can cause retinal hemorrhages, which appear as small, round or oval-shaped red lesions in the retina.",

"degenerative myopia with Retinal edema with Degenerative myopia can cause retinal edema, which appears as a saucer-like appearance or cobblestone appearance",

"degenerative myopia with Retinal pigment epithelial hyperplasia with Degenerative myopia can cause hyperplasia of the retinal pigment epithelium, which can appear as a dark, irregular area in the retina.",

"degenerative myopia with Retinal vasculature abnormalities with Degenerative myopia can cause abnormalities in the retinal vasculature, such as tortuosity, dilatation, and irregularity of the vessels.",

"degenerative myopia with Optic disc edema with Degenerative myopia can cause optic disc edema, which appears as a swelling of the optic disc."
],


#Gemini-pro

# "degenerative myopia":[
# "degenerative myopia with Posterior Staphyloma with Bulging of the posterior pole of the eye",
# "degenerative myopia with Posterior Staphyloma with May be localized or diffuse",
# "degenerative myopia with Retinal Atrophy with Thinning of the retina, especially in the macular area",
# "degenerative myopia with Retinal Atrophy with May have a pale or grayish appearance",
# "degenerative myopia with Myopic Crescent with Crescent-shaped area of temporal retinal atrophy adjacent to the optic disc",
# "degenerative myopia with Peripapillary Atrophy with Atrophy of the retina surrounding the optic disc",
# "degenerative myopia with Choroidal Changes with Choroidal thinning",
# "degenerative myopia with Choroidal Changes with Choroidal neovascularization (CNV) may be present",
# "degenerative myopia with Other Associated Findings with Macular hole",
# "degenerative myopia with Other Associated Findings with Retinal detachment",
# "degenerative myopia with Other Associated Findings with Glaucoma"
# ],


#Claude3
# "degenerative myopia":
# ["degenerative myopia with posterior staphyloma with outpouching or protrusion of the posterior fundus, often appearing as a localized area of distortion or thinning"
# "degenerative myopia with myopic crescent or peripapillary atrophy with A crescent-shaped area of atrophy or depigmentation surrounding the optic disc, often associated with tilting or torsion of the optic disc"
# "degenerative myopia with lacquer cracks with Linear or branching yellow-white lesions, representing areas of localized choroidal atrophy or Bruch membrane defects"
# "degenerative myopia with patchy chorioretinal atrophy with Irregular areas of atrophy or depigmentation of the retinal pigment epithelium and choriocapillaris"
# "degenerative myopia with myopic choroidal neovascularization with Abnormal growth of new blood vessels originating from the choroid, often appearing as a gray-green or reddish-brown lesion beneath the retina"
# "degenerative myopia with myopic choroidal neovascularization with May be associated with subretinal hemorrhage or fluid"
# "degenerative myopia with fuchs spot with A well-defined, round or oval area of RPE atrophy, often located in the macular area or along the arcades"
# "degenerative myopia with straightened or stretched retinal vessels with Retinal vessels appearing elongated or straightened due to the stretching and thinning of the retina"
# "degenerative myopia with tilted or torted optic disc with abnormal orientation or tilting of the optic disc, often associated with myopic crescent or peripapillary atrophy"],

#GPT
    # "degenerative myopia": ["degenerative myopia with myopic maculopathy with thinning of the macula, pigmentary alterations and lacquer cracks",
    #                         "degenerative myopia with choroidal thinning with the vascular layer beneath the retina thinning",
    #                         "degenerative myopia with staphyloma formation with abnormal bulging or stretching of the sclera",
    #                         "degenerative myopia with optic disc changes with tilting, stretching, and increased visibility of the optic nerve",
    #                         "degenerative myopia with foveal changes with thinning and atrophy changes in the fovea",
    #                         "degenerative myopia with macular holes and tears with the formation of macular holes or retinal tears",
    #                         "degenerative myopia with macular hemorrhage with red or dark spots"],









    "age-related macular degeneration": ["age-related macular degeneration with drusen formation with the presence of small yellow or white deposits beneath the retina",
                                         "age-related macular degeneration with drusen formation with drusen appear as discrete spots in the macular region of the fundus"
                                         "age-related macular degeneration with macular changes with drusen accumulation particularly affects the macula, the central part of the retina responsible for sharp, central vision",
                                         "age-related macular degeneration with macular changes with changes in macular pigmentation may occur, contributing to alterations in fundus appearance"
                                         "age-related macular degeneration with geographic atrophy with advanced AMD may lead to geographic atrophy, involving the loss of retinal pigment epithelium cells",
                                         "age-related macular degeneration with geographic atrophy with manifests as well-defined areas of retinal degeneration",
                                         "age-related macular degeneration with choroidal neovascularization with abnormal blood vessels grow beneath the retina",
                                         "age-related macular degeneration with choroidal neovascularization with  leakage of fluid or blood, causing sudden vision changes",
                                         "age-related macular degeneration with pigmentary changes with changes in fundus pigmentation, such as hyperpigmentation or hypopigmentation, are observed in AMD",
                                         "age-related macular degeneration with macular edema with fluid accumulation in the macula, known as macular edema, can occur, affecting vision",
                                         "age-related macular degeneration with retinal pigment epithelium with atrophy or degeneration of the retinal pigment epithelium is a characteristic feature of AMD",
                                         "age-related macular degeneration with loss of central vision with AMD primarily impacts central vision, leading to difficulties with tasks like reading and recognizing faces"],

    'media haze': ["media haze with blurred appearance with observe if there is an overall blurry or hazy appearance in the fundus image",
                   "media haze with retinal structure examination with check the clarity of retinal structures in the fundus image, assessing if they are affected by media haze",
                   "media haze with transparency assessment with evaluate the transparency of transparent media (such as cornea, lens, and vitreous) in the fundus image, checking for reduced transparency",
                   "media haze with iris examination with examine the details of the iris to see if there are unclear or blurry features",
                   "media haze with observation of light scattering effects with observe if there is a light scattering effect, leading to a shading effect on the fundus image",
                   "media haze with image quality assessment with assess the quality of the fundus image to understand if the image is not clear enough due to media haze",
                   "media haze with difficulty in identifying fundus details with note if details of the fundus are difficult to discern, potentially due to media haze",
                   "media haze with assessment of decreased visibility with look for areas on the fundus image where visibility may be reduced due to media haze",
                   "media haze with understanding potential causes with understand potential causes of media haze, such as cataracts, corneal opacities, or other vitreous abnormalities",
                   "media haze with vision impairment with consider whether the patient has symptoms of vision impairment associated with the observed fundus features"],

    "drusens": ["drusens with identification with identify the presence of small, yellow-white deposits known as drusens in the fundus image",
                "drusens with size assessment with assess the size of drusens, noting whether they appear small, medium, or large in the fundus image",
                "drusens with distribution examination with examine the distribution pattern of drusens across the retina, checking if they are clustered or scattered",
                "drusens with border characteristics with observe the borders of drusens to determine if they have well-defined or indistinct edges",
                "drusens with color analysis with analyze the color of drusens, typically appearing as yellow or white spots in the fundus image",
                "drusens with proximity to macula or optic nerve with note the proximity of drusens to the macula and optic nerve head, as their location can impact vision",
                "drusens with fundus autofluorescence examination with consider using fundus autofluorescence imaging to assess the autofluorescent properties of drusens",
                "drusens with optical coherence tomography confirmation with confirm the presence of drusens using optical coherence tomography for detailed cross-sectional imaging",
                "drusens with patient medical history with inquire about the patient's medical history, including any previous diagnoses or family history of drusens",
                "drusens with comprehensive eye examination with conduct a comprehensive eye examination to rule out other potential retinal conditions and confirm the diagnosis"],


    "myopia": [
"myopia with optic disc characteristics with a tilted or elongated appearance indicating axial elongation",
"myopia with retinal blood vessel features with increased tortuosity or abnormal courses",
"myopia with macular observations with myopic macular degeneration or presence of a posterior staphyloma",
"myopia with peripapillary atrophy with crescent-shaped chorioretinal atrophy around the optic disc",
"myopia with fundus tessellation with a mottled appearance in the periphery",
"myopia with choroidal thinning signs with thinning of the choroid, especially in the posterior pole",
"myopia with foveal changes manifestation with myopic changes like lacquer cracks or myopic foveoschisis",
"myopia with axial length estimation with indirect estimation of increased axial length by assessing the distance between the optic disc and fovea"],

"branch retinal vein occlusion": ["branch retinal vein occlusion with retinal hemorrhages with presence of flame-shaped or dot/blot hemorrhages in the affected quadrant of the retina",
"branch retinal vein occlusion with cotton-wool spots with identification of soft, fluffy, white lesions indicating ischemic areas",
"branch retinal vein occlusion with dilated and tortuous veins with observation of enlarged and twisted retinal veins in the affected region",
"branch retinal vein occlusion with macular edema with detection of fluid accumulation in the macular area, leading to swelling",
"branch retinal vein occlusion with hard exudates with visualization of yellowish deposits around the macula, suggesting lipid leakage",
"branch retinal vein occlusion with capillary non-perfusion, recognition of areas with reduced or absent blood flow, indicative of ischemia",
"branch retinal vein occlusion with optic disc swelling, presence of disc edema, often associated with severe cases or ischemic complications",
"branch retinal vein occlusion with venous sheathing, noting the thickening and sclerosis of retinal veins in the affected quadrant",
"branch retinal vein occlusion with collateral vessel formation, identification of new vessels as a response to the occluded vein, especially at the periphery",
"branch retinal vein occlusion with macular ischemia, assessment of decreased perfusion in the macular area, contributing to visual impairment"],



"tessellation": [
"tessellation with geographic atrophy: identification of well-defined areas of retinal pigment epithelium (RPE) loss, leading to a map-like appearance on the fundus",
"tessellation with drusen: presence of small, yellowish deposits between the RPE and Bruchs membrane, indicating early stages of age-related macular degeneration",
"tessellation with pigmentary changes: observation of alterations in retinal pigmentation, including hypo- or hyperpigmented areas, contributing to the tessellated pattern",
"tessellation with choroidal neovascularization (CNV): detection of abnormal blood vessel growth beneath the retina, often associated with exudative or wet macular degeneration",
"tessellation with reticular pseudodrusen: recognition of yellowish subretinal deposits forming a network pattern, distinct from conventional drusen",
"tessellation with outer retinal tubulations: visualization of tubular structures in the outer retina, indicative of degenerative changes in photoreceptor cells",
"tessellation with retinal thinning: measurement of reduced retinal thickness, especially in the macular area, contributing to the tessellated appearance",
"tessellation with ellipsoid zone disruption: identification of disruptions in the ellipsoid zone on optical coherence tomography, reflecting structural damage in the retina",
"tessellation with subretinal fluid: presence of fluid accumulation beneath the retina, often associated with macular diseases and contributing to the tessellation pattern",
"tessellation with visual field defects: correlation of the tessellated fundus pattern with specific visual field abnormalities, aiding in the overall diagnostic assessment"],

# "laser scar": [
# "laser scar with well-defined borders: identification of a distinct area on the fundus with clear demarcation from the surrounding retina",
# "laser scar with hyperpigmentation: observation of darker pigmentation within the scarred region, indicative of altered melanin content",
# "laser scar with tissue atrophy: recognition of thinning and loss of retinal tissue in the scarred area, contributing to the overall structural changes",
# "laser scar with vascular changes: noting alterations in blood vessel patterns or disruption within the scar, reflecting the impact on retinal vasculature",
# "laser scar with loss of retinal architecture: visualization of disruptions in the normal retinal layers and structures, especially in the scarred region",
# "laser scar with choroidal changes: detection of modifications in the choroid beneath the scar, potentially affecting blood supply and tissue support",
# "laser scar with scarring-related distortion: observation of distortion in the surrounding retinal anatomy due to the presence of the laser scar",
# "laser scar with absence of normal fluorescence: using fundus autofluorescence imaging to identify areas where the laser scar shows reduced or altered autofluorescence",
# "laser scar with visual field defects: correlation of the laser scar location with specific visual field abnormalities, contributing to the diagnostic evaluation",
# "laser scar with history of laser treatment: consideration of the patient's medical history, particularly any documented laser procedures, to contextualize the presence of the scar on the fundus"],


"laser scar": [
"laser scar with round or oval, yellowish-white with variable black pigment centrally",
"laser scar with 50 to 200 micron diameter lesions"
],



"macular scar" :["macular scar with central atrophy: identification of a region in the macula exhibiting significant tissue loss and retinal thinning",
"macular scar with pigment alterations: observation of changes in pigmentation, such as hypo- or hyperpigmented areas within the scarred macula",
"macular scar with disrupted retinal layers: visualization of irregularities or interruptions in the normal layering of the retina, indicating structural damage",
"macular scar with surrounding fibrosis: noting the presence of fibrotic tissue around the macular scar, contributing to the overall pathology",
"macular scar with photoreceptor loss: detection of a decrease in the number of photoreceptor cells in the scarred macular region",
"macular scar with distortion of foveal architecture: recognizing alterations in the central foveal structure due to the presence of the scar",
"macular scar with scarring-related vascular changes: identification of modifications in retinal blood vessels associated with the scarred macula",
"macular scar with fluorescein angiography abnormalities: using angiography to reveal any abnormal blood flow patterns or leakage around the macular scar",
"macular scar with disrupted ellipsoid zone on OCT: visualization of interruptions in the ellipsoid zone on optical coherence tomography, indicative of structural damage",
"macular scar with visual acuity changes: correlation of the macular scar location and size with documented changes in visual acuity, providing crucial diagnostic insights"],



"central serous retinopathy":[" with serous retinal detachment: identification of localized detachment of the neurosensory retina, typically in the macular region",
"central serous retinopathy with macular edema: detection of fluid accumulation in the macula, leading to swelling and potential distortion of the central vision",
"central serous retinopathy with pigment epithelial changes: observation of alterations in the retinal pigment epithelium (RPE) layer, often manifesting as RPE detachments or irregularities",
"central serous retinopathy with choroidal hyperpermeability: noting increased permeability of choroidal vessels, leading to subretinal fluid accumulation",
"central serous retinopathy with focal leakage on fluorescein angiography: visualization of dye leakage from choroidal vessels into the subretinal space, indicating active disease",
"central serous retinopathy with bullous retinal elevation: recognition of large, blister-like elevations in the retina due to accumulated subretinal fluid",
"central serous retinopathy with RPE window defects: identification of areas where the RPE appears window-like or atrophic, allowing visualization of choroidal vasculature",
"central serous retinopathy with mottled hyperautofluorescence: using fundus autofluorescence to reveal irregular areas of increased and decreased autofluorescence within the affected region",
"central serous retinopathy with decreased central macular thickness on OCT: measurement of reduced thickness in the central macula due to subretinal fluid accumulation",
"central serous retinopathy with symptoms of metamorphopsia or micropsia: consideration of patient-reported visual distortions, such as straight lines appearing wavy or objects seeming smaller than they are"],

"optic disc cupping":["optic disc cupping with increased cup-to-disc ratio: assessment of the ratio between the size of the cup (central depression) and the overall optic disc diameter, with an enlarged cup",
"optic disc cupping with thinning of neuroretinal rim: observation of a decrease in the thickness of the neuroretinal rim, the tissue surrounding the optic cup",
"optic disc cupping with notching: identification of a distinct notch or depression in the rim of the optic disc, often associated with glaucomatous damage",
"optic disc cupping with asymmetry between the two eyes: noting a significant difference in cupping appearance between the optic discs of the two eyes",
"optic disc cupping with pallor of the neuroretinal rim: visualization of a pale or whitened appearance in the neuroretinal rim due to reduced nerve fiber layer thickness",
"optic disc cupping with vascular changes: recognition of alterations in the pattern and appearance of blood vessels on the optic disc surface",
"optic disc cupping with peripapillary atrophy: presence of atrophic changes in the tissue surrounding the optic disc, often accompanied by pigmentary changes",
"optic disc cupping with glaucomatous visual field defects: correlation of the cupping findings with specific visual field abnormalities characteristic of glaucoma",
"optic disc cupping with disc hemorrhages: identification of small hemorrhages on or around the optic disc, which may indicate glaucomatous damage",
"optic disc cupping with progressive changes over time: comparison of current fundus findings with previous images to assess the progression of optic disc cupping and potential glaucomatous damage"],


"central retinal vein occlusion": ["central retinal vein occlusion with retinal hemorrhages: presence of flame-shaped or dot/blot hemorrhages scattered throughout the retina, especially in the posterior pole",
"central retinal vein occlusion with cotton-wool spots: identification of soft, fluffy, white lesions indicating areas of retinal ischemia",
"central retinal vein occlusion with macular edema: detection of fluid accumulation in the macular region, leading to central vision impairment",
"central retinal vein occlusion with dilated and tortuous veins: observation of enlarged and twisted retinal veins, particularly in the posterior pole",
"central retinal vein occlusion with optic disc edema: presence of swelling at the optic disc, often referred to as disc edema or papilledema",
"central retinal vein occlusion with widespread retinal ischemia: recognition of extensive areas of reduced blood flow and perfusion in the retina",
"central retinal vein occlusion with venous congestion: noting congestion and engorgement of retinal veins due to impaired blood outflow",
"central retinal vein occlusion with cherry-red spot on macula: identification of a cherry-red spot at the fovea, contrasting against the ischemic, pale retina",
"central retinal vein occlusion with collateral vessel formation: visualization of new vessels as a compensatory response to the occluded vein, especially in the periphery",
"central retinal vein occlusion with visual field defects: correlation of fundus findings with specific visual field abnormalities, contributing to the overall diagnostic assessment"],


"tortuous vessels":["tortuous vessels with identification of abnormality: examine the fundus image for the presence of blood vessels displaying abnormal winding or twisting, indicating tortuosity",
"tortuous vessels with distribution pattern: assess the distribution pattern of the tortuous vessels, considering whether they are localized to a specific area or involve a more widespread portion of the retina",
"tortuous vessels with comparison to normal vessels: compare the suspected tortuous vessels with adjacent normal vessels to highlight the extent of deviation from the typical vascular architecture",
"tortuous vessels with vessel caliber changes: look for changes in the caliber of the tortuous vessels, as abnormal dilations or constrictions may provide additional diagnostic information",
"tortuous vessels with impact on surrounding structures: evaluate whether the tortuous vessels exert any pressure or have an impact on neighboring structures, such as the optic nerve or macula"],


"asteroid hyalosis":["asteroid hyalosis with numerous small, reflective, yellow-white opacities in the vitreous humor: presence of multiple tiny, reflective opacities distributed throughout the vitreous humor",
"asteroid hyalosis with dense, spherical bodies resembling stellate or star-like patterns: observation of compact, spherical opacities with a characteristic star-like appearance",
"asteroid hyalosis with opacities casting shadows on the retina: identification of shadows cast by the opacities on the underlying retina, often visible during fundus examination",
"asteroid hyalosis with opacities exhibiting minimal impact on visual acuity: typically, these opacities have a limited effect on visual function, as they are situated in the vitreous rather than directly on the retina"],


# "optic disc pallor":["optic disc pallor with thinning and paleness of the optic disc rim: thinning and a pale appearance of the rim surrounding the optic disc",
# "optic disc pallor with loss of normal pink coloration: absence of the usual pink hue typically seen in a healthy optic disc",
# "optic disc pallor with sharp demarcation between the pale optic disc and surrounding retina: clear distinction between the pale optic disc and the adjacent retinal tissue",
# "optic disc pallor with decreased visibility of blood vessels on the optic disc: reduced prominence and visibility of blood vessels within the optic disc due to the pallor",
# "optic disc pallor with associated optic nerve atrophy: often indicative of optic nerve atrophy, where the nerve fibers become damaged, leading to a reduction in disc color",
# "optic disc pallor with involvement of one or both optic discs: the condition can affect either one or both optic discs, and the extent of pallor may vary"],
#

"optic disc pallor":["optic disc pallor with pale yellow discoloration that can be segmental or generalized on optic disc"],


"optic disc edema":["optic disc edema with blurring of the optic disc margins: presence of indistinct or blurred margins of the optic disc due to swelling",
"optic disc edema with hyperemia or engorgement of blood vessels on the optic disc: increased visibility and dilation of blood vessels on the surface of the optic disc",
"optic disc edema with elevation of the optic disc surface: a raised appearance of the optic disc, indicating fluid accumulation and swelling",
"optic disc edema with loss of physiological cupping: diminished or absent cupping, the normal depression at the center of the optic disc, due to increased intrapapillary pressure",
"optic disc edema with peripapillary hemorrhages: presence of hemorrhages in the surrounding region of the optic disc, often a sign of increased pressure within the optic nerve head",
"optic disc edema with associated cotton-wool spots: presence of cotton-wool spots in the vicinity of the optic disc, indicating localized retinal ischemia associated with the edema"],


# "shunt":["shunt with retinal vessel dilation: enlargement of retinal vessels, particularly veins, indicating increased blood flow through the shunt",
# "shunt with tortuous and engorged blood vessels: winding and swollen appearance of blood vessels, suggesting abnormal blood flow dynamics",
# "shunt with localized area of vessel congestion: presence of a specific region where blood vessels appear congested and engorged",
# "shunt with retinal hemorrhages: occurrence of bleeding within the retinal tissue due to the altered blood flow through the shunt",
# "shunt with presence of microaneurysms: small bulging areas on the retinal vessels, indicating weakened vessel walls and potential shunting",
# "shunt with distorted or irregular foveal avascular zone (FAZ): changes in the central retinal area due to altered blood flow patterns, often seen in the presence of a shunt",
# "shunt with associated exudates: accumulation of fluid and lipid deposits in the retina, possibly indicating vascular leakage associated with the shunt",
# "shunt with retinal ischemia in surrounding areas: reduced blood supply leading to localized retinal ischemia, particularly in regions adjacent to the shunt"],

"optociliary shunt vessels": [
"optociliary shunt vessels with collateral vessels connecting the choroidal and the retinal vasculature",
"optociliary shunt vessels with collateral vessels of large caliber and lack of leakage",
"optociliary shunt vessels with tortuous vascular loops that start and end on the disc",
"optociliary shunt vessels with tortuous red small lines that start and end on the disc",
"collateral vessels connecting the choroidal and the retinal vasculature",
                         "collateral vessels of large caliber and lack of leakage"
                              ],



# "anterior ischemic optic neuropathy":["anterior ischemic optic neuropathy with segmental swelling of the optic disc: localized swelling of the optic disc, often seen in a segmental or partial manner",
# "anterior ischemic optic neuropathy with pale or edematous appearance of the optic nerve head: the optic disc may appear pale or edematous due to compromised blood supply",
# "anterior ischemic optic neuropathy with optic disc hyperemia: increased redness or hyperemia of the optic disc, indicating possible inflammation or ischemia",
# "absence of optic disc hemorrhages: unlike some other optic neuropathies, anterior ischemic optic neuropathy typically lacks hemorrhages on or around the optic disc",
# "disc edema with peripapillary hemorrhages (in some cases): presence of hemorrhages in the peripapillary region, though not a consistent feature, may be observed in certain cases",
# "disc edema with cotton-wool spots: cotton-wool spots may be present, reflecting localized retinal ischemia associated with optic nerve head swelling",
# "anterior ischemic optic neuropathy with sectoral or diffuse nerve fiber layer infarction: infarction or damage to the nerve fiber layer, observed as localized or diffuse darkening or pallor",
# "associated visual field defects: examination of the fundus may not directly reveal visual field defects, but correlation with visual field testing is crucial for a comprehensive diagnosis"],


"anterior ischemic optic neuropathy":[
"anterior ischemic optic neuropathy with swelling optic disc with the edema can be either segmental or diffuse",
"anterior ischemic optic neuropathy with pale or edematous appearance of the optic nerve head with the optic disc may appear pale or edematous due to compromised blood supply",
"anterior ischemic optic neuropathy with optic disc hyperemia with increased redness or hyperemia of the optic disc, indicating possible inflammation or ischemia",
"anterior ischemic optic neuropathy with accompanying hemorrhages with linear or flame-shaped red bleeding around the optic disc",
"anterior ischemic optic neuropathy with swollen, pale or anamolous optic discc with blurring yellow optic discc"],




# "parafoveal telangiectasia":["parafoveal telangiectasia with telangiectatic vessels: identification of abnormal, dilated blood vessels near the fovea, often appearing as small, tortuous vessels",
# "parafoveal telangiectasia with right-angled venules: presence of venules that exhibit a right-angled turn, a characteristic feature of parafoveal telangiectasia",
# "parafoveal telangiectasia with retinal crystalline deposits: observation of crystalline-like deposits within the retina, a distinctive finding associated with this condition",
# "parafoveal telangiectasia with absence of macular edema: unlike some other retinal conditions, parafoveal telangiectasia typically presents without significant macular edema",
# "parafoveal telangiectasia with mild-to-moderate retinal atrophy: progressive thinning of the retina, particularly in the parafoveal region, indicating the stage of the disease",
# "parafoveal telangiectasia with reduced capillary density: a decrease in the density of capillaries in the affected area, contributing to altered blood flow patterns",
# "parafoveal telangiectasia with pigmentary changes: alterations in retinal pigmentation, including pigment clumping or migration, as the disease progresses",
# "parafoveal telangiectasia with subtle fluorescein angiography findings: the use of fluorescein angiography may reveal subtle abnormalities in the parafoveal region, aiding in the diagnosis of parafoveal telangiectasia"],

# "parafoveal telangiectasia":[
# "parafoveal telangiectasia with yellow, lipid-rich exudation or parafoveal graying or abnormalities from distention and tortuous blood vessels (ectatic)",
# "parafoveal telangiectasia with incompetent retinal capillaries in the juxtafoveolar region",
#                              ],
#


"parafoveal telangiectasia":[
"parafoveal telangiectasia with yellow, lipid-rich exudation or parafoveal graying or abnormalities from fovea",
"parafoveal telangiectasia with gray or yellow abnormalities in fovea",
"parafoveal telangiectasia with gray or yellow abnormalities in macula"
],



# "retinal traction":["retinal traction with distorted retinal vessels: observation of distortion or stretching of retinal vessels due to the traction forces exerted on the retina",
# "retinal traction with focal or diffuse retinal elevation: presence of localized or widespread elevation of the retina, indicative of traction-induced changes",
# "retinal traction with wrinkling or folding of the retinal surface: appearance of fine or coarse wrinkles on the retinal surface due to traction forces",
# "retinal traction with tractional retinal detachment: identification of retinal detachment caused by the pulling forces exerted on the retina",
# "retinal traction with macular involvement: involvement of the macular region, leading to distortion or displacement of the macula",
# "retinal traction with epiretinal membrane formation: development of a membrane on the surface of the retina due to the traction forces, often contributing to the observed retinal changes",
# "retinal traction with distortion of the optic disc: changes in the shape or displacement of the optic disc caused by the traction forces",
# "retinal traction with presence of vitreoretinal interface abnormalities: identification of abnormalities at the vitreoretinal interface, such as vitreomacular adhesion or vitreomacular traction, contributing to retinal traction"],

"retinal traction":[
"retinal traction with yellow line around",
"retinal traction with blurring yellow line",
"retinal traction with with retinal folds with the appearance of folds, manifesting as wrinkled or undulating patterns on the retina, observable on the fundus image",
"retinal traction with with disapperance of retinal vessels with distort the surrounding retinal blood vessels",
"retinal traction with retinal traction may result in the rupture of blood vessels within the vitreous, leading to vitreous hemorrhage with hemorrhages within the red spot",
"retinal traction with retinal tears with irregular defects and signs of retinal detachment",
"retinal traction with retinal detachment with signs of retinal separation, characterized by wrinkling, undulating changes, and possible holes and vitreous hemorrhage"],



# "retinitis":["retinitis with white, fluffy exudates: presence of white, fluffy exudates on the retina, indicative of inflammatory changes associated with retinitis",
# "retinitis with retinal hemorrhages: identification of hemorrhages on the retina, suggesting vascular involvement and inflammation",
# "retinitis with focal areas of retinal whitening: localized areas of whitening on the retina, corresponding to regions of active inflammation",
# "retinitis with blurred or indistinct retinal vessels: vessels appearing hazy or less distinct due to inflammatory changes in the surrounding tissue",
# "retinitis with perivascular sheathing: presence of inflammation around retinal blood vessels, often visible as a sheathing effect",
# "retinitis with optic disc swelling: swelling of the optic disc, indicating involvement of the optic nerve head in the inflammatory process",
# "retinitis with macular involvement: inflammation affecting the macular region, leading to potential visual impairment",
# "retinitis with the presence of inflammatory cells in the vitreous: identification of inflammatory cells, such as cells or debris, within the vitreous humor, further supporting the diagnosis of retinitis"],

"retinitis":["retinitis with vitreous inflammation",
             "retinitis with intraretinal hemorrhage ",
"retinitis with macular star",
"retinitis with phlebitis",
"retinitis with arteritis",
"retinitis withhyperemic disc",
"retinitis with white, fluffy exudates: presence of white, fluffy exudates on the retina",
             ],



"chorioretinitis":["chorioretinitis with focal areas of retinal whitening: localized areas of whitening on the retina, indicating inflammation and damage to the choroid and retina",
"chorioretinitis with irregular borders and fuzzy margins: presence of lesions with indistinct edges, often characterized by fuzzy margins due to inflammatory changes",
"chorioretinitis with inflammation of choroid and retina"

],



"exudation":["exudation with localized or diffuse retinal thickening with identification of areas where the retina appears thicker than normal, indicating fluid accumulation",
"exudation with white or yellowish lipid deposits with presence of fluffy, white lesions on the retina, often associated with microinfarctions and white or yellow spots",
"exudation with exudates with accumulation of lipid or protein deposits on the retina, often appearing as yellowish lesions",
"exudation with macular involvement with swelling and fluid accumulation in the macular region, potentially leading to decreased visual acuity",
"exudation with hard exudates with deposition of lipid-rich material on the retina, often presenting as yellowish, well-defined lesions",
"exudation with optic disc swelling with swelling of the optic disc, indicating increased pressure within the eye and potential involvement of the optic nerve head",
"exudation with serous retinal detachment with separation of the neurosensory retina from the underlying retinal pigment epithelium due to the accumulation of serous fluid",
"small white or yellowish white deposits with sharp margins", "bright lesion"


             ],

# "retinal pigment epithelium changes":["retinal pigment epithelium changes with mottled or granular appearance: observation of irregular or grainy alterations in the retinal pigment epithelium (RPE), often indicative of degenerative changes",
# "retinal pigment epithelium changes with hypo- or hyperpigmented patches: areas of the RPE displaying either lighter (hypopigmented) or darker (hyperpigmented) pigmentation compared to the surrounding tissue",
# "retinal pigment epithelium changes with presence of drusen: identification of small, yellowish deposits beneath the RPE, a common sign of age-related macular degeneration",
# "retinal pigment epithelium changes with geographic atrophy: development of well-defined areas of RPE loss, often leading to corresponding retinal thinning",
# "retinal pigment epithelium changes with pigment clumping: aggregation of pigmented material within the RPE layer, contributing to alterations in pigmentation",
# "retinal pigment epithelium changes with window defects: areas where the underlying choroidal vessels become visible due to RPE thinning or atrophy",
# "retinal pigment epithelium changes with alterations in autofluorescence patterns: variations in the natural fluorescence emitted by the RPE, detectable through imaging techniques like fundus autofluorescence",
# "retinal pigment epithelium changes with irregularities in the RPE layer: disruptions or irregularities in the normally smooth RPE layer, often associated with degenerative processes or diseases affecting the retina"],

"retinal pigment epithelium changes":["retinal pigment epithelium changes with increased thickness of Bruch’s membrane",
                                      "retinal pigment epithelium changes with loss of melanin granules",
                                      "retinal pigment epithelium changes with accumulation of lipofuscin",
                                      "retinal pigment epithelium changes with formation of drusen",
                                      "retinal pigment epithelium changes with increase in the density of residual bodies",
                                      "retinal pigment epithelium changes with accumulation of basal deposits on r within Bruch’s membrane",
                                      "retinal pigment epithelium changes with disorganization of the basal infoldings",
                                      "retinal pigment epithelium changes with microvilli atrophy"],



"macular hole":["macular hole with central foveal dehiscence with presence of a gap or opening in the central fovea, often observed as a well-defined break in the retinal tissue",
"macular hole with loss of foveal contour with flattening or distortion of the normal foveal shape, indicating structural changes associated with the macular hole",
"macular hole with small retinal break located in the center of the fovea",
                "macular hole with lesion in the macula",
                "macular hole with grayish fovea"],



# "retinitis pigmentosa":["retinitis pigmentosa with bone spicule-like pigmentation: presence of characteristic pigmentary changes resembling bone spicules, often distributed in the mid-peripheral and peripheral retina",
# "retinitis pigmentosa with attenuated retinal vessels: narrowing and attenuation of retinal blood vessels, particularly in the peripheral regions",
# "retinitis pigmentosa with waxy pallor of the optic disc: optic disc appearing pale and atrophic, indicating optic nerve head involvement",
# "retinitis pigmentosa with peripheral field constriction: visual field testing may reveal constriction, especially in the peripheral visual field, a common feature in retinitis pigmentosa",
# "retinitis pigmentosa with a ring of hyperautofluorescence: detection of a hyperautofluorescent ring on fundus autofluorescence imaging, often corresponding to the border of degenerated and preserved retina",
# "retinitis pigmentosa with macular involvement: although primarily a peripheral disease, macular changes may include atrophy, cystoid macular edema, or pigmentary alterations",
# "retinitis pigmentosa with a salt-and-pepper fundus appearance: description of a fundus appearance characterized by a mottled pattern of dark and light areas, resembling salt and pepper",
# "retinitis pigmentosa with rod-cone dystrophy: identification of a combined rod and cone photoreceptor dysfunction, leading to night blindness and progressive visual field loss"],
#


"retinitis pigmentosa":["retinitis pigmentosa with bone spicule-like pigmentation with presence of characteristic pigmentary changes resembling bone spicules, often distributed in the mid-peripheral and peripheral retina",
"retinitis pigmentosa with bone-spicule deposits with black lines around the retina ",
"retinitis pigmentosa with arterial narrowing with light red blood vessels narrowing"],

"cotton wool spots":["cotton wool spots with soft, fluffy edges: identification of soft-edged, white or off-white lesions on the retina, often associated with nerve fiber layer infarctions",
"cotton wool spots with nerve fiber layer thickening: thickening of the nerve fiber layer in areas surrounding the cotton wool spots, contributing to their characteristic appearance",
"cotton wool spots with blurred or indistinct retinal vessels: vessels appearing hazy or less distinct due to the presence of cotton wool spots along the course of the vessels",
"cotton wool spots with superficial retinal hemorrhages: associated hemorrhages on the retinal surface near the cotton wool spots, indicating localized ischemia",
"cotton wool spots with microinfarctions: small areas of tissue infarction, often seen as discrete patches adjacent to the cotton wool spots",
"cotton wool spots with asymmetrical distribution: uneven distribution of cotton wool spots throughout the retina, often more concentrated in specific areas",
"cotton wool spots with associated systemic conditions: consideration of underlying systemic conditions such as hypertension or diabetes, as cotton wool spots can be associated with these diseases",
"cotton wool spots with absence of hard exudates: differentiation from other retinal conditions, as cotton wool spots typically lack the presence of lipid-rich hard exudates"],


"colobomas":["colobomas with well-defined, excavated optic disc: identification of a well-defined, cup-shaped excavation of the optic disc, often larger than the physiological cup",
"colobomas with extension into the adjacent retina: presence of a gap or defect in the retinal tissue, extending from the optic disc towards the peripheral retina",
"colobomas with pigmentary changes: alterations in pigmentation within and around the colobomatous area, contributing to a distinctive appearance",
"colobomas with associated vascular changes: variations in retinal blood vessels, including tortuosity or anomalous branching patterns near the coloboma",
"colobomas with posterior staphyloma: a localized, outward bulging of the posterior eye wall often associated with colobomas, especially in the setting of high myopia",
"colobomas with adjacent choroidal thinning: thinning of the choroid in the region of the coloboma, visible as a darker area in fundus imaging",
"colobomas with peripapillary atrophy: the presence of atrophic changes surrounding the optic disc, often seen in conjunction with colobomas",
"colobomas with absence of retinal tissue at the colobomatous site: a clear void or absence of retinal tissue at the location of the coloboma, often visible on fundus examination"],


"optic disc pit":["optic disc pit maculopathy with peripapillary atrophy: observation of atrophic changes surrounding the optic disc, often extending into the adjacent retina",
"optic disc pit maculopathy with macular serous detachment: detection of serous retinal detachment in the macular region, commonly associated with fluid accumulation",
"optic disc pit maculopathy with schisis-like changes: identification of split-like changes or cavities in the layers of the macula, often visible on optical coherence tomography (OCT) imaging",
"optic disc pit maculopathy with pigmentary changes: alterations in retinal pigmentation within the macula, contributing to a mottled or speckled appearance",
"optic disc pit maculopathy with optic disc excavation: recognition of an excavated or depressed appearance of the optic disc, often associated with the optic disc pit",
"optic disc pit maculopathy with disrupted photoreceptor layer: visualizing interruptions or irregularities in the photoreceptor layer of the macula, indicative of structural changes",
"optic disc pit maculopathy with macular edema: presence of fluid accumulation leading to macular edema, often contributing to visual impairment",
"optic disc pit maculopathy with absence of exudates in the macular region: differentiation from other macular pathologies, as optic disc pit maculopathy typically lacks the presence of lipid-rich exudates in the macular area"],


"preretinal haemorrhage":["preretinal haemorrhage with layered appearance: identification of blood accumulation between the retina and the vitreous, often forming a distinct layered appearance",
"preretinal haemorrhage with sharp demarcation: clear boundaries between the preretinal hemorrhage and surrounding retinal tissue, visible on fundus examination",
"preretinal haemorrhage with obscured retinal vessels: partial or complete covering of retinal vessels by the hemorrhagic layer, contributing to vessel obscurity",
"preretinal haemorrhage with a localized distribution: concentration of blood in a specific area of the retina, often related to the site of vascular rupture",
"preretinal haemorrhage with associated retinal traction: detection of tractional forces on the retina caused by the hemorrhage, visible as distortion or pulling of retinal tissue",
"preretinal haemorrhage with variable coloration: ranging from bright red to darker hues as the hemorrhage undergoes changes in age",
"preretinal haemorrhage with absence of underlying retinal pathology: differentiation from retinal hemorrhages associated with other conditions, as preretinal hemorrhages are typically not directly related to retinal diseases",
"preretinal haemorrhage with gradual resolution over time: monitoring the fundus for signs of resolution as the hemorrhage is reabsorbed, indicating healing and improvement"],

"myelinated nerve fibers":["myelinated nerve fibers with feathered edges: identification of nerve fibers with distinct, feathered borders, often giving them a wispy or brush-like appearance",
"myelinated nerve fibers with a striated pattern: observation of a striped or streaked pattern along the course of the nerve fibers, enhancing their visibility",
"myelinated nerve fibers with variable coloration: ranging from a lighter, more translucent appearance to a more opaque, white or yellowish hue compared to the surrounding retina",
"myelinated nerve fibers with respect to retinal vessels: noting the relationship of myelinated nerve fibers in proximity to retinal vessels, as they often follow the course of blood vessels",
"myelinated nerve fibers with preservation of retinal layers: absence of retinal thinning or disruption in the areas occupied by myelinated nerve fibers, differentiating them from other pathological changes",
"myelinated nerve fibers with sharp demarcation: clear boundaries between the myelinated nerve fibers and adjacent retinal tissue, facilitating their recognition",
"myelinated nerve fibers with nerve fiber layer transparency: the transparency of the nerve fiber layer in the affected areas, allowing visibility of the underlying choroidal vessels",
"myelinated nerve fibers with absence of associated visual field defects: typically, myelinated nerve fibers do not cause visual field deficits, aiding in differentiation from other conditions affecting the visual field"],

"haemorrhagic retinopathy":["haemorrhagic retinopathy with flame-shaped hemorrhages: identification of flame-shaped, linear hemorrhages along the retinal nerve fiber layer, often associated with hypertensive retinopathy",
"haemorrhagic retinopathy with dot and blot hemorrhages: presence of small dot-like and larger blot-shaped hemorrhages scattered throughout the retina, indicating vascular damage",
"haemorrhagic retinopathy with cotton wool spots: detection of fluffy, white lesions on the retina, resulting from microinfarctions and ischemic changes",
"haemorrhagic retinopathy with macular edema: observation of fluid accumulation in the macular region, often contributing to visual impairment",
"haemorrhagic retinopathy with vascular changes: alterations in retinal blood vessels, including arteriolar narrowing, arteriovenous nicking, or vascular sheathing",
"haemorrhagic retinopathy with optic disc swelling: swelling of the optic disc, indicating involvement of the optic nerve head in the hemorrhagic process",
"haemorrhagic retinopathy with hemorrhagic choroidal detachment: presence of blood accumulation between the choroid and the sclera, visible as a dark, dome-shaped area on fundus examination",
"haemorrhagic retinopathy with associated systemic conditions: consideration of underlying systemic diseases such as hypertension or diabetes, as these conditions can contribute to the development of haemorrhagic retinopathy"],

"central retinal artery occlusion":["central retinal artery occlusion with pale retina: observation of a pale or whitened appearance of the retina due to the lack of blood supply, especially in the macular region",
"central retinal artery occlusion with cherry-red spot: identification of a cherry-red spot at the fovea, contrasting with the pale retina, caused by the transparency of the foveal area and the absence of blood flow",
"central retinal artery occlusion with attenuated retinal arteries: narrowing of retinal arteries, often visible as thin, thread-like vessels throughout the retina",
"central retinal artery occlusion with boxcarring of retinal arterioles: segmented appearance of retinal arterioles, resembling a series of boxes due to decreased blood flow",
"central retinal artery occlusion with retinal edema: presence of retinal edema, particularly in the posterior pole, contributing to the overall whitening of the retina",
"central retinal artery occlusion with emboli: detection of emboli, often visible as bright or refractile particles within the retinal vessels, contributing to the arterial occlusion",
"central retinal artery occlusion with cilioretinal artery sparing: in some cases, sparing of the cilioretinal artery may lead to a localized area of preserved retinal perfusion within the macula",
"central retinal artery occlusion with absence of venous pulsations: absence of venous pulsations due to compromised blood flow, especially in the larger retinal veins"],


"tilted disc":["tilted disc with oblique optic disc appearance: recognition of an oval or obliquely shaped optic disc, deviating from the typical round configuration",
"tilted disc with inferotemporal tilting: observation of the optic disc tilted in the inferotemporal direction, potentially resulting in a crescent-shaped or tilted appearance",
"tilted disc with associated peripapillary atrophy: presence of atrophic changes in the peripapillary region, often more noticeable on the side opposite to the tilt",
"tilted disc with asymmetric cup-to-disc ratio: uneven cupping of the optic disc, with one side appearing more excavated than the other due to the tilt",
"tilted disc with abnormal vascular branching patterns: alterations in the branching pattern of retinal vessels near the optic disc, reflecting the tilted nature of the optic disc",
"tilted disc with torsional changes in retinal vessels: twisting or torsion of retinal vessels as they approach the optic disc, indicative of the tilted disc configuration",
"tilted disc with absence of true optic disc swelling: differentiation from true optic disc swelling, as the tilting may create a pseudopapilledema appearance",
"tilted disc with compensatory head tilt: in some cases, patients may adopt a compensatory head tilt to align their visual axis with the tilted optic disc, potentially revealing a head posture abnormality"],


"cystoid macular edema":["cystoid macular edema with retinal cystoid spaces: identification of multiple cyst-like spaces within the macula, often visible as fluid-filled lacunae on fundus imaging",
"cystoid macular edema with petalloid pattern: recognition of a characteristic petal-shaped pattern of fluid accumulation in the macula, radiating from the fovea",
"cystoid macular edema with macular thickening: measurement of increased macular thickness, often seen on optical coherence tomography (OCT) imaging",
"cystoid macular edema with blurred or indistinct foveal reflex: haziness or loss of the normal foveal light reflex due to the presence of cystoid spaces and fluid",
"cystoid macular edema with fluorescein angiography leakage: visualization of leakage on fluorescein angiography, indicating abnormal fluid dynamics within the macula",
"cystoid macular edema with disruption of inner retinal layers: identification of irregularities or disorganization in the inner retinal layers, visible on OCT scans",
"cystoid macular edema with decreased visual acuity: associated vision impairment due to the accumulation of fluid in the macular region",
"cystoid macular edema with absence of other macular pathologies: differentiation from other macular conditions, as cystoid macular edema has specific characteristics on imaging that distinguish it from other macular abnormalities"],


"post traumatic choroidal rupture":["post traumatic choroidal rupture with linear configuration: identification of a linear, often jagged or irregular-shaped lesion on the fundus, corresponding to the choroidal rupture",
"post traumatic choroidal rupture with extension from the optic disc or peripapillary region: noting the origin of the choroidal rupture, often arising from the optic disc or extending radially from the peripapillary area",
"post traumatic choroidal rupture with associated overlying retinal pigment epithelium changes: observation of alterations in pigmentation overlying the choroidal rupture site, indicating disruption to the retinal pigment epithelium",
"post traumatic choroidal rupture with overlying subretinal hemorrhage: presence of hemorrhage between the neurosensory retina and the retinal pigment epithelium, directly overlying the choroidal rupture",
"post traumatic choroidal rupture with choroidal vessel visibility: visualization of choroidal vessels within the rupture site, contrasting with the surrounding normal choroid",
"post traumatic choroidal rupture with adjacent retinal folds: detection of retinal folds near the site of choroidal rupture, resulting from the mechanical forces involved in the traumatic event",
"post traumatic choroidal rupture with associated vitreous hemorrhage: in some cases, concurrent vitreous hemorrhage may be present, complicating the clinical picture",
"post traumatic choroidal rupture with corresponding visual field defects: consideration of visual field testing to identify any scotomas or defects corresponding to the location of the choroidal rupture"],

"choroidal folds":["choroidal folds with undulating appearance: recognition of wave-like or undulating folds in the choroid, often extending across the fundus",
"choroidal folds with parallel orientation: observation of folds running parallel to each other, typically separated by normal choroidal tissue",
"choroidal folds with associated retinal pigment epithelium changes: detection of alterations in pigmentation overlying the choroidal folds, reflecting the influence of the folds on the overlying retina",
"choroidal folds with preserved retinal layers: absence of significant disruption or damage to the neurosensory retina, as choroidal folds primarily affect the choroid",
"choroidal folds with displacement of choroidal vessels: visualization of choroidal vessels appearing displaced or distorted within the folds",
"choroidal folds with localized choroidal thickening: measurement of increased choroidal thickness in the areas corresponding to the folds, visible on optical coherence tomography (OCT) imaging",
"choroidal folds with absence of hemorrhage or exudates: differentiation from other fundus abnormalities, as choroidal folds typically do not present with associated hemorrhage or exudative changes",
"choroidal folds with correlation to patient symptoms: consideration of patient symptoms such as metamorphopsia or visual distortion, as choroidal folds may affect visual perception"],

"vitreous haemorrhage":["vitreous haemorrhage with obscured fundus details: presence of blood in the vitreous cavity leading to reduced visibility of retinal structures, making fundus details indistinct",
"vitreous haemorrhage with floating blood cells: observation of floating red blood cells within the vitreous humor, contributing to the hazy appearance",
"vitreous haemorrhage with blotchy or speckled fundus: fundus exhibiting irregular blotches or speckles due to the dispersed blood within the vitreous",
"vitreous haemorrhage with dense, layered blood accumulation: detection of dense, layered blood accumulation, potentially forming a horizontal level in the vitreous cavity",
"vitreous haemorrhage with obscuration of retinal vessels: obscuring or masking of retinal vessels as a result of the hemorrhage, leading to diminished vessel visibility",
"vitreous haemorrhage with dynamic movement of blood particles: potential movement or settling of blood particles within the vitreous, observable during eye movements",
"vitreous haemorrhage with associated retinal pathology: determination of any underlying retinal pathologies, such as diabetic retinopathy or retinal tears, that may have contributed to the vitreous hemorrhage",
"vitreous haemorrhage with potential clearing over time: consideration of the possibility of spontaneous clearing of the vitreous hemorrhage over time, allowing for improved visualization of the fundus"],

"macroaneurysm":["macroaneurysm with round or oval-shaped lesion: identification of a well-defined, round or oval-shaped lesion on the fundus, often distinguishable from surrounding vessels",
"macroaneurysm with dilated and tortuous appearance: recognition of a dilated and tortuous vessel segment, forming the macroaneurysm, often exceeding the normal caliber of surrounding vessels",
"macroaneurysm with associated hemorrhage: detection of adjacent retinal hemorrhage, either intraretinal or subretinal, indicating rupture or leakage from the macroaneurysm",
"macroaneurysm with exudates or lipid deposition: presence of lipid-rich exudates or deposits around the macroaneurysm, reflecting chronic leakage and tissue damage",
"macroaneurysm with hard exudates: observation of lipid-rich deposits at a distance from the macroaneurysm, suggestive of chronic leakage and lipid accumulation",
"macroaneurysm with fluorescein angiography findings: abnormal dye leakage or pooling during fluorescein angiography, highlighting the site of the macroaneurysm and associated vascular abnormalities",
"macroaneurysm with surrounding edema: presence of macular edema or localized retinal thickening in proximity to the macroaneurysm",
"macroaneurysm with absence of neovascularization: differentiation from other retinal pathologies, as macroaneurysms typically do not lead to the development of neovascularization"],


"vasculitis":["vasculitis with vessel wall inflammation: identification of signs indicating inflammation of retinal vessels, such as vessel wall thickening or hyperemia",
"vasculitis with perivascular sheathing: presence of white or yellowish sheathing around retinal vessels, indicative of inflammatory infiltration in the perivascular spaces",
"vasculitis with cuffing of retinal vessels: detection of localized or diffuse thickening or cuffing of retinal vessels due to inflammatory changes",
"vasculitis with retinal hemorrhages: observation of dot and blot retinal hemorrhages scattered along the course of affected vessels, reflecting vascular damage",
"vasculitis with cotton wool spots: presence of fluffy, white lesions on the retina, resulting from microinfarctions and ischemic changes associated with vasculitis",
"vasculitis with arterial narrowing: identification of narrowed or constricted retinal arteries, reflecting reduced blood flow due to inflammatory changes",
"vasculitis with neovascularization: potential development of abnormal, new blood vessels as a response to ischemia, visible on the disc or elsewhere in the retina",
"vasculitis with associated retinal edema: detection of fluid accumulation in the retinal layers, leading to retinal thickening and potential macular involvement"],


"branch retinal artery occlusion":["branch retinal artery occlusion with retinal whitening: identification of localized whitening of the retina in the distribution of the affected branch retinal artery, reflecting ischemia",
"branch retinal artery occlusion with emboli: visualization of emboli or plaque-like material within the affected branch retinal artery, indicating the source of the occlusion",
"branch retinal artery occlusion with abrupt vessel cutoff: observation of a sudden termination or sharp demarcation of the affected branch retinal artery, often visible as a straight edge on fundus examination",
"branch retinal artery occlusion with cherry-red spot at the fovea: recognition of a cherry-red spot at the fovea, surrounded by the whitened ischemic retina, due to transparency of the foveal area",
"branch retinal artery occlusion with narrowed and attenuated retinal arteries: identification of reduced caliber and attenuated appearance of the affected branch retinal artery and its tributaries",
"branch retinal artery occlusion with segmentation of retinal blood flow: appearance of segmented or fragmented blood flow within the occluded branch retinal artery, visible as a series of disconnected segments",
"branch retinal artery occlusion with associated cotton wool spots: presence of cotton wool spots in the affected area, indicating ischemic damage and nerve fiber layer infarction",
"branch retinal artery occlusion with delayed or absent arteriovenous transit: abnormal or delayed passage of dye through retinal vessels during fluorescein angiography, revealing impaired blood flow in the affected area"],

"plaque":["plaque with yellowish or white appearance: identification of a localized yellowish or white lesion on the fundus, often contrasting with the surrounding retinal tissue",
"plaque with well-defined borders: recognition of clear and demarcated borders outlining the plaque, facilitating differentiation from adjacent retinal structures",
"plaque with surface irregularities: observation of irregularities or undulations on the surface of the plaque, indicating variations in thickness or composition",
"plaque with associated retinal pigment epithelium changes: detection of alterations in pigmentation overlying the plaque, suggestive of chronic changes or interactions with the retinal pigment epithelium",
"plaque with subretinal fluid accumulation: presence of fluid between the plaque and the neurosensory retina, contributing to localized retinal detachment or elevation",
"plaque with overlying exudates or lipid deposition: identification of lipid-rich exudates or deposits around the plaque, reflecting chronic leakage and tissue damage",
"plaque with fluorescence characteristics on angiography: abnormal dye patterns during fluorescein angiography, revealing the plaque vascular or perfusion characteristics",
"plaque with absence of neovascularization: differentiation from other retinal pathologies, as plaques typically do not lead to the development of neovascularization",],


"haemorrhagic pigment epithelial detachment":["haemorrhagic pigment epithelial detachment with subretinal bleeding: identification of blood accumulation between the retinal pigment epithelium (RPE) and the neurosensory retina, leading to a noticeable detachment",
"haemorrhagic pigment epithelial detachment with irregular borders: recognition of the irregular or jagged borders outlining the area of pigment epithelial detachment",
"haemorrhagic pigment epithelial detachment with hemorrhagic or reddish appearance: observation of a reddish or hemorrhagic component within the pigment epithelial detachment, indicating the presence of blood",
"haemorrhagic pigment epithelial detachment with associated subretinal fluid: detection of fluid accumulation between the RPE and the retina, contributing to the detachment and potentially obscuring underlying details",
"haemorrhagic pigment epithelial detachment with overlying retinal changes: identification of changes in the overlying retina, such as exudates or lipid deposition, due to the presence of blood and altered RPE function",
"haemorrhagic pigment epithelial detachment with fluorescein angiography findings: abnormal dye patterns during fluorescein angiography, reflecting the vascular characteristics and leakage associated with the haemorrhagic pigment epithelial detachment",
"haemorrhagic pigment epithelial detachment with decreased visual acuity: consideration of associated vision impairment due to the presence of blood and fluid affecting the macula",
"haemorrhagic pigment epithelial detachment with absence of neovascularization: differentiation from other retinal pathologies, as haemorrhagic pigment epithelial detachments typically do not lead to the development of neovascularization"],


"collaterals":["collaterals with vessel dilation: identification of dilated retinal vessels, often forming collateral pathways that deviate from the normal vascular pattern",
"collaterals with tortuous appearance: recognition of tortuosity or twisting in the course of collateral vessels, reflecting the compensatory changes in blood flow",
"collaterals with anastomoses: observation of connections or anastomoses between retinal vessels, creating alternative pathways for blood circulation",
"collaterals with abnormal branching patterns: detection of irregularities or aberrant branching in retinal vessels, indicative of collateral formation",
"collaterals with visible pulsations: observation of pulsatile movements in collateral vessels, potentially visible with careful examination or dynamic imaging",
"collaterals with fluorescein angiography findings: abnormal dye patterns during fluorescein angiography, highlighting the presence and characteristics of collateral vessels",
"collaterals with associated retinal changes: identification of changes in the overlying retina, such as exudates or hemorrhages, due to altered blood flow and collateral circulation",
"collaterals with correlation to underlying vascular pathology: consideration of the underlying vascular pathology leading to collateral formation, such as occlusive diseases or venous abnormalities"],



    "health": ["health with normal with optic disc appears well-defined and within normal limits",
               "health with no findings with clear circular shape with distinctth  margins",
               "health with normal appearance of retina wia uniform color and texture",
               "health with normal with well-defined blood vessels, arteries and veins",
               "health with clear macula with clear retinal background",
               "health with normal with no signs of hemorrhages",
               "health with no findings with no signs of exudates",
               "health with no findings with no other abnormalities"],

    "other": [
              "other with cotton wool spots",
                "other with colobomas",
        "other with optic disc pit maculopathy",
        "other with preretinal haemorrhage",
        "other with myelinated nerve fibers",
        "other with haemorrhagic retinopathy",
        "other with central retinal artery occlusion",
        "other with tilted disc",
        "other with cystoid macular edema",
        "other with post traumatic choroidal rupture",
        "other with choroidal folds",
        "other with vitreous haemorrhage",
        "other with macroaneurysm",
        "other with vasculitis",
        "other with branch retinal artery occlusion",
        "other with plaque",
        "other with haemorrhagic pigment epithelial detachment",
        "other with collaterals with vessel dilation"],


"glaucoma":[
"glaucoma with optic disc atrophy with glaucoma can lead to atrophy of the optic disc, the initial part of the optic nerve. This may be characterized by a change in color of the optic disc, often appearing pale yellow or white",
"glaucoma with defects in the retinal nerve fiber layer: Glaucoma may cause damage to the retinal nerve fiber layer, resulting in specific areas of the fundus lacking nerve fibers, forming so-called nerve fiber layer defects",
"glaucoma with blurry optic disc margins with glaucoma may render the margins of the optic disc blurry or irregular, presenting an appearance distinct from the normal clear edges",
"glaucoma with cupping of the optic disc with Atrophy of the optic disc caused by glaucoma may lead to cupping, a phenomenon where the optic disc becomes inwardly concave",
"glaucoma with optic disc hemorrhage with Glaucoma may result in hemorrhage around the optic disc or within the optic disc itself"
],



"cataract":[
"cataract with opacification of the lens with the primary manifestation of cataracts is the opacification of the lens, possibly appearing as a blurry or hazy region in the lens area on fundus images",
"cataract with uneven pupil coloring with when the lens becomes cloudy due to cataracts, the pupil on fundus images may exhibit uneven coloring, as reduced transparency causes light scattering",
"cataract with reflection from the retina with opacification of the lens may lead to a reflection from the retina, manifesting as a reflective light within the pupil on fundus images",
"cataract with loss of clear lens edges with normally, the lens in fundus images should have clear edges, but cataracts can cause these edges to become blurred or indistinct"],

    "hypertensive retinopathy": ["hypertensive retinopathy with possible signs of haemorraghe with blot, dot, or flame-shaped",
                                 "hypertensive retinopathy with possible presence of microaneurysm, cotton-wool spot, or hard exudate",
                                 "hypertensive retinopathy with arteriolar narrowing", "hypertensive retinopathy with vascular wall changes", "hypertensive retinopathy with optic disk edema"],

"other disease":["other disease with a disease",

"other disease with may laser spot with bright or white small dots on the fundus image, contrasting sharply with the surrounding tissue",

"other disease with retinal Detachment with irregular, wavy, or separated features in the fundus image",

"other disease with macular hole with signs of central depression or absence in the macular region, potentially leading to decreased central vision",

"other disease with retinal artery occlusion with  ischemia in the corresponding area of the retina, presenting as a lightening or whitening of the affected region",

"other disease with retinal vein occlusion with hemorrhages and swelling in the affected retinal area, visible as spots and edema",

"other disease with optic neuropathy with color changes, swelling, or irregular edges in the optic nerve head, potentially affecting the surrounding retinal tissue",

"other disease with choroidal neovascularization with bleeding, leakage, and discoloration in the macular region",

"other disease with drusen with yellow or white deposits in the retina, often located on the surface of the retina",

"other disease with epiretinal membrane with folds or membranous structures on the surface of the retina",

"other disease with post laser photocoagulation with alterations around the laser spots, such as scar tissue formation",

"other disease with vitreous degeneration opacities or irregular shapes in the vitreous observed in the fundus image",

"other disease with pigment epithelium proliferation with pigment deposition and cellular proliferation in the fundus image"
                 ]




}

# Expert knowledge definitions dictionary
definitions_origin = {"no diabetic retinopathy": ["no diabetic retinopathy", "no microaneurysms"],
               "mild diabetic retinopathy": ["only few microaneurysms"],
               "severe diabetic retinopathy": ["venous beading",
                                               "many severe haemorrhages",
                                               "intraretinal microvascular abnormality"],
               "proliferative diabetic retinopathy": ["preretinal or vitreous haemorrhage",
                                                      "neovascularization"],
               "no referable diabetic macular edema": ["no apparent exudates"],
               "hard exudates": ["small white or yellowish deposits with sharp margins", "bright lesion"],
               "soft exudates": ["pale yellow or white areas with ill-defined edges", "cotton-wool spot",
                                 "small, whitish or grey, cloud-like, linear or serpentine, slightly elevated lesions"
                                 " with fimbriated edges"],
               "microaneurysms": ["small red dots"],
               "haemorrhages": ["dense, dark red, sharply outlined lesion"],
               "non clinically significant diabetic macular edema": ["presence of exudates outside the radius of one"
                                                                     " disc diameter from the macula center",
                                                                     "presence of exudates"],
               "age related macular degeneration": ["many small drusen", "few medium-sized drusen", "large drusen",
                                                    "macular degeneration"],
               "media haze": ["vitreous haze", "pathological opacity", "the obscuration of fundus details by vitreous"
                                                                       " cells and protein exudation"],
               "drusens": ["yellow deposits under the retina", "numerous uniform round yellow-white lesions"],
               "pathologic myopia": ["anomalous disc, macular atrophy and possible tessellation"],
               "branch retinal vein occlusion": ["occlusion of one of the four major branch retinal veins"],
               "tessellation": ["large choroidal vessels at the posterior fundus"],
               "epiretinal membrane": ["epiretinal membrane with greyish semi-translucent avascular membrane",
                                       "epiretinal membrane with a sheen or abnormal reflectivity of the macular surface",
                                       "epiretinal membrane with small translucent wrinkles or folds on the surface of the retina",
                                       "epiretinal membrane with retinal thickening in the macular area",
                                       "epiretinal membrane with macular gold foil-like reflection",
                                       "epiretinal membrane with blunting of the foveal contour or wrinkling on the retinal surface from membrane contracture"],
               "laser scar": ["round or oval, yellowish-white with variable black pigment centrally",
                              "50 to 200 micron diameter lesions"],
               "no laser scar": ["no laser scar"],
               "macular scar": ["macular scar"],
               "central serous retinopathy": ["subretinal fluid involving the fovea", "leakage"],
               "optic disc cupping": ["optic disc cupping"],
               "central retinal vein occlusion": ["central retinal vein occlusion"],
               "tortuous vessels": ["tortuous vessels"],
               "asteroid hyalosis": ["multiple sparking, yellow-white, and refractile opacities in the vitreous cavity",
                                     "vitreous opacities"],
               "optic disc pallor": ["pale yellow discoloration that can be segmental or generalized on optic disc"],
               "optic disc edema": ["optic disc edema"],
               "shunt": ["collateral vessels connecting the choroidal and the retinal vasculature",
                         "collateral vessels of large caliber and lack of leakage"],
               "anterior ischemic optic neuropathy": ["anterior ischemic optic neuropathy"],
               "parafoveal telangiectasia": ["parafoveal telangiectasia"],
               "retinal traction": ["retinal traction"],
               "retinitis": ["retinitis"],
               "chorioretinitis": ["chorioretinitis"],
               "exudates": ["small white or yellowish white deposits with sharp margins", "bright lesion"],
               "retinal pigment epithelium changes": ["retinal pigment epithelium changes"],
               "macular hole": ["lesion in the macula", "grayish fovea"],
               "retinitis pigmentosa": ["pigment deposits are present in the periphery"],
               "cotton wool spots": ["cotton wool spots", "soft exudates"],
               "colobomas": ["colobomas"],
               "optic disc pit maculopathy": ["optic disc pit maculopathy"],
               "preretinal haemorrhage": ["preretinal haemorrhage"],
               "myelinated nerve fibers": ["myelinated nerve fibers"],
               "haemorrhagic retinopathy": ["haemorrhagic retinopathy"],
               "central retinal artery occlusion": ["central retinal artery occlusion"],
               "tilted disc": ["tilted disc"],
               "cystoid macular edema": ["cysts in the macula region"],
               "post traumatic choroidal rupture": ["post traumatic choroidal rupture"],
               "choroidal folds": ["choroidal folds"],
               "vitreous haemorrhage": ["vitreous haemorrhage"],
               "macroaneurysm": ["macroaneurysm"],
               "vasculitis": ["vasculitis"],
               "branch retinal artery occlusion": ["branch retinal artery occlusion"],
               "plaque": ["plaque"],
               "haemorrhagic pigment epithelial detachment": ["haemorrhagic pigment epithelial detachment"],
               "collaterals": ["collaterals"],
               "normal": ["healthy", "no findings", "no lesion signs", "no glaucoma", "no retinopathy"],
               "large optic cup": ["abnormality in optic cup"],
               "retina detachment": ["retina detachment"],
               "Vogt-Koyanagi syndrome": ["Vogt-Koyanagi syndrome"],
               "maculopathy": ["maculopathy"],
               "glaucoma": ["optic nerve abnormalities", "abnormal size of the optic cup",
                            "anomalous size in the optic disc"],
               "optic atrophy": ["optic atrophy"],
               "severe hypertensive retinopathy": ["flame shaped hemorrhages at the disc margin, blurred disc margins,"
                                                   " congested retinal veins, papilledema, and secondary macular "
                                                   "exudates", "arterio-venous crossing changes, macular star and "
                                                               "cotton wool spots"],
               "disc swelling and elevation": ["disc swelling and elevation"],
               "dragged disk": ["dragged disk"],
               "congenital disk abnormality": ["disk abnormality", "optic disk lesion"],
               "Bietti crystalline dystrophy": ["Bietti crystalline dystrophy"],
               "peripheral retinal degeneration and break": ["peripheral retinal degeneration and break"],
               "neoplasm": ["neoplasm"],
               "yellow-white spots flecks": ["yellow-white spots flecks"],
               "fibrosis": ["fibrosis"],
               "silicon oil": ["silicon oil"],
               "no proliferative diabetic retinopathy": ["diabetic retinopathy with no neovascularization",
                                                         "no neovascularization"],
               "no glaucoma": ["no glaucoma"],
               "cataract": ["opacity in the macular area"],
               "hypertensive retinopathy": ["possible signs of haemorraghe with blot, dot, or flame-shaped",
                                            "possible presence of microaneurysm, cotton-wool spot, or hard exudate",
                                            "arteriolar narrowing", "vascular wall changes", "optic disk edema"],
               "neovascular age related macular degeneration": ["neovascular age-related macular degeneration"],
               "geographical age related macular degeneration": ["geographical age-related macular degeneration"],
               "acute central serous retinopathy": ["acute central serous retinopathy"],
               "chronic central serous retinopathy": ["chronic central serous retinopathy"],
               "no cataract": ["no cataract signs", "no obscure opacities"],
               "abnormal optic disc": ["abnormal optic disc"],
               "abnormal vessels": ["abnormal vessels"],
               "abnormal macula": ["abnormal macula"],
               "macular edema": ["macular edema with cystoid spaces",
                                 "macular edema with distortion of the retinal architecture",
                                 "macular edema with yellowish deposits in the macula",
                                 "macular edema with a blurring of the foveal reflex",
                                 "macular edema with disappearance of reflection in the macular",
                                 "macular edema with swelling and thickening of the macula"],
               "scar": ["scar"],
               "nevus": ["darkly pigmented lesion found in the back of the eye"],
               "increased cup disc": ["increased cup disc"],
               "intraretinal microvascular abnormalities": ["shunt vessels and appear as abnormal branching or"
                                                            " dilation of existing blood vessels (capillaries) "
                                                            "within the retina", "deeper in the retina than"
                                                                                 " neovascularization, has blurrier edges, is more"
                                                                                 " of a burgundy than a red, does not appear on the "
                                                                                 "optic disc",
                                                            "vascular loops confined within the"
                                                            " retina"],
               "red small dots": ["microaneurysms"],
               "neovascularisation": ["neovascularisation"],
               "a disease": ["no healthy", "lesions"],
               "superficial haemorrhages": ["superficial haemorrhages"],
               "deep haemorrhages": ["deep haemorrhages"],
               "ungradable": ["no fundus", "very noisy", "noisy"],
               "noisy": ["noisy"],
               "normal macula": ["normal macula"],
               "macular degeneration": ["macular degeneration"],
               "diabetic retinopathy": ["diabetic retinopathy with retinal hemorrhages",
                                        "diabetic retinopathy with cotton wool spots",
                                        "diabetic retinopathy with hard exudates",
                                        "diabetic retinopathy with microaneurysms",
                                        "diabetic retinopathy with venous beading"],
               "no hypertensive retinopathy": ["no presence of hypertensive retinopathy"],
               "mild hypertensive retinopathy": ["mild arteriovenous ratio", "mild tortuosity",
                                                 "focal arteriolar narrowing",
                                                 "arteriovenous nicking"],
               "moderate hypertensive retinopathy": ["moderate arteriovenous ratio", "moderate tortuosity",
                                                     "cotton wool spots",
                                                     "flame-shaped haemorrhages"],
               "malignant hypertensive retinopathy": ["severe arteriovenous ratio", "severe tortuosity",
                                                      "swelling optical disk",
                                                      "flame-shaped haemorrhages"],
               "non-exudative age related macular degeneration": [
                   "non-exudative age related macular degeneration with hard and soft drusen",
                   "non-exudative age related macular degeneration with pigment epithelial atrophy and proliferation",
                   "non-exudative age related macular degeneration with pigmentary disturbances",
                   "non-exudative age related macular degeneration with map-like atrophy of the retina and choroid"],
               "exudative age related macular degeneration": [
                   "exudative age related macular degeneration with subretinal fluid",
                   "exudative age related macular degeneration with serous or hemorrhagic pigment epithelial detachment",
                   "exudative age related macular degeneration with choroidal neovascularization",
                   "exudative age related macular degeneration with retinal edema",
                   "exudative age related macular degeneration with hemorrhage",
                   "exudative age related macular degeneration with exudation",
                   "exudative age related macular degeneration with fibrotic scarring",
                   "exudative age related macular degeneration with disciform degeneration"],
               "degenerative myopia": ["degenerative myopia with degenerative myopia",
                                       "degenerative myopia with pathological myopia",
                                       "degenerative myopia with pathologic myopia",
                                       "degenerative myopia with atrophy of the retina and choroid",
                                       "degenerative myopia with retinal fissures",
                                       "degenerative myopia with vitreomacular traction",
                                       "degenerative myopia with detachment of the retinal neurosensory layer",
                                       "degenerative myopia with macular hole",
                                       "degenerative myopia with macular hemorrhage"],

               }

# Datasets names
datasets = ["01_EYEPACS", "03_IDRID", "04_RFMid", "05_1000x39", "07_LAG", "09_PAPILA", "10_PARAGUAY", "12_ARIA",
            "14_AGAR300", "15_APTOS", "16_FUND-OCT", "17_DiaRetDB1", "18_DRIONS-DB", "19_Drishti-GS1", "20_E-ophta",
            "20_E-ophta", "21_G1020", "23_HRF", "24_ORIGA", "25_REFUGE", "26_ROC", "27_BRSET", "28_OIA-DDR",
            "02_MESIDOR", "05_20x3", "08_ODIR200x3", "13_FIVES"]

# Categories abbreviations
abbreviations = {"no diabetic retinopathy": "noDR", "mild diabetic retinopathy": "mildDR",
                 "moderate diabetic retinopathy": "modDR", "severe diabetic retinopathy": "sevDR",
                 "proliferative diabetic retinopathy": "prolDR", "diabetic macular edema": "DME",
                 "no referable diabetic macular edema": "noDME", "hard exudates": "hEX",
                 "soft exudates": "sEX", "microaneurysms": "MA", "haemorrhages": "HE",
                 "non clinically significant diabetic macular edema": "nonCSDME",
                 "age-related macular degeneration": "ARMD", "media haze": "MH", "drusens": "DN",
                 "pathologic myopia": "MYA", "branch retinal vein occlusion": "BRVO", "tessellation": "TSLN",
                 "epiretinal membrane": "ERM", "laser scar": "LS", "macular scar": "MS",
                 "central serous retinopathy": "CSR", "optic disc cupping": "ODC",
                 "central retinal vein occlusion": "CRVO", "tortuous vessels": "TV", "asteroid hyalosis": "AH",
                 "optic disc pallor": "ODP", "optic disc edema": "ODE",
                 "shunt": "ST", "anterior ischemic optic neuropathy": "AION", "parafoveal telangiectasia": "PT",
                 "retinal traction": "RT", "retinitis": "RS", "chorioretinitis": "CRS", "exudates": "EX",
                 "retinal pigment epithelium changes": "RPEC", "macular hole": "MHL", "retinitis pigmentosa": "RP",
                 "cotton wool spots": "CWS", "colobomas": "CB", "optic disc pit maculopathy": "ODM",
                 "preretinal haemorrhage": "PRH", "myelinated nerve fibers": "MNF", "haemorrhagic retinopathy": "HR",
                 "central retinal artery occlusion": "CRAO", "tilted disc": "TD", "cystoid macular edema": "CME",
                 "post traumatic choroidal rupture": "PTCR", "choroidal folds": "CF", "vitreous haemorrhage": "VH",
                 "macroaneurysm": "MCA", "vasculitis": "VS", "branch retinal artery occlusion": "BRAO", "plaque": "PLQ",
                 "haemorrhagic pigment epithelial detachment": "HPED", "collaterals": "CL", "normal": "N",
                 "large optic cup": "LOC", "retina detachment": "RD", "Vogt-Koyanagi syndrome": "VKH",
                 "maculopathy": "M", "glaucoma": "G", "optic atrophy": "OA", "severe hypertensive retinopathy": "sevHR",
                 "disc swelling and elevation": "DSE", "dragged disk": "DD", "congenital disk abnormality": "CDA",
                 "Bietti crystalline dystrophy": "BCD", "peripheral retinal degeneration and break": "PRDB",
                 "neoplasm": "NP", "yellow-white spots flecks": "YWSF", "fibrosis": "fibrosis", "silicon oil": "SO",
                 "no proliferative diabetic retinopathy": "noProlDR", "no glaucoma": "noG", "cataract": "CAT",
                 "hypertensive retinopathy": "HR", "neovascular age-related macular degeneration": "neovARMD",
                 "geographical age-related macular degeneration": "geoARMD",
                 "acute central serous retinopathy": "acCSR", "chronic central serous retinopathy": "chCSR",
                 "no cataract": "noCAT", "abnormal optic disc": "AOD", "abnormal vessels": "AV",
                 "abnormal macula": "AM", "macular edema": "ME", "scar": "S", "nevus": "NE",
                 "increased cup disc": "ICD", "intraretinal microvascular abnormalities": "IrMA",
                 "red small dots": "ReSD", "neovascularisation": "neoV", "a disease": "Dis"}






















definitions  = {
    "a disease": ["a disease with no healthy", "a disease with lesions", "a disease with abnormal","a disease with blurring sings"],


    "normal": ["normal with healthy with optic disc appears well-defined and within normal limits",
               "normal with no findings with clear circular shape with distinct margins",
               "normal with healthy appearance of retina wia uniform color and texture",
               "normal with health with well-defined blood vessels, arteries and veins",
               "normal with clear macula with clear retinal background",
               "normal with health with no hemorrhages",
               "normal with no findings and no exudates",
               "normal with no findings",
               "normal with no exudates",
               "normal with clear photo"],

    "epiretinal membrane": ["epiretinal membrane with surface membrane with small translucent wrinkles or folds on the surface of the retina",
                            "epiretinal membrane with color changes with greyish semi-translucent avascular membrane",
                            "epiretinal membrane with color changes with different from the surrounding normal tissue",
                            "epiretinal membrane with light reflection changes with a sheen or abnormal reflectivity of the macular surface",
                            "epiretinal membrane with light reflection changes with macular gold foil-like reflection",
                            "epiretinal membrane with vascular distortion with blood vessels underlying show irregular or distorted shapes",
                            "epiretinal membrane with changes in the macular area with changing the morphology of the macula",
                            "epiretinal membrane with changes in the macular area with blunting of the foveal contour or wrinkling on the retinal surface from membrane contracture",
                            "epiretinal membrane with changes in the macular area with retinal thickening in the macular area"],

    "macular edema": ["macular edema with macular thickening with swelling and thickening of the macula",
                      "macular edema with color changes with disappearance of reflection in the macular",
                      "macular edema with fluid accumulation with formation of cyst-like or blister-like structures, visible on fundus imaging",
                      "macular edema with color changes with opaque compared to the surrounding healthy tissue",
                      "macular edema with color changes with yellowish deposits in the macula",
                      "macular edema with vascular changes with irregular blood vessels",
                      ],

    "diabetic retinopathy": ["diabetic retinopathy with retinal hemorrhages with red spots in retina of damaged blood vessels",
                             "diabetic retinopathy with cotton wool spots with fluffy white lesions",
                             "diabetic retinopathy with hard exudates with yellowish or white lipid deposits",
                             "diabetic retinopathy with microaneurysms with round, red dots representing dilated capillaries and microaneurysms in retina",
                             "diabetic retinopathy with venous beading with beading veins",
                             "diabetic retinopathy with neovascularization with small, irregular red lines on the retina",
                             "diabetic retinopathy with ischemic areas with dark areas or black areas"],

    "non-exudative age related macular degeneration": [
        "non-exudative age related macular degeneration with hard and soft drusen with small yellow or white deposits beneath the retina",
        "non-exudative age related macular degeneration with pigment epithelial with changes in the pigmentation of the retinal pigment epithelium",
        "non-exudative age related macular degeneration with pigmentary disturbances with changes in the pigmentation of the retinal pigment epithelium",
        "non-exudative age related macular degeneration with geographic atrophy with atrophy and thinning of the retinal layers",
        "non-exudative age related macular degeneration with drusen with yellowish-white spots",
        "non-exudative age related macular degeneration with map-like atrophy of the retina and choroid"],

    "exudative age related macular degeneration": [
        "exudative age related macular degeneration with subretinal fluid with accumulation of fluid beneath the retina",
        "exudative age related macular degeneration with serous or hemorrhagic pigment epithelial detachment",
        "exudative age related macular degeneration with choroidal neovascularization with the formation of abnormal blood vessels beneath the retina",
        "exudative age related macular degeneration with retinal edema with swelling and morphological changes in the macular regio",
        "exudative age related macular degeneration with hemorrhage with red or dark red spots beneath the retina",
        "exudative age related macular degeneration with exudation with yellow or white fluid deposits beath the retina",
        "exudative age related macular degeneration with fibrotic scarring with prolonged presence of exudates and hemorrhages ",
        "exudative age related macular degeneration with disciform degeneration with the presence of a well-defined scar or fibrous tissue in the macular region."],

    "degenerative myopia": ["degenerative myopia with myopic maculopathy with thinning of the macula, pigmentary alterations and lacquer cracks",
                            "degenerative myopia with choroidal thinning with the vascular layer beneath the retina thinning",
                            "degenerative myopia with staphyloma formation with abnormal bulging or stretching of the sclera",
                            "degenerative myopia with optic disc changes with tilting, stretching, and increased visibility of the optic nerve",
                            "degenerative myopia with foveal changes with thinning and atrophy changes in the fovea",
                            "degenerative myopia with macular holes and tears with the formation of macular holes or retinal tears",
                            "degenerative myopia with macular hemorrhage with red or dark spots"],









    "age-related macular degeneration": ["age-related macular degeneration with drusen formation with the presence of small yellow or white deposits beneath the retina",
                                         "age-related macular degeneration with drusen formation with drusen appear as discrete spots in the macular region of the fundus"
                                         "age-related macular degeneration with macular changes with drusen accumulation particularly affects the macula, the central part of the retina responsible for sharp, central vision",
                                         "age-related macular degeneration with macular changes with changes in macular pigmentation may occur, contributing to alterations in fundus appearance"
                                         "age-related macular degeneration with geographic atrophy with advanced AMD may lead to geographic atrophy, involving the loss of retinal pigment epithelium cells",
                                         "age-related macular degeneration with geographic atrophy with manifests as well-defined areas of retinal degeneration",
                                         "age-related macular degeneration with choroidal neovascularization with abnormal blood vessels grow beneath the retina",
                                         "age-related macular degeneration with choroidal neovascularization with  leakage of fluid or blood, causing sudden vision changes",
                                         "age-related macular degeneration with pigmentary changes with changes in fundus pigmentation, such as hyperpigmentation or hypopigmentation, are observed in AMD",
                                         "age-related macular degeneration with macular edema with fluid accumulation in the macula, known as macular edema, can occur, affecting vision",
                                         "age-related macular degeneration with retinal pigment epithelium with atrophy or degeneration of the retinal pigment epithelium is a characteristic feature of AMD",
                                         "age-related macular degeneration with loss of central vision with AMD primarily impacts central vision, leading to difficulties with tasks like reading and recognizing faces"],

    'media haze': ["media haze with blurred appearance with observe if there is an overall blurry or hazy appearance in the fundus image",
                   "media haze with retinal structure examination with check the clarity of retinal structures in the fundus image, assessing if they are affected by media haze",
                   "media haze with transparency assessment with evaluate the transparency of transparent media (such as cornea, lens, and vitreous) in the fundus image, checking for reduced transparency",
                   "media haze with iris examination with examine the details of the iris to see if there are unclear or blurry features",
                   "media haze with observation of light scattering effects with observe if there is a light scattering effect, leading to a shading effect on the fundus image",
                   "media haze with image quality assessment with assess the quality of the fundus image to understand if the image is not clear enough due to media haze",
                   "media haze with difficulty in identifying fundus details with note if details of the fundus are difficult to discern, potentially due to media haze",
                   "media haze with assessment of decreased visibility with look for areas on the fundus image where visibility may be reduced due to media haze",
                   "media haze with understanding potential causes with understand potential causes of media haze, such as cataracts, corneal opacities, or other vitreous abnormalities",
                   "media haze with vision impairment with consider whether the patient has symptoms of vision impairment associated with the observed fundus features"],

    "drusens": ["drusens with identification with identify the presence of small, yellow-white deposits known as drusens in the fundus image",
                "drusens with size assessment with assess the size of drusens, noting whether they appear small, medium, or large in the fundus image",
                "drusens with distribution examination with examine the distribution pattern of drusens across the retina, checking if they are clustered or scattered",
                "drusens with border characteristics with observe the borders of drusens to determine if they have well-defined or indistinct edges",
                "drusens with color analysis with analyze the color of drusens, typically appearing as yellow or white spots in the fundus image",
                "drusens with proximity to macula or optic nerve with note the proximity of drusens to the macula and optic nerve head, as their location can impact vision",
                "drusens with fundus autofluorescence examination with consider using fundus autofluorescence imaging to assess the autofluorescent properties of drusens",
                "drusens with optical coherence tomography confirmation with confirm the presence of drusens using optical coherence tomography for detailed cross-sectional imaging",
                "drusens with patient medical history with inquire about the patient's medical history, including any previous diagnoses or family history of drusens",
                "drusens with comprehensive eye examination with conduct a comprehensive eye examination to rule out other potential retinal conditions and confirm the diagnosis"],


    "myopia": [
"myopia with optic disc characteristics with a tilted or elongated appearance indicating axial elongation",
"myopia with retinal blood vessel features with increased tortuosity or abnormal courses",
"myopia with macular observations with myopic macular degeneration or presence of a posterior staphyloma",
"myopia with peripapillary atrophy with crescent-shaped chorioretinal atrophy around the optic disc",
"myopia with fundus tessellation with a mottled appearance in the periphery",
"myopia with choroidal thinning signs with thinning of the choroid, especially in the posterior pole",
"myopia with foveal changes manifestation with myopic changes like lacquer cracks or myopic foveoschisis",
"myopia with axial length estimation with indirect estimation of increased axial length by assessing the distance between the optic disc and fovea"],

"branch retinal vein occlusion": ["branch retinal vein occlusion with retinal hemorrhages with presence of flame-shaped or dot/blot hemorrhages in the affected quadrant of the retina",
"branch retinal vein occlusion with cotton-wool spots with identification of soft, fluffy, white lesions indicating ischemic areas",
"branch retinal vein occlusion with dilated and tortuous veins with observation of enlarged and twisted retinal veins in the affected region",
"branch retinal vein occlusion with macular edema with detection of fluid accumulation in the macular area, leading to swelling",
"branch retinal vein occlusion with hard exudates with visualization of yellowish deposits around the macula, suggesting lipid leakage",
"branch retinal vein occlusion with capillary non-perfusion, recognition of areas with reduced or absent blood flow, indicative of ischemia",
"branch retinal vein occlusion with optic disc swelling, presence of disc edema, often associated with severe cases or ischemic complications",
"branch retinal vein occlusion with venous sheathing, noting the thickening and sclerosis of retinal veins in the affected quadrant",
"branch retinal vein occlusion with collateral vessel formation, identification of new vessels as a response to the occluded vein, especially at the periphery",
"branch retinal vein occlusion with macular ischemia, assessment of decreased perfusion in the macular area, contributing to visual impairment"],



"tessellation": [
"tessellation with geographic atrophy: identification of well-defined areas of retinal pigment epithelium (RPE) loss, leading to a map-like appearance on the fundus",
"tessellation with drusen: presence of small, yellowish deposits between the RPE and Bruchs membrane, indicating early stages of age-related macular degeneration",
"tessellation with pigmentary changes: observation of alterations in retinal pigmentation, including hypo- or hyperpigmented areas, contributing to the tessellated pattern",
"tessellation with choroidal neovascularization (CNV): detection of abnormal blood vessel growth beneath the retina, often associated with exudative or wet macular degeneration",
"tessellation with reticular pseudodrusen: recognition of yellowish subretinal deposits forming a network pattern, distinct from conventional drusen",
"tessellation with outer retinal tubulations: visualization of tubular structures in the outer retina, indicative of degenerative changes in photoreceptor cells",
"tessellation with retinal thinning: measurement of reduced retinal thickness, especially in the macular area, contributing to the tessellated appearance",
"tessellation with ellipsoid zone disruption: identification of disruptions in the ellipsoid zone on optical coherence tomography, reflecting structural damage in the retina",
"tessellation with subretinal fluid: presence of fluid accumulation beneath the retina, often associated with macular diseases and contributing to the tessellation pattern",
"tessellation with visual field defects: correlation of the tessellated fundus pattern with specific visual field abnormalities, aiding in the overall diagnostic assessment"],

# "laser scar": [
# "laser scar with well-defined borders: identification of a distinct area on the fundus with clear demarcation from the surrounding retina",
# "laser scar with hyperpigmentation: observation of darker pigmentation within the scarred region, indicative of altered melanin content",
# "laser scar with tissue atrophy: recognition of thinning and loss of retinal tissue in the scarred area, contributing to the overall structural changes",
# "laser scar with vascular changes: noting alterations in blood vessel patterns or disruption within the scar, reflecting the impact on retinal vasculature",
# "laser scar with loss of retinal architecture: visualization of disruptions in the normal retinal layers and structures, especially in the scarred region",
# "laser scar with choroidal changes: detection of modifications in the choroid beneath the scar, potentially affecting blood supply and tissue support",
# "laser scar with scarring-related distortion: observation of distortion in the surrounding retinal anatomy due to the presence of the laser scar",
# "laser scar with absence of normal fluorescence: using fundus autofluorescence imaging to identify areas where the laser scar shows reduced or altered autofluorescence",
# "laser scar with visual field defects: correlation of the laser scar location with specific visual field abnormalities, contributing to the diagnostic evaluation",
# "laser scar with history of laser treatment: consideration of the patient's medical history, particularly any documented laser procedures, to contextualize the presence of the scar on the fundus"],


"laser scar": [
"laser scar with round or oval, yellowish-white with variable black pigment centrally",
"laser scar with 50 to 200 micron diameter lesions"
],



"macular scar" :["macular scar with central atrophy: identification of a region in the macula exhibiting significant tissue loss and retinal thinning",
"macular scar with pigment alterations: observation of changes in pigmentation, such as hypo- or hyperpigmented areas within the scarred macula",
"macular scar with disrupted retinal layers: visualization of irregularities or interruptions in the normal layering of the retina, indicating structural damage",
"macular scar with surrounding fibrosis: noting the presence of fibrotic tissue around the macular scar, contributing to the overall pathology",
"macular scar with photoreceptor loss: detection of a decrease in the number of photoreceptor cells in the scarred macular region",
"macular scar with distortion of foveal architecture: recognizing alterations in the central foveal structure due to the presence of the scar",
"macular scar with scarring-related vascular changes: identification of modifications in retinal blood vessels associated with the scarred macula",
"macular scar with fluorescein angiography abnormalities: using angiography to reveal any abnormal blood flow patterns or leakage around the macular scar",
"macular scar with disrupted ellipsoid zone on OCT: visualization of interruptions in the ellipsoid zone on optical coherence tomography, indicative of structural damage",
"macular scar with visual acuity changes: correlation of the macular scar location and size with documented changes in visual acuity, providing crucial diagnostic insights"],



"central serous retinopathy":[" with serous retinal detachment: identification of localized detachment of the neurosensory retina, typically in the macular region",
"central serous retinopathy with macular edema: detection of fluid accumulation in the macula, leading to swelling and potential distortion of the central vision",
"central serous retinopathy with pigment epithelial changes: observation of alterations in the retinal pigment epithelium (RPE) layer, often manifesting as RPE detachments or irregularities",
"central serous retinopathy with choroidal hyperpermeability: noting increased permeability of choroidal vessels, leading to subretinal fluid accumulation",
"central serous retinopathy with focal leakage on fluorescein angiography: visualization of dye leakage from choroidal vessels into the subretinal space, indicating active disease",
"central serous retinopathy with bullous retinal elevation: recognition of large, blister-like elevations in the retina due to accumulated subretinal fluid",
"central serous retinopathy with RPE window defects: identification of areas where the RPE appears window-like or atrophic, allowing visualization of choroidal vasculature",
"central serous retinopathy with mottled hyperautofluorescence: using fundus autofluorescence to reveal irregular areas of increased and decreased autofluorescence within the affected region",
"central serous retinopathy with decreased central macular thickness on OCT: measurement of reduced thickness in the central macula due to subretinal fluid accumulation",
"central serous retinopathy with symptoms of metamorphopsia or micropsia: consideration of patient-reported visual distortions, such as straight lines appearing wavy or objects seeming smaller than they are"],

"optic disc cupping":["optic disc cupping with increased cup-to-disc ratio: assessment of the ratio between the size of the cup (central depression) and the overall optic disc diameter, with an enlarged cup",
"optic disc cupping with thinning of neuroretinal rim: observation of a decrease in the thickness of the neuroretinal rim, the tissue surrounding the optic cup",
"optic disc cupping with notching: identification of a distinct notch or depression in the rim of the optic disc, often associated with glaucomatous damage",
"optic disc cupping with asymmetry between the two eyes: noting a significant difference in cupping appearance between the optic discs of the two eyes",
"optic disc cupping with pallor of the neuroretinal rim: visualization of a pale or whitened appearance in the neuroretinal rim due to reduced nerve fiber layer thickness",
"optic disc cupping with vascular changes: recognition of alterations in the pattern and appearance of blood vessels on the optic disc surface",
"optic disc cupping with peripapillary atrophy: presence of atrophic changes in the tissue surrounding the optic disc, often accompanied by pigmentary changes",
"optic disc cupping with glaucomatous visual field defects: correlation of the cupping findings with specific visual field abnormalities characteristic of glaucoma",
"optic disc cupping with disc hemorrhages: identification of small hemorrhages on or around the optic disc, which may indicate glaucomatous damage",
"optic disc cupping with progressive changes over time: comparison of current fundus findings with previous images to assess the progression of optic disc cupping and potential glaucomatous damage"],


"central retinal vein occlusion": ["central retinal vein occlusion with retinal hemorrhages: presence of flame-shaped or dot/blot hemorrhages scattered throughout the retina, especially in the posterior pole",
"central retinal vein occlusion with cotton-wool spots: identification of soft, fluffy, white lesions indicating areas of retinal ischemia",
"central retinal vein occlusion with macular edema: detection of fluid accumulation in the macular region, leading to central vision impairment",
"central retinal vein occlusion with dilated and tortuous veins: observation of enlarged and twisted retinal veins, particularly in the posterior pole",
"central retinal vein occlusion with optic disc edema: presence of swelling at the optic disc, often referred to as disc edema or papilledema",
"central retinal vein occlusion with widespread retinal ischemia: recognition of extensive areas of reduced blood flow and perfusion in the retina",
"central retinal vein occlusion with venous congestion: noting congestion and engorgement of retinal veins due to impaired blood outflow",
"central retinal vein occlusion with cherry-red spot on macula: identification of a cherry-red spot at the fovea, contrasting against the ischemic, pale retina",
"central retinal vein occlusion with collateral vessel formation: visualization of new vessels as a compensatory response to the occluded vein, especially in the periphery",
"central retinal vein occlusion with visual field defects: correlation of fundus findings with specific visual field abnormalities, contributing to the overall diagnostic assessment"],


"tortuous vessels":["tortuous vessels with identification of abnormality: examine the fundus image for the presence of blood vessels displaying abnormal winding or twisting, indicating tortuosity",
"tortuous vessels with distribution pattern: assess the distribution pattern of the tortuous vessels, considering whether they are localized to a specific area or involve a more widespread portion of the retina",
"tortuous vessels with comparison to normal vessels: compare the suspected tortuous vessels with adjacent normal vessels to highlight the extent of deviation from the typical vascular architecture",
"tortuous vessels with vessel caliber changes: look for changes in the caliber of the tortuous vessels, as abnormal dilations or constrictions may provide additional diagnostic information",
"tortuous vessels with impact on surrounding structures: evaluate whether the tortuous vessels exert any pressure or have an impact on neighboring structures, such as the optic nerve or macula"],


"asteroid hyalosis":["asteroid hyalosis with numerous small, reflective, yellow-white opacities in the vitreous humor: presence of multiple tiny, reflective opacities distributed throughout the vitreous humor",
"asteroid hyalosis with dense, spherical bodies resembling stellate or star-like patterns: observation of compact, spherical opacities with a characteristic star-like appearance",
"asteroid hyalosis with opacities casting shadows on the retina: identification of shadows cast by the opacities on the underlying retina, often visible during fundus examination",
"asteroid hyalosis with opacities exhibiting minimal impact on visual acuity: typically, these opacities have a limited effect on visual function, as they are situated in the vitreous rather than directly on the retina"],


# "optic disc pallor":["optic disc pallor with thinning and paleness of the optic disc rim: thinning and a pale appearance of the rim surrounding the optic disc",
# "optic disc pallor with loss of normal pink coloration: absence of the usual pink hue typically seen in a healthy optic disc",
# "optic disc pallor with sharp demarcation between the pale optic disc and surrounding retina: clear distinction between the pale optic disc and the adjacent retinal tissue",
# "optic disc pallor with decreased visibility of blood vessels on the optic disc: reduced prominence and visibility of blood vessels within the optic disc due to the pallor",
# "optic disc pallor with associated optic nerve atrophy: often indicative of optic nerve atrophy, where the nerve fibers become damaged, leading to a reduction in disc color",
# "optic disc pallor with involvement of one or both optic discs: the condition can affect either one or both optic discs, and the extent of pallor may vary"],
#

"optic disc pallor":["optic disc pallor with pale yellow discoloration that can be segmental or generalized on optic disc"],


"optic disc edema":["optic disc edema with blurring of the optic disc margins: presence of indistinct or blurred margins of the optic disc due to swelling",
"optic disc edema with hyperemia or engorgement of blood vessels on the optic disc: increased visibility and dilation of blood vessels on the surface of the optic disc",
"optic disc edema with elevation of the optic disc surface: a raised appearance of the optic disc, indicating fluid accumulation and swelling",
"optic disc edema with loss of physiological cupping: diminished or absent cupping, the normal depression at the center of the optic disc, due to increased intrapapillary pressure",
"optic disc edema with peripapillary hemorrhages: presence of hemorrhages in the surrounding region of the optic disc, often a sign of increased pressure within the optic nerve head",
"optic disc edema with associated cotton-wool spots: presence of cotton-wool spots in the vicinity of the optic disc, indicating localized retinal ischemia associated with the edema"],


# "shunt":["shunt with retinal vessel dilation: enlargement of retinal vessels, particularly veins, indicating increased blood flow through the shunt",
# "shunt with tortuous and engorged blood vessels: winding and swollen appearance of blood vessels, suggesting abnormal blood flow dynamics",
# "shunt with localized area of vessel congestion: presence of a specific region where blood vessels appear congested and engorged",
# "shunt with retinal hemorrhages: occurrence of bleeding within the retinal tissue due to the altered blood flow through the shunt",
# "shunt with presence of microaneurysms: small bulging areas on the retinal vessels, indicating weakened vessel walls and potential shunting",
# "shunt with distorted or irregular foveal avascular zone (FAZ): changes in the central retinal area due to altered blood flow patterns, often seen in the presence of a shunt",
# "shunt with associated exudates: accumulation of fluid and lipid deposits in the retina, possibly indicating vascular leakage associated with the shunt",
# "shunt with retinal ischemia in surrounding areas: reduced blood supply leading to localized retinal ischemia, particularly in regions adjacent to the shunt"],

"optociliary shunt vessels": [
"optociliary shunt vessels with collateral vessels connecting the choroidal and the retinal vasculature",
"optociliary shunt vessels with collateral vessels of large caliber and lack of leakage",
"optociliary shunt vessels with tortuous vascular loops that start and end on the disc",
"optociliary shunt vessels with tortuous red small lines that start and end on the disc",
"collateral vessels connecting the choroidal and the retinal vasculature",
                         "collateral vessels of large caliber and lack of leakage"
                              ],



# "anterior ischemic optic neuropathy":["anterior ischemic optic neuropathy with segmental swelling of the optic disc: localized swelling of the optic disc, often seen in a segmental or partial manner",
# "anterior ischemic optic neuropathy with pale or edematous appearance of the optic nerve head: the optic disc may appear pale or edematous due to compromised blood supply",
# "anterior ischemic optic neuropathy with optic disc hyperemia: increased redness or hyperemia of the optic disc, indicating possible inflammation or ischemia",
# "absence of optic disc hemorrhages: unlike some other optic neuropathies, anterior ischemic optic neuropathy typically lacks hemorrhages on or around the optic disc",
# "disc edema with peripapillary hemorrhages (in some cases): presence of hemorrhages in the peripapillary region, though not a consistent feature, may be observed in certain cases",
# "disc edema with cotton-wool spots: cotton-wool spots may be present, reflecting localized retinal ischemia associated with optic nerve head swelling",
# "anterior ischemic optic neuropathy with sectoral or diffuse nerve fiber layer infarction: infarction or damage to the nerve fiber layer, observed as localized or diffuse darkening or pallor",
# "associated visual field defects: examination of the fundus may not directly reveal visual field defects, but correlation with visual field testing is crucial for a comprehensive diagnosis"],


"anterior ischemic optic neuropathy":[
"anterior ischemic optic neuropathy with swelling optic disc with the edema can be either segmental or diffuse",
"anterior ischemic optic neuropathy with pale or edematous appearance of the optic nerve head with the optic disc may appear pale or edematous due to compromised blood supply",
"anterior ischemic optic neuropathy with optic disc hyperemia with increased redness or hyperemia of the optic disc, indicating possible inflammation or ischemia",
"anterior ischemic optic neuropathy with accompanying hemorrhages with linear or flame-shaped red bleeding around the optic disc",
"anterior ischemic optic neuropathy with swollen, pale or anamolous optic discc with blurring yellow optic discc"],




# "parafoveal telangiectasia":["parafoveal telangiectasia with telangiectatic vessels: identification of abnormal, dilated blood vessels near the fovea, often appearing as small, tortuous vessels",
# "parafoveal telangiectasia with right-angled venules: presence of venules that exhibit a right-angled turn, a characteristic feature of parafoveal telangiectasia",
# "parafoveal telangiectasia with retinal crystalline deposits: observation of crystalline-like deposits within the retina, a distinctive finding associated with this condition",
# "parafoveal telangiectasia with absence of macular edema: unlike some other retinal conditions, parafoveal telangiectasia typically presents without significant macular edema",
# "parafoveal telangiectasia with mild-to-moderate retinal atrophy: progressive thinning of the retina, particularly in the parafoveal region, indicating the stage of the disease",
# "parafoveal telangiectasia with reduced capillary density: a decrease in the density of capillaries in the affected area, contributing to altered blood flow patterns",
# "parafoveal telangiectasia with pigmentary changes: alterations in retinal pigmentation, including pigment clumping or migration, as the disease progresses",
# "parafoveal telangiectasia with subtle fluorescein angiography findings: the use of fluorescein angiography may reveal subtle abnormalities in the parafoveal region, aiding in the diagnosis of parafoveal telangiectasia"],

# "parafoveal telangiectasia":[
# "parafoveal telangiectasia with yellow, lipid-rich exudation or parafoveal graying or abnormalities from distention and tortuous blood vessels (ectatic)",
# "parafoveal telangiectasia with incompetent retinal capillaries in the juxtafoveolar region",
#                              ],
#


"parafoveal telangiectasia":[
"parafoveal telangiectasia with yellow, lipid-rich exudation or parafoveal graying or abnormalities from fovea",
"parafoveal telangiectasia with gray or yellow abnormalities in fovea",
"parafoveal telangiectasia with gray or yellow abnormalities in macula"
],



# "retinal traction":["retinal traction with distorted retinal vessels: observation of distortion or stretching of retinal vessels due to the traction forces exerted on the retina",
# "retinal traction with focal or diffuse retinal elevation: presence of localized or widespread elevation of the retina, indicative of traction-induced changes",
# "retinal traction with wrinkling or folding of the retinal surface: appearance of fine or coarse wrinkles on the retinal surface due to traction forces",
# "retinal traction with tractional retinal detachment: identification of retinal detachment caused by the pulling forces exerted on the retina",
# "retinal traction with macular involvement: involvement of the macular region, leading to distortion or displacement of the macula",
# "retinal traction with epiretinal membrane formation: development of a membrane on the surface of the retina due to the traction forces, often contributing to the observed retinal changes",
# "retinal traction with distortion of the optic disc: changes in the shape or displacement of the optic disc caused by the traction forces",
# "retinal traction with presence of vitreoretinal interface abnormalities: identification of abnormalities at the vitreoretinal interface, such as vitreomacular adhesion or vitreomacular traction, contributing to retinal traction"],

"retinal traction":[
"retinal traction with yellow line around",
"retinal traction with blurring yellow line",
"retinal traction with with retinal folds with the appearance of folds, manifesting as wrinkled or undulating patterns on the retina, observable on the fundus image",
"retinal traction with with disapperance of retinal vessels with distort the surrounding retinal blood vessels",
"retinal traction with retinal traction may result in the rupture of blood vessels within the vitreous, leading to vitreous hemorrhage with hemorrhages within the red spot",
"retinal traction with retinal tears with irregular defects and signs of retinal detachment",
"retinal traction with retinal detachment with signs of retinal separation, characterized by wrinkling, undulating changes, and possible holes and vitreous hemorrhage"],



# "retinitis":["retinitis with white, fluffy exudates: presence of white, fluffy exudates on the retina, indicative of inflammatory changes associated with retinitis",
# "retinitis with retinal hemorrhages: identification of hemorrhages on the retina, suggesting vascular involvement and inflammation",
# "retinitis with focal areas of retinal whitening: localized areas of whitening on the retina, corresponding to regions of active inflammation",
# "retinitis with blurred or indistinct retinal vessels: vessels appearing hazy or less distinct due to inflammatory changes in the surrounding tissue",
# "retinitis with perivascular sheathing: presence of inflammation around retinal blood vessels, often visible as a sheathing effect",
# "retinitis with optic disc swelling: swelling of the optic disc, indicating involvement of the optic nerve head in the inflammatory process",
# "retinitis with macular involvement: inflammation affecting the macular region, leading to potential visual impairment",
# "retinitis with the presence of inflammatory cells in the vitreous: identification of inflammatory cells, such as cells or debris, within the vitreous humor, further supporting the diagnosis of retinitis"],

"retinitis":["retinitis with vitreous inflammation",
             "retinitis with intraretinal hemorrhage ",
"retinitis with macular star",
"retinitis with phlebitis",
"retinitis with arteritis",
"retinitis withhyperemic disc",
"retinitis with white, fluffy exudates: presence of white, fluffy exudates on the retina",
             ],



"chorioretinitis":["chorioretinitis with focal areas of retinal whitening: localized areas of whitening on the retina, indicating inflammation and damage to the choroid and retina",
"chorioretinitis with irregular borders and fuzzy margins: presence of lesions with indistinct edges, often characterized by fuzzy margins due to inflammatory changes",
"chorioretinitis with inflammation of choroid and retina"

],



"exudation":["exudation with localized or diffuse retinal thickening with identification of areas where the retina appears thicker than normal, indicating fluid accumulation",
"exudation with white or yellowish lipid deposits with presence of fluffy, white lesions on the retina, often associated with microinfarctions and white or yellow spots",
"exudation with exudates with accumulation of lipid or protein deposits on the retina, often appearing as yellowish lesions",
"exudation with macular involvement with swelling and fluid accumulation in the macular region, potentially leading to decreased visual acuity",
"exudation with hard exudates with deposition of lipid-rich material on the retina, often presenting as yellowish, well-defined lesions",
"exudation with optic disc swelling with swelling of the optic disc, indicating increased pressure within the eye and potential involvement of the optic nerve head",
"exudation with serous retinal detachment with separation of the neurosensory retina from the underlying retinal pigment epithelium due to the accumulation of serous fluid"],

# "retinal pigment epithelium changes":["retinal pigment epithelium changes with mottled or granular appearance: observation of irregular or grainy alterations in the retinal pigment epithelium (RPE), often indicative of degenerative changes",
# "retinal pigment epithelium changes with hypo- or hyperpigmented patches: areas of the RPE displaying either lighter (hypopigmented) or darker (hyperpigmented) pigmentation compared to the surrounding tissue",
# "retinal pigment epithelium changes with presence of drusen: identification of small, yellowish deposits beneath the RPE, a common sign of age-related macular degeneration",
# "retinal pigment epithelium changes with geographic atrophy: development of well-defined areas of RPE loss, often leading to corresponding retinal thinning",
# "retinal pigment epithelium changes with pigment clumping: aggregation of pigmented material within the RPE layer, contributing to alterations in pigmentation",
# "retinal pigment epithelium changes with window defects: areas where the underlying choroidal vessels become visible due to RPE thinning or atrophy",
# "retinal pigment epithelium changes with alterations in autofluorescence patterns: variations in the natural fluorescence emitted by the RPE, detectable through imaging techniques like fundus autofluorescence",
# "retinal pigment epithelium changes with irregularities in the RPE layer: disruptions or irregularities in the normally smooth RPE layer, often associated with degenerative processes or diseases affecting the retina"],

"retinal pigment epithelium changes":["retinal pigment epithelium changes with increased thickness of Bruch’s membrane",
                                      "retinal pigment epithelium changes with loss of melanin granules",
                                      "retinal pigment epithelium changes with accumulation of lipofuscin",
                                      "retinal pigment epithelium changes with formation of drusen",
                                      "retinal pigment epithelium changes with increase in the density of residual bodies",
                                      "retinal pigment epithelium changes with accumulation of basal deposits on r within Bruch’s membrane",
                                      "retinal pigment epithelium changes with disorganization of the basal infoldings",
                                      "retinal pigment epithelium changes with microvilli atrophy"],



"macular hole":["macular hole with central foveal dehiscence with presence of a gap or opening in the central fovea, often observed as a well-defined break in the retinal tissue",
"macular hole with loss of foveal contour with flattening or distortion of the normal foveal shape, indicating structural changes associated with the macular hole",
"macular hole with small retinal break located in the center of the fovea",
                "macular hole with lesion in the macula",
                "macular hole with grayish fovea"],



# "retinitis pigmentosa":["retinitis pigmentosa with bone spicule-like pigmentation: presence of characteristic pigmentary changes resembling bone spicules, often distributed in the mid-peripheral and peripheral retina",
# "retinitis pigmentosa with attenuated retinal vessels: narrowing and attenuation of retinal blood vessels, particularly in the peripheral regions",
# "retinitis pigmentosa with waxy pallor of the optic disc: optic disc appearing pale and atrophic, indicating optic nerve head involvement",
# "retinitis pigmentosa with peripheral field constriction: visual field testing may reveal constriction, especially in the peripheral visual field, a common feature in retinitis pigmentosa",
# "retinitis pigmentosa with a ring of hyperautofluorescence: detection of a hyperautofluorescent ring on fundus autofluorescence imaging, often corresponding to the border of degenerated and preserved retina",
# "retinitis pigmentosa with macular involvement: although primarily a peripheral disease, macular changes may include atrophy, cystoid macular edema, or pigmentary alterations",
# "retinitis pigmentosa with a salt-and-pepper fundus appearance: description of a fundus appearance characterized by a mottled pattern of dark and light areas, resembling salt and pepper",
# "retinitis pigmentosa with rod-cone dystrophy: identification of a combined rod and cone photoreceptor dysfunction, leading to night blindness and progressive visual field loss"],
#


"retinitis pigmentosa":["retinitis pigmentosa with bone spicule-like pigmentation with presence of characteristic pigmentary changes resembling bone spicules, often distributed in the mid-peripheral and peripheral retina",
"retinitis pigmentosa with bone-spicule deposits with black lines around the retina ",
"retinitis pigmentosa with arterial narrowing with light red blood vessels narrowing"],

"cotton wool spots":["cotton wool spots with soft, fluffy edges: identification of soft-edged, white or off-white lesions on the retina, often associated with nerve fiber layer infarctions",
"cotton wool spots with nerve fiber layer thickening: thickening of the nerve fiber layer in areas surrounding the cotton wool spots, contributing to their characteristic appearance",
"cotton wool spots with blurred or indistinct retinal vessels: vessels appearing hazy or less distinct due to the presence of cotton wool spots along the course of the vessels",
"cotton wool spots with superficial retinal hemorrhages: associated hemorrhages on the retinal surface near the cotton wool spots, indicating localized ischemia",
"cotton wool spots with microinfarctions: small areas of tissue infarction, often seen as discrete patches adjacent to the cotton wool spots",
"cotton wool spots with asymmetrical distribution: uneven distribution of cotton wool spots throughout the retina, often more concentrated in specific areas",
"cotton wool spots with associated systemic conditions: consideration of underlying systemic conditions such as hypertension or diabetes, as cotton wool spots can be associated with these diseases",
"cotton wool spots with absence of hard exudates: differentiation from other retinal conditions, as cotton wool spots typically lack the presence of lipid-rich hard exudates"],


"colobomas":["colobomas with well-defined, excavated optic disc: identification of a well-defined, cup-shaped excavation of the optic disc, often larger than the physiological cup",
"colobomas with extension into the adjacent retina: presence of a gap or defect in the retinal tissue, extending from the optic disc towards the peripheral retina",
"colobomas with pigmentary changes: alterations in pigmentation within and around the colobomatous area, contributing to a distinctive appearance",
"colobomas with associated vascular changes: variations in retinal blood vessels, including tortuosity or anomalous branching patterns near the coloboma",
"colobomas with posterior staphyloma: a localized, outward bulging of the posterior eye wall often associated with colobomas, especially in the setting of high myopia",
"colobomas with adjacent choroidal thinning: thinning of the choroid in the region of the coloboma, visible as a darker area in fundus imaging",
"colobomas with peripapillary atrophy: the presence of atrophic changes surrounding the optic disc, often seen in conjunction with colobomas",
"colobomas with absence of retinal tissue at the colobomatous site: a clear void or absence of retinal tissue at the location of the coloboma, often visible on fundus examination"],


"optic disc pit":["optic disc pit maculopathy with peripapillary atrophy: observation of atrophic changes surrounding the optic disc, often extending into the adjacent retina",
"optic disc pit maculopathy with macular serous detachment: detection of serous retinal detachment in the macular region, commonly associated with fluid accumulation",
"optic disc pit maculopathy with schisis-like changes: identification of split-like changes or cavities in the layers of the macula, often visible on optical coherence tomography (OCT) imaging",
"optic disc pit maculopathy with pigmentary changes: alterations in retinal pigmentation within the macula, contributing to a mottled or speckled appearance",
"optic disc pit maculopathy with optic disc excavation: recognition of an excavated or depressed appearance of the optic disc, often associated with the optic disc pit",
"optic disc pit maculopathy with disrupted photoreceptor layer: visualizing interruptions or irregularities in the photoreceptor layer of the macula, indicative of structural changes",
"optic disc pit maculopathy with macular edema: presence of fluid accumulation leading to macular edema, often contributing to visual impairment",
"optic disc pit maculopathy with absence of exudates in the macular region: differentiation from other macular pathologies, as optic disc pit maculopathy typically lacks the presence of lipid-rich exudates in the macular area"],


"preretinal haemorrhage":["preretinal haemorrhage with layered appearance: identification of blood accumulation between the retina and the vitreous, often forming a distinct layered appearance",
"preretinal haemorrhage with sharp demarcation: clear boundaries between the preretinal hemorrhage and surrounding retinal tissue, visible on fundus examination",
"preretinal haemorrhage with obscured retinal vessels: partial or complete covering of retinal vessels by the hemorrhagic layer, contributing to vessel obscurity",
"preretinal haemorrhage with a localized distribution: concentration of blood in a specific area of the retina, often related to the site of vascular rupture",
"preretinal haemorrhage with associated retinal traction: detection of tractional forces on the retina caused by the hemorrhage, visible as distortion or pulling of retinal tissue",
"preretinal haemorrhage with variable coloration: ranging from bright red to darker hues as the hemorrhage undergoes changes in age",
"preretinal haemorrhage with absence of underlying retinal pathology: differentiation from retinal hemorrhages associated with other conditions, as preretinal hemorrhages are typically not directly related to retinal diseases",
"preretinal haemorrhage with gradual resolution over time: monitoring the fundus for signs of resolution as the hemorrhage is reabsorbed, indicating healing and improvement"],

"myelinated nerve fibers":["myelinated nerve fibers with feathered edges: identification of nerve fibers with distinct, feathered borders, often giving them a wispy or brush-like appearance",
"myelinated nerve fibers with a striated pattern: observation of a striped or streaked pattern along the course of the nerve fibers, enhancing their visibility",
"myelinated nerve fibers with variable coloration: ranging from a lighter, more translucent appearance to a more opaque, white or yellowish hue compared to the surrounding retina",
"myelinated nerve fibers with respect to retinal vessels: noting the relationship of myelinated nerve fibers in proximity to retinal vessels, as they often follow the course of blood vessels",
"myelinated nerve fibers with preservation of retinal layers: absence of retinal thinning or disruption in the areas occupied by myelinated nerve fibers, differentiating them from other pathological changes",
"myelinated nerve fibers with sharp demarcation: clear boundaries between the myelinated nerve fibers and adjacent retinal tissue, facilitating their recognition",
"myelinated nerve fibers with nerve fiber layer transparency: the transparency of the nerve fiber layer in the affected areas, allowing visibility of the underlying choroidal vessels",
"myelinated nerve fibers with absence of associated visual field defects: typically, myelinated nerve fibers do not cause visual field deficits, aiding in differentiation from other conditions affecting the visual field"],

"haemorrhagic retinopathy":["haemorrhagic retinopathy with flame-shaped hemorrhages: identification of flame-shaped, linear hemorrhages along the retinal nerve fiber layer, often associated with hypertensive retinopathy",
"haemorrhagic retinopathy with dot and blot hemorrhages: presence of small dot-like and larger blot-shaped hemorrhages scattered throughout the retina, indicating vascular damage",
"haemorrhagic retinopathy with cotton wool spots: detection of fluffy, white lesions on the retina, resulting from microinfarctions and ischemic changes",
"haemorrhagic retinopathy with macular edema: observation of fluid accumulation in the macular region, often contributing to visual impairment",
"haemorrhagic retinopathy with vascular changes: alterations in retinal blood vessels, including arteriolar narrowing, arteriovenous nicking, or vascular sheathing",
"haemorrhagic retinopathy with optic disc swelling: swelling of the optic disc, indicating involvement of the optic nerve head in the hemorrhagic process",
"haemorrhagic retinopathy with hemorrhagic choroidal detachment: presence of blood accumulation between the choroid and the sclera, visible as a dark, dome-shaped area on fundus examination",
"haemorrhagic retinopathy with associated systemic conditions: consideration of underlying systemic diseases such as hypertension or diabetes, as these conditions can contribute to the development of haemorrhagic retinopathy"],

"central retinal artery occlusion":["central retinal artery occlusion with pale retina: observation of a pale or whitened appearance of the retina due to the lack of blood supply, especially in the macular region",
"central retinal artery occlusion with cherry-red spot: identification of a cherry-red spot at the fovea, contrasting with the pale retina, caused by the transparency of the foveal area and the absence of blood flow",
"central retinal artery occlusion with attenuated retinal arteries: narrowing of retinal arteries, often visible as thin, thread-like vessels throughout the retina",
"central retinal artery occlusion with boxcarring of retinal arterioles: segmented appearance of retinal arterioles, resembling a series of boxes due to decreased blood flow",
"central retinal artery occlusion with retinal edema: presence of retinal edema, particularly in the posterior pole, contributing to the overall whitening of the retina",
"central retinal artery occlusion with emboli: detection of emboli, often visible as bright or refractile particles within the retinal vessels, contributing to the arterial occlusion",
"central retinal artery occlusion with cilioretinal artery sparing: in some cases, sparing of the cilioretinal artery may lead to a localized area of preserved retinal perfusion within the macula",
"central retinal artery occlusion with absence of venous pulsations: absence of venous pulsations due to compromised blood flow, especially in the larger retinal veins"],


"tilted disc":["tilted disc with oblique optic disc appearance: recognition of an oval or obliquely shaped optic disc, deviating from the typical round configuration",
"tilted disc with inferotemporal tilting: observation of the optic disc tilted in the inferotemporal direction, potentially resulting in a crescent-shaped or tilted appearance",
"tilted disc with associated peripapillary atrophy: presence of atrophic changes in the peripapillary region, often more noticeable on the side opposite to the tilt",
"tilted disc with asymmetric cup-to-disc ratio: uneven cupping of the optic disc, with one side appearing more excavated than the other due to the tilt",
"tilted disc with abnormal vascular branching patterns: alterations in the branching pattern of retinal vessels near the optic disc, reflecting the tilted nature of the optic disc",
"tilted disc with torsional changes in retinal vessels: twisting or torsion of retinal vessels as they approach the optic disc, indicative of the tilted disc configuration",
"tilted disc with absence of true optic disc swelling: differentiation from true optic disc swelling, as the tilting may create a pseudopapilledema appearance",
"tilted disc with compensatory head tilt: in some cases, patients may adopt a compensatory head tilt to align their visual axis with the tilted optic disc, potentially revealing a head posture abnormality"],


"cystoid macular edema":["cystoid macular edema with retinal cystoid spaces: identification of multiple cyst-like spaces within the macula, often visible as fluid-filled lacunae on fundus imaging",
"cystoid macular edema with petalloid pattern: recognition of a characteristic petal-shaped pattern of fluid accumulation in the macula, radiating from the fovea",
"cystoid macular edema with macular thickening: measurement of increased macular thickness, often seen on optical coherence tomography (OCT) imaging",
"cystoid macular edema with blurred or indistinct foveal reflex: haziness or loss of the normal foveal light reflex due to the presence of cystoid spaces and fluid",
"cystoid macular edema with fluorescein angiography leakage: visualization of leakage on fluorescein angiography, indicating abnormal fluid dynamics within the macula",
"cystoid macular edema with disruption of inner retinal layers: identification of irregularities or disorganization in the inner retinal layers, visible on OCT scans",
"cystoid macular edema with decreased visual acuity: associated vision impairment due to the accumulation of fluid in the macular region",
"cystoid macular edema with absence of other macular pathologies: differentiation from other macular conditions, as cystoid macular edema has specific characteristics on imaging that distinguish it from other macular abnormalities"],


"post traumatic choroidal rupture":["post traumatic choroidal rupture with linear configuration: identification of a linear, often jagged or irregular-shaped lesion on the fundus, corresponding to the choroidal rupture",
"post traumatic choroidal rupture with extension from the optic disc or peripapillary region: noting the origin of the choroidal rupture, often arising from the optic disc or extending radially from the peripapillary area",
"post traumatic choroidal rupture with associated overlying retinal pigment epithelium changes: observation of alterations in pigmentation overlying the choroidal rupture site, indicating disruption to the retinal pigment epithelium",
"post traumatic choroidal rupture with overlying subretinal hemorrhage: presence of hemorrhage between the neurosensory retina and the retinal pigment epithelium, directly overlying the choroidal rupture",
"post traumatic choroidal rupture with choroidal vessel visibility: visualization of choroidal vessels within the rupture site, contrasting with the surrounding normal choroid",
"post traumatic choroidal rupture with adjacent retinal folds: detection of retinal folds near the site of choroidal rupture, resulting from the mechanical forces involved in the traumatic event",
"post traumatic choroidal rupture with associated vitreous hemorrhage: in some cases, concurrent vitreous hemorrhage may be present, complicating the clinical picture",
"post traumatic choroidal rupture with corresponding visual field defects: consideration of visual field testing to identify any scotomas or defects corresponding to the location of the choroidal rupture"],

"choroidal folds":["choroidal folds with undulating appearance: recognition of wave-like or undulating folds in the choroid, often extending across the fundus",
"choroidal folds with parallel orientation: observation of folds running parallel to each other, typically separated by normal choroidal tissue",
"choroidal folds with associated retinal pigment epithelium changes: detection of alterations in pigmentation overlying the choroidal folds, reflecting the influence of the folds on the overlying retina",
"choroidal folds with preserved retinal layers: absence of significant disruption or damage to the neurosensory retina, as choroidal folds primarily affect the choroid",
"choroidal folds with displacement of choroidal vessels: visualization of choroidal vessels appearing displaced or distorted within the folds",
"choroidal folds with localized choroidal thickening: measurement of increased choroidal thickness in the areas corresponding to the folds, visible on optical coherence tomography (OCT) imaging",
"choroidal folds with absence of hemorrhage or exudates: differentiation from other fundus abnormalities, as choroidal folds typically do not present with associated hemorrhage or exudative changes",
"choroidal folds with correlation to patient symptoms: consideration of patient symptoms such as metamorphopsia or visual distortion, as choroidal folds may affect visual perception"],

"vitreous haemorrhage":["vitreous haemorrhage with obscured fundus details: presence of blood in the vitreous cavity leading to reduced visibility of retinal structures, making fundus details indistinct",
"vitreous haemorrhage with floating blood cells: observation of floating red blood cells within the vitreous humor, contributing to the hazy appearance",
"vitreous haemorrhage with blotchy or speckled fundus: fundus exhibiting irregular blotches or speckles due to the dispersed blood within the vitreous",
"vitreous haemorrhage with dense, layered blood accumulation: detection of dense, layered blood accumulation, potentially forming a horizontal level in the vitreous cavity",
"vitreous haemorrhage with obscuration of retinal vessels: obscuring or masking of retinal vessels as a result of the hemorrhage, leading to diminished vessel visibility",
"vitreous haemorrhage with dynamic movement of blood particles: potential movement or settling of blood particles within the vitreous, observable during eye movements",
"vitreous haemorrhage with associated retinal pathology: determination of any underlying retinal pathologies, such as diabetic retinopathy or retinal tears, that may have contributed to the vitreous hemorrhage",
"vitreous haemorrhage with potential clearing over time: consideration of the possibility of spontaneous clearing of the vitreous hemorrhage over time, allowing for improved visualization of the fundus"],

"macroaneurysm":["macroaneurysm with round or oval-shaped lesion: identification of a well-defined, round or oval-shaped lesion on the fundus, often distinguishable from surrounding vessels",
"macroaneurysm with dilated and tortuous appearance: recognition of a dilated and tortuous vessel segment, forming the macroaneurysm, often exceeding the normal caliber of surrounding vessels",
"macroaneurysm with associated hemorrhage: detection of adjacent retinal hemorrhage, either intraretinal or subretinal, indicating rupture or leakage from the macroaneurysm",
"macroaneurysm with exudates or lipid deposition: presence of lipid-rich exudates or deposits around the macroaneurysm, reflecting chronic leakage and tissue damage",
"macroaneurysm with hard exudates: observation of lipid-rich deposits at a distance from the macroaneurysm, suggestive of chronic leakage and lipid accumulation",
"macroaneurysm with fluorescein angiography findings: abnormal dye leakage or pooling during fluorescein angiography, highlighting the site of the macroaneurysm and associated vascular abnormalities",
"macroaneurysm with surrounding edema: presence of macular edema or localized retinal thickening in proximity to the macroaneurysm",
"macroaneurysm with absence of neovascularization: differentiation from other retinal pathologies, as macroaneurysms typically do not lead to the development of neovascularization"],


"vasculitis":["vasculitis with vessel wall inflammation: identification of signs indicating inflammation of retinal vessels, such as vessel wall thickening or hyperemia",
"vasculitis with perivascular sheathing: presence of white or yellowish sheathing around retinal vessels, indicative of inflammatory infiltration in the perivascular spaces",
"vasculitis with cuffing of retinal vessels: detection of localized or diffuse thickening or cuffing of retinal vessels due to inflammatory changes",
"vasculitis with retinal hemorrhages: observation of dot and blot retinal hemorrhages scattered along the course of affected vessels, reflecting vascular damage",
"vasculitis with cotton wool spots: presence of fluffy, white lesions on the retina, resulting from microinfarctions and ischemic changes associated with vasculitis",
"vasculitis with arterial narrowing: identification of narrowed or constricted retinal arteries, reflecting reduced blood flow due to inflammatory changes",
"vasculitis with neovascularization: potential development of abnormal, new blood vessels as a response to ischemia, visible on the disc or elsewhere in the retina",
"vasculitis with associated retinal edema: detection of fluid accumulation in the retinal layers, leading to retinal thickening and potential macular involvement"],


"branch retinal artery occlusion":["branch retinal artery occlusion with retinal whitening: identification of localized whitening of the retina in the distribution of the affected branch retinal artery, reflecting ischemia",
"branch retinal artery occlusion with emboli: visualization of emboli or plaque-like material within the affected branch retinal artery, indicating the source of the occlusion",
"branch retinal artery occlusion with abrupt vessel cutoff: observation of a sudden termination or sharp demarcation of the affected branch retinal artery, often visible as a straight edge on fundus examination",
"branch retinal artery occlusion with cherry-red spot at the fovea: recognition of a cherry-red spot at the fovea, surrounded by the whitened ischemic retina, due to transparency of the foveal area",
"branch retinal artery occlusion with narrowed and attenuated retinal arteries: identification of reduced caliber and attenuated appearance of the affected branch retinal artery and its tributaries",
"branch retinal artery occlusion with segmentation of retinal blood flow: appearance of segmented or fragmented blood flow within the occluded branch retinal artery, visible as a series of disconnected segments",
"branch retinal artery occlusion with associated cotton wool spots: presence of cotton wool spots in the affected area, indicating ischemic damage and nerve fiber layer infarction",
"branch retinal artery occlusion with delayed or absent arteriovenous transit: abnormal or delayed passage of dye through retinal vessels during fluorescein angiography, revealing impaired blood flow in the affected area"],

"plaque":["plaque with yellowish or white appearance: identification of a localized yellowish or white lesion on the fundus, often contrasting with the surrounding retinal tissue",
"plaque with well-defined borders: recognition of clear and demarcated borders outlining the plaque, facilitating differentiation from adjacent retinal structures",
"plaque with surface irregularities: observation of irregularities or undulations on the surface of the plaque, indicating variations in thickness or composition",
"plaque with associated retinal pigment epithelium changes: detection of alterations in pigmentation overlying the plaque, suggestive of chronic changes or interactions with the retinal pigment epithelium",
"plaque with subretinal fluid accumulation: presence of fluid between the plaque and the neurosensory retina, contributing to localized retinal detachment or elevation",
"plaque with overlying exudates or lipid deposition: identification of lipid-rich exudates or deposits around the plaque, reflecting chronic leakage and tissue damage",
"plaque with fluorescence characteristics on angiography: abnormal dye patterns during fluorescein angiography, revealing the plaque vascular or perfusion characteristics",
"plaque with absence of neovascularization: differentiation from other retinal pathologies, as plaques typically do not lead to the development of neovascularization",],


"haemorrhagic pigment epithelial detachment":["haemorrhagic pigment epithelial detachment with subretinal bleeding: identification of blood accumulation between the retinal pigment epithelium (RPE) and the neurosensory retina, leading to a noticeable detachment",
"haemorrhagic pigment epithelial detachment with irregular borders: recognition of the irregular or jagged borders outlining the area of pigment epithelial detachment",
"haemorrhagic pigment epithelial detachment with hemorrhagic or reddish appearance: observation of a reddish or hemorrhagic component within the pigment epithelial detachment, indicating the presence of blood",
"haemorrhagic pigment epithelial detachment with associated subretinal fluid: detection of fluid accumulation between the RPE and the retina, contributing to the detachment and potentially obscuring underlying details",
"haemorrhagic pigment epithelial detachment with overlying retinal changes: identification of changes in the overlying retina, such as exudates or lipid deposition, due to the presence of blood and altered RPE function",
"haemorrhagic pigment epithelial detachment with fluorescein angiography findings: abnormal dye patterns during fluorescein angiography, reflecting the vascular characteristics and leakage associated with the haemorrhagic pigment epithelial detachment",
"haemorrhagic pigment epithelial detachment with decreased visual acuity: consideration of associated vision impairment due to the presence of blood and fluid affecting the macula",
"haemorrhagic pigment epithelial detachment with absence of neovascularization: differentiation from other retinal pathologies, as haemorrhagic pigment epithelial detachments typically do not lead to the development of neovascularization"],


"collaterals":["collaterals with vessel dilation: identification of dilated retinal vessels, often forming collateral pathways that deviate from the normal vascular pattern",
"collaterals with tortuous appearance: recognition of tortuosity or twisting in the course of collateral vessels, reflecting the compensatory changes in blood flow",
"collaterals with anastomoses: observation of connections or anastomoses between retinal vessels, creating alternative pathways for blood circulation",
"collaterals with abnormal branching patterns: detection of irregularities or aberrant branching in retinal vessels, indicative of collateral formation",
"collaterals with visible pulsations: observation of pulsatile movements in collateral vessels, potentially visible with careful examination or dynamic imaging",
"collaterals with fluorescein angiography findings: abnormal dye patterns during fluorescein angiography, highlighting the presence and characteristics of collateral vessels",
"collaterals with associated retinal changes: identification of changes in the overlying retina, such as exudates or hemorrhages, due to altered blood flow and collateral circulation",
"collaterals with correlation to underlying vascular pathology: consideration of the underlying vascular pathology leading to collateral formation, such as occlusive diseases or venous abnormalities"],



    "health": ["health with normal with optic disc appears well-defined and within normal limits",
               "health with no findings with clear circular shape with distinctth  margins",
               "health with normal appearance of retina wia uniform color and texture",
               "health with normal with well-defined blood vessels, arteries and veins",
               "health with clear macula with clear retinal background",
               "health with normal with no signs of hemorrhages",
               "health with no findings with no signs of exudates",
               "health with no findings with no other abnormalities"],

    "other": [
              "other with cotton wool spots",
                "other with colobomas",
        "other with optic disc pit maculopathy",
        "other with preretinal haemorrhage",
        "other with myelinated nerve fibers",
        "other with haemorrhagic retinopathy",
        "other with central retinal artery occlusion",
        "other with tilted disc",
        "other with cystoid macular edema",
        "other with post traumatic choroidal rupture",
        "other with choroidal folds",
        "other with vitreous haemorrhage",
        "other with macroaneurysm",
        "other with vasculitis",
        "other with branch retinal artery occlusion",
        "other with plaque",
        "other with haemorrhagic pigment epithelial detachment",
        "other with collaterals with vessel dilation"]





}