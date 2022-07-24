import enum


class ROLE_NAMES(enum.Enum):
    ADMIN = 'admin'
    DOCTOR = "doctor"
    NURSE = "nurse"
    RECORD_OFFICER = "record officer"
    PHARMACIST = "pharmacist"
    LABORATORY_TECHNICIAN = "laboratory technician"
    RADIOLOGY_TECHNICIAN = "radiology technician"
    MEDICAL_STORE_MANAGER = "medical store manager"
    CASHIER = "cashier"
    PHYSIOTHERAPIST = "physiotherapist"
    PHLEBOTOMIST = "phlebotomist"
    UNALLOCATED = "unknown"


class HOSPITAL_DEPARTMENT(enum.Enum):
    EMERGENCY = "Accident and emergency"  # Also called Casualty Department, where you're likely to be taken if you have arrived in an ambulance or emergency situation.
    ADMISSION = "Admissions"  # At the Admitting Department, the patient will be required to provide personal information and sign consent forms before being taken to the hospital unit or ward.
    ANESTHETICS = "Anesthetics"  # Doctors in this department give anesthetic for operations and procedures.
    BREAST_SCREENING = "Breast Screening"  # Screens women for breast cancer and is usually linked to the X-ray or radiology department.
    BURN_CENTER = "Burn Center"  # A hospital specializing in the treatment of burns. Burn centers are often used for the treatment and recovery of patients with more severe burns.
    CARDIOLOGY = "Cardiology"  # Provides medical care to patients who have problems with their heart or circulation.
    CSSD = 'Central Sterile Services Department'  # Sterile Processing - Central Supply Department (CSD) - Central Supply) - A place in hospitals and other health care facilities that performs sterilization and other actions on medical equipment, devices, and consumables.
    CHAPLAINCY = "Chaplaincy"  # Chaplains promote the spiritual and pastoral wellbeing of patients, relatives and staff.
    CCU = "Coronary Care Unit"  # A hospital ward specialized in the care of patients with heart attacks, unstable angina, cardiac dysrhythmia and other cardiac conditions that require continuous monitoring and treatment.
    CRITICAL_CARE = "Critical Care"  # Also called intensive care, this department is for seriously ill patients.
    DIAGNOSTIC_IMG = "Diagnostic Imaging"  # Also known as X-Ray Department and/or Radiology Department.
    DISCHARGE_LOUNGE = "Discharge Lounge"  # Patients who don't need to stay in a ward are transferred to the lounge on the day of discharge.
    ELDER_SERVICE = "Elderly Services"  # Covers and assists with a wide range of issues associated with seniors.
    FINANCE = "Finance Department"  # Performs all works related to budget and ideal use of the items of such budget
    GENERAL_SERVICES = "General Services"  # Support Services include services provided by Departments such as Portering, Catering, Housekeeping, Security, Health & Safety, Switch, Laundry and the management of facilities such as parking, baby tagging, access control, CCTV etc.
    GENERAL_SURGERY = "General Surgery"  # Covers a wide range of types of surgery and procedures on patients.
    GYNECHOLOGY = "Gynecology"  # Investigates and treats problems relating to the female urinary tract and reproductive organs, such as Endometriosis, infertility and incontinence.
    HAEMATOLOGY = "Haematology"  # These hospital services work with the laboratory. In addition doctors treat blood diseases and malignancies related to the blood.
    HEALTH_AND_SAFETY = "Health & Safety"  # The role of the occupational health and safety department is to promote and maintain the highest possible degree of health and safety for all employees, physicians, volunteers, students and contractors, and actively participates in quality, safety and risk initiatives.
    HR = "Human Resources"  # Role is to provide a professional, efficient and customer focused service to managers and staff and in turn facilitate the delivery of a professional, efficient and customer focused service to patients.
    INFECTION_CONTROL = "Infection Control"  # Primarily responsible for conducting surveillance of hospital-acquired infections and investigating and controlling outbreaks or infection clusters among patients and health care personnel.
    MATERNITY = "Maternity"  # Maternity wards provide antenatal care, delivery of babies and care during childbirth, and postnatal support.
    MEDICAL_RECORDS = "Medical Records"
    MICROBIOLOGY = "Microbiology"  # The microbiology department provides an extensive clinical service, including mycology, parasitology, mycobacteriology, a high security pathology unit, and a healthcare associated infection investigation unit, as well as routine bacteriology and an expanding molecular diagnostic repertoire.
    NEUROLOGY = "Neurology"  # A medical specialty dealing with disorders of the nervous system.
    NUTRITION_AND_DIETETICS = "Nutrition and Dietetics"  # Dietitians and nutritionists provide specialist advice on diet for hospital wards and outpatient clinics.
    ONCOLOGY = "Oncology"  # A branch of medicine that deals with cancer and tumors.A medical professional who practices oncology is an oncologist.The Oncology department provides treatments, including radiotherapy and chemotherapy, for cancerous tumors and blood disorders.
    OPHTHALMOLOGY = "Ophthalmology"  # Ophthalmology is a branch of medicine which deals with the diseases and surgery of the visual pathways, including the eye, hairs, and areas surrounding the eye, such as the lacrimal system and eyelids.
    ORTHOPAEDICS = "Orthopaedics"  # Treats conditions related to the musculoskeletal system, including joints, ligaments, bones, muscles, tendons and nerves.
    PHARMACY = "Pharmacy"  # Responsible for drugs in a hospital, including purchasing, supply and distribution.
    PHYSIOTHERAPY = "Physiotherapy"  # Physiotherapists work through physical therapies such as exercise, massage, and manipulation of bones, joints and muscle tissues.
    RADIOLOGY = "Radiology"  # The branch or specialty of medicine that deals with the study and application of imaging technology like x-ray and radiation to diagnosing and treating disease.
    RADIOTHERAPY = "Radiotherapy"  # Also called radiation therapy, is the treatment of cancer and other diseases with ionizing radiation.
    RHEUMATOLOGY = "Rheumatology"  # Rheumatologists care for and treat patients for musculoskeletal disorders such as: bones, joints, ligaments, tendons, muscles and nerves.
    UROLOGY = "Urology"  # The urology department is run by consultant urology surgeons and investigates areas linked to kidney and bladder conditions.
    OUTPATIENT = "Outpatient"
    NURSING = "Nursing"
    PARAMEDICS = "Paramedics"  # Paramedical departments are adjunctive to the practice of medicine in the maintenance or restoration of health and normal functioning.
    OT = "Operation Theatre Complex"  # This consists of one or more operation theatres and other facilities. OT complex must be located in a place where there is easy and quick access to the delivery suite.
    DIETARY = "Dietary"
    ACQUISITIONS = "Acquisitions"


class HOSPITAL_UNIT(enum.Enum):
    PATHOLOGY = "Pathology"
    NEUROSURGERY = "Neurosurgery"
    ORTHOPEDIC_SURGERY = "Orthopedic Surgery"
    GENERAL_SURGERY = "General Surgery"
    ENT_OTOLARYNGOLOGY = "ENT/Otolaryngology"
    PLASTIC_SURGERY = "Plastic Surgery"
    GENERAL_PRACTITIONER = "General Practitioner"
    DENTISTRY = "Dentistry"
    GI_PHYSIOLOGY = "GI physiology"
    NEUROLOGY = "Neurology"
    PEDIATRICS = "Pediatrics"
    CARDIOTHORASIC_SURGERY = "Cardiothorasic Surgery"
    RECORDS = "Records"
    ONCOLOGY = "Oncology"
    OBSTETRICS_AND_GYNECOLOGY = "Obstetrics and Gynecology"
    PEDIATRIC_SURGERY = "Pediatric Surgery"
    RADIOLOGY = "Radiology"
    NEPHROLOGY = "Nephrology"
    EMERGENCY = "Emergency"
    VIP = "VIP2"
    ENDOCRINOLOGY = "Endocrinology"
    FAMILY_MEDICINE = "Family Medicine"


class SERVICE_AREA(enum.Enum):
    CENTRAL_RECORDS = 'Central Records'
    LABORATORY = 'Laboratory'
    PAY_POINT = 'Pay Point'
    PAY_POINT_CASHIER = 'Pay Point/Cashier'
    PHARMACY = 'Pharmacy'
    PHYSIOTHERAPY = 'Physiotherapy'
    RADIOLOGY = 'Radiology'


class PROVIDER_ROLES(enum.Enum):
    ADMIN = 'admin'
    DOCTOR = "doctor"
    NURSE = "nurse"
    RECORD_OFFICER = "record officer"
    PHARMACIST = "pharmacist"
    LABORATORY_TECHNICIAN = "laboratory technician"
    RADIOLOGY_TECHNICIAN = "radiology technician"
    MEDICAL_STORE_MANAGER = "medical store manager"
    CASHIER = "cashier"
    PHYSIOTHERAPIST = "physiotherapist"
    PHLEBOTOMIST = "phlebotomist"
    UNALLOCATED = "unknown"

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value.capitalize()) for choice in cls]

    @classmethod
    def values(cls, *filters):
        return [
            choice.value
            for choice in cls
            if choice.value != cls.UNALLOCATED.value and choice.value not in filters
        ]

# MEDICAL DEPARTMENT
# The medical department has within it the various clinical services. They are: medicine, surgery, gynaecology, obstetrics, paediatrics, eye, ENT, dental, orthopaedics, neurology, cardiology, psychiatry, skin, V.D., plastic surgery, nuclear medicine, infectious disease etc. medical superintendent is a doctor who has control over all medical department.
