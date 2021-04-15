import pandas as pd
from sodapy import Socrata

def main():
    catalonia_association_dataset = extract_data_from_transparencia_catalunya_api(dataset_identifier="y6fz-g3ff")
    catalonia_association_dataset = filter_and_clean(catalonia_association_dataset)
    barcelona_association_dataset = generate_barcelona_dataset(catalonia_association_dataset)

def extract_data_from_transparencia_catalunya_api(dataset_identifier):
    client = Socrata("analisi.transparenciacatalunya.cat", None)
    results = client.get(dataset_identifier, limit=100000) #1000000
    dataset = pd.DataFrame.from_records(results)
    return dataset

def filter_and_clean(dataset):
    dataset = dataset.drop(["id_entitat","cif","num_inscripcio","fax"], axis=1)
    dataset = dataset.rename(columns={"contingut_finalitats": "finalitat"})

    colums_ordered = ['nom_entitat', 'tipus_entitat', 'data_inscripcio', 'adreca', 'nom_poblacio', 'codi_postal',
                    'nom_provincia', 'nom_comarca', 'classificacio_general', 'classificacio_especifica',
                    'telefon', 'fundadors', 'pagina_web', 'finalitat', 'finalitats2', 'finalitats3']
    dataset = dataset[colums_ordered]
    return dataset

def generate_barcelona_dataset(dataset):
    dataset = dataset[dataset.nom_poblacio == "Barcelona"]
    #dataset = dataset[dataset['codi_postal'].str.contains("080")]

    # postalcode_district_dict = {"08001": , "08002": , "08003": , "08004": , "08005": , "08006": , "08007": , "08008": ,
    #                             "08009": , "08010": , "08011": , "08012": , "08013": , "08014": ,"08015": , "08016": ,
    #                             "08017": , "08018": , "08019": , "08020": , "08021": , "08022": , "08023": ,
    #                             "08024":, "08025": , "08026": , "08027": , "08028": , "08029": , "08030": , "08031": ,
    # "08032":,  "08033": , "08034": , "08035": , "08036": ,"08037": , "08038": , "08039": }
    # print(dataset)
    dataset.to_csv("barcelona_dataset.csv", index=False)

if __name__ == "__main__":
    main()