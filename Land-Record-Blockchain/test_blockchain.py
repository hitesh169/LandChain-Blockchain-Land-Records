from blockchain import LandBlockchain

bc = LandBlockchain()

bc.add_record(
    "LAND-101",
    "REGISTER",
    {
        "owner": "Rahul",
        "location": "Sample Plot A",
        "area_sq_meters": 200
    }
)

print("Blockchain valid:", bc.verify_chain())
print("Number of blocks:", len(bc.chain))
print("Latest block:", bc.chain[-1])