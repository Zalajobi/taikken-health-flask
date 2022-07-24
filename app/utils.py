from app import ProviderTable, AddressTable


def get_provider(provider_id):
    return ProviderTable.find_by_id(provider_id)


def register_address(address, provider_id=None, patient_id=None):
    address = AddressTable(
        country=address['country'],
        state=address['state'],
        address=address['address'],
        city=address['city'],
        zip_code=address['zip_code'],
        provider_id=provider_id,
        patient_id=patient_id
    )
    address.save_to_db()
    return address
