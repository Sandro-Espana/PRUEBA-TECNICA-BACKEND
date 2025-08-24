def normalize_evidence_link(data_dict: dict) -> dict:
    if data_dict.get("evidence_link"):
        data_dict["evidence_link"] = str(data_dict["evidence_link"])
    return data_dict