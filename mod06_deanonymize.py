import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    data = {
        "anon_id": [],
        "matched_name": []
    }
    for row in anon_df.itertuples(index=True):
      for auxrow in aux_df.itertuples(index=True):
        #print(auxrow.name)
        if (row.age == auxrow.age) & (row.zip3 == auxrow.zip3) & (row.gender == auxrow.gender):
          data["anon_id"].append(row.anon_id)
          data["matched_name"].append(auxrow.name)
          break


    result = pd.DataFrame(data)
    return result


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    return (len(matches_df) / len(anon_df))
